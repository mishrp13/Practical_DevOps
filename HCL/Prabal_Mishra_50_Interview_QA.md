# 50 Interview Questions & Answers — Based on Your Resume

Organized by topic area so you can study in blocks. Each answer is written the way you'd actually say it in an interview — specific to your projects where possible, general DevOps knowledge where the resume doesn't give a direct hook.

---

## AWS Core (VPC, EC2, IAM, S3, RDS, ALB, CloudWatch)

**1. Walk me through the VPC architecture you designed for your EKS project.**
I designed a multi-AZ VPC spanning at least two availability zones for high availability. Each AZ had a public subnet (hosting the NAT Gateway and Internet-facing resources like the ALB) and a private subnet (hosting the EKS worker nodes, kept off the public internet). Route tables directed public subnet traffic through the Internet Gateway and private subnet traffic through the NAT Gateway for outbound-only access. This isolation meant worker nodes could pull images and talk to AWS APIs without being directly reachable from the internet.

**2. Why use private subnets for EKS worker nodes instead of putting everything in public subnets?**
Security and blast radius. Nodes in private subnets aren't directly addressable from the internet — the only way in is through the ALB, which terminates public traffic and forwards it to the cluster. If a node doesn't need inbound internet traffic, there's no reason to expose it; it only needs outbound access (via NAT Gateway) to pull images or reach AWS services like ECR.

**3. What's the difference between a NAT Gateway and an Internet Gateway, and why did you need both?**
An Internet Gateway allows two-way traffic between a VPC and the internet — public subnet resources use it directly. A NAT Gateway allows one-way outbound traffic from private subnets (so private resources can reach the internet or AWS APIs) without allowing unsolicited inbound connections. I used the IGW for public-facing resources like the ALB, and the NAT Gateway so private EKS nodes could still pull container images or call AWS APIs without being exposed.

**4. How did you scope IAM roles for the EKS cluster and its workloads?**
I followed least privilege — separate roles for the EKS control plane (cluster service role), the node groups (worker node role with permissions for ECR pull, CNI networking, and CloudWatch logging), and, where applications needed AWS access, IAM Roles for Service Accounts (IRSA) so individual pods get scoped permissions instead of inheriting the broader node role. This way a compromised pod doesn't automatically have account-wide access.

**5. What is IAM Roles for Service Accounts (IRSA) and why does it matter for EKS specifically?**
Normally, workloads on EC2/EKS nodes inherit the IAM permissions of the node's instance profile — meaning every pod on that node has the same AWS permissions, which is overly broad. IRSA lets you attach an IAM role directly to a Kubernetes service account via OIDC federation, so a specific pod only gets the permissions it actually needs (e.g., read access to one S3 bucket), rather than whatever the node happens to have.

**6. Where does S3 fit into your infrastructure, beyond just storage?**
The main use in my Terraform projects was as a remote state backend — storing `.tfstate` files centrally instead of locally, so the whole team and CI/CD pipeline work off the same state. I'd pair it with state locking to prevent concurrent applies from corrupting state. S3 is also a natural fit for storing build artifacts, logs, or backups referenced in a pipeline.

**7. How would you use CloudWatch alongside the Splunk-based monitoring you mention on your resume?**
CloudWatch is AWS-native — good for infrastructure-level metrics (EC2/EKS node CPU, memory, ALB request counts, error rates) and can trigger alarms or auto-scaling actions directly within AWS. Splunk is what I used for deeper log search and correlation across applications during troubleshooting. In practice they complement each other: CloudWatch alarms tell you something's wrong, and Splunk lets you dig into why by searching the actual application logs.

**8. What's an Application Load Balancer (ALB), and how did you integrate it with Kubernetes?**
The ALB is a Layer 7 (HTTP/HTTPS) load balancer that routes traffic to backend targets based on rules like path or host. I integrated it with EKS using the AWS Load Balancer Controller, which watches Kubernetes Ingress/Service resources and automatically provisions and configures an ALB to route external traffic into the cluster — so app teams just define a Kubernetes Ingress and the ALB gets created and wired up behind the scenes.

---

## Terraform & Infrastructure as Code

**9. Why did you choose Terraform over something like AWS CloudFormation?**
Terraform is cloud-agnostic — the same tool and syntax work across AWS, Azure, and other providers, which mattered since I also have working exposure to Azure. It also has a large module ecosystem, a clear plan/apply workflow that shows exactly what will change before it happens, and strong state management, which made it a good fit for managing infrastructure that multiple environments and teams touch.

**10. Explain the `terraform init → validate → plan → apply` workflow you used.**
`init` downloads providers and sets up the backend (in my case, S3 for remote state). `validate` checks the configuration syntax without touching real infrastructure. `plan` shows exactly what will be created, changed, or destroyed compared to current state — this is the safety check before anything happens. `apply` actually executes those changes. I treated `plan` as non-negotiable before any `apply`, especially in shared environments, since it catches unintended changes before they hit infrastructure.

**11. How do Terraform variables, locals, and outputs differ, and how did you use them?**
Variables are inputs you pass into a module (e.g., environment name, instance size) so the same code works across Dev/QA/Prod. Locals are computed or derived values used internally to avoid repeating expressions. Outputs expose values from a module (like a VPC ID or subnet IDs) so other modules or the root configuration can consume them. I used this combination so, for example, my EKS module could pull the VPC ID as an output from my networking module rather than hardcoding it.

**12. What happens if two people run `terraform apply` at the same time without state locking?**
Without locking, both runs could read the same state, calculate different plans, and then write conflicting changes back to the state file — this can corrupt state or cause Terraform to lose track of resources it's actually managing, sometimes resulting in duplicate resources or resources that exist in AWS but not in state (orphaned resources). State locking (via DynamoDB alongside an S3 backend) prevents this by making a second `apply` wait until the first finishes.

**13. How do you handle secrets (like database passwords) in Terraform without hardcoding them?**
I avoid putting secrets directly in `.tf` files or committing them to Git. Options include marking variables as `sensitive = true` so they're masked in plan/apply output, pulling values at runtime from AWS Secrets Manager or SSM Parameter Store via data sources, or injecting them through environment variables in the CI/CD pipeline rather than the codebase itself.

**14. What's the difference between a Terraform resource and a data source?**
A resource block tells Terraform to create and manage a piece of infrastructure — Terraform owns its lifecycle. A data source reads information about existing infrastructure that Terraform doesn't manage (e.g., looking up an existing AMI ID or an existing VPC) so you can reference it without recreating it.

**15. How would you roll back a bad Terraform apply?**
The safest path is version-controlled configuration — revert the `.tf` files to the last known-good commit and run `plan`/`apply` again, since Terraform is declarative and will reconcile infrastructure back to match that configuration. For state-only issues (not actual infrastructure damage), Terraform also keeps state file versioning if you're using S3 with versioning enabled, so you can restore a previous state file if needed. I always treated Git history as the actual source of truth, not manual state edits.

**16. How did you structure your reusable Terraform modules to avoid duplication across Dev, QA, and Production?**
I broke infrastructure into modules by concern — networking, compute, security groups, IAM, ALB, EKS — each parameterized through variables. Environment-specific differences (subnet CIDRs, instance sizes, node counts) lived in separate `.tfvars` files per environment, while the actual module logic stayed identical across all three. That meant a fix or improvement to, say, the networking module automatically applied everywhere once each environment's `tfvars` picked up the change.

---

## Kubernetes & Amazon EKS

**17. Walk me through how you provisioned and managed an Amazon EKS cluster with Terraform.**
I used Terraform to provision the EKS control plane and managed node groups, feeding in the VPC and subnet IDs from my networking module. I configured IAM roles for both the cluster and node groups, set up node group scaling parameters (min/max/desired), and made sure private subnets hosted the nodes. Once the cluster existed, I used `kubectl`/Helm for workload-level deployments rather than managing every Kubernetes object through Terraform, since that split keeps infrastructure and application concerns separate.

**18. What's the difference between a Kubernetes Deployment and a Service?**
A Deployment manages the desired state of a set of pods — how many replicas, which container image, rolling update strategy — and handles replacing failed pods automatically. A Service provides a stable network endpoint (a consistent DNS name/IP) to reach those pods, since individual pod IPs change as pods are created and destroyed. Without a Service, other workloads would have no reliable way to find and talk to a Deployment's pods.

**19. Explain readiness vs. liveness probes and why you configured both.**
A liveness probe checks whether a container is still functioning; if it fails repeatedly, Kubernetes kills and restarts the pod. A readiness probe checks whether a container is ready to receive traffic; if it fails, the pod is removed from the Service's endpoint list but not restarted. I configured both because they solve different problems — liveness recovers from a hung process, readiness prevents traffic from hitting a pod that's still starting up or temporarily overloaded (e.g., during a dependency outage).

**20. How do resource requests and limits work, and why did you configure them?**
Requests tell the Kubernetes scheduler the minimum CPU/memory a pod needs to be scheduled on a node with enough capacity. Limits cap the maximum a container can consume, preventing one workload from starving others on the same node. I set both on my EKS project for reliability — without requests, the scheduler could over-pack a node; without limits, a single misbehaving pod could consume all available resources and destabilize its neighbors.

**21. What did your Kubernetes Ingress Controller optimization POC actually involve, and how did you measure the 20% improvement?**
I reviewed the existing Ingress Controller's configuration — replica count, resource requests/limits — against actual traffic patterns and found it was over-provisioned relative to real load. I ran a proof-of-concept adjusting replica sizing and resource allocation, then compared cluster-wide resource utilization metrics before and after the change. The 20% improvement came from freeing up CPU/memory that had been reserved but unused, giving that capacity back to application workloads without adding new nodes.

**22. Explain Blue-Green vs. Canary deployments — when would you choose one over the other?**
Blue-Green runs the new version fully alongside the old version and switches all traffic over at once (typically at the load balancer or Service level) once health checks pass — rollback is instant since the old version is still running. Canary gradually shifts a small percentage of traffic to the new version first, monitoring error rates and latency before ramping up further. I'd lean toward Canary for higher-risk changes where I want real traffic validation before full exposure, and Blue-Green when I want a clean, fast cutover with an easy full rollback, like for a well-tested release.

**23. How do Helm charts differ from raw Kubernetes manifests, and why did you use them?**
Raw manifests are static YAML — any environment-specific difference (image tag, replica count, resource limits) means maintaining separate copies or manual edits. Helm charts template that YAML with variables pulled from values files, so one chart can deploy consistently across environments just by swapping which values file is used. It also gives versioned releases and easy rollback (`helm rollback`) instead of manually reapplying old manifests.

**24. What would you check first if pods in your EKS cluster were stuck in a "Pending" state?**
I'd start with `kubectl describe pod` to see the scheduling events — usually it's insufficient node resources (requests exceeding available capacity), a node affinity/taint mismatch, or the node group not having scaled up yet. I'd check node group capacity and autoscaler logs next, then confirm the pod's resource requests are actually satisfiable by the instance types in that node group.

---

## CI/CD (Jenkins, GitHub Actions, GitLab CI)

**25. Walk me through the CI/CD pipeline you built for the Citibank engagement.**
The pipeline used Jenkins and GitLab CI. On a commit to the target branch, it ran a build stage, then automated tests. On success, it built a Docker image, tagged it (typically by commit SHA or build number), and pushed it to Amazon ECR. The final stage deployed to EKS — applying updated Kubernetes manifests or running a Helm upgrade with the new image tag — so every successful merge produced a versioned, deployable artifact without manual intervention.

**26. How is the GitHub Actions pipeline you built for CBA different from a Jenkins pipeline?**
Functionally the stages are similar — build, test, containerize, deploy — but GitHub Actions is YAML-based, triggered directly by repo events, and uses marketplace actions to reduce boilerplate for things like AWS authentication or Docker builds, with less infrastructure to maintain since it's hosted. Jenkins requires managing your own controller/agents and plugins but gives more flexibility for complex, custom pipeline logic. For CBA, GitHub Actions fit well because of its tight integration with the repo and lower operational overhead.

**27. What specific optimizations did you make to improve CI/CD pipeline efficiency at CBA?**
I focused on removing manual steps and tightening the pipeline stages — automating what had been manual verification, parallelizing independent steps where possible, and reducing redundant work between stages. The result was improved delivery reliability and less need for manual intervention during releases, which also reduced the chance of human error in the deployment process.

**28. How would you handle secrets like AWS credentials or registry logins inside a CI/CD pipeline?**
I use the CI tool's native secrets store (GitHub Actions secrets, Jenkins credentials store) rather than hardcoding anything in the pipeline script, and I scope IAM roles narrowly — a pipeline pushing to one ECR repo doesn't need broader account access. Where the platform supports it, I'd prefer OIDC-based short-lived credentials over long-lived static access keys, since a leaked long-lived key has a much bigger blast radius.

**29. What would you do if a deployment pipeline succeeded but the application was broken in production?**
First, roll back immediately using whichever mechanism is fastest and safest — a Helm rollback, redeploying the previous image tag, or shifting traffic back in a Blue-Green setup — prioritizing restoring service. Then I'd investigate: check whether the pipeline's tests actually covered the failure scenario, review logs (Splunk/CloudWatch) around the deployment window, and add a test or health check gate so that failure mode is caught before the next deployment rather than after.

**30. How do you decide what should trigger a pipeline run versus what should require manual approval?**
Automated triggers (push to main, PR merge) make sense for lower-risk environments like Dev or QA, where fast feedback matters more than caution. For Production, I'd typically add a manual approval gate after the plan/build stage — especially for infrastructure changes via Terraform, where I want a human to review the plan output before `apply` runs against production resources.

---

## Docker & Containers

**31. What Docker security hardening practices did you implement at CBA?**
I focused on reducing image vulnerabilities and shrinking attack surface — using minimal/slim base images instead of full OS images, avoiding running containers as root, not baking secrets or credentials into image layers, and keeping base images patched against known CVEs. I also made sure images were scanned before being promoted through environments.

**32. Why push images to Amazon ECR instead of a public registry like Docker Hub?**
ECR integrates directly with IAM, so access control (who can push/pull) is managed through the same permission system as the rest of the AWS account, rather than separate registry credentials. It's also in-region with the EKS cluster, reducing pull latency, and supports native vulnerability scanning. For enterprise banking clients, keeping images inside the AWS account boundary is also a compliance and data-residency consideration.

**33. How did you configure Docker volumes for persistent storage, and why does that matter?**
Containers are ephemeral by design — anything written inside the container filesystem is lost when the container restarts. I configured Docker volumes to persist data outside the container lifecycle, mounting them so application data survived restarts. This matters for anything stateful — logs you need to retain, or application data that shouldn't disappear just because a container got recreated.

**34. Explain the difference between a Docker image and a Docker container.**
An image is a read-only, versioned template — the packaged application plus its dependencies and filesystem layers. A container is a running instance of that image, with its own writable layer on top. You can spin up multiple containers from the same image; each is an isolated running process, but they all start from the identical base image.

**35. What's your process for reducing a Docker image's size and attack surface?**
Start from a minimal base image (slim or Alpine variants where compatible), use multi-stage builds so build-time dependencies (compilers, dev tools) don't end up in the final image, only copy what's actually needed at runtime, and avoid installing unnecessary packages. Smaller images also mean faster pulls and deployments, which is a secondary benefit beyond security.

---

## Monitoring, Scripting & Version Control

**36. How did you use Splunk for troubleshooting production issues?**
I used Splunk to search and correlate application logs — filtering by service, time window, and error signatures to trace an issue back to its root cause, whether that was an application exception, a failed dependency call, or an infrastructure-level problem. It was particularly useful for post-incident review, reconstructing a timeline of events leading up to an alert.

**37. Describe a Python script you wrote to automate an operational task.**
At CBA, I wrote Python scripts to automate scheduled system backups — removing a manual step that had previously depended on someone remembering to run it, and making recovery more reliable since backups ran on a consistent, predictable schedule rather than an ad hoc basis.

**38. What Shell scripts did you build for infrastructure health, and what problem did they solve?**
I wrote Shell scripts for automated node health checks — periodically checking things like disk usage, CPU/memory pressure, and process/service status on worker nodes — so degrading nodes could be flagged and addressed before they caused pod evictions or a broader outage, rather than only finding out after something failed.

**39. Why is Infrastructure as Code (via Git-tracked Terraform) better than manually configuring infrastructure through the AWS console?**
Manual console changes aren't tracked, reviewable, or easily repeatable — there's no audit trail of who changed what or why, and recreating an environment means manually retracing steps. Git-tracked Terraform gives version history, code review via pull requests before changes are applied, and the ability to recreate an identical environment (Dev, QA, or a disaster recovery scenario) from the same codebase.

**40. How did Git fit into your day-to-day workflow across these projects?**
All Terraform code, Kubernetes manifests, and Helm charts were maintained in Git for version control and collaboration. I used feature branches and pull requests for changes so they could be reviewed before merging, and CI/CD pipelines were triggered off specific branches (e.g., merges to main deploying to production) so Git history directly reflected what had actually been deployed.

**41. If you found sensitive data (like a hardcoded credential) accidentally committed to Git, what would you do?**
First, rotate the exposed credential immediately — assume it's compromised the moment it's in Git history, regardless of whether the repo is private. Then remove it from the codebase and replace it with a proper secrets management approach (Secrets Manager, CI secrets store). Removing it from Git history itself (via tools like `git filter-repo` or BFG) is a secondary cleanup step, but rotating the credential is the priority since history rewrites don't undo any exposure that already happened.

---

## Methodologies & Cross-Cutting

**42. How did Agile/Scrum practices show up in your day-to-day work?**
I participated in sprint planning, daily standups, and retrospectives as part of the delivery team, with DevOps work — pipeline improvements, infrastructure changes — planned and tracked alongside application development work rather than treated as separate, ad hoc tasks. This kept infrastructure changes visible to the whole team and meant DevOps priorities got weighed against feature work rather than happening invisibly in the background.

**43. You mention "working understanding" of Microsoft Azure — how would core EKS/AWS concepts map to Azure equivalents?**
Amazon EKS maps to Azure Kubernetes Service (AKS) — both are managed Kubernetes control planes. VPC maps to Azure Virtual Network (VNet), IAM maps to Azure Active Directory/RBAC, S3 maps to Azure Blob Storage, and ALB maps to Azure Application Gateway or Azure Load Balancer depending on the layer. The underlying Kubernetes and Terraform concepts transfer directly — Terraform even uses the same workflow, just with the `azurerm` provider instead of `aws`.

**44. How do you decide what should be automated versus handled manually in a DevOps environment?**
Anything repetitive, error-prone when done by hand, or time-sensitive is a strong automation candidate — backups, health checks, deployments, infrastructure provisioning. I'd hold off on automating something that's still changing frequently or poorly understood, since automating a process too early can lock in the wrong approach. The backup scripts and node health checks I built were good candidates because the process itself was stable and well-defined — automation just removed the human dependency.

**45. What's your approach to documentation for infrastructure you build?**
On the EKS project, I documented the infrastructure flow (VPC → EKS → Node Groups → ECR → Kubernetes Workloads → ALB) and the Terraform module structure so the setup was understandable to someone joining later, not just to me. I think of documentation as part of making infrastructure "repeatable and maintainable" — the same standard I'd apply to the code itself — because tribal knowledge that only lives in one person's head is a risk to the team.

---

## Behavioral / Situational (STAR-style)

**46. Tell me about a time you improved something without being explicitly asked to.**
*Situation:* The Ingress Controller in our EKS cluster was running with inherited/default sizing that nobody had revisited as traffic grew. *Task:* I wanted to check whether we were over-provisioned before the team requested more cluster capacity. *Action:* I ran a proof-of-concept benchmarking resource requests, limits, and replica counts against actual traffic, then right-sized the configuration based on what I found. *Result:* A 20% improvement in cluster resource utilization without adding a single node — a concrete cost and efficiency win I could point back to.

**47. Describe a situation where you had to reduce risk in a production deployment.**
*Situation:* Releases to a production banking application carried real risk of downtime if something went wrong. *Task:* Reduce that risk without slowing delivery to a crawl. *Action:* I implemented Blue-Green deployments for major releases and Canary rollouts for smaller, lower-risk changes, gating traffic shifts on health checks. *Result:* Releases could be rolled back instantly if something broke, and canary testing caught problems on a small slice of traffic before they reached every user.

**48. Tell me about a time you had to work with limited information or an ambiguous requirement.**
*Situation:* Early infrastructure design decisions (like environment separation for Dev/QA/Prod) often weren't fully specified upfront. *Task:* Design a Terraform module structure that would still hold up as requirements got clearer. *Action:* I built modules around clear separations of concern (networking, compute, IAM) with variables for anything environment-specific, rather than hardcoding assumptions — a structure flexible enough to absorb changes without a rewrite. *Result:* When environment-specific requirements did solidify, they slotted into the existing module structure through `tfvars` changes rather than requiring rework.

**49. Give an example of when you had to balance speed of delivery against doing things the "right" way.**
*Situation:* CI/CD pipeline improvements at CBA needed to ship reasonably quickly, but cutting corners on automation would just recreate the manual-intervention problem I was trying to remove. *Task:* Improve pipeline efficiency without introducing new fragility. *Action:* I prioritized automating the steps with the highest manual burden and error rate first, rather than trying to perfect every stage at once, so wins landed incrementally and could be validated in production before moving to the next stage. *Result:* Delivery reliability improved and manual intervention dropped, without a long delay waiting for a "perfect" end-to-end redesign.

**50. Why did you move from a general DevOps role to increasingly infrastructure-and-cloud-focused work over your 4+ years?**
I found the infrastructure and platform layer — Terraform, Kubernetes, CI/CD design — was where I could have the most leverage: a well-designed pipeline or a properly modularized Terraform setup doesn't just solve one problem, it changes how every future deployment or environment gets built. Working across two different banking clients also showed me how much compliance, security posture, and reliability requirements shape infrastructure decisions in regulated environments, which pushed me to go deeper on things like IAM scoping, image hardening, and deployment strategies that minimize risk — rather than staying purely at the application/support layer.

---

*Tip: For any technical "walk me through X" question, structure your answer as Context → What you built or decided → Why you chose that approach → Outcome/impact. For behavioral questions, stick to the STAR shape (Situation, Task, Action, Result) and keep the Result concrete wherever your resume gives you a number to point to.*

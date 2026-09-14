Version 1 — Standard (2 minutes — use this most)
"Good morning. Thank you for this opportunity.

My name is Prabal Mishra and I am a DevOps
Engineer with 4+ years of hands-on experience
at Tata Consultancy Services where I have
worked for two major banking clients —
Citibank and Commonwealth Bank of Australia.

My core expertise spans the full DevOps
lifecycle — from infrastructure provisioning
using Terraform on AWS and Azure, to building
and managing CI/CD pipelines with Jenkins,
GitHub Actions, and Tekton, to deploying
and operating containerized microservices
on Kubernetes clusters including EKS and AKS.

On the security side I have embedded
DevSecOps practices across delivery pipelines
including SAST/DAST scanning, secrets
management, vulnerability scanning, and
compliance automation — achieving zero
production security incidents.

For observability I have integrated the
full monitoring stack — Prometheus, Grafana,
ELK Stack, Datadog, and Splunk — enabling
proactive alerting and faster root cause
analysis for production incidents.

Two specific achievements I am proud of:
I improved Kubernetes cluster resource
utilization by 20% through an Ingress
Controller optimization POC, and reduced
Java Maven pipeline build times by 20%
through intelligent caching and
parallelization strategies.

I work in Agile and Scrum environments
and have experience with GitOps, SRE
principles, and multi-cloud deployments
across AWS and Azure simultaneously.

I am excited about this opportunity and
look forward to discussing how my experience
can contribute to your team."
Version 2 — Short (1 minute)
"Good morning. My name is Prabal Mishra.

I am a DevOps Engineer at TCS with 4+
years of experience supporting Citibank
and Commonwealth Bank of Australia.

My expertise is in Kubernetes, Terraform,
CI/CD pipelines with Jenkins and GitHub
Actions, DevSecOps, and multi-cloud
infrastructure on AWS and Azure.

Key achievements: 20% Kubernetes resource
optimization, 20% Maven build speed
improvement, zero-downtime deployments
using Blue-Green and Canary strategies,
and full DevSecOps pipeline integration
with zero production security incidents.

I look forward to our discussion."
Version 3 — Senior Role (2.5 minutes)
"Good morning. My name is Prabal Mishra.

I bring 4+ years of enterprise DevOps
experience from TCS where I have operated
in some of the most demanding banking
environments in the world — Citibank
globally and Commonwealth Bank of Australia.

What differentiates my profile is the
combination of depth across the entire
DevOps toolchain and real production
experience in financial services where
uptime, security, and compliance are
non-negotiable.

On infrastructure I design and deploy
using Terraform across AWS and Azure —
everything from VPCs, IAM, EKS clusters
to Lambda and serverless architectures.
I manage multi-cloud environments
simultaneously with consistent IaC
practices and cost optimization built in.

On Kubernetes I go beyond basic deployment —
I manage cluster upgrades, node pool
management, Ingress controller configuration,
and operate Istio service mesh for mTLS,
traffic management, and resilience patterns.

On CI/CD I build pipelines that are not
just automated but security-embedded —
SAST/DAST at every stage, quality gates,
artifact management with JFrog Artifactory
and Nexus, and compliance checks
baked into the delivery workflow.

For observability I have built and
operated the full stack: Prometheus
and Grafana for metrics, ELK for
centralized logging, Datadog for
APM, and OpenTelemetry for
distributed tracing with Jaeger.

My numbers: 20% Kubernetes resource
improvement, 20% faster build pipelines,
zero security incidents post-DevSecOps
integration, and zero-downtime deployments
across multi-cloud with Blue-Green
and Canary strategies.

I am looking for an environment where
I can continue to push boundaries on
cloud-native architecture and I believe
this role offers exactly that.
I look forward to our conversation."
50 INTERVIEW QUESTIONS AND ANSWERS
SECTION 1 — CI/CD PIPELINES (Q1-Q10)

Q1: Walk me through a CI/CD pipeline you have built end to end

Answer:
"I will walk you through the pipeline
I built at Citibank using Jenkins
and integrated with our Kubernetes
deployment on EKS.

STAGE 1: Source Control Trigger
→ Developer pushes code to GitHub
→ Webhook triggers Jenkins pipeline
→ Branch strategy: feature branches
  merge to develop, develop to main
→ Pipeline starts automatically

STAGE 2: Build
→ Maven builds the Java application
→ Dependency caching enabled
  (reduced build time by 20% at CBA)
→ Unit tests run in parallel
→ Build artifact created as JAR

STAGE 3: Code Quality Gate
→ SonarQube SAST scan runs
→ Quality gate: must pass threshold
  (coverage %, code smells, bugs)
→ Pipeline fails if gate not passed
→ No exceptions in production branch

STAGE 4: Security Scanning
→ SAST: SonarQube static analysis
→ Dependency scan: OWASP
  Dependency Check for CVEs
→ Secret scanning: detect
  hardcoded credentials
→ Pipeline fails on critical findings

STAGE 5: Docker Build and Scan
→ Docker image built from Dockerfile
→ Trivy container image scan
→ Image must pass before push
→ Image tagged: app:git-commit-sha

STAGE 6: Artifact Push
→ Docker image pushed to
  JFrog Artifactory or ECR
→ Image promoted to staging registry
→ Build metadata stored in Nexus

STAGE 7: Deploy to Staging
→ Helm chart updated with new image tag
→ kubectl apply or helm upgrade
→ Kubernetes rolling update in staging
→ Health checks verify pods running

STAGE 8: Integration Tests
→ Automated regression tests run
→ API tests via Postman/Newman
→ Performance baseline check

STAGE 9: Approval Gate (Production)
→ Manual approval required
→ Release manager approves
→ Change ticket number required

STAGE 10: Production Deploy
→ Blue-Green or Canary strategy
→ Traffic shifted gradually
→ Monitoring alerts watched live
→ Automated rollback on error rate spike

STAGE 11: Post Deploy Verification
→ Smoke tests run automatically
→ Prometheus alerts checked
→ Pipeline marks build as Successful

Total pipeline time: approximately
25-35 minutes for full run."

Q2: What is the difference between Jenkins, GitHub Actions, and Tekton?

Answer:
"I have used all three in production
and each has distinct characteristics.

JENKINS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Type: Self-hosted CI/CD server
Deployment: Runs on your own server
  or VM — you manage it

Strengths:
→ Most mature and feature-rich
→ Huge plugin ecosystem (1800+ plugins)
→ Very flexible — can integrate
  with almost anything
→ Works well for complex pipelines
→ Good for legacy enterprise environments
→ Full control over execution environment

Weaknesses:
→ Requires maintenance (upgrades,
  plugin management, security patches)
→ UI feels dated compared to modern tools
→ Groovy DSL has learning curve
→ Can become complex to maintain

Jenkinsfile example:
pipeline {
  agent any
  stages {
    stage('Build') {
      steps { sh 'mvn clean package' }
    }
    stage('Test') {
      steps { sh 'mvn test' }
    }
    stage('Deploy') {
      steps { sh './deploy.sh' }
    }
  }
}

I used Jenkins at Citibank for complex
multi-stage enterprise pipelines.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

GITHUB ACTIONS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Type: Cloud-native, GitHub-integrated CI/CD
Deployment: Runs on GitHub-hosted runners
  or self-hosted runners

Strengths:
→ Native GitHub integration —
  triggers on any GitHub event
→ No server to maintain
→ YAML-based — easy to read
→ Marketplace with 15,000+ actions
→ Free for public repos
→ Excellent for cloud-native workflows
→ Matrix builds for parallel testing

Weaknesses:
→ Tightly coupled to GitHub
→ Less flexible for complex enterprise
  multi-system pipelines
→ Costs can grow with large teams

I used GitHub Actions at CBA —
reduced complexity significantly
compared to managing Jenkins.

YAML example:
on: [push]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Build
        run: mvn clean package
      - name: Deploy
        run: ./deploy.sh
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

TEKTON:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Type: Kubernetes-native CI/CD framework
Deployment: Runs as Kubernetes CRDs
  (Custom Resource Definitions)

Strengths:
→ Cloud-native — runs IN Kubernetes
→ Highly scalable (uses K8s pods)
→ Reusable Tasks and Pipelines
→ Perfect for GitOps workflows
→ No external server needed
→ CNCF graduated project

Weaknesses:
→ Steeper learning curve
→ Requires Kubernetes knowledge
→ Less out-of-box integrations
  compared to Jenkins

I used Tekton at Citibank for
Kubernetes-native deployments where
the pipeline runs as pods in the
same cluster — very clean architecture.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

When to use which:
Legacy enterprise → Jenkins
GitHub-centric teams → GitHub Actions
Kubernetes-native → Tekton"

Q3: What is the difference between Blue-Green and Canary deployment?

Answer:
"Both are zero-downtime deployment
strategies and I have implemented
both in production at Citibank.

BLUE-GREEN DEPLOYMENT:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Concept:
→ Two identical production environments:
  Blue = currently live (old version)
  Green = new version deployed to
→ All traffic goes to Blue
→ Deploy new version to Green
→ Run tests on Green
→ Switch ALL traffic from Blue to Green
→ Blue becomes standby for rollback

How it works:
Blue environment (v1.0): 100% traffic
Deploy v2.0 to Green
Test Green thoroughly
Switch load balancer: 100% to Green
Green (v2.0): 100% traffic
Blue (v1.0): standby

Traffic switch in Kubernetes:
Change service selector:
selector:
  app: myapp
  version: green  # was: blue

Rollback: switch selector back to blue
→ Instant rollback — one command

Advantages:
→ Zero downtime
→ Instant rollback capability
→ Full testing before traffic switch
→ Clean cutover

Disadvantages:
→ Requires 2x infrastructure (costly)
→ All-or-nothing traffic switch
→ Stateful applications are complex
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

CANARY DEPLOYMENT:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Concept:
→ Gradually shift traffic to new version
→ Monitor closely at each stage
→ Increase traffic if metrics are good
→ Rollback fast if metrics degrade

Traffic progression:
Stage 1: 5% to v2.0,  95% to v1.0
Stage 2: 20% to v2.0, 80% to v1.0
Stage 3: 50% to v2.0, 50% to v1.0
Stage 4: 100% to v2.0

Istio traffic splitting (I used this):
apiVersion: networking.istio.io/v1alpha3
kind: VirtualService
spec:
  http:
  - route:
    - destination:
        host: myapp
        subset: v1
      weight: 90
    - destination:
        host: myapp
        subset: v2
      weight: 10

Advantages:
→ Real user traffic validates new version
→ Limited blast radius if issues occur
→ Gradual confidence building
→ A/B testing capability

Disadvantages:
→ More complex to manage
→ Both versions run simultaneously
→ Stateful sessions need sticky routing
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

When I use which:
→ Blue-Green: Major releases, database
  schema changes, high-risk deploys
→ Canary: Feature releases, performance
  changes, UI updates where gradual
  rollout reduces risk"

Q4: How do you implement DevSecOps in a CI/CD pipeline?

Answer:
"DevSecOps means security is built
into every stage — not bolted on
at the end. This is exactly what
I implemented at Citibank achieving
zero production security incidents.

Security at each stage:

STAGE 1: Pre-commit (Developer machine)
→ Pre-commit hooks:
  - Secret detection (git-secrets,
    gitleaks) — stops hardcoded
    credentials before they are committed
  - Lint checks for security patterns

STAGE 2: Source Code (SAST)
→ Static Application Security Testing
→ SonarQube scans for:
  SQL injection vulnerabilities
  XSS vulnerabilities
  Insecure cryptography
  Security hotspots
→ Quality gate: pipeline fails on
  Critical or High findings

STAGE 3: Dependencies
→ OWASP Dependency Check
→ Snyk for known CVEs in libraries
→ Block on Critical CVEs
→ Example: Log4Shell (CVE-2021-44228)
  would have been caught here

STAGE 4: Container Image (SAST)
→ Trivy image scanner
→ Scans base image AND application layers
→ Block on Critical and High CVEs
→ Enforce approved base images only
  (no ubuntu:latest — must use
  specific pinned versions)

STAGE 5: Infrastructure as Code
→ Checkov scans Terraform code
→ Catches misconfigurations:
  S3 bucket with public access
  Security group open to 0.0.0.0/0
  Unencrypted RDS instances
→ Blocks pipeline if IaC violations found

STAGE 6: Secrets Management
→ NO secrets in code or environment variables
→ AWS Secrets Manager or
  HashiCorp Vault for all secrets
→ Kubernetes Secrets sealed with
  Sealed Secrets or External Secrets
→ Secrets rotation automated

STAGE 7: Runtime Security
→ Kubernetes Pod Security Standards
→ Non-root containers enforced
→ Read-only root filesystem
→ Falco for runtime threat detection

STAGE 8: Compliance
→ OPA (Open Policy Agent) for
  policy-as-code enforcement
→ All deployments must meet
  defined compliance policies
→ Automated evidence generation
  for audit

Result at Citibank:
Zero production security incidents
after full DevSecOps integration."

Q5: How do you manage artifacts and what is the difference between Nexus and JFrog Artifactory?

Answer:
"Artifact management is a critical
part of any enterprise CI/CD pipeline.
I have used both tools in production.

What is artifact management:
→ Store build outputs centrally
→ Version and promote artifacts
→ Avoid rebuilding same artifact
→ Single source of truth for releases
→ Scan artifacts for vulnerabilities
→ Control what reaches production

NEXUS REPOSITORY MANAGER:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
→ Open source (free) and Pro versions
→ Supports: Maven, npm, Docker,
  PyPI, NuGet, Helm charts, raw
→ Proxy repositories:
  Cache external dependencies locally
  (Maven Central, Docker Hub)
  Faster builds + control what
  developers can pull

I used Nexus at CBA for:
→ Maven JAR artifact storage
→ Docker image registry
→ Proxying Maven Central
  (builds never hit internet)

→ Lighter weight than Artifactory
→ Good for simpler setups
→ Free version is capable

JFROG ARTIFACTORY:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
→ Enterprise-grade artifact manager
→ More features than Nexus
→ Supports: same formats as Nexus
  plus more
→ Built-in Xray security scanning
  (deep CVE analysis of all artifacts)
→ Release lifecycle management:
  Promote artifact from DEV → QA → PROD
→ Distribution: deploy to remote
  edge nodes globally

I used JFrog Artifactory at Citibank for:
→ Full release lifecycle
→ Xray scanning every Docker image
  before promotion
→ Helm chart repository
→ Binary promotion between environments

Key difference summary:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Feature          Nexus       JFrog Artifactory
Cost             Free/Pro    Enterprise (costly)
Security         Basic       Advanced (Xray)
Promotion        Manual      Built-in lifecycle
Enterprise       Good        Excellent
Complexity       Lower       Higher

For Citibank's banking compliance
requirements: JFrog Artifactory
was the right choice — every artifact
scanned and traceable from build to prod."

Q6: How do you optimise a slow CI/CD pipeline?

Answer:
"Pipeline optimization is something
I directly delivered — improved
Maven pipeline speed by 20% at CBA.

Here is my systematic approach:

STEP 1: Measure first
→ Do not guess — instrument the pipeline
→ Note time for each stage:
  Checkout: 30s
  Build: 8 min
  Test: 15 min  ← bottleneck
  Docker build: 4 min
  Push: 2 min
  Deploy: 3 min
  Total: 32 min

STEP 2: Dependency caching
→ Most impactful optimization
→ Maven dependencies downloaded
  every build = massive waste

Jenkins pipeline cache:
cache:
  key: $CI_COMMIT_REF_SLUG
  paths:
    - ~/.m2/repository
    - node_modules/

→ First run: downloads everything
→ Subsequent runs: uses cache
→ Impact at CBA: 8 min build
  reduced to 3 min (dependencies cached)

STEP 3: Parallel execution
→ Identify independent stages
→ Run them simultaneously

Jenkins parallel:
stage('Parallel Tests') {
  parallel {
    stage('Unit Tests') {
      steps { sh 'mvn test' }
    }
    stage('Security Scan') {
      steps { sh 'trivy scan' }
    }
    stage('Code Quality') {
      steps { sh 'sonar-scanner' }
    }
  }
}

→ 3 stages in parallel instead of series
→ Time = longest stage not sum of all

STEP 4: Optimise Docker builds
→ Order Dockerfile layers correctly
  (less-changing layers first)
→ Use multi-stage builds
→ Use .dockerignore aggressively
→ Use smaller base images:
  alpine instead of ubuntu
  distroless for production

STEP 5: Selective testing
→ Run unit tests always
→ Run integration tests only on
  merge to main or specific flag
→ Use test impact analysis:
  only run tests for changed modules

STEP 6: Optimise artifact push
→ Push only when tests pass
→ Use layer caching in registry

Results at CBA:
Before: 32 minute total pipeline
After: 26 minutes (20% improvement)
Key wins: Maven caching + parallel stages"

Q7: What are Quality Gates in a CI/CD pipeline?

Answer:
"Quality Gates are automated checkpoints
in the pipeline that must pass before
the code can proceed to the next stage.
They enforce standards automatically —
no human can bypass them.

Types of Quality Gates I implement:

CODE QUALITY GATE (SonarQube):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Conditions we enforce:
→ Code coverage >= 80%
  (new code must be tested)
→ No new Critical or Blocker bugs
→ No new Critical security hotspots
→ Technical debt ratio < 5%
→ Duplicated lines < 3%

If any condition fails:
→ Pipeline stops at this stage
→ Build marked FAILED
→ Developer gets notification
→ Cannot merge to main
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SECURITY GATE (SAST/DAST):
→ No Critical CVEs in dependencies
→ No Critical CVEs in Docker image
→ No hardcoded secrets detected
→ IaC must pass Checkov scan
→ Failure = pipeline stops

PERFORMANCE GATE:
→ Load test must pass
→ p95 response time < 200ms
→ Error rate < 0.1%
→ Failure = pipeline stops

COMPLIANCE GATE:
→ All required labels on containers
→ Approved base images only
→ Required security context set
→ Failure = pipeline stops

Why Quality Gates matter:
→ Enforces standards consistently
→ Removes human bias/pressure
  ('we will fix it later' is blocked)
→ Catches issues early when fix is cheap
→ Provides audit evidence for compliance

At Citibank: Quality gates were
non-negotiable for banking compliance.
Every pipeline had code quality,
security, and compliance gates.
Nothing reached production without
passing all three."

Q8: What is GitOps and how have you applied it?

Answer:
"GitOps is an operational framework
where Git is the single source of
truth for both infrastructure and
application configuration.

Core principles:
→ Entire system state defined
  declaratively in Git
→ Desired state in Git =
  actual state in cluster
→ Approved changes only through
  Git (pull requests)
→ Automated agent continuously
  reconciles actual vs desired state

How it works in practice:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Developer makes change:
→ Updates Kubernetes manifest or
  Helm values in Git repository
→ Raises Pull Request
→ Code review and approval
→ Merge to main

GitOps controller (ArgoCD/Flux):
→ Watches the Git repository
→ Detects change in main branch
→ Compares desired state (Git)
  with actual state (cluster)
→ Applies diff automatically
→ Cluster now matches Git

Drift detection:
→ If someone makes manual change
  directly in cluster (kubectl apply)
→ GitOps controller detects drift
→ Automatically reverts to
  Git state (desired state wins)
→ No snowflake environments
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Benefits I have seen:
→ Full audit trail: every change
  is a Git commit with author,
  message, and reviewer
→ Rollback = git revert
  (instant, reliable)
→ Environment consistency:
  dev/staging/prod all defined
  in Git — no configuration drift
→ Disaster recovery: lose a cluster,
  redeploy from Git in minutes

My application at Citibank:
→ All Kubernetes manifests in Git
→ Helm values per environment in Git
→ Terraform state referenced from Git
→ Any change via PR — reviewed,
  approved, traceable
→ No direct kubectl in production
  — all changes via GitOps"

Q9: What is a Helm chart and how do you use it?

Answer:
"Helm is the package manager for
Kubernetes — Helm charts are
reusable templates for Kubernetes
applications.

Without Helm:
→ Maintain separate YAML files for
  every environment (dev/staging/prod)
→ 10 services × 4 files × 3 envs
  = 120 YAML files to manage
→ Manual updates everywhere when
  image tag changes

With Helm:
→ One chart template
→ Values files per environment
→ Change one value → all refs updated

Helm chart structure:
myapp/
  Chart.yaml        # metadata
  values.yaml       # default values
  values-prod.yaml  # prod overrides
  templates/
    deployment.yaml
    service.yaml
    ingress.yaml
    configmap.yaml
    hpa.yaml

Template example (deployment.yaml):
apiVersion: apps/v1
kind: Deployment
spec:
  replicas: {{ .Values.replicas }}
  template:
    spec:
      containers:
      - name: myapp
        image: {{ .Values.image.repo }}:
               {{ .Values.image.tag }}
        resources:
          requests:
            cpu: {{ .Values.resources.cpu }}
            memory: {{ .Values.resources.memory }}

values.yaml (defaults):
replicas: 1
image:
  repo: myapp
  tag: latest
resources:
  cpu: 100m
  memory: 128Mi

values-prod.yaml (overrides):
replicas: 5
image:
  tag: v2.4.1
resources:
  cpu: 500m
  memory: 512Mi

Deploy commands I use:
helm install myapp ./myapp
  -f values-prod.yaml
  --namespace production

helm upgrade myapp ./myapp
  -f values-prod.yaml
  --set image.tag=v2.4.2

helm rollback myapp 1
  (rollback to previous release)

helm list -n production
  (list all releases)

At Citibank I developed and maintained
Helm charts for all microservices —
significantly reduced deployment
complexity and drift between environments."

Q10: What is Nexus/JFrog used for and how does artifact promotion work?

Answer:
"Artifact promotion is the process
of moving a validated artifact through
environments — ensuring the exact
same binary that passed all tests
reaches production.

The key principle:
BUILD ONCE — PROMOTE MANY TIMES

Never rebuild for each environment.
Rebuild = potential inconsistency.
Promote = guaranteed consistency.

Promotion flow I implemented:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. CI pipeline builds artifact:
   myapp:abc123 (git commit SHA as tag)
   → Pushed to: artifactory/dev-repo

2. Unit and integration tests pass:
   → Artifact promoted to:
     artifactory/qa-repo
   → Tag: myapp:abc123 (same artifact)

3. QA tests pass + security scan:
   → Artifact promoted to:
     artifactory/staging-repo
   → JFrog Xray scan runs here

4. Staging tests + approval:
   → Artifact promoted to:
     artifactory/prod-repo
   → Tag: myapp:v2.4.1 (release tag)

5. Production deployment:
   → Pulls from prod-repo only
   → Never from dev-repo or staging-repo

Why this matters:
→ Immutable artifacts — same bits
  deployed everywhere
→ Full traceability: which commit,
  who built it, which tests passed
→ Production can ONLY deploy
  artifacts that passed all gates
→ Rollback = promote previous
  artifact back to prod-repo

At Citibank for banking compliance:
→ Every artifact has full lineage
→ Auditors can trace any production
  binary back to its source commit
→ JFrog Xray CVE report attached
  to every promoted artifact
→ This is required for SOX compliance"
SECTION 2 — KUBERNETES & CONTAINERS (Q11-Q20)

Q11: Explain your Kubernetes experience in detail

Answer:
"Kubernetes is one of my strongest
areas — I manage EKS on AWS and
AKS on Azure in production at Citibank.

My day-to-day Kubernetes work:

CLUSTER MANAGEMENT:
→ Cluster provisioning with Terraform
  (eksctl or Terraform AWS provider)
→ Node group management:
  on-demand for critical workloads
  spot instances for batch/non-critical
→ Cluster upgrades:
  Blue-Green cluster upgrade strategy
  New cluster version deployed,
  workloads migrated, old cluster removed
→ RBAC configuration:
  Roles, RoleBindings, ClusterRoles
  Integrated with AWS IAM via IRSA

WORKLOAD MANAGEMENT:
→ Deployments, StatefulSets, DaemonSets
→ HPA (Horizontal Pod Autoscaler):
  Scale based on CPU/memory/custom metrics
→ VPA (Vertical Pod Autoscaler):
  Right-size container resources
→ Pod Disruption Budgets:
  Minimum availability during updates
→ Resource requests and limits:
  Every pod has both — no unbounded pods

NETWORKING:
→ Ingress controllers (Nginx, ALB)
→ Ingress Controller optimization:
  Reduced resource waste by 20%
→ Network Policies: pod-to-pod firewall
→ Service mesh with Istio:
  mTLS between all services
  Traffic management rules
  Circuit breaking
  Observability with Kiali/Jaeger

STORAGE:
→ PersistentVolumes and PVCs
→ StorageClasses for EBS and EFS
→ StatefulSet persistent storage

SECURITY:
→ Pod Security Standards enforced
→ Non-root containers
→ Read-only root filesystems
→ Secrets management via
  External Secrets Operator
→ Image pull from approved registry only

MONITORING:
→ Prometheus operator installed
→ ServiceMonitors for each application
→ Grafana dashboards per namespace"

Q12: What is Istio and how have you used it?

Answer:
"Istio is a service mesh that adds
observability, security, and traffic
management to Kubernetes without
changing application code.

What Istio adds:
→ Sidecar proxy (Envoy) injected
  into every pod automatically
→ All traffic flows through proxies
→ Control plane manages all proxies

KEY FEATURES I USE:

MTLS (Mutual TLS):
→ All service-to-service communication
  encrypted automatically
→ No code changes needed
→ Certificate rotation automated
→ Critical for banking compliance

PeerAuthentication policy:
apiVersion: security.istio.io/v1beta1
kind: PeerAuthentication
metadata:
  name: default
  namespace: production
spec:
  mtls:
    mode: STRICT  # all traffic must be mTLS

TRAFFIC MANAGEMENT:
→ Canary deployments via VirtualService
→ Traffic splitting (90/10, 50/50)
→ Retry policies:
  Retry failed requests 3 times
  Timeout after 5 seconds
→ Circuit breaking:
  Stop sending requests to
  unhealthy service instances

VirtualService example:
spec:
  http:
  - retries:
      attempts: 3
      perTryTimeout: 2s
    route:
    - destination:
        host: myservice
        subset: v1
      weight: 90
    - destination:
        host: myservice
        subset: v2
      weight: 10

OBSERVABILITY with Kiali:
→ Service topology visualization
→ See real-time traffic flow
→ Identify which service is failing
→ Latency between services visible

DISTRIBUTED TRACING with Jaeger:
→ Trace a request across 10 microservices
→ See exactly where time is spent
→ Identify bottlenecks in service chain

At Citibank:
→ Istio deployed across EKS clusters
→ Strict mTLS mode for all services
→ Traffic policies for each microservice
→ Kiali for ops team visualization
→ Critical for zero-trust security model"

Q13: How did you optimize Kubernetes Ingress Controller by 20%?

Answer:
"This was a POC I led at Citibank
that I am particularly proud of
because it started from an observation
and ended with a measurable improvement
presented to senior stakeholders.

THE PROBLEM I OBSERVED:
→ Nginx Ingress Controller pods were
  consuming 40% of CPU and memory
  on the nodes they ran on
→ Actual traffic routing was simple —
  did not warrant that resource usage
→ This was limiting how many
  application pods we could schedule

INVESTIGATION:
Step 1: Metrics analysis
→ Checked Prometheus metrics for
  Ingress controller pods
→ Found: worker processes were
  over-provisioned
→ Default config had 4 worker
  processes but traffic did not
  justify this

Step 2: Configuration review
→ Reviewed nginx Ingress ConfigMap
→ Found several sub-optimal settings:
  worker-processes: auto (took 4 CPUs)
  upstream keep-alive connections: 0
  (new connection per request)
  Buffer sizes: over-configured

Step 3: Optimizations applied in POC environment:
worker-processes: 2
  (right-sized for our traffic volume)

upstream keepalive: 100
  (reuse connections to backends)

proxy-buffer-size: 4k
  (reduced from 8k — sufficient
  for our response headers)

enable-brotli: true
  (better compression than gzip)

load-balance: least_conn
  (better distribution than round-robin)

Step 4: Results measured:
CPU usage: 40% → 22% (45% reduction)
Memory: reduced by 30%
Request latency: improved 8ms avg
Cluster node capacity for app pods:
  increased by 20%

Step 5: Presented to stakeholders
→ Before/after metrics graphs
→ Cost savings calculation
→ Recommended rolling to production

Result: Approved and implemented.
20% more pods schedulable per node
= effectively 20% more cluster capacity
without adding nodes = cost saving."

Q14: What is the difference between a Deployment and a StatefulSet in Kubernetes?

Answer:
"This is a fundamental Kubernetes
concept and choosing wrong causes
production issues.

DEPLOYMENT:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
→ For STATELESS applications
→ Pods are interchangeable
→ Pod names: myapp-xyz123 (random)
→ No stable network identity
→ No persistent storage per pod
→ Can be scaled up/down freely
→ Rolling update replaces pods randomly

Use for:
→ Web servers (Nginx, APIs)
→ Microservices
→ Worker processes
→ Any app where pods are identical

Example:
→ 3 replicas of an API service
→ Any pod can handle any request
→ Load balancer distributes randomly
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STATEFULSET:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
→ For STATEFUL applications
→ Pods have stable identity
→ Pod names: mydb-0, mydb-1, mydb-2
  (ordered, predictable)
→ Stable network identity:
  mydb-0.mydb.default.svc.cluster.local
→ Each pod gets its OWN persistent volume
→ Ordered deployment and scaling
→ Ordered rolling updates (one at a time)

Use for:
→ Databases (MySQL, PostgreSQL, MongoDB)
→ Message queues (Kafka, RabbitMQ)
→ Distributed systems (Elasticsearch)
→ Any app where pod identity matters

Example:
→ Kafka cluster needs:
  kafka-0 to always be the same node
  kafka-0's data to persist even
  if pod restarts
  kafka-1 to know it can reach
  kafka-0 at stable DNS name
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

KEY DIFFERENCES:
Feature          Deployment        StatefulSet
Pod names        Random suffix     Ordered (0,1,2)
Network identity Unstable          Stable DNS
Storage          Shared or none    Per-pod PVC
Scaling          Any order         Ordered
Updates          Random            Ordered
Use case         Stateless         Stateful

At Citibank:
→ Deployments for all microservices
→ StatefulSets for Kafka message
  queues and Redis cluster
→ Choosing wrong = data loss"

Q15: How do you manage Kubernetes secrets securely?

Answer:
"Kubernetes native Secrets are base64
encoded — NOT encrypted. Storing them
in Git exposes credentials. This is
a critical security problem I solved
at Citibank using proper secrets management.

THE PROBLEM with native K8s Secrets:
→ kubectl get secret mysecret -o yaml
  → shows base64 encoded value
→ base64 decode = plaintext
→ Anyone with kubectl access sees secrets
→ Stored in etcd unencrypted by default
→ In GitOps: secrets in Git = disaster

MY SOLUTION at Citibank:

APPROACH 1: AWS Secrets Manager + External Secrets Operator
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
→ Secrets stored in AWS Secrets Manager
→ External Secrets Operator installed in K8s
→ ExternalSecret resource defined:

apiVersion: external-secrets.io/v1beta1
kind: ExternalSecret
metadata:
  name: db-credentials
spec:
  refreshInterval: 1h
  secretStoreRef:
    name: aws-secrets-manager
    kind: ClusterSecretStore
  target:
    name: db-credentials  # creates K8s secret
  data:
  - secretKey: password
    remoteRef:
      key: prod/myapp/db
      property: password

→ ESO fetches secret from AWS SM
→ Creates K8s Secret automatically
→ Refreshes every 1 hour
→ Rotation in AWS SM = automatic
  pod refresh

APPROACH 2: HashiCorp Vault
→ Vault Agent Injector as sidecar
→ Secrets injected into pod filesystem
→ Never stored in K8s etcd at all

APPROACH 3: Sealed Secrets
→ kubeseal CLI encrypts the secret
→ Encrypted SealedSecret stored in Git
→ Controller decrypts in cluster only
→ Safe for GitOps — encrypted in repo

Secrets rotation:
→ AWS SM supports automatic rotation
→ Lambda function rotates DB password
→ External Secrets picks up new value
→ Application restarts to get new secret
→ Zero manual rotation needed"

Q16: What is a DaemonSet and when do you use it?

Answer:
"A DaemonSet ensures that a specific
pod runs on EVERY node in the cluster
(or a selected subset of nodes).

When you add a node: DaemonSet
pod automatically scheduled on it.
When you remove a node: DaemonSet
pod automatically cleaned up.

Use cases (I use all of these):

LOG COLLECTION:
→ Fluentd or Fluent Bit DaemonSet
→ Runs on every node
→ Collects logs from all containers
→ Ships to Elasticsearch/Splunk

NODE MONITORING:
→ Prometheus Node Exporter DaemonSet
→ Runs on every node
→ Collects CPU, memory, disk metrics
  for that specific node
→ Prometheus scrapes each Node Exporter

NETWORKING:
→ Calico or Flannel CNI plugin
→ Must run on every node
  to provide pod networking
→ Without this: pods cannot communicate

SECURITY:
→ Falco DaemonSet
→ Runtime security monitoring
→ Must be on every node to monitor
  all container syscalls

NODE AGENT:
→ AWS Node Termination Handler
→ Watches for EC2 spot interruptions
→ Gracefully drains node before termination

DaemonSet vs Deployment:
→ Deployment: I decide replica count
  (scale: 3, scale: 10)
→ DaemonSet: One pod per node
  automatically — I do not set replicas

At Citibank DaemonSets I managed:
→ Fluent Bit: log collection to ELK
→ Node Exporter: Prometheus metrics
→ Datadog Agent: APM and metrics
→ Falco: runtime security
→ AWS VPC CNI: pod networking"

Q17: How do you handle pod autoscaling in Kubernetes?

Answer:
"Autoscaling is critical for
handling variable traffic in
banking applications.

THREE TYPES OF AUTOSCALING:

HPA — Horizontal Pod Autoscaler:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
→ Scales number of pod REPLICAS
→ Based on: CPU, memory,
  or custom metrics (requests/sec)
→ Most commonly used

HPA configuration:
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: myapp-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: myapp
  minReplicas: 2
  maxReplicas: 20
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70

→ When avg CPU > 70%: scale up
→ When avg CPU < 70%: scale down
→ Always minimum 2 pods for HA
→ Maximum 20 pods (cost control)

VPA — Vertical Pod Autoscaler:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
→ Adjusts CPU and memory REQUESTS
  for existing pods
→ Right-sizes containers automatically
→ Recommends or auto-applies changes

I use VPA in recommendation mode:
→ VPA analyzes actual usage
→ Recommends better resource requests
→ I review and apply
→ Prevents over-provisioning
  and under-provisioning

KEDA — Kubernetes Event-Driven Autoscaling:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
→ Scale based on external metrics
→ Examples:
  Scale based on SQS queue depth
  Scale based on Kafka lag
  Scale based on Prometheus metric
  Scale to ZERO when no messages

I use KEDA for batch processing:
→ Consumer pods scale to 0 when idle
→ Scale up when messages arrive
→ Cost saving: zero pods = zero cost
  during quiet periods

At Citibank combination:
→ HPA for API services (CPU-based)
→ VPA recommendations for right-sizing
→ KEDA for event-driven consumers"

Q18: How do you troubleshoot a pod that is not starting?

Answer:
"Pod not starting is one of the
most common Kubernetes issues.
Systematic approach every time.

STEP 1: Check pod status
kubectl get pods -n namespace
→ Look at STATUS column:
  Pending: not scheduled yet
  CrashLoopBackOff: crashing repeatedly
  ImagePullBackOff: cannot pull image
  OOMKilled: out of memory
  Error: exited with error
  Running/0/1: container not ready

STEP 2: Describe the pod
kubectl describe pod pod-name -n namespace
→ Look at: Events section at bottom
→ This tells you EXACTLY what failed:
  'Failed to pull image':
    → Wrong image name, tag, or registry
    → Image pull secret missing
  'Insufficient cpu/memory':
    → Node does not have enough resources
    → Need to scale cluster
  'FailedScheduling':
    → No nodes match pod requirements
    → Check nodeSelector/affinity
  'Liveness probe failed':
    → App started but health check failing

STEP 3: Check logs
kubectl logs pod-name -n namespace
→ Application logs — what did app print?
→ If container keeps crashing:
kubectl logs pod-name --previous
  (logs from previous crashed container)

STEP 4: Common issues and fixes

CrashLoopBackOff:
→ Application is crashing on startup
→ Check logs: what error is app printing?
→ Common causes:
  Missing environment variable
  Cannot connect to database
  Port already in use
  Application bug on startup

ImagePullBackOff:
→ kubectl describe pod shows image pull error
→ Fix: Verify image name and tag exist
→ Fix: Create imagePullSecret if
  private registry:
  kubectl create secret docker-registry
  regcred --docker-server=registry.io
  --docker-username=user
  --docker-password=pass

OOMKilled:
→ Container exceeded memory limit
→ Fix: Increase memory limit in
  Deployment spec
→ Investigate memory leak if
  limit is already reasonable

Pending forever:
→ kubectl describe pod → Events
→ 'Insufficient memory' →
  scale cluster or reduce request
→ 'No nodes with label X' →
  fix node selector or label"

Q19: What is a Kubernetes Network Policy?

Answer:
"Network Policy is Kubernetes' firewall
for pod-to-pod communication. By default
ALL pods can talk to ALL pods — which
is a security nightmare in banking.

Without Network Policy:
→ Compromised frontend pod can
  directly query database pods
→ Any pod can reach any other pod
→ No segmentation

With Network Policy:
→ Define exactly which pods can
  communicate with which
→ Default deny all → explicitly allow

Default deny all policy
(I apply this first in every namespace):
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny-all
  namespace: production
spec:
  podSelector: {}  # applies to all pods
  policyTypes:
  - Ingress
  - Egress

Then explicitly allow what is needed:
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-frontend-to-api
spec:
  podSelector:
    matchLabels:
      app: api-service
  ingress:
  - from:
    - podSelector:
        matchLabels:
          app: frontend
    ports:
    - protocol: TCP
      port: 8080

This means:
→ Only pods with label app: frontend
  can reach app: api-service on port 8080
→ Database pods not reachable from frontend
→ Explicit allow required for each path

At Citibank:
→ Default deny all in every namespace
→ Explicit policies for each service pair
→ Required for PCI-DSS and banking
  security compliance
→ Istio mTLS + Network Policy = defense
  in depth for zero-trust networking"

Q20: What is the difference between a ConfigMap and a Secret in Kubernetes?

Answer:
"Both inject configuration into pods
but for different types of data.

CONFIGMAP:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
→ Non-sensitive configuration data
→ Stored as PLAIN TEXT in etcd
→ Visible to anyone with kubectl access
→ Safe to store in Git (no secrets)

Use for:
→ Application configuration files
→ Environment-specific settings
→ Database hostnames and ports
  (NOT passwords)
→ Feature flags
→ Log levels

Creating ConfigMap:
kubectl create configmap app-config
  --from-literal=DB_HOST=db.prod.svc
  --from-literal=LOG_LEVEL=INFO
  --from-file=config.properties

Using in pod:
env:
- name: DB_HOST
  valueFrom:
    configMapKeyRef:
      name: app-config
      key: DB_HOST

OR mount as file:
volumeMounts:
- name: config
  mountPath: /app/config
volumes:
- name: config
  configMap:
    name: app-config
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SECRET:
→ Sensitive data
→ Base64 encoded (NOT encrypted by default)
→ Should be encrypted at rest with KMS
→ More restricted access via RBAC
→ Do NOT store in Git unencrypted

Use for:
→ Passwords
→ API keys and tokens
→ TLS certificates
→ SSH keys
→ OAuth credentials

As mentioned in Q15: I use External
Secrets Operator or Sealed Secrets
rather than native K8s secrets
for proper security.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Key rule I follow:
→ ConfigMap: anything you would put
  in a config file (not sensitive)
→ Secret: anything you would not
  want visible in plain text
→ Secret stored in AWS Secrets Manager,
  NOT in Kubernetes or Git"
SECTION 3 — TERRAFORM & INFRASTRUCTURE AS CODE (Q21-Q27)

Q21: Walk me through how you use Terraform in production

Answer:
"Terraform is my primary IaC tool —
I use it to provision all cloud
infrastructure across AWS and Azure
at Citibank.

MY TERRAFORM WORKFLOW:

Project structure:
terraform/
  modules/
    vpc/
    eks-cluster/
    rds/
    iam/
  environments/
    dev/
      main.tf
      variables.tf
      terraform.tfvars
    staging/
      main.tf
      terraform.tfvars
    prod/
      main.tf
      terraform.tfvars
  global/
    s3-backend/
    iam-base/

REMOTE STATE (critical for teams):
→ State stored in S3, not locally
→ State locking with DynamoDB
→ Multiple engineers cannot apply
  at same time (prevents corruption)

backend.tf:
terraform {
  backend 's3' {
    bucket         = 'citibank-tf-state'
    key            = 'prod/eks/terraform.tfstate'
    region         = 'us-east-1'
    dynamodb_table = 'tf-state-lock'
    encrypt        = true
  }
}

MODULES for reusability:
module 'eks_cluster' {
  source       = '../../modules/eks-cluster'
  cluster_name = 'prod-cluster'
  node_type    = 't3.large'
  min_nodes    = 3
  max_nodes    = 10
  vpc_id       = module.vpc.vpc_id
}

WORKFLOW per change:
1. terraform fmt → format code
2. terraform validate → syntax check
3. terraform plan → preview changes
   (ALWAYS review plan before apply)
4. Peer review of plan output
5. terraform apply -auto-approve
   (only in CI/CD after approval)
6. Verify resources in console

DRIFT DETECTION:
→ terraform plan regularly
→ If plan shows changes but
  no code change: someone made
  manual change in console
→ Either import or fix manually
→ Manual changes are anti-pattern"

Q22: What is Terraform state and why is it important?

Answer:
"Terraform state is the most critical
concept in Terraform — misunderstanding
it causes serious production issues.

WHAT IS STATE:
→ A JSON file (terraform.tfstate)
→ Records what Terraform has created:
  Which resources exist
  Their IDs (ami-12345, i-67890)
  Their current configuration
  Relationships between resources

WHY IT EXISTS:
→ Terraform does not query AWS/Azure
  every time to find your resources
→ State is the source of truth
  for what Terraform manages
→ plan compares: code vs state
→ apply makes actual match code

WHAT HAPPENS WITHOUT STATE:
→ Terraform loses track of resources
→ Cannot update or destroy them
→ May create duplicates
→ Catastrophic for production

REMOTE STATE (I use S3):
Why not local state:
→ Only works on your laptop
→ Team cannot collaborate
→ Lost if laptop dies
→ No locking — concurrent applies
  corrupt state

S3 backend with DynamoDB locking:
→ State stored in S3
→ DynamoDB record prevents concurrent apply
→ Any team member can run Terraform
→ State versioning for recovery

STATE COMMANDS I USE:

terraform state list
→ List all resources in state

terraform state show aws_instance.web
→ Show details of specific resource

terraform import aws_instance.web i-1234567
→ Import existing resource into state
→ Used when someone created resource
  manually in AWS console

terraform state rm aws_s3_bucket.logs
→ Remove resource from state
  WITHOUT destroying it
→ Used when transferring management

terraform state mv
→ Rename resource in state

SENSITIVE DATA IN STATE:
→ State may contain passwords, keys
→ S3 bucket must be encrypted
→ Access restricted by IAM
→ Enable versioning for recovery"

Q23: What is the difference between Terraform and Ansible?

Answer:
"Both are IaC tools but they serve
fundamentally different purposes.
I use BOTH together at Citibank.

TERRAFORM:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Purpose: Infrastructure PROVISIONING
→ Creates and manages cloud resources:
  VPCs, EC2 instances, EKS clusters,
  RDS databases, S3 buckets, IAM roles

Type: Declarative
→ You describe WHAT you want
→ Terraform figures out HOW to get there
→ Plan shows the delta

State management: YES
→ Tracks what it created
→ Knows what to update vs create

Idempotent: YES
→ Run same config 10 times =
  same result every time
→ Second run: no changes if first worked

Best for:
→ Cloud infrastructure provisioning
→ Immutable infrastructure
→ Multi-cloud management
→ Network topology

Provider: 1000+ providers
(AWS, Azure, GCP, Kubernetes,
GitHub, PagerDuty...)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ANSIBLE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Purpose: Configuration MANAGEMENT
→ Configures what is already running:
  Install packages on servers
  Deploy application configs
  Manage services (start/stop)
  Apply OS patches
  Configure users and permissions

Type: Procedural (playbooks = steps)
→ You describe the STEPS to take
→ Ansible executes them in order

State management: NO
→ No state file
→ Checks current state before acting

Agentless: YES
→ Uses SSH only
→ No agent installed on target

Best for:
→ Application configuration
→ Server hardening
→ Patch management
→ Ad-hoc operations
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

HOW I USE THEM TOGETHER:
Terraform creates the EC2 instance
↓
Ansible configures the EC2 instance
(installs Java, deploys app config,
sets up monitoring agent)

Never use Ansible to create cloud
resources → use Terraform
Never use Terraform to configure
application inside a server → use Ansible"

Q24: How do you handle Terraform in a team environment?

Answer:
"Team Terraform usage without proper
controls leads to state corruption,
drift, and production disasters.

PRACTICES I IMPLEMENT:

1. Remote State with Locking:
→ S3 for state storage
→ DynamoDB for state locking
→ Only one person applies at a time
→ Encrypted state bucket

2. Terraform in CI/CD (not local):
→ Engineers submit PR with
  Terraform code changes
→ CI pipeline runs:
  terraform fmt --check (format)
  terraform validate (syntax)
  terraform plan (preview)
→ Plan output posted as PR comment
→ Review the PLAN not just code
→ Approver reviews impact
→ Merge triggers terraform apply
  in CI/CD with appropriate permissions

3. Workspace or directory per environment:
→ environments/dev/
→ environments/staging/
→ environments/prod/
→ Never use same state for
  multiple environments
→ Changes tested in dev first

4. Module versioning:
→ Modules pinned to specific versions:
  source = './modules/eks?ref=v1.2.0'
→ Prevents unexpected changes
  when module updated

5. Terraform plan review process:
→ Plan must be reviewed by
  at least one senior engineer
  before production apply
→ Look for: unexpected destroys,
  resource replacements,
  security group changes

6. Drift detection:
→ Scheduled terraform plan in CI/CD
→ Alert if plan shows drift
  (someone made manual change)
→ Zero tolerance for manual
  console changes in prod

7. Variable management:
→ Sensitive variables in
  CI/CD secrets or Vault
→ Never hardcode credentials
→ terraform.tfvars in .gitignore
  for local development"

Q25: What are Terraform modules and why do you use them?

Answer:
"Modules are reusable packages of
Terraform configuration. They are
the building blocks of well-structured
Terraform code.

WITHOUT modules:
→ Copy-paste VPC code for every environment
→ Change something → update 5 places
→ Inconsistency creeps in over time
→ Hard to maintain at scale

WITH modules:
→ Write VPC code once in a module
→ Call the module in each environment
→ Change module once → all environments
  get the update
→ Standardized, consistent resources

Module I created for EKS:
modules/eks-cluster/
  main.tf      (EKS resource definitions)
  variables.tf (input parameters)
  outputs.tf   (output values)

main.tf inside module:
resource 'aws_eks_cluster' 'this' {
  name     = var.cluster_name
  role_arn = aws_iam_role.eks.arn
  version  = var.kubernetes_version
  vpc_config {
    subnet_ids         = var.subnet_ids
    security_group_ids = [aws_security_group.eks.id]
  }
}

variables.tf:
variable 'cluster_name' {
  type        = string
  description = 'EKS cluster name'
}
variable 'node_instance_type' {
  type    = string
  default = 't3.medium'
}
variable 'min_nodes' { type = number }
variable 'max_nodes' { type = number }

Using the module in prod:
module 'prod_eks' {
  source              = '../../modules/eks-cluster'
  cluster_name        = 'citibank-prod'
  node_instance_type  = 'm5.xlarge'
  min_nodes           = 3
  max_nodes           = 20
  kubernetes_version  = '1.28'
  subnet_ids          = module.vpc.private_subnets
}

Using the same module in dev:
module 'dev_eks' {
  source              = '../../modules/eks-cluster'
  cluster_name        = 'citibank-dev'
  node_instance_type  = 't3.medium'
  min_nodes           = 1
  max_nodes           = 5
  kubernetes_version  = '1.28'
  subnet_ids          = module.vpc.private_subnets
}

Benefits I see daily at Citibank:
→ 80% less Terraform code to maintain
→ Consistent security settings
  enforced in module
→ Easier to upgrade Kubernetes version
  across all clusters: change once"

Q26: How do you manage multiple environments with Terraform?

Answer:
"Managing dev, staging, and prod
environments with Terraform requires
clear separation strategy.

MY APPROACH: Directory per environment

terraform/
  modules/          (shared modules)
  environments/
    dev/
      main.tf
      variables.tf
      terraform.tfvars  (.gitignored)
      backend.tf        (dev state bucket)
    staging/
      main.tf
      variables.tf
      backend.tf        (staging state bucket)
    prod/
      main.tf
      variables.tf
      backend.tf        (prod state bucket)

Each environment:
→ Has its OWN state file
→ In its OWN S3 bucket
→ With its OWN DynamoDB table
→ Changes to prod DO NOT affect dev

dev/main.tf:
module 'eks' {
  source     = '../../modules/eks-cluster'
  cluster_name = 'dev-cluster'
  node_type    = 't3.medium'  # cheap
  min_nodes    = 1
  max_nodes    = 3
}

prod/main.tf:
module 'eks' {
  source     = '../../modules/eks-cluster'
  cluster_name = 'prod-cluster'
  node_type    = 'm5.xlarge'  # powerful
  min_nodes    = 3
  max_nodes    = 20
}

PROMOTION WORKFLOW:
1. Change tested in dev
2. Same change promoted to staging:
   cd environments/staging
   terraform plan
   (review diff)
   terraform apply
3. Validated in staging
4. PR raised for prod change
5. Reviewed and approved
6. Applied via CI/CD in maintenance window

This ensures:
→ No prod changes without dev/staging validation
→ Independent state per environment
→ Different sizing for cost optimization
→ Full audit trail via Git history"

Q27: What is Terraform import and when do you use it?

Answer:
"Terraform import brings existing
infrastructure that was created
OUTSIDE of Terraform under
Terraform management.

When I need it:
→ Someone created a resource manually
  in AWS Console (bad practice but happens)
→ Migrating existing infrastructure
  to Terraform management
→ Taking over a project with
  manually created resources

The process:

Step 1: Write the Terraform resource
  first (empty placeholder):
resource 'aws_security_group' 'web' {
  # configuration here
}

Step 2: Run import command:
terraform import aws_security_group.web sg-0123456789

Step 3: Terraform reads the actual resource
  and adds it to state

Step 4: Run terraform plan
→ Plan shows the differences between
  your code and the actual resource
→ You MUST update your code to match
  the actual configuration
→ Plan should show: No changes
  when your code matches reality

Step 5: Commit the Terraform code
→ Now this resource is under
  Terraform management

IMPORTANT LIMITATIONS:
→ Import adds to state but does NOT
  generate the Terraform code
→ You still need to write the code yourself
→ terraform plan will show what is different

Alternative in newer Terraform (1.5+):
import block in code:
import {
  to = aws_instance.web
  id = 'i-1234567890'
}

Then run:
terraform plan -generate-config-out=generated.tf
→ Auto-generates the Terraform code
→ Much faster than writing manually

At Citibank I used import when
inheriting infrastructure that was
built before Terraform was adopted.
Took 3 weeks to import all resources
but worth it for full IaC management."
SECTION 4 — MONITORING & OBSERVABILITY (Q28-Q33)

Q28: Explain your monitoring stack and how you set it up

Answer:
"I have set up and operated the
full observability stack at Citibank.

Three pillars of observability:
1. Metrics → Prometheus + Grafana
2. Logs → ELK Stack
3. Traces → Jaeger (via Istio)

METRICS — PROMETHEUS + GRAFANA:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Deployment:
→ Prometheus Operator via Helm
→ Creates: Prometheus, AlertManager,
  Grafana, Node Exporter, kube-state-metrics

What Prometheus scrapes:
→ Node Exporter: CPU, memory, disk, network
→ kube-state-metrics: pod counts,
  deployment status, HPA status
→ Application metrics (custom):
  HTTP request rate, error rate, latency
→ JVM metrics: heap usage, GC pauses
→ Istio metrics: service-to-service latency

ServiceMonitor example:
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: myapp-metrics
spec:
  selector:
    matchLabels:
      app: myapp
  endpoints:
  - port: metrics
    path: /metrics
    interval: 30s

Grafana dashboards I build:
→ Kubernetes cluster overview
→ Per-namespace resource usage
→ Application RED metrics
  (Rate, Errors, Duration)
→ JVM performance dashboard
→ Istio service mesh topology
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

LOGS — ELK STACK:
→ Fluent Bit DaemonSet on every node
→ Collects all container logs
→ Ships to Logstash for processing
→ Stored in Elasticsearch
→ Kibana for search and visualization

Index pattern: logs-prod-*
Kibana dashboards:
→ Error rate over time
→ Top error messages
→ Application logs per service
→ Security events
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ALERTS — AlertManager:
Critical alert example:
- alert: HighErrorRate
  expr: |
    rate(http_requests_total
    {status=~'5..'}[5m]) /
    rate(http_requests_total[5m]) > 0.05
  for: 2m
  labels:
    severity: critical
  annotations:
    summary: 'Error rate above 5%'

Routes: PagerDuty for critical,
Slack for warning."

Q29: What is the difference between Datadog and Prometheus/Grafana?

Answer:
"Both are monitoring solutions but
with fundamentally different approaches.
I have used both in production.

PROMETHEUS + GRAFANA:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Type: Open source, self-hosted
Cost: Free (infrastructure costs only)

Deployment:
→ You run Prometheus on your cluster
→ You manage Grafana dashboards
→ You configure scrape targets
→ You manage retention and storage

Strengths:
→ No data leaves your environment
  (critical for banking data)
→ Highly customizable
→ Native Kubernetes integration
→ Large community, many exporters
→ No per-host cost
→ PromQL is very powerful

Weaknesses:
→ You manage the infrastructure
→ Long-term storage needs Thanos/Cortex
→ More setup and maintenance

I use Prometheus+Grafana for:
→ Kubernetes cluster metrics
→ Application custom metrics
→ Cost-sensitive environments
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

DATADOG:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Type: SaaS, commercial, fully managed
Cost: Per-host licensing (expensive)

What you get:
→ Infrastructure monitoring
→ APM (Application Performance Monitoring)
  — distributed tracing without Jaeger
→ Log management (replaces ELK)
→ RUM (Real User Monitoring)
→ Security monitoring
→ Synthetics (uptime testing)
→ Everything in ONE platform

Strengths:
→ No infrastructure to manage
→ Excellent out-of-box dashboards
→ APM is best-in-class
→ Correlation: logs + metrics + traces
  in one click
→ Easy to set up
→ Excellent alerting

Weaknesses:
→ Very expensive at scale
→ Data goes to Datadog cloud
  (data sovereignty concerns)
→ Vendor lock-in
→ Less flexible than Prometheus

I use Datadog for:
→ APM and distributed tracing
→ When budget allows
→ When team lacks infra expertise

At Citibank:
→ Prometheus+Grafana for cluster metrics
→ Datadog for APM and distributed tracing
→ ELK for log aggregation
→ Splunk for security events
  (SIEM use case)"

Q30: How do you set up alerting and what makes a good alert?

Answer:
"Alerting is one of the most
important and most frequently
misconfigured parts of observability.
Bad alerts cause alert fatigue —
engineers ignore them — and real
incidents get missed.

PRINCIPLES FOR GOOD ALERTS:

1. Alert on SYMPTOMS not CAUSES:
Bad: 'CPU above 80%'
  → May not affect users at all

Good: 'Error rate above 1%'
  → Users are experiencing errors

2. Alert on SLOs (Service Level Objectives):
→ Define: 99.9% of requests
  must complete in < 500ms
→ Alert: 'Error budget burning fast'
  → This alerts when you are
    about to miss your SLO

3. Every alert needs a runbook:
→ Alert fires → engineer looks at
  runbook: what to check, what to do
→ No runbook = useless alert at 2 AM

4. Reduce noise:
→ Set appropriate 'for' duration:
  for: 5m (not just 1 spike)
→ Deduplicate in AlertManager
→ Group similar alerts

ALERT LEVELS I CONFIGURE:

Critical (PagerDuty — wake someone up):
→ Service completely down
→ Error rate > 5% for 2 minutes
→ P99 latency > 2 seconds

Warning (Slack notification):
→ Error rate > 1% for 5 minutes
→ CPU > 80% for 10 minutes
→ Disk > 85%
→ Pod restart count > 3

Info (Dashboard only):
→ Deployment triggered
→ Scaling event occurred

ALERTMANAGER ROUTING:
route:
  group_by: [alertname, cluster]
  group_wait: 30s
  group_interval: 5m
  repeat_interval: 4h
  receiver: slack-warning
  routes:
  - match:
      severity: critical
    receiver: pagerduty-critical
  - match:
      severity: warning
    receiver: slack-warning

At Citibank I reduced alert noise
by 60% by converting CPU/memory alerts
to error-rate and latency-based alerts.
Fewer pages, more meaningful pages."

Q31: What is OpenTelemetry and how is it different from traditional monitoring?

Answer:
"OpenTelemetry (OTel) is a CNCF
project that standardizes how
observability data (metrics, logs,
traces) is collected and exported.

THE PROBLEM before OpenTelemetry:
→ Using Datadog: instrument with Datadog SDK
→ Switch to Jaeger: re-instrument everything
→ Vendor lock-in for observability
→ Different SDKs for each tool
→ Inconsistent data formats

WHAT OPENTELEMETRY SOLVES:
→ Single standard for all three signals:
  Metrics, Logs, and Traces
→ Instrument once, export anywhere
→ Open standard: vendor neutral
→ CNCF graduated project

Components:
OTel SDK: Instruments your application
  → Collects traces, metrics, logs
  → Language specific (Java, Python, Go)
  → Auto-instrumentation available
    (no code changes for common frameworks)

OTel Collector: Central processing
  → Receives from all services
  → Processes, filters, batches
  → Exports to multiple backends

OTel Collector pipeline example:
receivers:
  otlp:
    protocols:
      grpc:
        endpoint: 0.0.0.0:4317

processors:
  batch:
  resource:
    attributes:
    - action: insert
      key: environment
      value: production

exporters:
  jaeger:
    endpoint: jaeger:14250
  prometheus:
    endpoint: '0.0.0.0:8889'
  elasticsearch:
    endpoints: ['http://es:9200']

service:
  pipelines:
    traces:
      receivers: [otlp]
      processors: [batch, resource]
      exporters: [jaeger]
    metrics:
      receivers: [otlp]
      exporters: [prometheus]

At Citibank:
→ Java microservices auto-instrumented
  with OTel Java agent
→ OTel Collector deployed as DaemonSet
→ Traces → Jaeger
→ Metrics → Prometheus
→ Switch backends without code changes"

Q32: How do you use Splunk in your environment?

Answer:
"Splunk is the SIEM (Security Information
and Event Management) and log analysis
platform I use at Citibank alongside
ELK Stack.

Why both ELK and Splunk:
→ ELK: Application and infrastructure logs
  (development and operations focused)
→ Splunk: Security events, audit logs,
  compliance reporting
  (security and compliance focused)

What I send to Splunk:
→ Kubernetes audit logs
  (who did what in the cluster)
→ AWS CloudTrail events
  (API calls to AWS)
→ Application security events
  (failed logins, privilege escalation)
→ Network flow logs
→ Container runtime events (Falco)

Splunk searches I use:
Find failed login attempts:
index=security sourcetype=k8s-audit
  verb=create user=*
  responseStatus.code=403
  | stats count by user, sourceIP
  | sort -count

Find suspicious pod creation:
index=security sourcetype=k8s-audit
  verb=create kind=Pod
  namespace=production
  | where user != 'system:serviceaccount*'

Find API calls from unusual IPs:
index=aws sourcetype=cloudtrail
  | stats count by sourceIPAddress, userIdentity.userName
  | where count > 100

Splunk dashboards I maintain:
→ Security events summary
→ Failed authentication attempts
→ Privileged access usage
→ Change management activity
→ Compliance reporting dashboard

At Citibank Splunk is primarily
the security and compliance team's
tool — I feed data into it and
use it for security investigations
during incident response."

Q33: How do you use Prometheus PromQL for alerting?

Answer:
"PromQL is Prometheus Query Language —
essential for writing meaningful alerts
and dashboards.

KEY FUNCTIONS I USE:

rate(): Request rate over time
rate(http_requests_total[5m])
→ Requests per second
   averaged over 5 minutes

Error rate calculation:
sum(rate(http_requests_total{code=~'5..'}[5m]))
/
sum(rate(http_requests_total[5m]))
→ Proportion of 5xx responses

Latency p99:
histogram_quantile(0.99,
  sum(rate(http_request_duration_seconds_bucket[5m]))
  by (le))
→ 99th percentile latency

CPU usage per pod:
sum(rate(container_cpu_usage_seconds_total
  {namespace='production'}[5m]))
by (pod)

Memory usage:
container_memory_working_set_bytes
  {namespace='production'}
/ container_spec_memory_limit_bytes
  {namespace='production'}
→ Memory usage as percentage of limit

Pod restart rate:
rate(kube_pod_container_status_restarts_total[1h])
> 0
→ Pods that are restarting

Disk space alert:
(node_filesystem_avail_bytes
  {mountpoint='/'} /
node_filesystem_size_bytes
  {mountpoint='/'}) < 0.15
→ Less than 15% disk free

ALERT RULES:
groups:
- name: application
  rules:
  - alert: HighErrorRate
    expr: |
      sum(rate(http_requests_total
        {status=~'5..'}[5m]))
      /
      sum(rate(http_requests_total[5m]))
      > 0.05
    for: 2m
    labels:
      severity: critical
    annotations:
      summary: 'Error rate is {{ $value | humanizePercentage }}'

  - alert: SlowRequests
    expr: |
      histogram_quantile(0.99,
        rate(http_duration_seconds_bucket[5m]))
      > 2
    for: 5m
    labels:
      severity: warning"
SECTION 5 — AWS & AZURE (Q34-Q39)

Q34: What AWS services do you use most in production?

Answer:
"I use AWS extensively at Citibank.
Key services I work with daily:

COMPUTE:
EKS (Elastic Kubernetes Service):
→ Primary container platform
→ Managed Kubernetes control plane
→ Node groups: on-demand + spot mix
→ IRSA for pod IAM permissions

EC2 and Auto Scaling:
→ Worker nodes for EKS
→ Bastion hosts for secure access
→ Launch Templates for node config

Lambda:
→ Event-driven automation
→ Secrets rotation
→ Cost optimization triggers
→ CI/CD event handlers

NETWORKING:
VPC:
→ Separate VPCs per environment
→ Private subnets for workloads
→ Public subnets only for load balancers
→ VPC peering between environments

Security Groups:
→ Least privilege ingress/egress
→ No 0.0.0.0/0 rules in prod
→ Managed by Terraform

Load Balancers:
→ ALB for HTTP/HTTPS
→ NLB for TCP
→ AWS Load Balancer Controller
  for Kubernetes Ingress

STORAGE:
S3:
→ Terraform state storage
→ Application artifacts
→ Log archival
→ Static assets

EBS:
→ Kubernetes PersistentVolumes
→ Database storage

EFS:
→ Shared storage across pods
→ ReadWriteMany workloads

SECURITY & IAM:
IAM roles and policies:
→ Least privilege for all services
→ IRSA (IAM Roles for Service Accounts)
  → Pods get IAM permissions
    without static credentials

AWS Secrets Manager:
→ All application secrets stored here
→ Automatic rotation configured
→ Accessed via External Secrets Operator

CloudTrail:
→ All API calls logged
→ Sent to Splunk for SIEM

MONITORING:
CloudWatch:
→ EKS control plane logs
→ Lambda function logs
→ RDS metrics
→ Custom application metrics"

Q35: What is IRSA (IAM Roles for Service Accounts) and why is it important?

Answer:
"IRSA is a critical AWS EKS security
feature I implement at Citibank.
Without it: serious security risk.

THE PROBLEM without IRSA:

Option 1 (bad): Static credentials
→ Create IAM user
→ Put access key/secret in pod
→ ALL pods on node share credentials
→ If any pod is compromised:
  attacker has all credentials
→ Rotation is painful

Option 2 (bad): Node IAM role
→ Give worker node an IAM role
→ ALL pods on that node inherit
  the node's permissions
→ Over-privileged pods
→ No pod-level granularity

IRSA (correct approach):
→ Each Kubernetes ServiceAccount
  gets its own IAM role
→ Only that specific pod
  gets those specific permissions
→ Credentials are temporary (rotated by AWS)
→ No static credentials in code
→ Least privilege per pod

How I configure it:

Step 1: Enable OIDC on EKS cluster
(Terraform does this automatically)

Step 2: Create IAM role with
trust policy for the ServiceAccount:
{
  'Effect': 'Allow',
  'Principal': {
    'Federated': 'arn:aws:iam::123456789:
    oidc-provider/oidc.eks.us-east-1...'
  },
  'Action': 'sts:AssumeRoleWithWebIdentity',
  'Condition': {
    'StringEquals': {
      'oidc...sub':
      'system:serviceaccount:
       production:myapp-sa'
    }
  }
}

Step 3: Annotate ServiceAccount:
apiVersion: v1
kind: ServiceAccount
metadata:
  name: myapp-sa
  namespace: production
  annotations:
    eks.amazonaws.com/role-arn:
      arn:aws:iam::123456789:role/myapp-role

Step 4: Use ServiceAccount in pod:
spec:
  serviceAccountName: myapp-sa

Result: Pod gets exactly the permissions
assigned to myapp-role and nothing else.
At Citibank: every microservice has
its own ServiceAccount and IAM role."

Q36: What is the difference between AWS EKS and Azure AKS?

Answer:
"I manage both EKS and AKS at
Citibank in a multi-cloud setup.
Both are managed Kubernetes services
but with platform-specific differences.

AWS EKS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Control plane: Managed by AWS
  → You pay per cluster per hour
  → You manage node groups

IAM Integration:
→ IRSA for pod permissions
→ aws-auth ConfigMap for
  cluster access control
→ Very mature IAM integration

Networking:
→ AWS VPC CNI (pods get VPC IPs)
→ Good for VPC-native networking
→ ALB/NLB via Load Balancer Controller

Storage:
→ EBS for block storage
→ EFS for shared storage
→ S3 via IRSA credentials

Monitoring:
→ CloudWatch Container Insights
→ CloudTrail for audit
→ Excellent AWS ecosystem integration

Add-ons:
→ AWS manages: CoreDNS, kube-proxy,
  VPC CNI
→ AWS Marketplace add-ons

Upgrade:
→ AWS manages control plane upgrade
→ You manage node group upgrade
→ In-place node group rolling upgrade
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

AZURE AKS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Control plane: FREE (no control
  plane charge unlike EKS)

IAM Integration:
→ Azure Active Directory integration
→ Azure RBAC for Kubernetes
→ Workload Identity (similar to IRSA)
→ Very tight Azure AD integration

Networking:
→ Azure CNI (pods get VNet IPs)
→ Application Gateway Ingress Controller
→ Azure Load Balancer native

Storage:
→ Azure Disks (like EBS)
→ Azure Files (like EFS)
→ Native Azure integration

Monitoring:
→ Azure Monitor Container Insights
→ Log Analytics Workspace
→ Good but less mature than AWS CloudWatch

Add-ons:
→ Managed via AKS add-on profiles
→ Azure Policy for AKS

Upgrade:
→ One-click upgrade via portal
  or az aks upgrade command
→ Control plane first, then nodes

KEY PRACTICAL DIFFERENCE:
→ EKS: More control, more complexity,
  AWS-native tooling is excellent
→ AKS: Easier setup, free control plane,
  Azure AD integration is seamless

At Citibank: AKS for Azure-resident
workloads, EKS for AWS-resident workloads.
Same Helm charts deploy to both —
abstraction via GitOps."

Q37: How do you implement cost optimization in AWS?

Answer:
"Cloud cost optimization is a
continuous responsibility. At Citibank
I implemented several strategies.

KUBERNETES COST OPTIMIZATION:

1. Right-sizing with VPA:
→ VPA analyzes actual usage
→ Identifies over-provisioned pods
→ Reduced average pod resource
  requests by 30%

2. Cluster Autoscaler:
→ Scale down nodes when underutilized
→ Scale up when pods pending
→ Nodes not needed at 2 AM scaled down
→ Significant overnight savings

3. Spot instances for non-critical:
→ Batch jobs on spot instances
→ Dev/test environments on spot
→ Spot saves 70-90% vs on-demand
→ Node Termination Handler for graceful drain

4. Ingress Controller optimization:
→ My 20% improvement:
  Right-sized controller resources
→ More pods per node = fewer nodes needed

AWS RESOURCE OPTIMIZATION:

5. Reserved Instances / Savings Plans:
→ Commit to 1-3 year for consistent workloads
→ EKS worker nodes on 1-year RI
→ Saves 40% vs on-demand

6. S3 Lifecycle policies:
→ Move old logs to Glacier after 30 days
→ Delete after 1 year
→ Reduced S3 costs by 60%

7. Right-size EC2:
→ CloudWatch metrics show CPU/memory usage
→ Downsize underutilized instances
→ Use Graviton (ARM) instances:
  20-40% cheaper, often same performance

8. Clean up unused resources:
→ Terraform drift detection finds
  orphaned resources
→ Unattached EBS volumes deleted
→ Old AMIs cleaned up
→ Unused Elastic IPs released

9. Cost allocation tags:
→ Every resource tagged:
  Environment, Team, Application
→ Cost Explorer shows spend by team
→ Accountability drives behavior

Monthly cost review:
→ AWS Cost Explorer dashboard
→ Spot outliers and investigate
→ Rightsize based on utilization data"

Q38: What is Docker volume and how did you use it at CBA?

Answer:
"Docker volumes provide persistent
storage that survives container
restarts and removals.

WHY VOLUMES ARE NEEDED:
→ Container filesystem is ephemeral
→ When container stops: all data lost
→ For databases, logs, uploads:
  data must persist

TYPES OF DOCKER STORAGE:

Volume (managed by Docker):
→ Stored in /var/lib/docker/volumes/
→ Docker manages lifecycle
→ Best practice for container data
→ Can be shared between containers

Bind Mount:
→ Maps host directory to container
→ /host/path:/container/path
→ Direct access to host filesystem
→ Good for development (live code reload)

tmpfs Mount:
→ Stored in host memory
→ Never written to disk
→ For temporary, sensitive data

HOW I CONFIGURED AT CBA:

Production PostgreSQL with persistent storage:
volumes:
  postgres_data:
    driver: local

services:
  postgres:
    image: postgres:15
    volumes:
      - postgres_data:/var/lib/postgresql/data
    environment:
      POSTGRES_PASSWORD_FILE: /run/secrets/pg_password

→ Data in postgres_data volume
→ Survives container restart
→ Database data not lost on update

Shared log volume between containers:
services:
  app:
    volumes:
      - app_logs:/app/logs

  log_shipper:
    volumes:
      - app_logs:/logs:ro  # read-only

→ App writes logs to volume
→ Log shipper reads same volume
→ Sends to ELK stack

In Kubernetes context (my main env):
→ Docker volumes map to
  PersistentVolumeClaims
→ StorageClass determines backend
  (EBS for block, EFS for shared)
→ ConfigMap + VolumeMount for config files

At CBA specifically: I configured
Docker volumes for stateful components
in our docker-compose development
environments and validated the same
patterns worked in Kubernetes PVCs
for production."

Q39: How do you implement Docker security hardening?

Answer:
"Container security hardening is
part of my DevSecOps work.
At CBA I implemented these practices:

IMAGE SECURITY:

1. Use minimal base images:
→ alpine: 5MB vs ubuntu: 77MB
→ distroless: no shell, no package manager
→ Smaller attack surface
→ FROM gcr.io/distroless/java17

2. Pin specific image versions:
→ FROM nginx:1.25.3 NOT nginx:latest
→ latest tag changes silently
→ Pin = reproducible, auditable builds

3. Multi-stage builds:
→ Stage 1: Build environment (has compiler,
  build tools — not needed at runtime)
→ Stage 2: Runtime (only the artifact)

FROM maven:3.9 AS builder
WORKDIR /app
COPY pom.xml .
RUN mvn dependency:go-offline
COPY src ./src
RUN mvn package -DskipTests

FROM gcr.io/distroless/java17
COPY --from=builder /app/target/app.jar /app.jar
ENTRYPOINT ['java', '-jar', '/app.jar']

Result: production image has no Maven,
no JDK, no shell — only JRE and the JAR.

4. Scan images before push:
trivy image myapp:v1.0
→ Fails pipeline on Critical CVEs
→ Every image scanned before
  pushed to registry

RUNTIME SECURITY:

5. Non-root user:
RUN addgroup -S appgroup
    && adduser -S appuser -G appgroup
USER appuser
→ Container runs as non-root
→ Even if compromised:
  no root on host

6. Read-only root filesystem:
securityContext:
  readOnlyRootFilesystem: true
  → Cannot write to container filesystem
  → Forces use of explicit volume mounts
  → Prevents attackers writing malware

7. Drop capabilities:
securityContext:
  capabilities:
    drop: ['ALL']
    add: ['NET_BIND_SERVICE']  # only if needed
→ Containers get no Linux capabilities
→ Cannot perform privileged operations

8. No privileged containers:
securityContext:
  privileged: false  # enforce this
→ Privileged = root on host = dangerous

At CBA: All these implemented as
Kubernetes Pod Security Standards
(Restricted profile) — enforced
at namespace level, not individual pod."
SECTION 6 — SCENARIO BASED (Q40-Q50)

Q40: Production deployment failed and rolled back. Walk me through your process

Answer:
"This happened at Citibank and
my structured approach resolved it
within our SLA.

THE SCENARIO:
Deployed v2.4.1 to production
Application started returning 503 errors
Error rate spiked to 15% (threshold: 1%)
Prometheus alert fired immediately

IMMEDIATE RESPONSE (first 5 minutes):

Step 1: Confirm it is the deployment
→ Check when errors started:
  Kibana: grep errors by timestamp
→ Check deployment time:
  kubectl get deployment myapp -o yaml
  | grep 'deployment.kubernetes.io/revision'
→ Timeline matches: deployment = cause

Step 2: Decision — rollback immediately
→ Error rate 15% → rollback first
→ Do not debug in production
  with users impacted

Step 3: Execute rollback
→ Kubernetes deployment rollback:
  kubectl rollout undo deployment/myapp
  -n production

→ Helm rollback (I use Helm):
  helm rollback myapp 5
  (reverts to revision 5)

Step 4: Monitor rollback
→ kubectl rollout status deployment/myapp
→ Watch Prometheus: error rate dropping?
→ Within 3 minutes: error rate back to 0%

Step 5: Communicate
→ All-clear message sent:
  'Service restored via rollback.
   v2.4.1 rolled back to v2.4.0.
   Investigating root cause.
   Update in 1 hour.'

ROOT CAUSE INVESTIGATION:

Step 6: Compare versions
→ What changed between v2.4.0 and v2.4.1?
→ git diff v2.4.0..v2.4.1

Step 7: Check application logs for v2.4.1
→ Logs from failed pods (before rollback):
  kubectl logs myapp-xyz --previous
→ Found: NullPointerException on
  new configuration property
  that was not set in production

Step 8: Root cause
→ New feature required new environment
  variable DB_POOL_SIZE
→ Added in code but not in
  production ConfigMap
→ Application crashed on startup
  with NPE

FIX AND REDEPLOY:
→ Add DB_POOL_SIZE to ConfigMap
→ Test in staging: works
→ Redeploy v2.4.1 to production
→ Success — no errors

PREVENTION:
→ Added configuration validation
  on startup: fail fast with
  clear error if config missing
→ Staging environment ConfigMap
  now maintained identically to prod"

Q41: A Kubernetes pod is in CrashLoopBackOff. How do you debug it?

Answer:
"CrashLoopBackOff means the container
is crashing repeatedly. Kubernetes
keeps trying but keeps failing.
Systematic debug:

STEP 1: Get pod name
kubectl get pods -n production
→ See: myapp-xyz123 CrashLoopBackOff

STEP 2: Describe the pod
kubectl describe pod myapp-xyz123 -n production

LOOK AT:
Events section:
  'Back-off restarting failed container'
  'OOMKilled' → memory issue
  'Error: failed to create containerd task'
  → image issue

Last State section:
  'Exit Code: 1' → application error
  'Exit Code: 137' → OOMKilled
  'Exit Code: 143' → SIGTERM received

STEP 3: Check current logs
kubectl logs myapp-xyz123 -n production
→ See what error the app prints
  before crashing

STEP 4: Check PREVIOUS container logs
kubectl logs myapp-xyz123 -n production --previous
→ CRITICAL — shows logs from
  the container that crashed
→ Current container may not have
  enough log yet

COMMON CAUSES AND FIXES:

Exit Code 1 — Application error:
→ Read the exception in logs
→ Common: missing environment variable
  SOLUTION: Add to ConfigMap or Secret

→ Cannot connect to database
  SOLUTION: Check database is running,
  check credentials, check network policy
  Test connectivity:
  kubectl run debug --image=busybox --rm -it
  -- nc -zv db-service 5432

Exit Code 137 — OOMKilled:
→ Container exceeded memory limit
  kubectl describe pod → OOMKilled confirmed
  SOLUTION: Increase memory limit:
  resources:
    limits:
      memory: 512Mi  # was 256Mi
→ Or investigate memory leak

ImagePullBackOff (different status):
→ kubectl describe shows image pull error
→ Check image name and tag exist
→ Check imagePullSecret exists

Exit Code 126/127 — Script not found/executable:
→ Entrypoint script missing or not executable
  SOLUTION: chmod +x the script in Dockerfile

AFTER IDENTIFYING ISSUE:
→ Fix Helm values or Dockerfile
→ Rebuild and push new image
→ Update deployment:
  helm upgrade myapp ./chart
  --set image.tag=v2.4.2"

Q42: Your Terraform apply is failing in CI/CD. How do you debug?

Answer:
"Terraform failures in CI/CD need
systematic debugging. I have
hit most common errors at Citibank.

STEP 1: Read the error message carefully
→ Terraform errors are usually descriptive
→ Note: which resource, which provider,
  what specific error

COMMON ERRORS AND MY FIXES:

Error: State lock acquired by another process
Message: 'Error acquiring the state lock'
→ Another apply is running
→ OR previous apply crashed leaving lock
→ Check DynamoDB table for lock entry
→ If confirmed stale lock:
  terraform force-unlock LOCK-ID
→ Do NOT force-unlock if someone
  is actively applying

Error: Insufficient permissions
Message: 'AccessDenied' or 'Unauthorized'
→ CI/CD IAM role lacks permissions
→ Check which resource was being created
→ Add required permission to CI/CD role:
  terraform plan shows: aws_s3_bucket
  → Add S3 permissions to role
→ Always least privilege but complete

Error: Resource already exists
Message: 'already exists'
→ Resource exists in AWS but not in state
→ Options:
  1. Import it: terraform import aws_s3_bucket.logs myapp-logs-prod
  2. Use a different name in Terraform
  3. Delete the existing resource (dangerous)

Error: Provider version mismatch
Message: 'provider constraints not satisfied'
→ Run: terraform init -upgrade
→ Pin provider versions in terraform.tf:
  required_providers {
    aws = {
      source  = 'hashicorp/aws'
      version = '~> 5.0'
    }
  }

Error: Cycle detected
Message: 'cycle: resource_a, resource_b'
→ Circular dependency in resources
→ Resource A depends on B
  and B depends on A
→ Break the cycle using depends_on
  carefully or restructure

Error: Timeout
→ AWS resource took too long to create
→ Increase timeout in resource:
  timeouts {
    create = '30m'
  }
→ Check if resource was created partially

DEBUGGING APPROACH:
1. terraform plan -out=tfplan first
   (review what will happen)
2. Enable detailed logging:
   TF_LOG=DEBUG terraform apply
3. Target specific resource:
   terraform apply -target=aws_eks_cluster.main
   (isolate the failing resource)"

Q43: How do you handle a security vulnerability found in your Docker image?

Answer:
"Security vulnerability discovery
and response is part of my DevSecOps
work at Citibank.

THE SCENARIO:
Trivy scan in CI/CD pipeline detects:
CVE-2024-XXXX: Critical severity
In: base image ubuntu:20.04
Component: libssl 1.1.1
Fix available: libssl 1.1.1t

IMMEDIATE ASSESSMENT:

Step 1: Understand the CVE
→ What does it allow? RCE? Data exposure?
→ Is the vulnerable component
  actually used by our application?
→ Is this exploitable in our context?
  (container without network access
  may not be exploitable even if
  vulnerable)
→ Is there a fix available?

Step 2: Check scope
→ How many images are affected?
→ Are they in production already?
→ When was the last image rebuild?

RESOLUTION:

If base image update fixes it:
→ Update Dockerfile:
  FROM ubuntu:20.04 → FROM ubuntu:22.04
  OR: FROM ubuntu:20.04 (with apt upgrade)
→ Rebuild all affected images
→ Test in staging
→ Deploy to production via normal pipeline

If only library needs update:
→ Add to Dockerfile:
  RUN apt-get update && apt-get upgrade -y
  → Forces latest security patches
→ Rebuild and redeploy

If no fix available yet:
→ Assess actual risk in context
→ Add compensating controls:
  Network policy blocking external access
  Non-root container (limits impact)
  Runtime security monitoring
→ Track CVE for when fix is released
→ Document risk acceptance with approver

PREVENTION:

→ Trivy scan in CI/CD blocks Critical/High
  before images reach registry
→ Trivy scan scheduled weekly on
  existing production images
  (new CVEs may affect old images)
→ Base image rebuild automation:
  Weekly scheduled pipeline rebuilds
  all base images with latest patches
→ Grype/Trivy in JFrog Xray scans
  all artifacts at promotion time

At Citibank: Log4Shell (CVE-2021-44228)
was a real incident.
We identified all affected images in
2 hours using Trivy + JFrog Xray scan
and redeployed all services within 8 hours."

Q44: How do you onboard a new microservice into your DevOps platform?

Answer:
"Onboarding new services efficiently
is important as Citibank teams
release many microservices.

I have streamlined this into a
repeatable process:

STEP 1: Repository setup (Day 1)
→ Create GitHub repository
→ Add standard files:
  .github/workflows/ci.yml (pipeline)
  Dockerfile (standardized template)
  Helm chart (from our template)
  .gitignore
  README.md
  CODEOWNERS
→ Branch protection: main requires
  PR review + CI passing

STEP 2: CI/CD pipeline
→ Copy standard GitHub Actions workflow
→ Customize: language (Java/Python/Node),
  test commands, artifact type
→ Pipeline automatically does:
  Build → Test → Scan → Push to registry

STEP 3: Container configuration
→ Dockerfile from our secure template
→ Developer fills: base image, build steps
→ I review: ensure non-root user,
  multi-stage build, no secrets
→ Image added to approved registry

STEP 4: Kubernetes namespace
→ Create namespace for the service:
  kubectl create namespace myservice-prod
→ Apply network policies (default deny)
→ Configure RBAC for the service account
→ Create IRSA role if AWS permissions needed

STEP 5: Helm chart customization
→ Start from our standard Helm template
→ Developer fills: resource requests,
  health check paths, environment variables
→ I review: security contexts set,
  resource limits defined

STEP 6: Monitoring
→ Add Prometheus ServiceMonitor:
  configure metrics scrape
→ Add Grafana dashboard:
  start from standard template
  customize for service-specific metrics
→ Add AlertManager rules:
  error rate, latency, restart alerts

STEP 7: Secrets
→ Store secrets in AWS Secrets Manager
→ Create ExternalSecret resource
→ No secrets in Git or ConfigMaps

STEP 8: First deployment
→ Deploy to dev → staging → prod
→ Verify all health checks green
→ Verify metrics appearing in Grafana
→ Verify logs appearing in Kibana

Total time: 2-3 days for a new service
From zero to production-ready."

Q45: What do you do when a Kubernetes cluster runs out of resources?

Answer:
"Resource exhaustion is a serious
production situation. I have
managed this at Citibank.

DETECTION:
→ Prometheus alert: node CPU > 90% for 10 mins
→ kubectl get pods shows: Pending pods
→ kubectl describe pod pending-pod-xyz shows:
  'Insufficient cpu' or 'Insufficient memory'

IMMEDIATE INVESTIGATION:

Check node resources:
kubectl top nodes
→ See CPU and memory per node
→ Which nodes are saturated?

Check what is consuming resources:
kubectl top pods -n production
  --sort-by=cpu | head -20
→ Find the top CPU consumers
→ Any runaway process?

Check for pods without limits:
kubectl get pods -n production -o json
  | jq '.items[] | select(
    .spec.containers[].resources.limits
    == null) | .metadata.name'
→ Pods without limits can consume
  unlimited resources

IMMEDIATE ACTIONS:

If runaway pod consuming everything:
→ kubectl delete pod problematic-pod
→ Check what caused the resource spike
→ Fix and redeploy with proper limits

If legitimately need more capacity:
→ Check Cluster Autoscaler logs:
  kubectl logs -n kube-system
  -l app=cluster-autoscaler
→ Is it already scaling up nodes?
→ If not: check autoscaler configuration
→ Manually add nodes if urgent:
  Update node group min/max in AWS console
  OR update Terraform and apply

If pending pods are non-critical:
→ Cordon the saturated node:
  kubectl cordon node-name
  (no new pods scheduled here)
→ Prioritise critical pods with
  PriorityClass

LONG TERM FIX:

→ Set resource requests on ALL pods
  (VPA helps automate this)
→ Set PodDisruptionBudgets
→ Review HPA max replicas vs
  cluster capacity
→ Implement capacity planning:
  Quarterly review of growth vs capacity
→ Ensure Cluster Autoscaler is
  properly configured and has
  IAM permissions to add nodes"

Q46: How do you manage a multi-cloud environment (AWS + Azure)?

Answer:
"Managing AWS and Azure simultaneously
is my daily reality at Citibank.

WHY MULTI-CLOUD AT CITIBANK:
→ Some applications already on Azure
  (legacy migration path)
→ Azure AD integration for certain
  enterprise applications
→ Regulatory: no single cloud dependency
→ Best-of-breed services:
  Azure AD for identity,
  AWS for containers and compute

CHALLENGES AND HOW I HANDLE THEM:

Challenge 1: Different tooling
→ AWS has eksctl/terraform aws provider
→ Azure has az CLI/terraform azurerm provider
→ SOLUTION: Abstract with Terraform modules
  Same module interface, different backends:

module 'kubernetes_cluster' {
  source = '../../modules/k8s-cluster'
  provider = var.cloud_provider  # aws or azure
  cluster_name = var.name
  node_count   = var.nodes
}

Challenge 2: Different networking concepts
→ AWS: VPC, Security Groups, NACLs
→ Azure: VNet, NSGs, Route Tables
→ SOLUTION: Document network architecture
  separately per cloud
  Consistent IP allocation strategy
  across both (non-overlapping CIDRs)

Challenge 3: Different IAM models
→ AWS: IAM roles and IRSA
→ Azure: Managed Identities and
  Workload Identity Federation
→ SOLUTION: Same Kubernetes approach
  (annotate ServiceAccount)
  Implementation differs per cloud

Challenge 4: Observability across clouds
→ Different monitoring endpoints
→ SOLUTION: OpenTelemetry Collector
  aggregates from both environments
  Single Grafana with both data sources
  Single ELK cluster receives from both

Challenge 5: DNS and service discovery
→ Services in AWS need to reach Azure
→ SOLUTION: VPN Gateway or ExpressRoute
  Private DNS resolution across clouds
  Istio can route cross-cloud

CONSISTENCY:
→ Same Helm charts for both clouds
→ Same Kubernetes manifests
→ Same CI/CD pipeline:
  Build once → deploy to both
→ Same monitoring dashboards
→ GitOps: ArgoCD manages both clusters
  from same Git repo
→ Different values files per cloud"

Q47: Explain how you approach a new DevOps project from scratch

Answer:
"Starting a new project from scratch
is something I have done at Citibank.
Here is my structured approach:

WEEK 1: DISCOVERY AND ASSESSMENT

Questions I ask:
→ What application type? (Java, Python, Node)
→ What environments needed? (dev/staging/prod)
→ What cloud? (AWS, Azure, or both)
→ What compliance requirements? (PCI-DSS, SOX)
→ What is the team's DevOps maturity?
→ What is the deployment frequency goal?
→ What is the acceptable downtime?
→ What monitoring exists today?

WEEK 2: FOUNDATION

Infrastructure provisioning:
→ VPCs and networking (Terraform)
→ EKS/AKS clusters (Terraform)
→ IAM roles and policies (least privilege)
→ S3 buckets for state and artifacts
→ Container registry (ECR or ACR)

WEEK 3: CI/CD PIPELINE

→ Repository setup with branch protection
→ Basic pipeline:
  Build → Test → Security scan
  → Push image → Deploy to dev
→ Quality gates configured
→ Artifact management (Nexus or Artifactory)

WEEK 4: SECURITY (DevSecOps)

→ SAST tool (SonarQube) configured
→ Container scanning (Trivy) in pipeline
→ Secrets management (AWS SM + ESO)
→ Network policies applied
→ Pod security standards enforced

WEEK 5: MONITORING

→ Prometheus + Grafana deployed
→ Standard dashboards configured
→ AlertManager with proper routing
→ ELK for log aggregation
→ Runbooks for common alerts

WEEK 6: DEPLOYMENT STRATEGIES

→ Blue-Green for production
→ Canary via Istio if needed
→ HPA configured for scalability
→ Rollback tested and documented

WEEK 7-8: VALIDATION AND HANDOVER

→ Load testing in staging
→ Security penetration test
→ Disaster recovery test
→ Runbook documentation
→ Team training
→ Handover to development team

ONGOING:
→ Weekly cost review
→ Monthly security scan review
→ Quarterly capacity planning"

Q48: How do you stay current with DevOps technologies?

Answer:
"The DevOps landscape changes rapidly —
continuous learning is not optional.

WHAT I DO ACTIVELY:

Community resources:
→ CNCF blog and announcements
  (cncf.io) — first source for
  Kubernetes and cloud-native news
→ KubeWeekly newsletter
→ DevOps Weekly newsletter
→ AWS and Azure blogs for
  service updates

Hands-on practice:
→ Home lab on AWS free tier or
  local Kind cluster
→ Every tool I recommend to
  production: I test it first
→ KodeKloud labs for structured
  hands-on practice

Certifications I am targeting:
→ AWS Solutions Architect Associate
  validates my AWS knowledge formally
→ CKA (Certified Kubernetes Administrator)
  validates Kubernetes operations depth
→ HashiCorp Terraform Associate
  validates IaC expertise

Conference content:
→ KubeCon talks on YouTube
  (free, excellent quality)
→ AWS re:Invent recordings
→ HashiConf sessions

How I validated new tools at Citibank:
→ Tekton: read docs → built POC locally
  → proposed to team → implemented
→ External Secrets Operator: tested
  against dev cluster before recommending
→ OpenTelemetry: attended virtual KubeCon
  session → implemented collector pattern

What I am learning now:
→ Platform Engineering patterns
  (Internal Developer Platforms)
→ eBPF for networking and security
  (Cilium, Falco eBPF)
→ WASM in containers
  (Kubernetes wasm integration)
→ AI/ML in DevOps
  (intelligent monitoring, AIOps)"

Q49: What is SRE and how does it relate to DevOps?

Answer:
"SRE — Site Reliability Engineering —
was invented by Google and is a
discipline I apply principles from
in my DevOps work at Citibank.

SRE IN A NUTSHELL:
→ Apply software engineering
  to operations problems
→ Write code to solve ops problems
  rather than doing them manually
→ Measure everything with SLOs
→ Manage operations work vs
  engineering work balance

KEY SRE CONCEPTS I APPLY:

SLI (Service Level Indicator):
→ Metric that measures service behavior
→ Examples:
  Request success rate
  API latency p99
  Availability percentage

SLO (Service Level Objective):
→ Target value for an SLI
→ Examples:
  99.9% of requests succeed
  p99 latency < 200ms
  99.9% availability per month

SLA (Service Level Agreement):
→ Business contract based on SLOs
→ Consequence if SLO is breached

Error Budget:
→ 99.9% SLO = 0.1% allowed failures
→ 0.1% of monthly requests = error budget
→ Budget remaining → ship features
→ Budget exhausted → freeze releases
  and focus on reliability

Toil reduction:
→ Toil = manual repetitive operations work
→ SRE principle: automate toil away
→ My shell scripts and Python automation
  directly reduces toil
→ Goal: ops team spends more time
  on engineering, less on manual tasks

ERROR BUDGET IN PRACTICE at Citibank:
→ Monthly reliability review
→ How much error budget consumed?
→ If less than 10% consumed:
  deploy more frequently (safe to)
→ If more than 50% consumed:
  slow down releases, focus on reliability
→ If budget exhausted:
  feature freeze until budget recovers

DEVOPS vs SRE:
→ DevOps: culture and practices
  for dev-ops collaboration
→ SRE: implementation of DevOps
  with engineering rigor
→ Not competing — complementary
→ I bring SRE principles
  (SLOs, error budgets, toil reduction)
  into DevOps workflows"

Q50: Where do you see yourself in 3 years and what is your next step?

Answer:
"In 3 years I want to have grown
into a Senior DevOps Engineer or
Platform Engineering role where
I am not just maintaining pipelines
but architecting the developer
platform that entire product teams
rely on.

TECHNICAL DEPTH I WANT TO BUILD:

Kubernetes at architect level:
→ Currently: operational expertise
→ Goal: design multi-cluster architectures,
  build platform teams' Kubernetes
  abstraction layers
→ CKA first, then CKAD and CKS

Cloud architecture:
→ AWS Solutions Architect Associate
  is my immediate certification goal
→ Validates and formalizes what I practice

Platform Engineering:
→ Build Internal Developer Platforms (IDP)
→ Give developers self-service
  infrastructure provisioning
→ This is where DevOps is evolving —
  from per-project CI/CD to
  standardized platforms

FinOps:
→ Deeper cloud cost engineering
→ FinOps Foundation certification
→ Cost optimization at architecture level

WHAT I WANT FROM THIS ROLE:
→ More complex architecture challenges
  than my current scope
→ Exposure to larger-scale infrastructure
→ Mentoring from senior architects
→ Opportunity to lead technical decisions
  not just implement them

MY COMMITMENT:
→ I am not someone who wants to
  collect tools — I want to go
  deep on fewer things and become
  genuinely expert
→ The CKA certification this year
  is my concrete next step
→ Every year I want a meaningful
  before and after — something
  I could not do before
  that I can do now

I believe this role gives me
that trajectory and I am genuinely
excited about what I could
contribute and learn here."
INTERVIEW CHEAT SHEET
YOUR KEY NUMBERS — MEMORISE THESE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
→ 4+ years DevOps experience
→ 20% Kubernetes resource improvement
   (Ingress Controller POC)
→ 20% Maven pipeline speed improvement
   (CBA — caching + parallelization)
→ Zero production security incidents
   (DevSecOps integration)
→ Zero-downtime deployments
   (Blue-Green + Canary)
→ Two banking clients
   (Citibank + CBA)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

QUESTIONS MOST LIKELY ASKED:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⭐ Walk me through a CI/CD pipeline (Q1)
⭐ Jenkins vs GitHub Actions vs Tekton (Q2)
⭐ Blue-Green vs Canary deployment (Q3)
⭐ How do you implement DevSecOps? (Q4)
⭐ Explain your Kubernetes experience (Q11)
⭐ What is Istio and how used? (Q12)
⭐ Terraform state and why important (Q22)
⭐ Terraform vs Ansible difference (Q23)
⭐ Monitoring stack explanation (Q28)
⭐ Production deployment failed — what do? (Q40)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

GOLDEN ANSWER FORMULA:
Every answer = Context + What I did
             + Result + Why it matters

CONFIDENCE REMINDER:
You have done ALL of this in
production at Citibank and CBA.
Two of the most demanding banking
environments in the world.
Speak with confidence — you have
earned every answer. 🚀
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
You are out of free messages until 7:30 PM




Claude is AI and can make mistakes. Please double-check responses.
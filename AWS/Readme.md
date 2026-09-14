
15.
---------------------------------------------------------------------------------------------------
There are two AWS accounts:

Account A = Provider
Account B = Consumer

Account A owns the application/service.

Account B wants to privately access that service.

The architecture is:

                 ACCOUNT B
                Consumer
                   |
                EC2
                   |
                   ↓
        Interface VPC Endpoint
                   |
                   ↓
            AWS PrivateLink
                   |
                   ↓
                 NLB
                   |
                   ↓
             Service EC2
                 ACCOUNT A
                Provider
In simple words

Account A exposes its application using an Endpoint Service. Account B creates an Interface VPC Endpoint to consume that service privately. The traffic travels through AWS PrivateLink and reaches Account A's Network Load Balancer, which forwards it to the backend application.

There is no internet connection required.

2. What is the problem?

The interviewer says:

The endpoint in Account B shows "Available", but when EC2 tries to call the service, the connection times out.

The important point is:

"Available" does NOT necessarily mean the application is reachable.

It basically tells us that the endpoint resource/connection is established, but traffic can still fail somewhere along the path.

So I would troubleshoot the entire traffic path.

3. My interview troubleshooting approach

I would say:

“I would troubleshoot this layer by layer, starting from the PrivateLink endpoint connection and then moving toward the backend application.”

I would check four major areas.

4. Step 1 — Check Endpoint Connection Acceptance

This is the first thing I would check.

Account A creates:

VPC Endpoint Service

Account B creates:

Interface VPC Endpoint

But Account A may need to accept the endpoint connection.

The flow is:

Account B
    |
    | Create endpoint
    ↓
Account A
    |
    | Accept connection
    ↓
PrivateLink connection

If it is still:

Pending Acceptance

then traffic won't flow.

Interview answer

“First, I would check the Endpoint Service in Account A and verify the endpoint connection from Account B has been accepted. If acceptance is pending, the provider needs to accept it, unless auto-accept is configured.”

5. Step 2 — Check NLB Target Health

This is probably the most important troubleshooting step.

The Endpoint Service in Account A is backed by a:

Network Load Balancer

And the NLB forwards traffic to target EC2 instances.

So:

Account B EC2
      ↓
Interface Endpoint
      ↓
PrivateLink
      ↓
NLB
      ↓
Target Group
      ↓
Application EC2

Suppose the NLB target is unhealthy:

NLB
 ↓
Target = Unhealthy ❌

Then the NLB won't successfully forward traffic.

What would I check?

Go to:

Account A
   ↓
EC2
   ↓
Load Balancers
   ↓
Target Groups
   ↓
Target Health

Check whether the backend targets are:

Healthy ✅

or:

Unhealthy ❌
Interview answer

“Next, I would check the NLB target group health. The Endpoint Service is backed by the NLB, so if the registered EC2 targets are unhealthy, the connection can reach the PrivateLink endpoint but won't successfully reach the application.”

6. Step 3 — Check Private DNS

This is another common issue.

An Interface Endpoint creates endpoint-specific DNS names.

For example, conceptually:

vpce-12345....amazonaws.com

There are two possible approaches.

Option A — Use the endpoint-specific DNS

The client uses the DNS name provided by the VPC endpoint.

Option B — Enable Private DNS

If Private DNS is enabled, the consumer can use the service's normal DNS name, and AWS resolves it privately through the interface endpoint.

For example:

app.internal.example.com
          ↓
Private DNS
          ↓
Interface Endpoint
          ↓
PrivateLink

If Private DNS isn't configured correctly, the application may resolve the hostname to the wrong destination.

Interview answer

“I would verify DNS resolution from the consumer EC2. I would check whether Private DNS is enabled on the interface endpoint and whether the application hostname resolves to the expected PrivateLink endpoint rather than a public IP.”

7. Step 4 — Check Security Groups

This is another very common reason for a timeout.

There are potentially two sides of security to check.

Consumer side

Account B's EC2 needs to be able to connect to the Interface Endpoint.

Conceptually:

EC2 SG
  ↓
Interface Endpoint SG
  ↓
Service port

For example, if the service listens on port 443:

EC2 → Endpoint :443

The endpoint's security group must allow that traffic.

Provider side

The backend application must accept traffic coming from the NLB.

Conceptually:

PrivateLink
     ↓
NLB
     ↓
Backend EC2

The backend security group must allow the required application port.

For example:

NLB → EC2 :8080
Interview answer

“Then I would check security groups on both sides. In Account B, the endpoint security group must allow the consumer EC2 to connect to the endpoint port. In Account A, the backend security configuration must allow the NLB to reach the application on its listener or target port.”

8. Complete troubleshooting flow

This is the part I would memorize:

Account B
   |
   ↓
EC2
   |
   | 1. Can EC2 reach endpoint?
   ↓
Interface VPC Endpoint
   |
   | 2. Is endpoint connection accepted?
   ↓
PrivateLink
   |
   | 3. Does DNS resolve correctly?
   ↓
Endpoint Service
   |
   ↓
NLB
   |
   | 4. Are targets healthy?
   ↓
Target Group
   |
   | 5. Is traffic allowed?
   ↓
Backend EC2
   |
   ↓
Application
9. What does "timeout" tell you?

This is a good interview follow-up.

A timeout usually makes me think about network connectivity, rather than immediately blaming the application.

I'd investigate:

DNS
 ↓
Routing
 ↓
Security Groups
 ↓
NACLs
 ↓
NLB
 ↓
Target health
 ↓
Application port

For example, from Account B's EC2 I could test:

nslookup <service-dns-name>

Then:

curl -v <service-dns-name>:<port>

or:

nc -vz <hostname> <port>

These help determine whether the issue is DNS or TCP connectivity.

10. The best interview answer

If the interviewer gives you this scenario, you can say this almost directly:

“This is a cross-account AWS PrivateLink setup. Account A is the service provider. It creates an Endpoint Service backed by a Network Load Balancer. Account B is the consumer and creates an Interface VPC Endpoint to connect privately to that service.”

“If the endpoint shows Available but the application connection times out, I wouldn't assume the application is reachable. I would troubleshoot the complete traffic path.”

“First, I would check whether Account A has accepted the endpoint connection. Second, I would check the NLB target group and make sure the backend targets are healthy. Third, I would verify DNS resolution and confirm that Private DNS is configured correctly if we're using the service's normal hostname. Fourth, I would check security groups on both sides — the consumer EC2 must be able to reach the interface endpoint, and the provider-side backend must allow the NLB to reach the application.”

“I would also verify that the application is actually listening on the expected port and check NACLs and routing if the previous checks are correct. I would test from the consumer EC2 using tools such as nslookup, curl and nc to identify exactly where the connection is failing.”

🧠 Easy way to remember it

Remember:

A → H → D → S → App

A — Acceptance

Was the endpoint connection accepted?

H — Health

Are NLB targets healthy?

D — DNS

Does the hostname resolve correctly?

S — Security

Do SGs/NACLs allow the traffic?

App — Application

Is the application listening on the expected port?

So if the interviewer asks:

“PrivateLink endpoint says Available but connection times out. What do you check?”

Your short answer is:

“I check endpoint acceptance, NLB target health, DNS/Private DNS, security groups and finally the backend application's listening port. I troubleshoot from the consumer EC2 all the way through the interface endpoint, PrivateLink, NLB and backend target.”

That's the cleanest interview explanation.

----------------------------------------------------------------------------------------------------------------
16.


Yes. This scenario is testing whether you understand Route 53 Private Hosted Zones + VPC DHCP options + DNS resolver behavior.

The key issue is:

The EC2 instances stopped using the AWS VPC DNS resolver after the DHCP option change, so they could resolve public DNS names but could no longer resolve Route 53 Private Hosted Zone names.

1. First understand the architecture

Before the DHCP change:

EC2
 |
 | DNS query
 ↓
AWS VPC DNS Resolver
169.254.169.253
 |
 ├── google.com → Public DNS
 |
 └── service-a.internal
          ↓
   Route 53 Private Hosted Zone

So everything worked.

After the DHCP change:

EC2
 |
 | DNS query
 ↓
Custom / On-prem DNS
 |
 ├── google.com → ✅ Works
 |
 └── service-a.internal
          ↓
       ❌ Doesn't know
       about Route 53 PHZ

That's why:

google.com              ✅
service-a.internal      ❌

This difference is the big clue.

2. What changed?

The important AWS concept is DHCP Options Set.

When an EC2 instance gets its network configuration through DHCP, the DHCP options tell it things such as:

DNS servers
Domain name
NTP servers

Previously, the VPC probably used:

AmazonProvidedDNS

which points to the AWS VPC resolver:

169.254.169.253

or equivalently:

VPC CIDR + 2

For example, if:

VPC = 10.0.0.0/16

the resolver can be reached at:

10.0.0.2
3. Why does the AWS resolver matter?

Because the AWS resolver knows about your VPC's Route 53 Private Hosted Zones.

Suppose you have:

Private Hosted Zone:

internal.example.com

and:

service-a.internal.example.com
        ↓
     10.0.2.50

If EC2 asks the AWS resolver:

EC2
 ↓
169.254.169.253
 ↓
Route 53 Private Hosted Zone
 ↓
10.0.2.50

it can resolve the name.

But if you change the EC2 DNS server to an external/custom DNS server:

EC2
 ↓
Custom DNS
 ↓
"service-a.internal.example.com?"

the custom DNS server might say:

"I don't know that private zone."

Therefore:

Internal DNS ❌
External DNS  ✅
4. Step-by-step troubleshooting

In an interview, say:

“I would troubleshoot this from the EC2 instance outward, starting with which DNS server the instance is actually using.”

Step 1 — Check the DNS server on EC2

On the affected EC2:

cat /etc/resolv.conf

You may see:

nameserver 10.0.0.2

or:

nameserver 169.254.169.253

That's what we want for Amazon-provided DNS.

But after the DHCP change, you might see:

nameserver 192.168.1.10

or some corporate/on-prem DNS server.

You can also use:

resolvectl status

to see the DNS servers being used.

Interview explanation

“First I check /etc/resolv.conf or resolvectl status to determine which DNS server the EC2 instance is actually using. If it changed from the AWS VPC resolver to a custom DNS server, that explains why private Route 53 names stopped resolving.”

5. Step 2 — Test the AWS resolver directly

Now bypass the configured DNS server and test the AWS resolver directly.

For example:

dig service-a.internal.example.com @169.254.169.253

Or:

nslookup service-a.internal.example.com 169.254.169.253

If you get an answer:

service-a.internal.example.com
        ↓
10.0.x.x

then we have strong evidence that:

Route 53 Private Hosted Zone is working correctly.

The problem is the DNS server configured on the EC2 instance.

This is a very useful troubleshooting technique:

Configured DNS → fails
AWS resolver → works

Therefore:

Problem = DNS configuration
6. Step 3 — Check the Route 53 Private Hosted Zone

In AWS:

Route 53
   ↓
Hosted Zones
   ↓
internal.example.com

Verify:

Private hosted zone?

It should be:

Type: Private hosted zone
VPC association?

Make sure the correct VPC is associated:

internal.example.com
        ↓
VPC
10.0.0.0/16

If the private hosted zone isn't associated with the VPC, the AWS resolver won't return the private record.

7. Step 4 — Check DHCP Options Set

Now go to:

VPC
 ↓
DHCP Options Sets

Check what DNS servers are configured.

If it says:

domain-name-servers:
    192.168.x.x

then the VPC is telling instances:

"Use this custom DNS server."

Previously it may have been:

domain-name-servers:
    AmazonProvidedDNS

That's likely what caused the issue.

8. Important interview trick: DHCP changes are not immediate

This is one of the most important details in the question.

Suppose you change:

Old DHCP options
      ↓
AmazonProvidedDNS

to:

New DHCP options
      ↓
Custom DNS

Existing EC2 instances don't necessarily immediately change their DNS configuration.

They may continue using their old DHCP lease until it renews.

So you can have:

EC2 #1 → old DNS → works
EC2 #2 → new DNS → fails

for some time.

That's why the problem can appear inconsistent.

Interview statement

“DHCP option changes don't necessarily affect running instances immediately. Existing instances may retain their current DHCP lease until renewal. So after changing the DHCP options, I would force a DHCP lease renewal or restart the networking service on affected instances.”

9. Step 5 — Force DHCP renewal

On Linux, depending on the networking stack, you can renew the lease.

For example:

sudo dhclient -r
sudo dhclient

Or restart the appropriate networking service/interface.

Then check again:

cat /etc/resolv.conf

You want to verify that the DNS server is now the intended one.

Then test:

dig service-a.internal.example.com
10. Step 6 — Test public and private DNS separately

This is a great troubleshooting technique.

Run:

dig google.com

Then:

dig service-a.internal.example.com

Suppose:

google.com
    ↓
ANSWER

but:

service-a.internal.example.com
    ↓
NXDOMAIN / timeout

That tells you:

General DNS connectivity is working, but the DNS server doesn't have access to the private namespace.

That's exactly what the scenario is showing.

11. Two possible solutions

Now tell the interviewer there are two common designs.

Solution A — Use AmazonProvidedDNS

If you don't actually need custom DNS:

EC2
 ↓
AmazonProvidedDNS
169.254.169.253
 ↓
Route 53 Private Hosted Zone

Configure the VPC DHCP options to use:

AmazonProvidedDNS

Then renew the DHCP lease on existing instances.

This is the simplest solution.

12. Solution B — Keep custom DNS but forward internal queries

Suppose the company requires:

EC2
 ↓
Corporate DNS

You don't necessarily have to remove it.

Instead, configure conditional forwarding.

For example:

Corporate DNS
      |
      ├── google.com
      │       ↓
      │   Normal DNS
      │
      └── internal.example.com
              ↓
       AWS DNS Resolver
              ↓
       Route 53 PHZ

So the corporate DNS server is configured:

*.internal.example.com
        ↓
AWS resolver

This allows you to keep corporate DNS while still resolving AWS private zones.

For more complex hybrid environments, AWS Route 53 Resolver endpoints can be used for DNS forwarding between VPCs and on-premises networks.

13. Complete troubleshooting checklist

In an interview, give this sequence:

1. Check EC2 DNS configuration
        ↓
2. Check /etc/resolv.conf / resolvectl
        ↓
3. Identify actual DNS server
        ↓
4. Query AWS resolver directly
        ↓
5. Verify Route 53 Private Hosted Zone
        ↓
6. Verify PHZ is associated with the VPC
        ↓
7. Check DHCP Options Set
        ↓
8. Check whether custom DNS replaced AmazonProvidedDNS
        ↓
9. Remember DHCP lease behavior
        ↓
10. Renew DHCP lease / restart networking
        ↓
11. Retest private DNS
        ↓
12. If custom DNS is required,
    configure conditional forwarding
14. The commands I'd actually mention
Check DNS configuration
cat /etc/resolv.conf

or:

resolvectl status
Test public DNS
dig google.com
Test private DNS
dig service-a.internal.example.com
Test AWS resolver directly
dig service-a.internal.example.com @169.254.169.253
Renew DHCP
sudo dhclient -r
sudo dhclient

Then:

cat /etc/resolv.conf

and test again.

🎯 Interview-ready answer

If the interviewer asks this exact question, I would answer:

“The key clue is that public DNS works but the Route 53 private hostname doesn't. That tells me the EC2 instance still has general DNS connectivity, but it's probably no longer using the AWS VPC DNS resolver.”

“First, I would check /etc/resolv.conf or resolvectl status on the EC2 instance to identify the DNS server. The AWS-provided resolver is 169.254.169.253, or VPC CIDR plus 2. Route 53 Private Hosted Zones are resolved through that AWS resolver.”

“Then I would directly test the AWS resolver using dig service-a.internal.example.com @169.254.169.253. If that works while the normal query fails, I've isolated the problem to the DNS configuration.”

“Next, I would check the VPC DHCP Options Set. Most likely, the DNS server was changed from AmazonProvidedDNS to a custom or on-premises DNS server. That custom DNS can resolve public names like google.com but doesn't know about the Route 53 Private Hosted Zone.”

“I would also remember that DHCP changes don't immediately update all running instances because they can retain their existing DHCP lease. I would renew the DHCP lease or restart networking on affected instances and retest.”

“If the organization requires custom DNS, I wouldn't necessarily switch back to AmazonProvidedDNS. Instead, I would configure conditional forwarding for the internal AWS domain toward the AWS Route 53 Resolver, using the appropriate hybrid DNS architecture.”

🧠 Remember this flow

DNS server → AWS Resolver → Private Hosted Zone → DHCP Options → DHCP Lease → Forwarding

And the key sentence:

“Public DNS working does not prove private DNS is working; I need to verify that the instance's DNS server knows how to resolve the Route 53 Private Hosted Zone.”


-----------------------------------------------------------------------------------------------------------

18.

Absolutely. This is a very common AWS networking interview question because it tests whether you understand the difference between network routing and DNS resolution.

The easiest way to explain it is:

“VPC Peering gives connectivity between VPCs, but it does not automatically share DNS records or Private Hosted Zones between them.”

1. First understand the architecture

You have two VPCs:

        VPC-A                         VPC-B
   ┌──────────────┐              ┌──────────────┐
   │              │              │              │
   │ S3 Endpoint  │              │     EC2      │
   │ 10.0.1.50    │              │              │
   │              │              │              │
   └──────┬───────┘              └──────┬───────┘
          │                              │
          └──────── VPC Peering ─────────┘

VPC-A has:

S3 Interface VPC Endpoint
+
Private DNS enabled

VPC-B has:

EC2

and the VPCs are:

VPC-A ←── Peering ──→ VPC-B

The team thinks:

"Because the VPCs are peered, VPC-B should use VPC-A's private S3 endpoint."

But that's not how it works.

2. The most important concept

Remember these two separate things:

VPC Peering = Network connectivity

It allows:

VPC-A IP
    ↕
VPC-B IP

So IP packets can travel between the VPCs.

DNS = Name resolution

DNS answers:

s3.amazonaws.com
       ↓
Which IP address should I connect to?

These are different functions.

So:

Peering gives you the road, but it doesn't give you the other VPC's DNS phonebook.

That's a great analogy for an interview.

3. What happens in VPC-A?

In VPC-A, you created:

S3 Interface Endpoint

and enabled:

Private DNS

So when an EC2 inside VPC-A asks:

dig s3.amazonaws.com

AWS can return the endpoint's private IP:

s3.amazonaws.com
       ↓
10.0.1.50

Traffic becomes:

EC2-A
  ↓
10.0.1.50
  ↓
S3 Interface Endpoint
  ↓
S3

Everything works.

4. What happens in VPC-B?

Now EC2 in VPC-B runs:

dig s3.amazonaws.com

The important question is:

Which DNS resolver is VPC-B using?

VPC-B has its own VPC DNS resolver.

It doesn't automatically know:

VPC-A Private Hosted Zone

Therefore, VPC-B resolves:

s3.amazonaws.com
       ↓
Public DNS
       ↓
S3 public IP

So the traffic becomes:

EC2-B
  ↓
Public S3 IP
  ↓
S3

It completely bypasses:

VPC-A Interface Endpoint ❌
5. Why doesn't peering fix DNS?

This is the core interview question.

You can say:

“VPC Peering operates at Layer 3 and provides IP connectivity between the VPC CIDR ranges. DNS resolution is a separate service. The private DNS configuration associated with an interface endpoint isn't automatically propagated across VPC peering.”

In simple terms:

VPC Peering
     ↓
IP connectivity ✅
     
Private DNS
     ↓
DNS information sharing ❌

So:

Peering ≠ DNS sharing
6. What exactly does Private DNS do?

When you enable private DNS for an Interface Endpoint, AWS provides private DNS behavior for that VPC.

Conceptually:

VPC-A DNS

s3.amazonaws.com
       ↓
Private Endpoint IP
10.0.1.50

But that private DNS behavior is associated with VPC-A.

VPC-B doesn't automatically inherit it.

Therefore:

             VPC-A
        ┌───────────────┐
        │ Private DNS   │
        │               │
        │ S3 → 10.0.1.50│
        └───────────────┘
               ❌
          Doesn't cross
          automatically
               ❌
        ┌───────────────┐
             VPC-B
        │ DNS Resolver  │
        │               │
        │ S3 → Public IP│
        └───────────────┘
7. The easiest way to prove the problem

From an EC2 in VPC-B:

dig s3.amazonaws.com

You may get:

s3.amazonaws.com → Public S3 IP

Then compare with VPC-A.

From VPC-A:

dig s3.amazonaws.com

You may see:

s3.amazonaws.com → 10.x.x.x

That difference immediately tells you:

The issue is DNS resolution, not VPC peering connectivity.

8. What about "Allow DNS resolution from remote VPC"?

This is a subtle interview point.

VPC peering has DNS-related options.

Someone might say:

"But I enabled DNS resolution on the VPC peering connection!"

You should say:

“That doesn't mean the private DNS configuration of an interface endpoint is shared across the peering connection.”

The peering DNS settings can help with resolving certain private hostnames/IP addresses associated with resources in the peered VPC, but they don't magically make VPC-A's Route 53 private hosted zones available to VPC-B.

So remember:

Peering DNS settings
        ≠
Private Hosted Zone sharing
9. Solution 1 — Create an endpoint in VPC-B

This is usually the simplest answer.

Create an S3 endpoint directly in VPC-B.

             VPC-A
        ┌─────────────┐
        │ S3 Endpoint │
        └─────────────┘


             VPC-B
        ┌─────────────┐
        │     EC2     │
        │      ↓      │
        │ S3 Endpoint │
        └─────────────┘

Now:

EC2-B
  ↓
S3 private endpoint
  ↓
S3

No dependency on VPC-A's endpoint.

Interview answer

“My first choice would usually be to create an S3 endpoint directly in VPC-B. It's simpler, easier to troubleshoot, and keeps the endpoint close to the workloads that consume it.”

10. Important S3 detail: Gateway vs Interface Endpoint

For S3, there are two endpoint types you should know:

S3 Gateway Endpoint
S3 Interface Endpoint

A Gateway Endpoint is commonly used because it doesn't have the same per-hour endpoint ENI cost as interface endpoints and is designed for private S3 access through VPC route tables.

An Interface Endpoint uses private IP addresses through ENIs and supports PrivateLink-style access.

So in an interview, don't blindly say:

"Always create an Interface Endpoint."

Instead say:

“For S3, I'd evaluate whether a Gateway Endpoint is sufficient. If I specifically need Interface Endpoint/PrivateLink behavior, then I'd create an Interface Endpoint in the consumer VPC.”

That's a better answer.

11. Solution 2 — Centralized DNS

Suppose you have:

VPC-A
VPC-B
VPC-C
VPC-D
VPC-E

Creating and managing everything independently might become difficult.

You can build centralized DNS using:

Route 53 Resolver

Conceptually:

              DNS VPC
                 |
       ┌─────────┴─────────┐
       ↓                   ↓
 Resolver Endpoint    DNS Rules
       |
       ↓
 Private DNS
       |
 ┌─────┼─────┐
 ↓     ↓     ↓
VPC-A VPC-B VPC-C

Then VPCs can forward appropriate DNS queries to the central DNS infrastructure.

This is useful in larger enterprise environments.

12. Solution 3 — Route 53 Resolver forwarding

You can also use Resolver endpoints and forwarding rules for DNS queries.

For example:

VPC-B EC2
    |
    | s3.amazonaws.com?
    ↓
Route 53 Resolver
    |
    ↓
Forwarding rule
    |
    ↓
Resolver/DNS infrastructure

But there's an important architectural point:

Don't casually forward s3.amazonaws.com to 169.254.169.253 in VPC-B and assume that will make VPC-A's endpoint's private DNS work.

The AWS resolver at 169.254.169.253 is local to the VPC context; you need an appropriate Resolver/PrivateLink architecture rather than simply treating that address as a remotely reachable DNS server.

For this scenario, the cleanest answer remains:

Create the endpoint in VPC-B, or design centralized DNS intentionally.

13. How I would troubleshoot this in an interview

Say:

“I would first prove whether the problem is DNS or routing.”

Step 1 — Check VPC peering

Verify:

VPC-A ↔ VPC-B

is active.

Also verify route tables have the appropriate routes for the peer CIDRs.

Step 2 — Test DNS from VPC-B

From EC2:

dig s3.amazonaws.com

If it returns a public S3 address, that's the clue.

Step 3 — Compare with VPC-A

Run the same:

dig s3.amazonaws.com

If:

VPC-A → private endpoint IP
VPC-B → public S3 IP

then the issue is clearly DNS scope, not peering.

Step 4 — Check endpoint

In VPC-A:

VPC
 ↓
Endpoints
 ↓
S3 Interface Endpoint

Verify:

Private DNS = Enabled

and verify the endpoint is healthy.

Step 5 — Decide on the architecture

For a small/simple environment:

Create S3 endpoint in VPC-B

For a large enterprise:

Centralized DNS / Resolver architecture
🎯 Interview-ready answer

If the interviewer asks:

“VPC-B is peered with VPC-A, so why isn't it using VPC-A's private S3 endpoint?”

Answer:

“Because VPC Peering provides Layer 3 IP connectivity, but it doesn't automatically share DNS resolution or Private Hosted Zones between VPCs.”

“In VPC-A, the S3 Interface Endpoint has Private DNS enabled, so when an instance in VPC-A resolves s3.amazonaws.com, the VPC's DNS resolver returns the endpoint's private IP. But VPC-B has its own DNS resolver and doesn't automatically know about VPC-A's private DNS configuration. Therefore, an EC2 instance in VPC-B resolves s3.amazonaws.com to the public S3 endpoint and bypasses the PrivateLink endpoint.”

“I would verify this by running dig s3.amazonaws.com from both VPCs. If VPC-A returns a private IP and VPC-B returns a public S3 IP, I've confirmed it's a DNS-resolution issue rather than a peering issue.”

“For a simple solution, I'd create an S3 endpoint directly in VPC-B. Since S3 supports Gateway Endpoints as well, I'd evaluate using a Gateway Endpoint if the requirements allow it. In a larger enterprise environment, I could use Route 53 Resolver and a centralized DNS architecture to manage DNS resolution across multiple VPCs.”

🧠 Remember this one line

“Peering shares network connectivity, not DNS knowledge.”

And remember the troubleshooting chain:

Peering
  ↓
Can I reach the other VPC?       → Routing
  ↓
What IP does s3.amazonaws.com resolve to? → DNS
  ↓
Private IP? → Endpoint
Public IP?  → Bypassing endpoint

That's the core concept the interviewer is looking for.


-------------------------------------------------------------------------------------------------------------
19.


Absolutely. This is an important EKS networking interview scenario. The key thing the interviewer wants to know is whether you understand that EKS pods consume real VPC IP addresses when using the AWS VPC CNI plugin.

1. First understand the problem

The cluster is healthy:

Nodes → Healthy ✅
EKS → Running ✅

But pods are failing:

kubectl describe pod
        ↓
0/5 nodes available:
5 Insufficient IPs

This does not mean CPU or memory is insufficient.

It means:

The node/subnet doesn't have enough available IP addresses for the AWS VPC CNI to assign to new pods.

2. The most important concept

Normally, people think:

Pod → gets some Kubernetes internal IP

But with the AWS VPC CNI, pods receive IP addresses from the AWS VPC networking layer.

Conceptually:

VPC
│
└── Subnet: 10.0.11.0/24
       │
       ├── EC2 Node → 10.0.11.10
       │
       ├── Pod A   → 10.0.11.50
       ├── Pod B   → 10.0.11.51
       ├── Pod C   → 10.0.11.52
       └── ...

So pods consume addresses from your subnet's IP pool.

3. Why can scaling nodes actually cause this problem?

Suppose you have:

Subnet = 10.0.11.0/24

A /24 has:

256 total addresses

AWS reserves some addresses, so you have roughly:

251 usable IPv4 addresses

Now imagine:

5 nodes
20 pods per node

That's approximately:

5 × 20 = 100 pod IPs

Plus:

Node IPs
ENI IPs
AWS infrastructure reservations
Other resources

As the cluster grows:

IP pool
│
├── Nodes
├── Pods
├── ENIs
└── Other resources
        ↓
   IPs get consumed
        ↓
   No free IPs ❌

Then Kubernetes says:

Insufficient IPs
4. There are actually TWO limits to think about

This is a very important interview point.

When you see:

Insufficient IPs

don't think only about subnet size.

There are two different constraints.

Limit 1 — Subnet IP capacity

Does the subnet have enough free IP addresses?

Subnet
  ↓
Available IPs?

If:

Available IPv4 = 0

you can't allocate more pod IPs from that subnet.

Limit 2 — EC2 networking capacity

Even if the subnet has plenty of IP addresses, an EC2 instance has limits on:

Number of ENIs
IPv4 addresses per ENI
Maximum pod/network capacity

So:

Subnet has free IPs ✅
        ↓
EC2 networking limit reached ❌
        ↓
New pod can't get an IP

This is why you need to check both subnet capacity and instance type limits.

5. How the AWS VPC CNI works

You don't need to explain the entire CNI implementation in an interview.

Say:

“The AWS VPC CNI plugin is responsible for assigning VPC networking to pods. It attaches or manages ENIs and secondary IP addresses on the worker nodes, and those addresses are used by pods.”

Conceptually:

EC2 Node
   |
   ├── Primary ENI
   │      └── Node IP
   │
   ├── Secondary IP → Pod A
   ├── Secondary IP → Pod B
   ├── Secondary IP → Pod C
   └── ...

So more pods means more IP consumption.

6. Step-by-step troubleshooting

This is the part you should memorize for an interview.

Say:

“I would troubleshoot this in two directions: first check whether the subnet has enough IP addresses, then check whether the EC2 instance type has enough networking capacity.”

Step 1 — Check the subnet's available IPs

In AWS Console:

VPC
 ↓
Subnets
 ↓
Select EKS subnet
 ↓
Available IPv4 addresses

If you see something like:

Available IPv4 addresses: 5

and you're trying to schedule many pods, that's a strong indication of subnet exhaustion.

You can also check through AWS CLI:

aws ec2 describe-subnets \
  --subnet-ids subnet-xxxx \
  --query 'Subnets[*].{CIDR:CidrBlock,AvailableIPs:AvailableIpAddressCount}'
7. Step 2 — Check where the pods are running

Use:

kubectl get nodes -o wide

and:

kubectl get pods -A -o wide

This lets you see:

Node
 ↓
Pod
 ↓
Pod IP

You can identify whether a particular subnet is getting exhausted.

8. Step 3 — Check the node instance type

Suppose your nodes are:

t3.medium

Now check its network limits.

For example:

aws ec2 describe-instance-types \
  --instance-types t3.medium \
  --query 'InstanceTypes[*].NetworkInfo'

You're interested in values such as:

MaximumNetworkInterfaces
Ipv4AddressesPerInterface

These determine how much networking capacity the node has.

9. Important correction about the formula

Your material gives:

Max Pods = (max ENIs × IPs per ENI) - 1

This is useful as a rough conceptual explanation, but don't present it as a universal exact EKS formula.

Actual EKS pod density depends on the:

EC2 instance type
AWS VPC CNI configuration
ENI/IP allocation behavior
Prefix delegation settings
EKS maximum-pods configuration

So in an interview, say:

“The pod limit depends on the EC2 instance's ENI and IP-per-ENI limits and the VPC CNI configuration. I would verify the actual supported pod capacity for the specific instance type rather than relying on a generic formula.”

That's safer technically.

10. Step 4 — Check the AWS VPC CNI

Check:

kubectl get pods -n kube-system

Look for:

aws-node

You can also check:

kubectl describe daemonset aws-node -n kube-system

The AWS VPC CNI is responsible for providing pod networking.

If there is a CNI issue, you'll want to investigate its logs/configuration as well.

11. Step 5 — Decide whether the problem is subnet capacity or node capacity

This distinction is critical.

Case A: Subnet exhausted
Subnet:
Available IPs = 0

Then:

Problem → Subnet CIDR too small

Solution:

Add larger/new subnets
Case B: Subnet has plenty of IPs

But:

EC2 networking capacity = reached

Then:

Problem → Node instance type/networking limit

Solution could be:

Use larger instance type
or
increase pod networking capacity
12. How do you fix subnet exhaustion?

There are two common approaches.

Option 1 — Add new subnets

For example:

Old:
10.0.11.0/24

New:
10.0.12.0/22
10.0.16.0/22

Then configure your EKS node group to use the new subnets.

Conceptually:

EKS Node Group
      |
      ├── Subnet A /24
      ├── Subnet B /24
      └── Subnet C /22 ← New IP capacity

New nodes can be launched in the new subnet and pods can consume IPs there.

13. Can you simply resize the existing subnet?

This is a common interview trick.

Generally:

You cannot simply change an existing subnet's CIDR to make it larger.

Instead, create another subnet with an available CIDR range.

If the VPC itself doesn't have enough address space, you may need to associate a secondary CIDR block with the VPC and then create additional subnets from that range.

Conceptually:

VPC
10.0.0.0/16
      +
10.1.0.0/16   ← secondary CIDR

Then:

10.1.0.0/22
10.1.4.0/22

can be used for additional EKS capacity.

14. What subnet size should you use?

Don't memorize:

/24 is always wrong.

Instead say:

“Subnet sizing should be based on expected node count, pod density, AWS networking overhead, scaling requirements and IP growth. For production EKS, I would generally allocate significantly more address space than a small /24 if the cluster is expected to scale.”

For example:

/24 → ~251 usable IPv4 addresses
/22 → ~1,019 usable IPv4 addresses
/21 → ~2,043 usable IPv4 addresses

The exact usable number accounts for AWS subnet reservations.

So /22 provides roughly 4× the address space of /24.

15. Another important solution: Prefix Delegation

If the interviewer goes deeper, mention:

“With AWS VPC CNI, prefix delegation can significantly improve pod IP scalability by assigning prefixes to ENIs rather than allocating individual secondary IPs one at a time.”

Conceptually:

Without prefix delegation
ENI
 ├── IP → Pod
 ├── IP → Pod
 ├── IP → Pod
 └── IP → Pod
With prefix delegation
ENI
 └── /28 prefix
       ├── Pod IP
       ├── Pod IP
       ├── Pod IP
       ├── Pod IP
       └── ...

This can improve how efficiently the CNI allocates pod IP capacity.

But remember:

Prefix delegation doesn't create unlimited VPC addresses. You still need enough subnet CIDR space.

16. A good troubleshooting flow

Memorize this:

Pod Pending
     ↓
"Insufficient IPs"
     ↓
Check subnet available IPs
     ↓
 ┌───────────────┐
 │               │
 ↓               ↓
No IPs         Plenty of IPs
 │               │
 ↓               ↓
Subnet issue   Node networking limit?
 │               │
 ↓               ↓
Add subnet     Check instance type
or CIDR        ENI/IP limits
                 │
                 ↓
            Check VPC CNI
                 │
                 ↓
        Prefix delegation /
        larger instance
🎯 Interview-ready answer

If the interviewer asks:

“Your EKS pods can't schedule because of Insufficient IPs. What's happening?”

Say:

“I would first identify whether this is subnet IP exhaustion or an EC2 networking limit. EKS commonly uses the AWS VPC CNI, which gives pods VPC-routable IP addresses rather than purely overlay IPs. So every pod consumes IP capacity from the networking resources available to the nodes and ultimately from the VPC subnet address space.”

“First, I would check the EKS worker-node subnets and their Available IPv4 addresses in the VPC console or using describe-subnets. Then I'd use kubectl get pods -A -o wide and kubectl get nodes -o wide to understand pod and node placement.”

“If the subnet is exhausted, I would add new appropriately sized subnets and configure the node group to use them. If the VPC itself doesn't have enough address space, I could add a secondary VPC CIDR and create additional subnets from it. I would not try to resize the existing subnet.”

“If the subnet has plenty of free IPs, I'd check the EC2 instance type's ENI and IPv4-per-ENI limits and verify the VPC CNI configuration. Depending on the requirements, I could use a larger instance type or enable features such as prefix delegation to improve pod IP allocation efficiency.”

“For production, I would plan EKS subnet CIDRs based on maximum expected nodes and pods rather than waiting until the subnet is exhausted.”

🧠 The one-line answer

Remember this:

“In EKS with AWS VPC CNI, pods consume VPC networking IP capacity. Insufficient IPs means either the subnet doesn't have enough addresses or the node has reached its ENI/IP networking limit.”

And your troubleshooting keywords are:

Subnet → Available IPs → Pod IPs → EC2 ENI limits → VPC CNI → Prefix Delegation → Add CIDR/Subnets


--------------------------------------------------------------------------------------------------------------
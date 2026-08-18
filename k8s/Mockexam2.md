1. Create a storage class called orange-stc-cka07-str as per the properties given below:

Provisioner should be kubernetes.io/no-provisioner.
Volume binding mode should be WaitForFirstConsumer.
Next, create a persistent volume called orange-pv-cka07-str as per the properties given below:
Capacity should be 150Mi.
Access mode should be ReadWriteOnce.
Reclaim policy should be Retain.
It should use storage class orange-stc-cka07-str.
Local path should be /opt/orange-data-cka07-str.
Also add node affinity to create this value on cluster1-controlplane.
Finally, create a persistent volume claim called orange-pvc-cka07-str as per the properties given below:
Access mode should be ReadWriteOnce.
It should use storage class orange-stc-cka07-str.
Storage request should be 128Mi.
The volume should be orange-pv-cka07-str.

sol. 

Run:

kubectl get storageclass orange-stc-cka07-str -o yaml

It should effectively match:

apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: orange-stc-cka07-str
provisioner: kubernetes.io/no-provisioner
volumeBindingMode: WaitForFirstConsumer

Checklist:

✅ Name = orange-stc-cka07-str
✅ provisioner: kubernetes.io/no-provisioner
✅ volumeBindingMode: WaitForFirstConsumer

You can also do:

kubectl describe storageclass orange-stc-cka07-str

Expected important fields:

Provisioner:          kubernetes.io/no-provisioner
VolumeBindingMode:    WaitForFirstConsumer
2. Verify PersistentVolume

Run:

kubectl get pv orange-pv-cka07-str -o yaml

It should look like this:

apiVersion: v1
kind: PersistentVolume
metadata:
  name: orange-pv-cka07-str
spec:
  capacity:
    storage: 150Mi
  accessModes:
    - ReadWriteOnce
  persistentVolumeReclaimPolicy: Retain
  storageClassName: orange-stc-cka07-str

  local:
    path: /opt/orange-data-cka07-str

  nodeAffinity:
    required:
      nodeSelectorTerms:
      - matchExpressions:
        - key: kubernetes.io/hostname
          operator: In
          values:
          - cluster1-controlplane

Checklist:

✅ Name = orange-pv-cka07-str
✅ Capacity = 150Mi
✅ Access mode = ReadWriteOnce
✅ Reclaim policy = Retain
✅ Storage class = orange-stc-cka07-str
✅ Local path = /opt/orange-data-cka07-str
✅ Node affinity → cluster1-controlplane

Quick check:

kubectl describe pv orange-pv-cka07-str

Expected:

StorageClass:     orange-stc-cka07-str
Reclaim Policy:   Retain
Access Modes:     RWO
Capacity:         150Mi
Path:             /opt/orange-data-cka07-str
3. Verify PersistentVolumeClaim

Run:

kubectl get pvc orange-pvc-cka07-str -o yaml

Expected:

apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: orange-pvc-cka07-str
spec:
  accessModes:
    - ReadWriteOnce
  storageClassName: orange-stc-cka07-str
  resources:
    requests:
      storage: 128Mi
  volumeName: orange-pv-cka07-str

Checklist:

✅ Name = orange-pvc-cka07-str
✅ Access mode = ReadWriteOnce
✅ Storage class = orange-stc-cka07-str
✅ Request size = 128Mi
✅ Bound to orange-pv-cka07-str

Check status:

kubectl get pvc orange-pvc-cka07-str

Expected:

NAME                    STATUS   VOLUME                 CAPACITY
orange-pvc-cka07-str    Bound    orange-pv-cka07-str   150Mi
Fast validation commands

Run these:

kubectl get sc orange-stc-cka07-str
kubectl get pv orange-pv-cka07-str
kubectl get pvc orange-pvc-cka07-str

Expected:

storageclass.storage.k8s.io/orange-stc-cka07-str
persistentvolume/orange-pv-cka07-str
persistentvolumeclaim/orange-pvc-cka07-str

If you paste the output of:

kubectl get sc,pv,pvc -o yaml
------------------------------------------------------------------
2. As a Kubernetes administrator, you are unable to run any of the kubectl commands on the cluster. Troubleshoot the problem and get the cluster to a functioning state.

sol.

Think of it as moving from outside → inside of the cluster.

1. Start with the symptom

Run:

kubectl version

Interpret the output:

Case A — only client version
Client Version: v1.32.0
The connection to the server x.x.x.x:6443 was refused

Meaning:

kubectl works
kubeconfig exists
API server unreachable

This was our case.

Case B — localhost:8080 refused
The connection to the server localhost:8080 was refused

Meaning:

kubeconfig missing/broken

Check:

kubectl config view
kubectl config current-context
echo $KUBECONFIG
Case C — auth/cert issue
Unauthorized
certificate signed by unknown authority

Meaning:

cert or RBAC issue
2. Verify kubectl itself

Before touching the cluster, confirm CLI health:

which kubectl
kubectl version --client

Questions:

Is binary present?
Does client version work?

In our case:

/usr/bin/kubectl
Client Version: v1.32.0

So CLI was fine.

3. Determine what exactly is broken

We ran:

kubectl version

Got:

connection refused to cluster2-controlplane:6443

Key deduction:

Port 6443 = Kubernetes API server.

So ask:

Why is kube-apiserver unavailable?

That immediately narrows scope to control plane.

4. Check control plane containers

On control plane node:

crictl ps -a

Look for:

kube-apiserver
kube-controller-manager
kube-scheduler
etcd

Our output:

etcd → Running
kube-controller-manager → Exited
kube-scheduler → Exited
kube-apiserver → missing

Deduction:

API server never started.

Since etcd worked, container runtime wasn’t fully dead.

5. Check manifests

Control plane static pods live here:

ls /etc/kubernetes/manifests/

Expected:

etcd.yaml
kube-apiserver.yaml
kube-controller-manager.yaml
kube-scheduler.yaml

We saw all files existed.

Deduction:

Manifest missing? ❌

So next question:

Who reads these manifests?

Answer:

kubelet

6. Check kubelet

We tried:

systemctl status kubelet

Output:

Unit kubelet.service could not be found

Huge clue.

Then:

ps aux | grep kubelet

Output:

grep kubelet

Meaning:

kubelet not running.

Deduction:

No kubelet = no static pods.

That explains:

no apiserver
scheduler exited
controller-manager exited
6443 refused
7. Verify whether kubelet exists

Check binary:

which kubelet
find / -type f -name kubelet

Output:

not found

Then package state:

dpkg -l | grep kubelet

Output:

rc kubelet

Critical interpretation:

rc = removed, config remains

Meaning:

kubelet package removed.

Root cause found.

8. Fix

Reinstall kubelet:

sudo apt update
sudo apt install -y kubelet=1.32.0-1.1

Start service:

sudo systemctl daemon-reload
sudo systemctl enable kubelet
sudo systemctl start kubelet

Why this works:

kubelet automatically reads:

/etc/kubernetes/manifests/

and recreates:

kube-apiserver
kube-controller-manager
kube-scheduler

No manual pod recreation needed.

9. Verify cluster recovery

Run:

kubectl version
kubectl get nodes
kubectl get pods -A

Healthy signs:

Server Version: v1.32.0

Nodes:

Ready

Control-plane pods:

Running
The mental model to remember

Use this order every time:

kubectl
   ↓
API server (6443)
   ↓
control plane pods
   ↓
kubelet
   ↓
container runtime
   ↓
manifests/certs/network

A fast exam checklist:

kubectl version
which kubectl
kubectl version --client

crictl ps -a
ls /etc/kubernetes/manifests/

systemctl status kubelet
ps aux | grep kubelet

which kubelet
dpkg -l | grep kubelet

kubectl get nodes
kubectl get pods -A

---------------------------------------------------------

3. 
Create a PriorityClass named high-priority with a value of 1000000. A deployment named hp-webapp is in the namespace high-priority. Modify the deployment to use the priority class you created.
Is the hp-webapp deployment utilizing a high-priority PriorityClass?

sol.

apiVersion: scheduling.k8s.io/v1
kind: PriorityClass
metadata:
  name: high-priority
value: 1000000
globalDefault: false
description: "High priority class"

Apply it:

kubectl apply -f priorityclass.yaml

Or create it directly:

kubectl create priorityclass high-priority --value=1000000
2. Modify the deployment to use the PriorityClass

Patch the deployment hp-webapp in namespace high-priority:

kubectl patch deployment hp-webapp \
  -n high-priority \
  -p '{"spec":{"template":{"spec":{"priorityClassName":"high-priority"}}}}'

Alternatively, edit it manually:

kubectl edit deployment hp-webapp -n high-priority

Add:

spec:
  template:
    spec:
      priorityClassName: high-priority
3. Verify whether hp-webapp is utilizing the PriorityClass

Run:

kubectl get deployment hp-webapp \
  -n high-priority \
  -o jsonpath='{.spec.template.spec.priorityClassName}'

Expected output:

high-priority

You can also verify the running pods:

kubectl get pods -n high-priority -o custom-columns=NAME:.metadata.name,PRIORITYCLASS:.spec.priorityClassName

-------------------------------------------------------------------------------
Q
4. 
One application, webpage-server-01, is deployed on the Kubernetes cluster by the Helm tool in default namespace. Now, the team wants to deploy a new version of the application by replacing the existing one. A new version of the helm chart is given in the /root/new-version directory on the cluster1-controlplane. Validate the chart before installing it on the Kubernetes cluster.

Use the helm command to validate and install the chart. After successfully installing the newer version, uninstall the older version.

sol.

1. SSH to the control plane (if not already there)
ssh cluster1-controlplane
2. Identify the current Helm release

Check the existing release in the default namespace:

helm list -n default

You should see the existing application release for webpage-server-01. Note the release name.

3. Validate the new Helm chart

Validate the chart located at /root/new-version:

helm lint /root/new-version

(Optional but useful to inspect manifests before install)

helm template /root/new-version
4. Install the newer version

Install the new chart into the default namespace (choose a temporary release name, for example webpage-server-01-v2):

helm install webpage-server-01-v2 /root/new-version -n default

Verify it is deployed:

helm list -n default
kubectl get pods -n default
5. Uninstall the older version

After confirming the new release is healthy, uninstall the old release (replace <old-release-name> with the release name found in step 2):

helm uninstall <old-release-name> -n default
6. Verify final state
helm list -n default
kubectl get all -n default

----------------------------------------------------------------------------
Q
5. 
Your cluster has a failed deployment named backend-api with multiple pods. Troubleshoot the deployment so that all pods are in a running state. Do not make adjustments to the resource limits defined on the deployment pods.
NOTE: A ResourceQuota named cpu-mem-quota is applied to the default namespace and should not be edited or modified.

sol:

The deployment is failing because the namespace has a ResourceQuota and the requested third replica likely exceeds the quota, causing FailedCreate. Since you must not change limits and must not edit the ResourceQuota, the fix is to adjust the deployment so it fits within the quota while preserving the existing pod limits.

Current per-pod resources:

Requests: 100m CPU, 128Mi memory
Limits: 150m CPU, 150Mi memory
Replicas desired: 3

Two pods already exist and are available; the third cannot be created.

Troubleshooting steps
Confirm the quota issue:
kubectl describe quota cpu-mem-quota
kubectl get events --sort-by=.metadata.creationTimestamp

You should see quota exhaustion (CPU or memory request/limit exceeded).

Reduce replicas so all pods can run without changing limits:
kubectl scale deployment backend-api --replicas=2
Verify:
kubectl get pods
kubectl get deployment backend-api
kubectl describe deployment backend-api
kubectl describe quota cpu-mem-quota

--------------------------------------------------------------------------------------
Q
6. 
Deploy a Vertical Pod Autoscaler (VPA) named analytics-vpa for a deployment named analytics-deployment in the cka24456 namespace. The VPA should automatically adjust the CPU and memory requests of the pods to optimize resource utilization. Ensure that the VPA operates in Auto mode, allowing it to evict and recreate pods with updated resource requests as needed.
Is the VPA configured to target the correct deployment?
Is the VPA mode configured to "Auto"?

sol:

apiVersion: autoscaling.k8s.io/v1
kind: VerticalPodAutoscaler
metadata:
  name: analytics-vpa
  namespace: cka24456
spec:
  targetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: analytics-deployment
  updatePolicy:
    updateMode: Auto

Deploy it:

kubectl apply -f analytics-vpa.yaml

Or inline:

kubectl apply -f - <<EOF
apiVersion: autoscaling.k8s.io/v1
kind: VerticalPodAutoscaler
metadata:
  name: analytics-vpa
  namespace: cka24456
spec:
  targetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: analytics-deployment
  updatePolicy:
    updateMode: Auto
EOF

Verify:

kubectl get vpa -n cka24456
kubectl describe vpa analytics-vpa -n cka24456

-------------------------------------------------------------------------------------
Q
7. 

A pod called pink-pod-cka16-trb is created in the default namespace in cluster4. This app runs on port tcp/5000, and it is to be exposed to end-users using an ingress resource called pink-ing-cka16-trb such that it becomes accessible using the command curl http://kodekloud-pink.app on the cluster4-controlplane host. There is an ingress.yaml file under the root folder in cluster4-controlplane. Create an ingress resource by following the command and continue with the task.

kubectl create -f ingress.yaml

--------------------------------------------------------------------------------------

Q
8. 
A pod named beta-pod-cka01-arch has been created in the beta-cka01-arch namespace. Inspect the logs and save all logs starting with the string ERROR in file /root/beta-pod-cka01-arch_errors on the cluster1-controlplane.
Is the error log captured?

kubectl logs -n beta-cka01-arch beta-pod-cka01-arch | grep "^ERROR" > /root/beta-pod-cka01-arch_errors

-------------------------------------------------------------------------------------
Q
9. 
Solve this question on: ssh cluster1-controlplane
John is setting up a two-tier application stack that is supposed to be accessible using the service curlme-cka01-svcn. To test that the service is accessible, he is using a pod called curlpod-cka01-svcn. However, at the moment, he is unable to get any response from the application.
Troubleshoot and fix this issue so the application stack is accessible.
You may delete and recreate the service curlme-cka01-svcn if needed.
Can curlpod-cka01-svcn access "curlme-cka01-svcn" pod?

sol:
The Service selector is wrong:

Current selector:

run=curlme-ckaO1-svcn

Actual pod label:

run=curlme-cka01-svcn

Notice the typo:

Service → ckaO1 (letter O)
Pod → cka01 (zero 0)

Because of this mismatch, the service has no endpoints.

You can fix it by recreating the service (allowed by the question).

Delete the bad service
kubectl delete svc curlme-cka01-svcn
Recreate the service with the correct selector
kubectl expose pod curlme-cka01-svcn \
  --name=curlme-cka01-svcn \
  --port=80 \
  --target-port=80
Verify endpoints
kubectl get endpoints curlme-cka01-svcn

You should now see a pod IP instead of empty output.

Test from curl pod
kubectl exec -it curlpod-cka01-svcn -- curl curlme-cka01-svcn

You should now get a response from the application.

You can also confirm via:

kubectl describe svc curlme-cka01-svcn

The Endpoints: field should no longer be empty.

--------------------------------------------------------------------------------------
Q
10. 



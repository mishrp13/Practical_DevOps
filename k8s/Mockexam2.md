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

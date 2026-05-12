1. Just write HPA refrence K8s docs


Q. We have created a service account called green-sa-cka22-arch, a cluster role called green-role-cka22-arch, and a cluster role binding called green-role-binding-cka22-arch.
Update the permissions of this service account so that it can only get all the namespaces in cluster1.
Are service account permissions updated?
2. You don’t need to touch the ServiceAccount itself — the fix is in the ClusterRole permissions.

Right now, the role likely has broader access. You need to restrict it so it can only “get” namespaces.

✅ Step 1: Edit the ClusterRole

Run:

kubectl edit clusterrole green-role-cka22-arch
✏️ Modify it to this:
rules:
- apiGroups: [""]
  resources: ["namespaces"]
  verbs: ["get"]
✅ Step 2: Save and exit

This will immediately update permissions because:

The ClusterRoleBinding (green-role-binding-cka22-arch) already links
the role to the ServiceAccount green-sa-cka22-arch
🔍 Step 3: Verify

You can test with:

kubectl auth can-i get namespaces \
--as=system:serviceaccount:default:green-sa-cka22-arch

Expected output:

yes

And test something else (should fail):

kubectl auth can-i list pods \
--as=system:serviceaccount:default:green-sa-cka22-arch

Expected:

no
🧠 Key idea
apiGroups: [""] → core API group (namespaces live here)
resources: ["namespaces"] → target resource
verbs: ["get"] → only allow read of a single namespace (not list, not create)
cd
 
3. 
The pink-depl-cka14-trb Deployment was scaled to 2 replicas; however, the current replica count is still 1.

Troubleshoot and fix this issue. Make sure the CURRENT count is equal to the DESIRED count.

You can SSH into the cluster4 using ssh cluster4-controlplane command.

ANS:

The Deployment configuration is now correct, but no ReplicaSet and no Pods are being created.

That means the Kubernetes Deployment controller is not working.

Check the controller manager pod:

kubectl get pods -n kube-system

Look for:

kube-controller-manager

It is likely:

not running
crashing
or unhealthy

Then inspect it:

kubectl describe pod -n kube-system <kube-controller-manager-pod-name>

and:

kubectl logs -n kube-system <kube-controller-manager-pod-name>


4. 
A persistent volume called papaya-pv-cka09-str is already created with a storage capacity of 150Mi. It's using the papaya-stc-cka09-str storage class with the path /opt/papaya-stc-cka09-str.

A persistent volume claim named papaya-pvc-cka09-str has also been created on this cluster. This PVC has requested 50Mi of storage from papaya-pv-cka09-str volume.

Resize the PVC to 80Mi and make sure the PVC is in the Bound state.

Ans:

Check the PVC:

kubectl get pvc papaya-pvc-cka09-str

Edit the PVC:

kubectl edit pvc papaya-pvc-cka09-str

Change:

storage: 50Mi

to:

storage: 80Mi

Save and exit.

Now check status:

kubectl get pvc papaya-pvc-cka09-str

If it stays Bound, the task is complete.

If resizing fails, the StorageClass may not allow expansion. Check:

kubectl get sc papaya-stc-cka09-str -o yaml

Look for:

allowVolumeExpansion: true

If missing, patch it:

kubectl patch sc papaya-stc-cka09-str -p '{"allowVolumeExpansion":true}'

Then re-edit the PVC to 80Mi.

Final verification:

kubectl get pvc papaya-pvc-cka09-str

Expected:

NAME                    STATUS   VOLUME                CAPACITY   ACCESS MODES   STORAGECLASS
papaya-pvc-cka09-str   Bound    papaya-pv-cka09-str  80Mi       RWO            papaya-stc-cka09-str

PVC resizing requires the StorageClass to support allowVolumeExpansion.


5. 

On the cluster2-controlplane, a Helm chart repository is given under the /opt/ path. It contains the files that describe a set of Kubernetes resources that can be deployed as a single unit. The files have some issues. Fix those issues and deploy them with the following specifications: -

The release name should be webapp-color-apd.
All the resources should be deployed on the frontend-apd namespace.
The service type should be node port.
Scale the deployment to 3.
Application version should be 1.20.0.
NOTE: - Remember to make necessary changes in the values.yaml and Chart.yaml files according to the specifications, and, to fix the issues, inspect the template files.


sol. 
SSH into cluster2-controlplane and locate the Helm chart under /opt.
Update Chart.yaml:
appVersion: "1.20.0"
Update values.yaml:
replicaCount: 3

service:
  type: NodePort
Inspect and fix issues in the templates under the templates/ directory.
Typical fixes include:
Incorrect template syntax
Wrong indentation
Invalid selector labels
Missing .Values references
Incorrect API versions
Create the namespace:
kubectl create namespace frontend-apd
Deploy the chart using the required release name:
helm install webapp-color-apd /opt/<chart-directory> -n frontend-apd
Verify the deployment:
helm list -n frontend-apd
kubectl get all -n frontend-apd

Expected validations:

Release name:
helm list -n frontend-apd

Should show:

webapp-color-apd
Namespace:
kubectl get all -n frontend-apd
Service type:
kubectl get svc -n frontend-apd

Should show:

NodePort
Replicas:
kubectl get deploy -n frontend-apd

Should show:

3/3
Application version:
helm show chart /opt/<chart-directory>

Should show:

appVersion: 1.20.0
Resources running:
kubectl get pods -n frontend-apd

All pods should be in:

Running

6. 
Create an HTTPRoute named web-route in the nginx-gateway namespace that directs traffic from the web-gateway to a backend service named web-service on port 80 and ensures that the route is applied only to requests with the hostname cluster2-controlplane.


To test the configuration, run the following command:

curl http://cluster2-controlplane:30080


sol:

Create the HTTPRoute manifest:

apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: web-route
  namespace: nginx-gateway
spec:
  parentRefs:
  - name: web-gateway
  hostnames:
  - "cluster2-controlplane"
  rules:
  - backendRefs:
    - name: web-service
      port: 80

Apply it:

kubectl apply -f web-route.yaml

Verify:

kubectl get httproute -n nginx-gateway

Test the configuration:

curl http://cluster2-controlplane:30080

You should receive a successful response from the web-service backend.


7. Create a service account called deploy-cka20-arch. Further, create a cluster role called deploy-role-cka20-arch with permissions to get the deployments in cluster1.


Finally, create a cluster role binding called deploy-role-binding-cka20-arch to bind deploy-role-cka20-arch cluster role with the deploy-cka20-arch service account.


sol: 
Create the ServiceAccount:
kubectl create serviceaccount deploy-cka20-arch
Create the ClusterRole with permissions to get deployments:
kubectl create clusterrole deploy-role-cka20-arch \
  --verb=get \
  --resource=deployments
Create the ClusterRoleBinding:
kubectl create clusterrolebinding deploy-role-binding-cka20-arch \
  --clusterrole=deploy-role-cka20-arch \
  --serviceaccount=default:deploy-cka20-arch
Verify:
kubectl get sa
kubectl get clusterrole deploy-role-cka20-arch
kubectl get clusterrolebinding deploy-role-binding-cka20-arch

8. 

Create an nginx pod called nginx-resolver-cka06-svcn using the image nginx, and expose it internally with a service called nginx-resolver-service-cka06-svcn.

Test that you are able to look up the service and pod names from within the cluster. Use the image busybox:1.28 for dns lookup. Record results in /root/CKA/nginx.svc.cka06.svcn and /root/CKA/nginx.pod.cka06.svcn on cluster1-controlplane.

sol:

Create the nginx pod:
kubectl run nginx-resolver-cka06-svcn \
  --image=nginx
Expose the pod internally with a ClusterIP service:
kubectl expose pod nginx-resolver-cka06-svcn \
  --name=nginx-resolver-service-cka06-svcn \
  --port=80 \
  --target-port=80
Verify pod and service:
kubectl get pod nginx-resolver-cka06-svcn
kubectl get svc nginx-resolver-service-cka06-svcn
Test Service DNS resolution using BusyBox and save output:
kubectl run test-dns-service \
  --image=busybox:1.28 \
  --restart=Never \
  --rm -it \
  -- nslookup nginx-resolver-service-cka06-svcn > /root/CKA/nginx.svc.cka06.svcn

If redirection does not work interactively, use:

kubectl run test-dns-service \
  --image=busybox:1.28 \
  --restart=Never \
  --command -- nslookup nginx-resolver-service-cka06-svcn \
  > /root/CKA/nginx.svc.cka06.svcn
Test Pod DNS resolution and save output:
kubectl run test-dns-pod \
  --image=busybox:1.28 \
  --restart=Never \
  --command -- nslookup nginx-resolver-cka06-svcn \
  > /root/CKA/nginx.pod.cka06.svcn
Verify the files:
cat /root/CKA/nginx.svc.cka06.svcn
cat /root/CKA/nginx.pod.cka06.svcn

Expected:

Pod nginx-resolver-cka06-svcn exists
Service nginx-resolver-service-cka06-svcn exposes the pod
DNS lookup results are recorded in the required files
 
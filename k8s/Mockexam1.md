1. Just write HPA refrence K8s docs


Q. We have created a service account called green-sa-cka22-arch, a cluster role called green-role-cka22-arch, and a cluster role binding called green-role-binding-cka22-arch.
Update the permissions of this service account so that it can only get all the namespaces in cluster1.
Are service account permissions updated?

-------------------------------------------------------------
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
 -------------------------------------------------------------------
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
------------------------------------------------------------------

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

------------------------------------------------------------------------
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
--------------------------------------------------------------------------
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

---------------------------------------------------------------------
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
----------------------------------------------------------------------
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
 
----------------------------------------------------------------------
 9. 
 We tried to schedule the grey-cka21-trb pod on cluster4-controlplane, which was supposed to be deployed by the kubernetes scheduler so far, but somehow it is stuck in a Pending state. Look into the issue and fix it. Make sure the pod is in the Running state.

sol:

# Check pod status and node assignment
kubectl get pod grey-cka21-trb -o wide

# Describe the pod to see scheduling errors/events
kubectl describe pod grey-cka21-trb

# Check scheduler-related events
kubectl get events --sort-by=.metadata.creationTimestamp

# Verify the target node is Ready
kubectl get nodes
kubectl describe node cluster4-controlplane

1. when i describe nodes got to know node is tainted then  i ran below command:
kubectl taint nodes cluster4-controlplane node-role.kubernetes.io/control-plane-
kubectl taint nodes cluster4-controlplane node-role.kubernetes.io/control-plane:NoSchedule-

2. even after removing the taint from the node the pod was still in pending state then when i checked the while describing the pod i found that there was no scheduler events at all that means scheduler itself not functioning

kubectl get pods -n kube-system | grep scheduler  -> (crashloop backoff)
kubectl logs -n kube-system kube-scheduler-cluster4-controlplane

vi /etc/kubernetes/manifests/kube-scheduler.yaml -> change config to conf

3. Then checked the status of
kubectl get pods -n kube-system | grep scheduler -> runnig
and pod also came in running state.
-------------------------------------------------------------------------

10. 
In the dev-wl07 namespace, one of the developers has performed a rolling update and upgraded the application to a newer version. But somehow, application pods are not being created.
To get back the working state, rollback the application to the previous version .
After rolling the deployment back, on the cluster1-controlplane node, save the image currently in use to the /root/rolling-back-record.txt file and increase the replica count to 5.

sol. 

kubectl get deploy -n dev-wl07

Check rollout history:

kubectl rollout history deployment <deployment-name> -n dev-wl07

Rollback to the previous working revision:

kubectl rollout undo deployment <deployment-name> -n dev-wl07

Verify pods start successfully:

kubectl get pods -n dev-wl07 -w

Once pods are Running, get the image currently in use:

kubectl get deploy <deployment-name> -n dev-wl07 -o jsonpath='{.spec.template.spec.containers[0].image}'

Save it to the required file:

kubectl get deploy <deployment-name> -n dev-wl07 -o jsonpath='{.spec.template.spec.containers[0].image}' > /root/rolling-back-record.txt

Increase replicas to 5:

kubectl scale deployment <deployment-name> --replicas=5 -n dev-wl07

Final verification:

kubectl get deploy,pods -n dev-wl07
cat /root/rolling-back-record.txt

11. 
The db-deployment-cka05-trb deployment is having 0 out of 1 PODs ready.
Figure out the issues and fix them, but do not remove or rename any DB-related environment variable names in the deployment
Do not modify the contents or keys of any existing Secrets.

1. Check Pod Status
kubectl get pods

Observed:

CreateContainerConfigError
2. Describe the Failing Pod
kubectl describe pod <db-pod-name>

Initial error:

couldn't find key db in Secret default/db-cka05-trb
3. Inspect the Secret
kubectl get secret db-cka05-trb -o yaml

Found:

data:
  database: ...

The deployment referenced key db, but the actual key was database.

4. Edit Deployment
kubectl edit deployment db-deployment-cka05-trb

Changed:

key: db

to:

key: database

while keeping env var name unchanged:

name: DB_DATABASE
5. Check Pods Again
kubectl get pods

Still failing.

6. Describe New Pod
kubectl describe pod <new-db-pod>

Error:

secret "db-user-cka05-trb" not found
7. List Existing Secrets
kubectl get secrets

Found:

db-user-pass-cka05-trb

but NOT:

db-user-cka05-trb
8. Inspect User Secret
kubectl get secret db-user-pass-cka05-trb -o yaml

Found keys:

username:
password:
9. Fix DB_USER Reference

Edited deployment again:

kubectl edit deployment db-deployment-cka05-trb

Changed:

name: db-user-cka05-trb
key: db-user

to:

name: db-user-pass-cka05-trb
key: username
10. Fix DB_PASSWORD Reference

Also changed:

key: db-password

to:

key: password

while keeping env var name unchanged:

name: DB_PASSWORD
. Verify Deployment
kubectl get pods

Result:

db-deployment-cka05-trb-xxxxx   1/1 Running

12. 
Create a new deployment called ocean-tv-wl09 in the default namespace using the image kodekloud/webapp-color:v1.
Use the following specs for the deployment:


1. Replica count should be 3.

2. Set the Max Unavailable to 40% and Max Surge to 55%.

3. Create the deployment and ensure all the pods are ready.

4. After successful deployment, upgrade the deployment image to kodekloud/webapp-color:v2 and inspect the deployment rollout status.

5. Check the rolling history of the deployment, and on the cluster1-controlplane, save the current revision count number to the /opt/revision-count.txt file.

6. Finally, perform a rollback and revert the deployment image to the older version.


sol:

1. Create Deployment
kubectl create deployment ocean-tv-wl09 \
--image=kodekloud/webapp-color:v1 \
--replicas=3
2. Edit Deployment Strategy
kubectl edit deployment ocean-tv-wl09

Under spec, add/change:

strategy:
  type: RollingUpdate
  rollingUpdate:
    maxUnavailable: 40%
    maxSurge: 55%

Save and exit.

3. Verify Deployment
kubectl get deployment ocean-tv-wl09

Expected:

READY   3/3

Check pods:

kubectl get pods
4. Upgrade Image to v2
kubectl set image deployment/<deployment-name> <container-name>=<image>
kubectl set image deployment/ocean-tv-wl09 \
webapp-color=kodekloud/webapp-color:v2
5. Check Rollout Status
kubectl rollout status deployment ocean-tv-wl09

Expected:

successfully rolled out
6. Check Rollout History
kubectl rollout history deployment ocean-tv-wl09

Example:

REVISION  CHANGE-CAUSE
1         <none>
2         <none>
7. Save Revision Number
echo 2 > /opt/revision-count.txt

Verify:

cat /opt/revision-count.txt

Output:

2
8. Roll Back Deployment
kubectl rollout undo deployment ocean-tv-wl09
9. Verify Rollback
kubectl describe deployment ocean-tv-wl09 | grep Image

Expected:

kodekloud/webapp-color:v1

13. 

There is a deployment nginx-deployment-cka04-svcn in cluster3 which is exposed using service nginx-service-cka04-svcn.
Create an ingress resource nginx-ingress-cka04-svcn to load balance the incoming traffic with the following specifications:
ingressClassName: nginx-cka04
pathType: Prefix and path: /
Backend Service Name: nginx-service-cka04-svcn
Backend Service Port: 80
ssl-redirect is set to false
IS the "nginx-ingress-cka04-svcn" ingress resource created?

Is PathType: "Prefix"?

Is Path: "/"?

Is Backend serviceName: "nginx-service-cka04-svcn"?

Is Backend servicePort: "80"?

Is "ssl-redirect" is set to "false"?

Is ingress working?

sol:
1. Create Ingress YAML
vi ingress.yaml

Paste:

apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: nginx-ingress-cka04-svcn
  annotations:
    nginx.ingress.kubernetes.io/ssl-redirect: "false"

spec:
  ingressClassName: nginx-cka04

  rules:
  - http:
      paths:
      - path: /
        pathType: Prefix

        backend:
          service:
            name: nginx-service-cka04-svcn
            port:
              number: 80

Save and exit.

2. Apply the Ingress
kubectl apply -f ingress.yaml

Expected:

ingress.networking.k8s.io/nginx-ingress-cka04-svcn created
3. Verify Ingress Created
kubectl get ingress

Expected:

nginx-ingress-cka04-svcn
4. Check Ingress Details
kubectl describe ingress nginx-ingress-cka04-svcn

14. 

It appears that the black-cka25-trb deployment in cluster1 isn't up to date. While listing the deployments, we are currently seeing 0 under the UP-TO-DATE section for this deployment. Troubleshoot, fix, and make sure that this deployment is up to date.

sol:

1. Describe the deployment
2. kubectl rollout resume deployment black-cka25-trb

15. 







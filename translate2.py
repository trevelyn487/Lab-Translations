# Making sure Kubernetes Engine API and Container Registry API are enabled
gcloud services list

# Placing the zone in an environment variable
export $MY_ZONE=us-central1-a

# Starting a Kubernetes cluster with 2 nodes
gcloud container clusters create zone $MY_ZONE wenfrontend --num-nodes 2

# Checking installed version of Kubernetes
kubectl version

# To view the running nodes
gcloud compute instances list

# Launching a single instance of the nginx container
kubectl create deploy nginx --image=nginx:1.17.10

# To view the pod running the nginx container
kubectl get pods

# Exposing the nginx container to the internet
kubectl expose deployment nginx --port 80 --type LoadBalancer

# To view the new service created
kubectl get services

# Scaling up the number of pods running on the service to 3
kubectl scale deployment nginx --replicas 3

# Confirming that Kubernetes has updated the number of pods
kubectl get pods

# Making sure the external IP address has not changed
kubectl get services


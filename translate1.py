# Creating first VM with name my-vm-1
gcloud compute instances create "my-vm-1" --zone=us-central1-a --machine-type "n1-standard-1" \
--image=debian-9-stretch-v20200910 --image-project=debian-cloud \

# Creating firewall rule to allow http traffic to the VM
gcloud compute --project=PROJECT_ID firewall-rules create "default-allow-http" \
--direction=INGRESS --priority=1000 --network=default --action=ALLOW --rules=tcp:80 \
--source-ranges=0.0.0.0/0 --target-tags=http-server

# Creating second VM with name my-vm-2
gcloud compute instances create "my-vm-2" --zone=us-central1-b --machine-type "n1-standard-1" \
--image-project "debian-cloud" --image "debian-9-stretch-v20190213" --subnet "default" \

# Connecting to second VM via SSH
gcloud compute --project PROJECT_ID --zone us-central1-b my-vm-2

# Pinging the first VM
ping my-vm-1

# Aborting the ping
ctrl+C

# Opening a command prompt on first VM
ssh my-vm-1

# Installing nginx web server on it
sudo apt-get install nginx-light -y

# Using text editor to add a custom message to the web server home page
nano var/www/html/index.nginx-debian.html

# Saving and exiting text editor after adding custom message
ctrl+O, Enter and then ctrl+X

# Confirming the web server is serving the new page
curl http://localhost/

# To confirm that second VM can reach the web server on first VM
exit # This exits first VM and returns to second VM's command line
curl http://my-vm-1/  # Enter this on second VM's command line

# Reaching web server from first VM
# Query to get external IP address for first VM
curl -H "Metadata-Flavor: Google" http://169.254.169.254/computeMetadata/v1/instance/network-interfaces/0/access-configs/0/external-ip && echo
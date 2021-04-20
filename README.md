#### README

#### Prerequisite
- docker installed on ubuntu
- docker-compose installed on ubuntu

### TODO
- add ssh and security steps to production [priority]
- entry data from agrobot previous app [priority]
- explore django bulk data upload package [priority]
- crop issue should also have an image file with it :/

#### First Deploy Workflow
- connect to ec2 instance using ssh
- install docker and docker-compose on ec2 instance (run `deploy-scripts/install-docker-and-docker-compose.sh`)
- install git
- setup ssh for github profile that contains source code
- git clone source code
- update all .env file variables (e.g: ALLOWED_HOSTS should be according to the ec2 instance's public dns)
- make sure you are in master branch
- run `deploy-scripts/first-deploy.sh`
- run `sudo docker ps` to find the container for the django app

#### Update Source Code Workflow
- connect to ec2 instance using ssh
- git pull master 
- if you have new migrations keep the generated migrations in the specific app's migration folder. docker entrypoint script will migrate available migrations before deploy but wont create new migrations.
- run `deploy-update.sh`


#### Miscellaneous
##### Connecting to a shell in your docker container:
- sudo docker ps # find the container_id of your container
- sudo docker exec -it <container_id> sh
##### Run any command in the container context using docker-compose
- docker-compose exec <service_name> <command>
##### Restart Docker daemon
- sudo service docker restart
##### Removing the docker container
- docker-compose down -v
##### check if nginx .conf file is OK
- sudo nginx -t

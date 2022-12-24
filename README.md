################ flaskapp
Pragmatic final project Georgi Ivanov
I am developing a python web application with the flask library with using the best DevOps tools and practices to deploy my app:
1.Create a GitHub repo
2.Generate ssh keys and deploy the public key to your GitHub account.
3.Create the infrastructure via terraform in a folder called infra
4.Terraform should create a VPC, EKS, ec2 instance, security group as well as an ECR.
5.The ec2 instance must install git, Jenkins, Docker, Kubectl and Helm.
6.Make sure the Jenkins user can access all of those tools.
7.Create a folder helm and configure your application to be deployed in a deployment with a service of type LoadBalancer.
8.Create Dockerfile in order to containerise your application.
9.Create a Jenkinsfile that will automate the deployment of your application to Kubernetes.
10.Configure Jenkins to create a multi branch pipeline and connect it to your GitHub repo.
If everything was set up correctly you should be able to see the pipeline trigged.
Once the application is deployed you should be able to access the endpoint http://IP:30000/picture
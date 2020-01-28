# Welcome to Catho Challenge
_Please read these instructions carefully._

## Purpose

**There are 3 challenges in this project:**

#### 1. Development Skills

We have an API Application called **devopsExam** , it based in Python Language and it has 2 main routes _/users_, _/user/\{id\}_. The route _/users_ has 2 methods (_GET_ and _POST)_, the method _GET_ return all users on database (in this application, database is a ElastiCache Redis) and the method _POST_ create a new user. The route _/user/\{id\}_ has only 1 method (_GET_), this method returns a specific user based on _id_.

The main objective in this challenge, is solve a problem in application code (really basic problem).

**OBS: It is not necessary has advanced knowledge in development, our expectations are about your development skills;**

#### 2. Terraform

The main objective here, is create an AWS Environment using Terraform, where the application **devopsExam** must be deployed, ensuring _High Availability_, _Scalability_ and _Resilience_.

The architecture must have the following resources:

- VPC
	- Network: 10.253.0.0/16;
- 2 Private Subnets Multi A-Z (Only LAN Traffic)
	- Networks: 10.253.0.0/24 and 10.253.1.0/24;
- 2 Public Subnets Multi A-Z (Only WAN Traffic)
	- Networks: 10.253.2.0/24 and 10.253.3.0/24;
- SecurityGroup
	- Granting access to the application **(Only HTTP)**;
- ElastiCache Redis Cluster
	- Application's Database;
- Lambda Function
	- To host application **devopsExam**;
- API Gateway
	- Integrated with Lambda function (According routes described on challenge 1).

#### 3. CICD

The main objective here, is create a pipeline (Jenkins _**[Preferred]**_, Code Pipeline or Github Actions) to deploy all AWS Environment (Terraform) and Application **devopsExam**.

## Expectations

Our expectations about all challenges are:

1. Perform the pipeline to create entire AWS environment, including deploy the Application **devopsExam** ;
2. If there isn&#39;t pipeline, the repository must have a **README.md** with the procedure to run terraform and deploy application;
3. We&#39;ll perform a _curl_ in the API Gateway DNS and the returns must be:
	- In Route _/users_ with method _POST_
	```Return 201 HTTP Code and create a user;```

	- In Route _/users_ with method _GET_
	```Return 200 HTTP Code and all users saved in database (Redis);```

	- In Route _/user/{id}_ with method _GET_
	```Return 200 HTTP Code and specific user saved in database (Redis);```

## Submissions

You should send us a git patch file with your solution. To do so follow these steps:

**Clone (do NOT fork) this repository to your machine:**
```$ git clone https://github.com/catho/infra_devops_exam.git```

_Implement your solution_

**Take a look at your changes:**
```$ git status```

**Add some new file/dir:**
```$ git add -N terraform/main.tf```

**Take a new look at your changes and confirm if it's everything ok:**
```$ git status```

**check the diff:**
```$ git diff```

_Make sure that it looks like your solution, otherwise repeat the steps above. If everything looks ok, move to the next step._

**Commit your changes locally:**
```$ git commit -am "My solution"```

**Create a patch file containing your changes:**
```$ git format-patch origin/master --stdout > result.patch```

_Check result.patch, it should look like git diff output. To check the diff after committing, use git diff origin/master HEAD.
If something looks wrong, run git reset origin/master and go to step 2.
If everything looks right Email us the result.patch file._

**Please do not fork this repository and do not publish your solution online!**

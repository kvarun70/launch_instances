# launch instances

## Description: 

Launches AWS EC2 instances in one or more regions

## Command to launch in one region (us-east-1) : 

We need to specify the following values in the parameters separated by ":"

`<region name>:<AMI ID>:<instance type>:<Maximum count of instances>:<Minimum number of instances>`


Eg : `python launch_instances.py --values us-east-1:ami-0b5eea76982371e91:t2.nano:1:1`


us-east-2:ami-0a606d8395a538502:t2.nano:1:1

## Command to launch in more than one region : 

Same as above but separated with a comma ","

Eg : `python launch_instances.py --values us-east-1:ami-0b5eea76982371e91:t2.nano:1:1,us-east-2:ami-0a606d8395a538502:t2.nano:1:1`

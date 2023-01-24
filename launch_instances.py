import argparse
import boto3
parser = argparse.ArgumentParser(description="Passes Region Name, AMI ID, Instance Type, Max Count, Min Count as arguments")
parser.add_argument('--values',help='syntax : python launch_instances.py --values us-east-1:ami-123456abcd:t2.nano:1:1,us-east-2:ami-7894abcd:t2.micro:1:1',required=True)
args = parser.parse_args()

def passed_args(values):
    return values

try:
    split_args = passed_args(args.values).split(',')
    for i in split_args:
        region,ami_id,instance_type,min_count,max_count = i.split(":")
        ec2 = boto3.resource('ec2',region_name=region)
        instance = ec2.create_instances(
            ImageId=ami_id,
            MinCount=int(min_count),
            MaxCount=int(max_count),
            InstanceType=instance_type
        )
        resp_list = instance
        for instance_id in resp_list:
            print(f'Created instance. Instance ID : {instance_id.id} in {region}')
except Exception as e:
    print(f'An error occured {e}')


import boto3
import csv
import json
from pprint import pprint
import datetime
import random


ec2_cli=boto3.client(service_name= "ec2")
s3 =  boto3.resource('s3')
rds = boto3.client('rds')
iam = boto3.client('iam')
cloudwatch = boto3.client('cloudwatch')
ses = boto3.client('ses')
sqs = boto3.client('sqs')
client = boto3.client('ssm')
rds = boto3.client('rds')





       
###################################""""
# List SQS queues
response = sqs.list_queues()


#      ###########################################################""""""
#      #vpc
client = boto3.client('ec2',region_name='us-east-1')
response = client.describe_vpcs(
    Filters=[
        {
            'Name': 'tag:Name',
            'Values': [
                '<Enter you VPC name here>',
            ]
        },
        {
            'Name': 'cidr-block-association.cidr-block',
            'Values': [
                '10.0.0.0/16', #Enter you cidr block here
            ]
        },        
    ]
)
resp = response['Vpcs']
if resp:
    print(resp)
else:
    print('No vpcs found')




collect_all_regions=[]
for each_region in ec2_cli.describe_regions()['Regions']:
    collect_all_regions.append(each_region['RegionName'])
print(collect_all_regions)
fo=open('inven_new.csv','w')
data_obj=csv.writer(fo)


# pour ec2
cnt=1
data_obj.writerow(["########################## ec2 #########################"])
data_obj.writerow(['Sno','Instance ID',"InstanceType","KeyName","Private_ip","Public_IP"])
for each_region in collect_all_regions:
    ec2_re=boto3.resource(service_name='ec2',region_name=each_region)
    for each_ins_in_reg in ec2_re.instances.all():
        data_obj.writerow([cnt,each_ins_in_reg.instance_id,each_ins_in_reg.instance_type,each_ins_in_reg.key_name,each_ins_in_reg.private_ip_address,each_ins_in_reg.public_ip_address])
        cnt+=1

# pour vpc
cnt=1
data_obj.writerow(["########################## ec2 #########################"])
     
# pour s3
cnt=1
data_obj.writerow(["########################## S3 #########################"])
data_obj.writerow(['Sno','Bucket Name'])
for bucket in s3.buckets.all():
    my_bucket = s3.Bucket(bucket.name)
    data_obj.writerow([cnt,my_bucket])
    cnt+=1

# pour sqs
cnt=1
data_obj.writerow(["########################## sqs #########################"])
data_obj.writerow(['Sno',"queueURL"])
for each_region in collect_all_regions:
    sqs=boto3.resource(service_name='sqs',region_name=each_region)
    for sqs_per_region in sqs.queues.all():
        data_obj.writerow([cnt,sqs_per_region])
        cnt+=1

# pour sns
cnt=1
data_obj.writerow(["########################## sns #########################"])
data_obj.writerow(['Sno','Topic'])
for each_region in collect_all_regions:
    sns=boto3.resource(service_name='sns',region_name=each_region)
    for sns_per_region in sns.topics.all():
        data_obj.writerow([cnt,sns_per_region])
        cnt+=1
# fo.close()               

# pour Lambda
cnt=1
data_obj.writerow(["########################## Lambda #########################"])
data_obj.writerow(['Sno','Name'])
for each_region in collect_all_regions:
    lamb = boto3.client('lambda',region_name=each_region)
    for lambda_per_region in lamb.list_functions().values():
        data_obj.writerow([cnt,lambda_per_region])
        cnt+=1

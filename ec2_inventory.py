

import boto3
import csv
import json
from pprint import pprint
import datetime
import random


ec2_cli=boto3.client(service_name= "ec2")
s3 =  boto3.resource('s3')
client = boto3.client('rds')
iam = boto3.client('iam')

## pourS3
for bucket in s3.buckets.all():  
    my_bucket = s3.Bucket(bucket.name)
    for file in my_bucket.objects.all():
     print (f"Bucket:{bucket.name} Key: {file.key}")

## pour ec2
collect_all_regions=[]
for each_region in ec2_cli.describe_regions()['Regions']:
    collect_all_regions.append(each_region['RegionName'])
print(collect_all_regions)
fo=open('ec2_inven_new.csv','w')
data_obj=csv.writer(fo)
data_obj.writerow(['Sno','Instance ID',"InstanceType","KeyName","Private_ip","Public_IP"])

cnt=1
for each_region in collect_all_regions:
    ec2_re=boto3.resource(service_name='ec2',region_name=each_region)
    for each_ins_in_reg in ec2_re.instances.all():
        data_obj.writerow(each_ins_in_reg.public_ip_address)
       
fo.close()               

 
## kinesis

STREAM_NAME = "ExampleInputStream"


def get_data():
    return {
        'EVENT_TIME': datetime.datetime.now().isoformat(),
        'TICKER': random.choice(['AAPL', 'AMZN', 'MSFT', 'INTC', 'TBV']),
        'PRICE': round(random.random() * 100, 2)}


def generate(stream_name, kinesis_client):
    while True:
        data = get_data()
        print(data)
        kinesis_client.put_record(
            StreamName=stream_name,
            Data=json.dumps(data),
            PartitionKey="partitionkey")


if __name__ == '__main__':
    generate(STREAM_NAME, boto3.client('kinesis'))
    
    

## create policy
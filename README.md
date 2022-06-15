# get-aws-inventory
## aws_inventory.py
A simple script that uses uses the Amazon Web Services Boto3 python module to
generate a CSV file of some aws services.

## Prerequisites
This script assumes that you have Python3 and [Boto3](https://boto3.readthedocs.io/en/latest/)
installed as well as the other modules listed at the top of the script.

## Create an AWS Profile
In a text editor, create a new file under .aws/credentials, modify the profile_name, aws_access_key_id and aws_secret_access_key with your own:
```sh
[profile-name]
aws_access_key_id = XXXXXXX
aws_secret_access_key = XXXXXXXXXXXXXXXXX
```
## example eventory "EC2"
- So here I wrote a boto3 python script to generate the ec2 inventory
```sh
cnt=1
data_obj.writerow(['Sno','Instance ID',"InstanceType","KeyName","Private_ip","Public_IP"])
for each_region in collect_all_regions:
    ec2_re=boto3.resource(service_name='ec2',region_name=each_region)
    for each_ins_in_reg in ec2_re.instances.all():
        data_obj.writerow([cnt,each_ins_in_reg.instance_id,each_ins_in_reg.instance_type,each_ins_in_reg.key_name,each_ins_in_reg.private_ip_address,each_ins_in_reg.public_ip_address])
        cnt+=1
```

## Description
The resulting output will look something like [inven.csv](../inven.csv).
- generate a CSV file that records the inventory of AWS resources

```sh
collect_all_regions=[]
for each_region in ec2_cli.describe_regions()['Regions']:
    collect_all_regions.append(each_region['RegionName'])
print(collect_all_regions)
fo=open('inven_new.csv','w')
data_obj=csv.writer(fo)
```
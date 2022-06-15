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


## Description
The resulting output will look something like [inven.csv](../inven.csv).
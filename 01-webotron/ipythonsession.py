# coding: utf-8
import boto3
session = boto3.Session(profile_name='pythonAutomation')
s3 = session.resource('s3')
new_bucket = s3.create_bucket(Bucket='automatingawsmbf-boto3')
for bucket in s3.buckets.all():
print(bucket)
for bucket in s3.buckets.all():print(bucket)
for bucket in s3.buckets.all():
    print(bucket)
    
new_bucket = s3.create_bucket(Bucket='automatingawsmbf-boto3', CreateBucketConfiguration={'LocationConstraint': 'us-east-1'})
test = session.client('ec2')

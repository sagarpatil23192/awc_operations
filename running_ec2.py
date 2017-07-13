#!/usr/bin/env python
__author__ = 'sagarpatil'

import boto3.ec2

def running_instances():

   running_instance_ids = []


   #Populate the list below as per your requirements 
   aws_regions = [
        'us-east-1',
        'us-west-1'
    ]

   for rgn in aws_regions:
       print 'in region : ', rgn

       ec2 = boto3.client('ec2',region_name=rgn)
       response = ec2.describe_instances(
            DryRun=False,
            Filters=[
                {
                    'Name': 'instance-state-name',
                    'Values': ['running']
                },
                {
                    'Name': 'vpc-id',
                    'Values': ['vpc-ID']
                }
            ]
       )

       ## Iterate reservations
       for reservation in response['Reservations']:
            for inst in reservation['Instances']:
                running_instance_ids.append(inst['InstanceId'])

       print "Running instances :  " ,running_instance_ids


if __name__ == "__main__":
      running_instances()


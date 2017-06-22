#!/usr/bin/env python
__author__ = 'sagarpatil'

import boto3.ec2

def stop_instances():

   running_instance_ids = []
   
   #Mention the instance id's which you don't want to stop
   exception_instance_ids = []
   
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
                }
            ]
       )
        
       ## Iterate reservations
       for reservation in response['Reservations']:
            for inst in reservation['Instances']:
                running_instance_ids.append(inst['InstanceId'])
    
       instance_ids_to_be_stopped = list(set(running_instance_ids) - set(exception_instance_ids))
       print "Running instances :  " ,running_instance_ids
       running_instance_ids = []
       if len(instance_ids_to_be_stopped) > 0:
            response = ec2.stop_instances(
                DryRun=False,
                InstanceIds=instance_ids_to_be_stopped,
                Force=True
            )
       

if __name__ == "__main__":
      stop_instances()

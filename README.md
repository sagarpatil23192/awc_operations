# awc_operations

First, install the library required by python:

pip install boto3

Next, set up credentials (in e.g. ~/.aws/credentials):

[default]
aws_access_key_id = YOUR_KEY
aws_secret_access_key = YOUR_SECRET


Then, set up a default region (in e.g. ~/.aws/config):

[default]
region=us-east-1

Then you can make the changes needed in the stop_ec2.py file and run it to stop all the running instances in your AWS account.

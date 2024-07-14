import boto3
import logging
import os

logging.basicConfig(
      level=logging.INFO,
      format='%{asctime}s - %{levelname}s - %{message}s',
      style='{'
)

# ec2_names = ["test-ins"]

def create_ec2():

    ec2_client = boto3.resource(
        'ec2',
        aws_access_key_id = "",
        aws_secret_access_key = "",
        # aws_session_token = "",
        region_name = "us-west-2"
        )
    
    try:
     ec2_response = ec2_client.create_instances(
        MinCount = 1,
        MaxCount = 1,
        ImageId = 'ami-078701cc0905d44e4',
        InstanceType = 't2.nano',
        # KeyName = 'test-key',
        Monitoring = {
            'Enabled': True
        },
        # SubnetId = 'subnet-0f56ea93e0b3bd84f',
        Placement = {
            'AvailabilityZone': 'us-west-2a'
        }
    )
     logging.info(f"EC2 created {ec2_response}")
     
    except:  
        logging.info("No instances created")    

create_ec2()        

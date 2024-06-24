import boto3
import logging
import os

ec2_names = ["test-ins", "dev-instance"]

def create_ec2():

    ec2_client = boto3.client(
        'ec2',
        aws_access_key_id = "",
        aws_secret_access_key = "",
        aws_session_token = "",
        region_name = "us-west-2"
        )
    
    ec2_response = ec2_client.run_instances(
        MinCount = 1,
        MaxCount = 2,
        ImageId = 'ami-6cd6f714',
        InstanceType = 't2.micro',
        KeyName = 'test-key',
        Monitoring = {
            'Enabled': True
        },
        SubnetId = 'subnet-0f56ea93e0b3bd84f',
        Placement = {
            'AvailabilityZone': 'us-west-2a'
        }
    )

    for instance in ec2_response:
        print(f"New instance created: {instance}")

    print(ec2_response)     

create_ec2()        

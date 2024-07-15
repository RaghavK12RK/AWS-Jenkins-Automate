import boto3
from botocore.exceptions import ClientError


def delete_def_vpc():
        
    session = boto3.Session(
               aws_access_key_id = "",
               aws_secret_access_key = ""                               
                                  )
    ec2_client = session.client('ec2')
    regions = [region['RegionName'] for region in ec2_client.describe_regions()['Regions']]

    for region in regions:
        print(f"processing region: {region}")
        ec2 = session.client('ec2',region_name=region)

        try:
         #Describe Def VPC
         response = ec2.describe_vpcs(
            Filters=[
                {
                'Name': 'isDefault',
                'Values': ['true']
                }
            ]
         )
         default_vpcs = response['Vpcs']

         if not default_vpcs:
            print(f"No default vpc found in region {region}")
            continue

        #There shld be one default vpc per region
         default_vpc = default_vpcs[0]
         vpc_id = default_vpc['VpcId']

        #Get subnets
         subnets = ec2.describe_subnets(Filters=[{'Name':'vpc-id', 'Values': [vpc_id]}])['Subnets']
         for subnet in subnets:
            try:
             print(f"Deleting Subnet {subnet['SubnetId']} in VPC {vpc_id} in region {region}")
             ec2.delete_subnet(SubnetId=subnet['SubnetId'])
            except ClientError as e:
               print(f"error in deleting subnet {subnet['SubnetId']} : {e}") 

        #Get security group and delete them
         Sg_groups = ec2.describe_security_groups(Filters=[{'Name':'vpc-id', 'Values': [vpc_id]}])['SecurityGroups']                                  
         for sg in Sg_groups:
             if sg['GroupName'] != 'default':
               try: 
                print(f"Deleting Sg {sg['GroupId']} in VPC {vpc_id} in region {region}")
                ec2.delete_security_group(GroupId=sg['GroupId'])
               except ClientError as e:
                print(f"error in deleting subnet {sg['GroupId']} : {e}")  

        #Get route tables and delete them
         route_tables= ec2.describe_route_tables(Filters=[{'Name':'vpc-id', 'Values': [vpc_id]}])['RouteTables']
         for rt in route_tables:
            if not rt['Associations'][0]['Main']:
               try: 
                print(f"Deleting Route Table {rt['RouteTableId']} in VPC {vpc_id} in region {region}")
                ec2.delete_route_table(RouteTableId=rt['RouteTableId'])
               except ClientError as e:
                print(f"error in deleting route {rt['RouteTableId']} : {e}")  

        #Get internet gateways and delete them
         igws = ec2.describe_internet_gateways(Filters=[{'Name':'attachment.vpc-id', 'Values': [vpc_id]}])['InternetGateways']
         for internet in igws:
           try: 
            print(f"Deleting internet gateway {internet['InternetGatewayId']} in VPC {vpc_id} in region {region}")
            ec2.detach_internet_gateway(InternetGatewayId=internet['InternetGatewayId'], VpcId=vpc_id)
            ec2.delete_internet_gateway(InternetGatewayId=internet['InternetGatewayId'])
           except ClientError as e:
                print(f"error in deleting internet GW {internet['InternetGatewayId']} : {e}")              

        #Finally delete VPC
         try:        
          print(f"Deleting VPC {vpc_id} in region {region}")
          ec2.delete_vpc(VpcId=vpc_id)
         except ClientError as e:
                print(f"error in deleting internet GW {vpc_id} : {e}")

        except ClientError as e:
                print(f"error processing region {region} : {e}") 

    print("Default VPC deleted completed in all regions.")

delete_def_vpc()                    


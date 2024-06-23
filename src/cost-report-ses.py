import boto3
import logging
import os
import datetime
from dateutil.relativedelta import relativedelta

logging.basicConfig(
      level=logging.INFO,
      format='%{asctime}s - %{levelname}s - %{message}s',
      style='{'
)

def cost_spend_ses():

    billing_client = boto3.client(
        #Set up aws cost explorer client
        'ce',
          aws_access_key_id = os.environ.get("AWS_ACCESS_KEY_ID"),
          aws_secret_access_key = os.environ.get("AWS_SECRET_ACCESS_KEY"),
          aws_session_token = os.environ.get("AWS_SESSION_TOKEN")                 
    )

    # adding first day of current month and first day of previous month
     
    today = datetime.date.today()
    first_day_current_month = datetime.datetime(today.year, today.month, 1) #it calculates the first day of PRV month
    first_day_previous_month = first_day_current_month - relativedelta(months=1)
    
    time_period = {
        'Start' : first_day_previous_month.strftime('%Y-%m-%d'),
        'End' : first_day_current_month.strftime('%Y-%m-%d')
    }
    Granularity='MONTHLY'
    Metrics=['BlendedCost']

    # requesting cost explorer API
    billing_response = billing_client.get_cost_and_usage(
        TimePeriod = time_period,
        Granularity = Granularity,
        Metrics = Metrics,
        GroupBy=[
           {
            'Type' : 'DIMENSION',
            'Key' : 'SERVICE' 
        }
    ]
)
    
    # CRAETE A empty list var to store service usage details
    service_usage = []

    # initialize todal cost
    cost = 0.0

    #identify cost by service grouping

    for group in billing_response.get('ResultByTime',[]):
        for service_group in group.get('Groups',[]):
            service_name = service_group.get('Keys',[])[0]
            cost_amount = float(service_group.get('Metrics', {}).get('BlendedCost', {}).get('Amount', 0.0))
            service_usage.append(f"{service_name}: {cost_amount: .2f}")

            # updated total cost
            cost += cost_amount

    service_usage.append("\n")
    service_usage.append(f"**Total cost in: {cost:.2f}**")
    service_usage.append("\n")
    subject = f"AWS Monthly Cost Report - {first_day_previous_month.strftime('%B %Y')}"
    formatted_details = '\n'.join(service_usage)

    # send email using send email function

    email_client = boto3.client(
        'ses',
          aws_access_key_id = os.environ.get("AWS_ACCESS_KEY_ID"),
          aws_secret_access_key = os.environ.get("AWS_SECRET_ACCESS_KEY"),
          aws_session_token = os.environ.get("AWS_SESSION_TOKEN"),
          region_name = "us-west-2"                     
    )

    #Sender and Receiver will be your verfied ses mails
    sender_email = "raghavendra.rao@toyota.com"
    receiver_email = "raghavendra.rao@toyota.com"

    email_response = email_client.send_email(
        Source=sender_email,
        Destination={'ToAddresses': [receiver_email]},
        Message={
            'Subject': {'Data': subject},
            'Body': {'Text': {'Data': formatted_details}}
        }
    )
    
    print("Email sent. Message ID:", email_response['MessageId'])

cost_spend_ses()

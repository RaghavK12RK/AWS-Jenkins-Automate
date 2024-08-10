import boto3
from botocore.exceptions import BotoCoreError
from datetime import datetime


def create_budget():

    budget_client = boto3.client('budgets',
              aws_access_key_id = "",
              aws_secret_access_key = "",
              region_name = "ap-south-1"
    )

    budget_response = budget_client.create_budget(
    AccountId='', #AddaccountID
    Budget={
        'BudgetName': 'RagTestBudget',
        'BudgetLimit': {
            'Amount': '200',
            'Unit': 'USD'
        },
        # 'CostFilters': {
        #     'string': [
        #         'Amazon EC2',
        #     ]
        # },
        # 'CostTypes': {
        #     'IncludeTax': True,
        #     'IncludeSubscription': False,
        #     'UseBlended': False,
        #     'IncludeRefund': True,
        #     'IncludeCredit': True,
        #     'IncludeUpfront': True,
        #     'IncludeRecurring': True,
        #     'IncludeOtherSubscription': True,
        #     'IncludeSupport': True,
        #     'IncludeDiscount': True,
        #     'UseAmortized': False
        # },
        'TimeUnit': 'MONTHLY',
        'BudgetType': 'COST',
        'TimePeriod': {
            'Start': datetime(2024, 8, 1),
            'End': datetime(2024, 9, 1)
        },
        },
    NotificationsWithSubscribers=[
        {
            'Notification': {
                'NotificationType': 'FORECASTED',
                'ComparisonOperator': 'GREATER_THAN',
                'Threshold': 80.0,
                'ThresholdType': 'PERCENTAGE',
                'NotificationState': 'ALARM'
            },
            'Subscribers': [
                {
                    'SubscriptionType': 'EMAIL',
                    'Address': ''
                },
            ]
        },
    ],
)
    print(budget_response)

create_budget()    

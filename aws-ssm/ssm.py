import boto3
import os

ssm_client = boto3.client('ssm', region_name="ap-south-1")

env = os.getenv('ENV', "")
service = os.getenv('SERVICE', "")
key = '/conf/' + service + '/' + env + '/v1'

next_token = None
response = None
for i in range(10):
    if response is None:
        response = ssm_client.get_parameters_by_path(
            Path=key,
            Recursive=True,
            WithDecryption=True,
            MaxResults=10,
            ParameterFilters=[
            ],
        )
    else:
        response = ssm_client.get_parameters_by_path(
            Path=key,
            Recursive=True,
            WithDecryption=True,
            MaxResults=10,
            ParameterFilters=[
            ],
            NextToken=response["NextToken"]
        )

    if response is not None and response['Parameters'] is not None:
        for p in response['Parameters']:
            nameWithKey = p['Name']
            name = nameWithKey.replace(key + "/", '')
            value = p['Value']
            print(name, "=", value)
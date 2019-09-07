import boto3
client = boto3.client('ec2')
response = client.run_instances( ImageId='ami-00c03f7f7f2ec15c3',
                                 InstanceType='t2.micro',
                                 MinCount=1,
                                 MaxCount=1 )

for instance in response['Instances']:
    print(instance['InstanceId'])
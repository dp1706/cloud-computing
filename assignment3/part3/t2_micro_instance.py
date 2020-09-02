import boto3
import time

ec2 = boto3.resource('ec2', region_name='us-east-2')
fh = open('apache_script.sh')
s = ''
for lines in fh:
	s += lines

instances = ec2.create_instances(
    ImageId='ami-07c8bc5c1ce9598c3',
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',
    KeyName='dwarka',
    SecurityGroupIds=['sg-01f0b320d6d41edf3'],
    UserData=s #executed at startup script...
)

micro_ins = instances[0]
micro_ins.wait_until_running()
micro_ins.load()
print(micro_ins.public_dns_name)

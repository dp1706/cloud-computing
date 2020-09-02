import boto3
ec2 = boto3.resource('ec2')


outfile = open('ec2-keypair1.pem','w')


key_pair = ec2.create_key_pair(KeyName='ec2-keypair1')


KeyPairOut = str(key_pair.key_material)
outfile.write(KeyPairOut)

#####

import boto3


s3 = boto3.client('s3')
s3.upload_file('assignment_1.pdf', 'dwarka' ,'assignment_1.pdf') 



#using aws cli command we can upload file 

 # aws s3 cp server_1801061.c s3://dwarka


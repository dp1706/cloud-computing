#####


import boto3

s3 = boto3.client('s3')
s3.download_file('dwarka' , 'assignment_1.pdf','/home/dwarka/Desktop/assignment_1_1.pdf')


#using aws Cli command in terminal we can also download

# aws s3 cp s3://dwarka/assignment_1.pdf /home/dwarka/Videos/test2.pdf

#!/bin/bash
yum -y update
yum -y install httpd
service httpd start
aws configure set aws_access_key_id AKIAIKGFXxxxxxxxxxxx
aws configure set aws_secret_access_key MMbLhCzdmL9Kt6/Edxxxxxxxxxx
aws configure set default.region us-east-2
aws s3 cp s3://dwarka/index.html /var/www/html/
aws s3 cp s3://dwarka/style.css /var/www/html/

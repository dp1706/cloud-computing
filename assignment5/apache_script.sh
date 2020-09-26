#!/bin/bash
yum -y update
yum -y install httpd
service httpd start
aws configure set aws_access_key_id AKIAIKGFXVQQQQSR5YVQ
aws configure set aws_secret_access_key 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
aws configure set default.region us-east-2
aws s3 cp s3://dwarka/index.php /var/www/html/
aws s3 cp s3://dwarka/login.php /var/www/html/
aws s3 cp s3://dwarka/login2.php /var/www/html/
aws s3 cp s3://dwarka/r2.php /var/www/html/
aws s3 cp s3://dwarka/show.php /var/www/html/
aws s3 cp s3://dwarka/feed.php /var/www/html/


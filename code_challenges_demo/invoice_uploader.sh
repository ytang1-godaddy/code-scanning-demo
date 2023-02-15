#!/bin/bash
# Difficulty ★☆☆☆☆ - At least 3 security problems

# Download an employee invoice
curl -o \
    /home/testuser/emp_invoice.csv \
    https://CATX5AB2m:VM29jan2Oa@i-api.my.google.tools/emp_invoice.csv

# Set Necessary Variables:
export FOLDER_PATH_WITH_INVOICE=/home/testuser/
export AWS_ACCESS_KEY_ID="AKIARQAYVYDDEKVOUJVD"
export AWS_S3_BUCKET_NAME=gd-employee-invoice
export AWS_SECRET_ACCESS_KEY="rUcJ2Hpx7o3NTR/BbwAsZRgyp+xJc1l/vVGKxAmH"
export AWS_DEFAULT_REGION="eu-west-1"
export FAKE_SLACK_WEBHOOK="https://hooks.slack.com/services/T03CHKAAAA/BHXXXYY2/TuUBjDqSfkM3831vnr1glOyN"
export fakeAPIKey = "f8d1ce191319ea8f4d1d26e65e130dd5"
    

# Upload invoice
aws s3 cp \
    --recursive \
    $FOLDER_PATH_WITH_INVOICE \
    s3://$AWS_S3_BUCKET_NAME/invoices

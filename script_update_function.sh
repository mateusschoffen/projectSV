#!/usr/bin/env bash

function_name="dev-smartvout"
bucket="dev-smartvout"
aws lambda update-function-code --function-name $function_name --s3-bucket $bucket --s3-key lambda.zip
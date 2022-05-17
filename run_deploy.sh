#!/usr/bin/env bash

root_dir=$PWD
venv_dir="$root_dir/venv/lib/python3.9/site-packages"

# Zip Package

mkdir zip && cp -r app/ zip/app/ \
&& cd $venv_dir && zip -r9 "$root_dir/lambda.zip" . \
&& cd "$root_dir/zip" && zip -g ../lambda.zip -r . \
&& cd "$root_dir" && rm -r zip


# Upload S3

root_dir=$PWD
bucket_name="dev-smartvout"
cd $root_dir
aws s3 cp lambda.zip s3://$bucket_name/lambda.zip

# Update Function Lambda

function_name="dev-smartvout"
bucket="dev-smartvout"
aws lambda update-function-code --function-name $function_name --s3-bucket $bucket --s3-key lambda.zip

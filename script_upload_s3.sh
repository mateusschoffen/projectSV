#!/usr/bin/env bash

root_dir=$PWD
bucket_name="dev-smartvout"
cd $root_dir
aws s3 cp lambda.zip s3://$bucket_name/lambda.zip
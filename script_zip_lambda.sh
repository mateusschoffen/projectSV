#!/usr/bin/env bash

root_dir=$PWD
venv_dir="$root_dir/venv/Lib/site-packages"

mkdir zip && cp -r fornecedorlog/ zip/fornecedorlog/ \
&& cd $venv_dir && zip -r9 "$root_dir/lambda.zip" . \
&& cd "$root_dir/zip" && zip -g ../lambda.zip -r . \
&& cd "$root_dir" && rm -r zip


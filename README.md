# UDM Flood Workflow

[![upload](https://github.com/OpenCLIM/udm-flood-workflow/actions/workflows/upload.yml/badge.svg)](https://github.com/OpenCLIM/udm-flood-workflow/actions/workflows/upload.yml)

## Description
This repository contains a JSON file describing the udm-flood-impacts workflow (`workflow.json`) and a jinja2 template for 
creating parameter sets (`parameter_set.json`). `login.py` contains a function for generating the necessary 
authentication headers based on environment variables `DAFNI_SERVICE_ACCOUNT_USERNAME` and 
`DANFI_SERVICE_ACCOUNT_PASSWORD`. `parameter_sets.py` contains a function for generating parameter sets for each of the 
5 SSPs, based on a given workflow ID, using the jinja2 template. `upload.py` combines these functions to upload the 
workflow and parameter sets onto DAFNI. If any errors occur when uploading parameter sets, the created workflow is 
deleted.

## Usage 
`python upload.py`
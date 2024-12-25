#!/bin/bash

# Set the AWS region (change if needed)
AWS_REGION="ap-south-1"

cd ./terraform 

# Initialize Terraform
terraform init -input=false

# Directly apply Terraform destroy without the plan
terraform destroy -auto-approve

echo "EKS Cluster has been destroyed successfully!"

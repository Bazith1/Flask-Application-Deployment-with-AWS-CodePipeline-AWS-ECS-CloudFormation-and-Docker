#!/bin/bash

# Set the AWS region (change if needed)
AWS_REGION="ap-south-1"

# Initialize Terraform (ensure you are in the correct directory with Terraform files)
echo "Initializing Terraform..."
terraform init -backend-config=backend.tf

# Apply the Terraform destroy plan
echo "Applying Terraform destroy plan..."
terraform plan -destroy -out=tfplan
terraform apply tfplan

# Clean up any Terraform-related resources
echo "Cleaning up..."
terraform destroy -auto-approve

echo "EKS Cluster has been destroyed successfully!"

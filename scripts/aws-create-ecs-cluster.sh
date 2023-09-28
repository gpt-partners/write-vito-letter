#!/bin/bash

# Set the name of the CloudFormation stack
STACK_NAME="ecs-cluster"

# Set the path to the CloudFormation template file
TEMPLATE_FILE="./.aws/cfn_ecs-cluster.yaml"

# Create the CloudFormation stack
aws cloudformation create-stack \
    --stack-name $STACK_NAME \
    --template-body file://$TEMPLATE_FILE
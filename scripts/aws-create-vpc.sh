#!/bin/bash

# Set the name of the CloudFormation stack
STACK_NAME="ecs-vpc"

# Set the path to the CloudFormation template file
TEMPLATE_FILE="./.aws/cfn_vpc.yaml"

# Create the CloudFormation stack
aws cloudformation create-stack \
    --stack-name $STACK_NAME \
    --template-body file://$TEMPLATE_FILE
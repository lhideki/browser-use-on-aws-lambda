#!/usr/bin/env python3
import os
import aws_cdk as cdk

from stacks.cdk_stack import BrowserUseOnAwsLambdaStack


app = cdk.App()
stack = BrowserUseOnAwsLambdaStack(app, "browser-use-on-aws-lambda")

cdk.Tags.of(stack).add("ProjectName", "browser-use-on-aws-lambda")

app.synth()

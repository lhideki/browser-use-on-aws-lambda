import aws_cdk as cdk
from constructs import Construct
from dotenv import load_dotenv
from aws_cdk import aws_lambda as lambda_
import os

load_dotenv()


class BrowserUseOnAwsLambdaStack(cdk.Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        main_function = lambda_.DockerImageFunction(
            self,
            "MainFunction",
            function_name="browser-use-on-aws-lambda-MainFunction",
            code=lambda_.DockerImageCode.from_image_asset(
                "../app/browser_use_on_aws_lambda", file="Dockerfile"
            ),
            timeout=cdk.Duration.seconds(300),
            memory_size=4096,
            environment={
                "OPENAI_API_KEY": os.getenv("OPENAI_API_KEY", ""),
                "POWERTOOLS_SERVICE_NAME": "browser-use-on-aws-lambda",
            },
        )

# ref: https://github.com/browser-use/browser-use
# Define function directory
ARG FUNCTION_DIR="/function"

FROM --platform=linux/x86_64 mcr.microsoft.com/playwright/python:v1.49.1-noble as build-image

# Install aws-lambda-cpp build dependencies
RUN apt-get update && \
    apt-get install -y \
    g++ \
    make \
    cmake \
    unzip \
    libcurl4-openssl-dev

# Include global arg in this stage of the build
ARG FUNCTION_DIR
# Create function directory
RUN mkdir -p ${FUNCTION_DIR}

# Copy function code
COPY . ${FUNCTION_DIR}


RUN pip3 install  \
    --target ${FUNCTION_DIR} \
    awslambdaric
RUN pip install --no-cache-dir -r ${FUNCTION_DIR}/requirements.txt --target ${FUNCTION_DIR}

# Multi-stage build: grab a fresh copy of the base image
FROM --platform=linux/x86_64 mcr.microsoft.com/playwright/python:v1.49.1-noble

# Include global arg in this stage of the build
ARG FUNCTION_DIR
# Set working directory to function root directory
WORKDIR ${FUNCTION_DIR}

# Copy in the build image dependencies
COPY --from=build-image ${FUNCTION_DIR} ${FUNCTION_DIR}

ENTRYPOINT [ "/usr/bin/python", "-m", "awslambdaric" ]
CMD [ "browser_use_on_aws_lambda.functions.main_function.lambda_handler" ]
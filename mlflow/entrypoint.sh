#!/bin/bash

mlflow server --backend-store-uri ${DIALECT}://${USERNAME}:${PASSWORD}@${POSTGRES_HOST}:${POSTGRES_PORT}/${DATABASE} --artifacts-destination s3://${BUCKET} -h ${MLFLOW_HOST} -p ${MLFLOW_PORT}
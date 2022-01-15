#!/bin/sh

cdk deploy "$@"
success=$?
if [ $success != 0 ]; then
    exit $success
fi

./post_deployment.sh "$@"
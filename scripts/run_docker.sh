#!/usr/bin/env bash
set -e
docker build -t devops-python-practice .
docker run --rm -p 5000:5000 devops-python-practice

#!/bin/bash

set -a; source .env; set +a;

doctl serverless deploy .

# doctl serverless functions invoke supplement_scraper/main --no-wait
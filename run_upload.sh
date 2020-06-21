#!/bin/bash
cd $(dirname $0)
source .env/bin/activate
python upload_cycle.py
deactivate

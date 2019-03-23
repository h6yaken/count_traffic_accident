#!/bin/bash
set -e

function main () {
  python3 -m venv venv
  source venv/bin/avtivate

  pip install -r requirements.txt
  
  python3 -m count_traffic_accident

  deactivate
}

main $?
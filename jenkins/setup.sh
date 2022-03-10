#!/bin/bash
#get environment ready
sudo apt update
sudo apt install python3-venv python3 pip python3 -y
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
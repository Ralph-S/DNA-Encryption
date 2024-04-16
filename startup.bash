#!/bin/bash

gnome-terminal -e "bash -c 'cd ~/Desktop/DNA-Encryption; npm run dev'"

gnome-terminal -e "bash -c 'cd ~/Desktop/DNA-Encryption/src; python3 app.py'"

sleep 3

gnome-terminal -e "bash -c 'firefox http://localhost:5173/'"
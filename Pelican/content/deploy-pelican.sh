#!/bin/bash
# This script is forked from the original version in the Notes app.

cd "$(dirname "$0")/Pelican
pelican content -o .. -s pelicanconf.py
cd ..
cp about.html index.html
git checkout main
git add --all
git commit -m “updating pelican outputs"”
git push origin main


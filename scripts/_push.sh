#!/bin/bash

git checkout main
git add .
read -p "Enter commit message: " msg
git commit -m "$msg"
git push origin main

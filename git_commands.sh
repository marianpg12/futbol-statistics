#!/bin/bash

echo "create a new repository on the command line"
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin git@github.com:marianpg12/futbol-statistics.git
git push -u origin main

echo "actualiza el repositorio:"

#git remote add origin git@github.com:marianpg12/futbol-statistics.git
#git branch -M main
#git push -u origin main

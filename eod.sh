#!/bin/bash

#Download latest data
curl -v http://127.0.0.1:8000/loadLatestData

#Git commit and push
git add -A
git commit -a -m "Daily Update"
git push

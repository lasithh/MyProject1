#!/bin/bash
cd /home/computer/project/MyProject1

#Start the service
python manage.py runserver 0.0.0.0:8000 > output

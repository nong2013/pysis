#!/usr/bin/env python

import os
import sys
from os.path import abspath, dirname, join
sys.path.insert(0, abspath(join(dirname(__file__), "../")))
sys.path.insert(0, abspath(join(dirname(__file__), "../../")))
os.environ["DJANGO_SETTINGS_MODULE"] = "settings.settings"

from django.conf import settings
sys.path.insert(0, join(settings.PROJECT_ROOT, "apps"))

import csv
from django.contrib.auth.models import User
from myprofile.models import Profile

# Meaning p
PASSWD = 'sha1$eac2a$36d970cfe5781f78c04e6b15ef7a4dc661d7eb71'

# Output of
# select distinct reg_no, name from Result where reg_no like '08MCA%' order by reg_no;
CSV_FILE = '/tmp/students.csv'
students = csv.reader(open(CSV_FILE), delimiter='|', skipinitialspace=True)

def get_names(name):
    name = name.replace('.', ' ') # Remove Dot
    parts = name.split() # Remove extra whitespace and split into words

    first_name = ''
    last_name = ''
    for part in parts:
        if len(part) == 1:
            last_name = last_name + ' ' + part
        else:
            first_name = first_name + ' ' + part

    first_name = first_name.strip().title()
    last_name = last_name.strip().title()

    return first_name, last_name


for register_number, name in students:
    register_number = register_number.lower()
    first_name, last_name = get_names(name)

    try:
        user = User(username=register_number, password=PASSWD, first_name=first_name, last_name=last_name)
        user.save()

        profile = Profile.objects.get_or_create(user=user)

        print 'Created %s' % register_number

    except Exception as e:
        print 'Error while creating %s : %s' % (register_number, str(e))
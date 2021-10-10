#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime, time

def current():
	now = datetime.datetime.now()
	return int(time.mktime(now.timetuple()))

d = current()
print d

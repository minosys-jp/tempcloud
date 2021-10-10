#!/usr/bin/python
# -*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText

msg = MIMEText("This is a test message by python2")
msg['Subject'] = 'Test by python mailer'
msg['From'] = 'minoru@minosys.com'
msg['To'] = 'minoru@minosys.com'

s = smtplib.SMTP('minosys.sakura.ne.jp', 587);
s.login('minoru@minosys.sakura.ne.jp', 'Minoru21')
s.sendmail('minoru@minosys.com', ['minoru@minosys.com'], msg.as_string())
s.close()

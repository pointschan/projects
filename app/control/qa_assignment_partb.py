__author__ = 'pointschan'

import time
import glob
import re
import os

current_time = time.time() + 60*60*24*30

dirList =  glob.glob('\content\paytek\ejbProperties\cybersource\*.crt')
q = re.compile('^Owner:.*CN=([^\s\,]+)')
p = re.compile('until: (\w+) (\w+) (\d+) (\d+):(\d+):(\d+) \w+ (\d+)')
cert_name = ""
days = {"Mon":0, "Tue":1, "Wed":2, "Thu":3, "Fri":4, "Sat":5, "Sun":6}
months = {"Jan":1, "Feb":2, "Mar":3, "Apr":4,
    "May":5, "Jun":6, "Jul":7, "Aug":8,
    "Sep":9, "Oct":10, "Nov":11, "Dec":12}
for fname in dirList:
    cmd = "keytool -printcert -file " + fname
    for line in os.popen(cmd).readlines():
        line = line.rstrip()
        m = p.search(line)
        if m:
            sue = time.mktime(
                (int(m.group(7)), int(months[m.group(2)]), int(m.group(3)),
                    int(m.group(4)), int(m.group(5)), int(m.group(6)),
                    int(days[m.group(1)]), 0, 0)
            )
            expire_time = (sue - current_time)/60/60/24
            if expire_time < 0:
                print cert_name + " has already expired!"
            elif expire_time < 31:
                print cert_name + " expires in " +str(int(expire_time)) + " days"
        else:
            m = q.search(line)
            if m:
                cert_name = m.group(1)

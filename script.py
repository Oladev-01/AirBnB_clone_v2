#!/usr/bin/python3

from datetime import datetime

time_of_crt = datetime.now()
archive_name = "web_static_{}.tgz".format(time_of_crt.strftime("%Y%m%d%H%M%S"))
with open(archive_name, 'w') as file:
    pass

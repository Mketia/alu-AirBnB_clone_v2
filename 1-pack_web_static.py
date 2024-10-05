#!/usr/bin/python3
# Fabfile to generate a .tgz archive from the contents of web_static.

import os.path
from datetime import datetime
from fabric.api import local


def do_pack():
    """ Create a tar gzipped archive of directory web_static."""
    time = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(time.year,
                                                         time.month,
                                                         time.day,
                                                         time.hour,
                                                         time.minute,
                                                         time.second)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    return file

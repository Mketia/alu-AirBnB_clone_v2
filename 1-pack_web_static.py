#!/usr/bin/python3
"""
Fabric script that generates a tgz archive of the 'web_static' folder.
"""

from datetime import datetime
from fabric.api import local
from os.path import isdir


def do_pack():
    """
    Generates a tgz archive from the contents of the 'web_static' folder.
    Archive will be stored in the 'versions' folder.
    """
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        
        # Ensure 'versions' directory exists
        if not isdir("versions"):
            local("mkdir versions")
        
        file_name = "versions/web_static_{}.tgz".format(date)
        
        # Create the archive
        local("tar -cvzf {} web_static".format(file_name))
        
        return file_name
    except Exception as e:
        print(f"Error occurred: {e}")
        return None
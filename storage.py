#######################################################################################
# Author: Muneeb Mennad                                                              #
# Project Name: Passman                                                             #
# File Name: storage.py                                                            #
# Project Start: 2026-01-24                                                         #
# Github: https://github.com/mnbmnd                                                  #
#######################################################################################

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
import json
from pathlib import Path


def save_master_credentials(username, salt, passwordHash):
    # Create passman dir in user's homme dir
    password_dir = Path.home() / ".passman"
    password_dir.mkdir(exist_ok=True)

    # Structure of the master credentials
    data = {"username": username, "salt": salt, "hash": passwordHash}

    # Writing credentials to master.json
    master_file = password_dir / "master.json"
    with open(master_file, "w") as f:
        json.dump(data, f)

    master_file.chmod(0o600)  # Setting file permissions: only owner can read and write


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# mnbmnd

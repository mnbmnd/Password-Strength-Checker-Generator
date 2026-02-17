#######################################################################################
# Author: Muneeb Mennad                                                              #
# Project Name: Passman                                                             #
# File Name: encrypt.py                                                            #
# Project Start: 2026-01-24                                                         #
# Github: https://github.com/mnbmnd                                                  #
#######################################################################################

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
import hashlib
import os


def generate_salt():
    return os.urandom(32)  # Generate a random 32-byte salt for password hashing


def generate_hash(password, salt):
    # Hash using PBKDF2 with SHA-256, 100k iterations slows brute-force attacks
    return hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 100000).hex()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# mnbmnd

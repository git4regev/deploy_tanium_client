# add_known_hosts.sh
# Created by Yaron Regev, yaron.regev@tanium.com
#
# This Python script takes the first column (space delimited) from each line of the
# file ansible_hosts, and adds their SSH public keys to the known_hosts file so that
# Ansible can establish an SSH connection to those hosts. This script ignore the hosts
# under the [windows_endpoints] section

#!/usr/bin/env python3
import argparse
import paramiko
import os.path
import csv

ansible_file = 'ansible_hosts'
known_hosts = os.path.expanduser('~') + '/.ssh/known_hosts'
ignore_line = False

# Create known_hosts file if one does not already exists
if not os.path.isfile(known_hosts):
    open(known_hosts, 'w+').close()

# Adding the fingerprint from a remote serve to a local machine
# This is a Python implementation of ssh-keyscan utility. Code taken from https://gist.github.com/Pristavkin/e3d6b909d0745656064c7525942ca7e3
with open(ansible_file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=' ')
    for row in csv_reader:
        try:
            if len(row)>0:
                host = row[0]
                if host[0]!='[' and host[0]!='#' and ignore_line!=True:
                    address = host+':22'
                    transport = paramiko.Transport(host,'22')
                    transport.connect()
                    key = transport.get_remote_server_key()
                    transport.close()
                    hostfile = paramiko.HostKeys(filename=known_hosts)
                    hostfile.add(hostname = host, key=key, keytype=key.get_name())
                    hostfile.save(filename=known_hosts)
                elif host[0]=='[':
                    if host=='[windows_endpoints]':
                        ignore_line = True
                    else:
                        ignore_line = False
        except:
            print ('service not known for host '+address)

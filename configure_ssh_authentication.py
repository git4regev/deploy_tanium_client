# add_known_hosts.sh
# Created by Yaron Regev, yaron.regev@tanium.com
#
# This Python script takes the first column (space delimited) from each line of the
# file ansible_hosts, and adds their SSH public keys to the known_hosts file so that
# Ansible can establish an SSH connection to those hosts. This script ignore the hosts
# under the [windows_endpoints] section
# This is Python file used code taken from following sources:
#    https://gist.github.com/Pristavkin/e3d6b909d0745656064c7525942ca7e3
#    https://gist.github.com/batok/2352501
#    https://29a.ch/2010/9/8/deploy-ssh-public-key-multiple-servers-python-paramiko

#!/usr/bin/env python3
import argparse
import paramiko
import os.path
import os
import csv

ansible_file = 'ansible_hosts'
known_hosts = os.path.expanduser('~') + '/.ssh/known_hosts'
ignore_line = False
hosts_keys_folder = 'hosts_authentication'

ansible_key = open(os.path.expanduser('~/.ssh/id_rsa.pub')).read()

# Create known_hosts file if one does not already exists
if not os.path.isfile(known_hosts):
    open(known_hosts, 'w+').close()

with open(ansible_file) as csv_file:
    print ("Reading content of {}...".format(ansible_file))
    csv_reader = csv.reader(csv_file, delimiter=' ')
    for row in csv_reader:
        try:
            if len(row)>0:
                host = row[0]
                if host[0]!='[' and host[0]!='#' and ignore_line!=True:
                    # Find username for host from ansible hosts file
                    host_username = ""
                    for item in row:
                        if "ansible_user" in item:
                            host_username = (item.split("="))[1]
                    # Adding the fingerprint from a remote server to a local machine
                    print ("Adding fingerpring for host {} to Ansible host...".format(host))
                    address = host+':22'
                    transport = paramiko.Transport(host,'22')
                    transport.connect()
                    key = transport.get_remote_server_key()
                    transport.close()
                    hostfile = paramiko.HostKeys(filename=known_hosts)
                    hostfile.add(hostname = host, key=key, keytype=key.get_name())
                    hostfile.save(filename=known_hosts)
                    # Add public key of local host to remote server
                    if (host_username != ""):
                        print ("Adding Ansible public key to remote host {}...".format(host))
                        remote_server_key_file = os.path.dirname(os.path.realpath(__file__)) + "/" + hosts_keys_folder + "/" + host + ".pem"
                        os.chmod(remote_server_key_file, 0o600)
                        remote_server_key = paramiko.RSAKey.from_private_key_file(remote_server_key_file)
                        client = paramiko.SSHClient()
                        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                        #client.connect(server, username=username, password=password)
                        client.connect( hostname = host, username = host_username, pkey = remote_server_key )
                        client.exec_command('echo "%s" > ~/.ssh/authorized_keys' % ansible_key)
                        client.close()
                elif host[0]=='[':
                    if host=='[windows_endpoints]':
                        ignore_line = True
                    else:
                        ignore_line = False
        except:
            print ('service not known for host '+address)

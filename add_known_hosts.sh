# add_known_hosts.sh
# Created by Yaron Regev, yaron.regev@tanium.com
#
# This shell script takes the first column (tab delimited) from each line of the
# file ansible_hosts, and adds their SSH public keys to the known_hosts file so that
# Ansible can establish an SSH connection to those hosts
while IFS=$'\t' read -r -a tmp ; do
ssh-keyscan "${tmp[0]}" >> ~/.ssh/known_hosts
done < ansible_hosts

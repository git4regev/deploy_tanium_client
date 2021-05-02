# parse_discover_report.py
# Created by Yaron Regev, yaron.regev@tanium.com
#
# This Python script converts a CSV report generated by Tanium Discover module
# into an Ansible hosts file that can then be used with the deploy-tanium-client
# Ansible playbook

import csv

report_file = 'Discovered_Unmanaged_Endpoints.csv'
output_file = 'ansible_hosts'

linux_endpoints = []
windows_endpoints = []
mac_endpoints = []
linux_mac_endpoints = []

with open(report_file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            try:
                IpAddress_index = row.index('IpAddress')
                HostName_index = row.index('HostName')
                Os_index = row.index('Os')
            except:
                print("Either IpAddress, HostName, or Os fields are missing in the report.")
                exit()
            line_count += 1
        else:
            if row[Os_index] == 'Linux':
                if row[HostName_index] and (row[HostName_index] not in linux_endpoints):
                    linux_endpoints.append(row[HostName_index])
                elif row[IpAddress_index] and (row[IpAddress_index] not in linux_endpoints):
                    linux_endpoints.append(row[IpAddress_index])
            elif row[Os_index] == 'Windows':
                if row[HostName_index] and (row[HostName_index] not in windows_endpoints):
                    windows_endpoints.append(row[HostName_index])
                elif row[IpAddress_index] and (row[IpAddress_index] not in windows_endpoints):
                    windows_endpoints.append(row[IpAddress_index])
            elif row[Os_index] == 'Mac':
                if row[HostName_index] and (row[HostName_index] not in mac_endpoints):
                    mac_endpoints.append(row[HostName_index])
                elif row[IpAddress_index] and (row[IpAddress_index] not in mac_endpoints):
                    mac_endpoints.append(row[IpAddress_index])
            elif row[Os_index] == 'Linux/Mac':
                if row[HostName_index] and (row[HostName_index] not in linux_mac_endpoints):
                    linux_mac_endpoints.append(row[HostName_index])
                elif row[IpAddress_index] and (row[IpAddress_index] not in linux_mac_endpoints):
                    linux_mac_endpoints.append(row[IpAddress_index])
            line_count += 1

output = open(output_file, "w")
output.write("[linux_endpoints]\n")
for item in linux_endpoints:
    output.write(item + '     ansible_connection=ssh     ansible_user=root\n')
output.write('\n')
output.write("[windows_endpoints]\n")
for item in windows_endpoints:
    output.write(item + '     ansible_connection=winrm     ansible_winrm_server_cert_validation=ignore     ansible_port=5986     ansible_user=Administrator\n')
output.write('\n')
output.write("[mac_endpoints]\n")
for item in mac_endpoints:
    output.write(item + '     ansible_connection=ssh     ansible_user=root\n')
output.write('\n')
output.write("[linux/mac_endpoints]\n")
for item in linux_mac_endpoints:
    output.write(item + '     ansible_connection=ssh     ansible_user=root\n')
output.write('\n')

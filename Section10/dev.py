#!/usr/bin/python

import pprint

file = open('devices', 'r')
dev_list = []
dev = []
knownip = set()

for line in file:
    dev = line.split(',')
    dev_list.append(dev)

file.close()

print('Name	OS Type		IP Address	Software   ')
print('------	---------	------------	-----------')

for item in dev_list:
    print('{0:<7} {1:<15} {2:<15} {3:<20}'.format(item[0],item[1],item[2], item[3]),end='')
    ip = item[2].split(':')[1]
    if ip in knownip:
        print('\t *Duplicate IP*')
        continue
    knownip.add(ip)
    print()
print('\n\n')

while True:
    try:
        ip_address = input('Enter device IP address to find (Ctrl-C to exit):')        
        for item in dev_list:
            ip = item[2][5:]
            if ip == ip_address:
                print('Matched device!\n')
                print('Name     OS Type         IP Address      Software   ')
                print('------   ---------       ------------    -----------')
                print('{0:<7} {1:<15} {2:<15} {3:<20}\n'.format(item[0],item[1],item[2], item[3]))
    except KeyboardInterrupt:
        break

print('\n')
print('Device search terminated.\n')


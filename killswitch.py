#!/usr/bin/env python3

# # imports
import subprocess
import os

# # functions
# function for filtering out the network name
def filter_networks(grep):
    grep_list = grep.split('\n')
    out = []
    for s in grep_list:
        if len(s) > 0:
            out.append(s.split()[0])

    return out


# function for getting command output as string (and waiting for the command to finish)
def command_wait(command):
    child = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    child.wait()
    output = child.communicate()[0]
    return output.decode()


# # variables
on = ('sudo ufw --force reset',
      'sudo ufw default deny incoming',
      'sudo ufw default deny outgoing',
      'sudo ufw allow out on #interface from any to any',
      'sudo ufw allow in on #interface from any to any',
      'sudo ufw allow out #port/udp',
      'sudo ufw enable',
      'sudo ufw status')

off = ('sudo ufw --force reset',
       'sudo ufw default deny incoming',
       'sudo ufw default allow outgoing',
       'sudo ufw enable',
       'sudo ufw status')

interface = 'tun0'
port = '1194'

# # main script
os.system('clear') # clear screen

print('- kill switch -\n') # print title
command_wait('sudo -v') # authorize

# # main loop
while True:
    os.system('clear') # clear screen

    print('select firewall for [v]pn or [n]ormal operation or [q]uit.') # print options
    in_string = input('> ')

    # options
    if in_string == 'v' or in_string == 'V': # vpn
        for c in on:
            s = c.replace('#interface', interface)
            s = s.replace('#port', port)

            print(command_wait(s))
    elif in_string == 'n' or in_string == 'N': # normal
        for c in off:
            print(command_wait(c))
    elif in_string == 'q' or in_string == 'Q': # quit
        break
    else:
        print('wrong input.') # other

    input('\npress [enter] to continue.') # wait for enter



# 'nmcli con show | grep vpn'
# 'nmcli con show --active | grep vpn'

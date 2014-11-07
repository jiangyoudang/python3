#! /usr/bin/python3
import pexpect, sys, json, time

#global constants
SSH_NEWKEY = '(yes/no)?'
COMMAND_PROMPT = r'[#$>]'
PASSWORD_PROMPT = 'assword: '
EOF_error = 'ERROR:  Unexpected exit! '
timeout_error = 'ERROR: Time out! '

def main():
    global COMMAND_PROMPT, SSH_NEWKEY

    username = 'ray'
    password = '5jWUDFn7rGEF'
    en_password = '+6.H>x>!pZy='

    #data_json = sys.argv[1]
    # device = sys.argv[2]
    device = '10.255.253.93'
    data_json = '{"name":"BAS-1070J-08-C3550-C.SJC","selectedGroupIp":"198.200.48.0","groupIpmask":"24",' \
                '"interfaceName":"f0\/26","type":"C3550",' \
                '"gatewayArray":[{"ip":"192.74.228.182","mask":"255.255.255.248"},' \
                '{"ip":"198.200.48.254","mask":"255.255.255.0"},{"ip":"199.188.177.166","mask":"255.255.255.248"}]}'


    data = json.loads(data_json)
    print(data)

    type = data['type']
    interfaceName = data['interfaceName']
    gatewayArray = data['gatewayArray']
    ips = []
    masks = []
    for ip_mask in gatewayArray:
        ips.append(ip_mask['ip'])
        masks.append(ip_mask['mask'])

    groupIp = None
    groupMask = None
    if type != 'NonGroup':
        groupIp = data['selectedGroupIp']
        groupMask = data['groupIpmask']



    child = pexpect.spawnu('ssh -l {} {}'.format(username, device))
    child.logfile_read = sys.stdout

    i = child.expect_exact([SSH_NEWKEY, PASSWORD_PROMPT, pexpect.EOF, pexpect.TIMEOUT])
    if i==0:
        child.sendline('yes')
        child.expect_exact(PASSWORD_PROMPT)
    if i==2:
        print(EOF_error)
    if i==3:
        print(timeout_error)
        print(child.before, child.after)
        print(str(child))
        sys.exit(1)
    if i==1:
        child.sendline(password)
        i = child.expect([r'\>',r'#'])
        if i==0:
            child.sendline('enable')
            child.expect_exact(PASSWORD_PROMPT)
            child.sendline(en_password)
            child.expect(r'#')

    if type=='NonGroup':
        child.sendline('conf t')
        child.expect_exact('(conf)#')
        child.sendline('int {}'.format(interfaceName))
        child.expect_exact(')#')
        child.sendline('ip add {} {}'.format(ips[0], masks[0]))
        child.expect_exact(')#')
        for i in range(1, len(ips)):
            child.sendline('ip add {ip} {mask} se'.format(ip=ips[i], mask=masks[i]))
            child.expect_exact(')#')
        child.sendline('end')
        child.expect_exact('#')
        child.sendline('wr')
        i = child.expect_exact(['#', pexpect.TIMEOUT])
        if i==1:
            print(timeout_error)
            print(child.before, child.after)
            print(str(child))
            sys.exit(1)
        print('\nconfigration start\n')
        child.sendline('show run int {}'.format(interfaceName))
        child.expect_exact('#')
        child.sendline('!')
        child.expect_exact('#')
        print('\nconfigration end\n')
        child.sendline('exit')
        child.expect(pexpect.EOF)



    elif type=='S50N':
        child.sendline('conf t')
        child.expect_exact('(conf)#')
        child.sendline('ip pre c2o')
        child.expect_exact('prefixl)#')
        child.sendline('permit {}/{}'.format(groupIp, groupMask))
        child.expect_exact('prefixl)#')
        child.sendline('exit')
        child.expect_exact('conf)#')
        child.sendline('int {}'.format(interfaceName))
        child.expect_exact(')#')
        child.sendline('ip add {} {}'.format(ips[0], masks[0]))
        child.expect_exact(')#')
        child.sendline('ip add {ip} {mask} se'.format(ip=ips[1], mask=masks[1]))
        child.expect_exact(')#')
        child.sendline('end')
        child.expect_exact('#')
        child.sendline('wr')
        i = child.expect_exact(['#', pexpect.TIMEOUT])
        if i==1:
            print(timeout_error)
            print(child.before, child.after)
            print(str(child))
            sys.exit(1)
        print('\nconfigration start\n')
        child.sendline('show run int {}'.format(interfaceName))
        child.expect_exact('#')
        child.sendline('!')
        child.expect_exact('#')
        print('\nconfigration end\n')
        child.sendline('exit')
        child.expect(pexpect.EOF)


    elif type=='C3550':
        child.sendline('conf t')
        child.expect_exact('(conf)#')
        child.sendline('ip pre c2o permit {}/{}'.format(groupIp, groupMask))
        child.expect_exact('config)#')
        child.sendline('int {}'.format(interfaceName))
        child.expect_exact(')#')
        child.sendline('ip add {} {}'.format(ips[0], masks[0]))
        child.expect_exact(')#')
        child.sendline('ip add {ip} {mask} se'.format(ip=ips[1], mask=masks[1]))
        child.expect_exact(')#')
        child.sendline('end')
        child.expect_exact('#')
        child.sendline('wr')
        i = child.expect_exact(['#', pexpect.TIMEOUT])
        if i==1:
            print(timeout_error)
            print(child.before, child.after)
            print(str(child))
            sys.exit(1)
        print('\nconfigration start\n')
        child.sendline('show run int {}'.format(interfaceName))
        child.expect_exact('#')
        # time.sleep(10)
        child.sendline('!')
        child.expect_exact('#')
        print('\nconfigration end\n')
        child.sendline('exit')
        child.expect(pexpect.EOF)

if __name__ == '__main__':
    main()
#
#     int g0/8
# ip add 199.188.104.118  255.255.255.248
# end
# wr
# !
ip = '192.168.3.1'
iplist = ip.split('.')

ip_template = '''
{0:<8} {1:<8} {2:<8} {3:<8}
{0:08b} {1:08b} {2:08b} {3:08b}
'''
print(ip_template.format(int(iplist[0], 10), int(iplist[1], 10), int(iplist[2], 10), int(iplist[3], 10)))

fullipaddr = input("Enter IP/Short Mask: ")
fulliplist = fullipaddr.split('/')
iplist = fulliplist[0].split('.')
mask = int(fulliplist[1])
zeromask = 32-mask 
a = str('1'*mask)+str('0'*zeromask)
#a = '11111111111111111111111100000000' 
#print(a)
oct1 = a[0:8]
oct2 = a[8:16]
oct3 = a[16:24]
oct4 = a[24:32]

#make following convertion before  proceed with bitwise operations:
#int_a = int(bin(int(iplist[0])), 2)  #str->int(10)->str(bin)->int(bin)

ip_oct1 = int(bin(int(iplist[0])), 2) 
ip_oct2 = int(bin(int(iplist[1])), 2) 
ip_oct3 = int(bin(int(iplist[2])), 2) 
ip_oct4 = int(bin(int(iplist[3])), 2) 

net_ip1 =  ip_oct1&int(oct1, 2)
net_ip2 =  ip_oct2&int(oct2, 2)
net_ip3 =  ip_oct3&int(oct3, 2)
net_ip4 =  ip_oct4&int(oct4, 2)


print(f"{net_ip1} {net_ip2} {net_ip3} {net_ip4}")

#print(f"{oct1} {oct2} {oct3} {oct4}")
#print(oct4)

ip_template = '''
{0:<8} {1:<8} {2:<8} {3:<8}
{0:08b} {1:08b} {2:08b} {3:08b}
'''
print("Netwotk IP")
print(ip_template.format(net_ip1, net_ip2, net_ip3, net_ip4))

print("Ip Address: ")
print(ip_template.format(int(iplist[0], 10), int(iplist[1], 10), int(iplist[2], 10), int(iplist[3], 10)))

print("Mask: ")
print("/"+fulliplist[1])
print(ip_template.format(int(oct1, 2), int(oct2, 2), int(oct3, 2), int(oct4, 2)))


#print(ipaddr)

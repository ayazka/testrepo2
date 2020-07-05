mac = 'AAAA:BBBB:CCCC'
mac = mac.replace(':', '')  #stroka polnaya bez :
#bbb = "101010101010101010111011101110111100110011001100"
#print(len(bbb))
#mac_dec = int(mac, 16)
#maclist = list(mac)
#template = "{:08b}"
#print(template.format())
#print(mac)
converted_mac = bin(int(mac, 16))
print(converted_mac[2:])
#print("{:08b}".format(mac))

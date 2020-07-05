mac = ['aabb:cc80:7000', 'aabb:dd80:7340', 'aabb:ee80:7000', 'aabb:ff80:7000']
mac_cisco = []
for cur_mac in mac:
	mac_cisco.append(cur_mac.replace(':', '.'))
print(mac_cisco)



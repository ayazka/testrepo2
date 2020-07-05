ip_addr = input("Please enter an IP address:")
ip_addr_list = ip_addr.split('.')
fbyte = int(ip_addr_list[0], 10)
if(fbyte>=1 and fbyte<=223):
	print("Unicast Address")
elif(fbyte>=224 and fbyte<=239):
	print("Multicast")
elif(ip_addr == "255.255.255.255"):
	print("Local Broadcast")
elif(ip_addr == "0.0.0.0"):
	print("Unassigned")
else:
	print("Unused")

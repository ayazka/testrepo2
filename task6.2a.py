ip_addr_list_int = []

ipcorrect = False

while not ipcorrect:
	ip_addr = input("Please enter an IP address:")
	ip_addr_list = ip_addr.split('.')

	if(len(ip_addr_list)==4):
		for octet in ip_addr_list:
			if(octet.isnumeric()):
				a = int(octet, 10)
				if(a >=0 and a <= 255):
					ip_addr_list_int.append(int(octet, 10))
					ipcorrect = True
				else:
					print("IP address incorrect!")
					ipcorrect = False
					break
			else:
				print("IP must consist of only from numbers!")
				ipcorrect = False
				break

	else:
		print("IP length does not match!")

else:
	print("IP is correct!")
	#ip_addr_list = ip_addr.split('.')
	fbyte = ip_addr_list_int[0]
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

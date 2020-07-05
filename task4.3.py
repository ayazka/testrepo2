config="switchport allowed trunk vlan 1,3,10,20,30,330"
conflist = config.split(" ")
print(conflist)
lastlist = conflist[-1].split(",")
print(lastlist)

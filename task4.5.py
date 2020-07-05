command1 = 'switchport trunk allowed vlan 1,2,3,5,8'
command2 = 'switchport trunk allowed vlan 1,3,8,9'

comlis1 =  command1.split(" ")
vlanlist1 = comlis1[-1].split(",")
comlis2 =  command2.split(" ")
vlanlist2 = comlis2[-1].split(",")
vlanset1 = set(vlanlist1)
vlanset2 = set(vlanlist2)

finishlist1 = sorted(list(vlanset1.intersection(vlanset2)))
print(finishlist1)
#print(vlanset1)
#print("\n")
#print(vlanset2)




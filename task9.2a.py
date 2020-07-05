trunk_mode_template = [
    'switchport mode trunk', 'switchport trunk native vlan 999',
    'switchport trunk allowed vlan'
]

trunk_config = {
    'FastEthernet0/1': [10, 20, 30],
    'FastEthernet0/2': [11, 30],
    'FastEthernet0/4': [17]
}

def generate_trunk_config(intf_vlan_mapping, trunk_template):
	finaldict = {}
	for key in intf_vlan_mapping:
		k = (f"Interface {key}")
		templist=[]
		for templ in trunk_template:
			if templ.endswith("allowed vlan"):
				templist.append(f"{templ} {str(intf_vlan_mapping[key]).strip('[]')}")
			else:
				templist.append(f"{templ}")
		finaldict[k] = templist
	return finaldict

print(generate_trunk_config(trunk_config, trunk_mode_template))







generate_trunk_config(trunk_config, trunk_mode_template)

access_mode_template = [
    'switchport mode access', 'switchport access vlan',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

access_config = {
    'FastEthernet0/12': 10,
    'FastEthernet0/14': 11,
    'FastEthernet0/16': 17
}

def generate_access_config(intf_vlan_mapping, access_template):
	allportslist = []
	for key in intf_vlan_mapping:
		allportslist.append(f"interface {key}")
		for temp_k in access_template:
			if temp_k.endswith('access vlan'):
				allportslist.append(f"{temp_k} {intf_vlan_mapping[key]}")
			else:
				allportslist.append(temp_k)
	return allportslist

print(generate_access_config(access_config, access_mode_template))

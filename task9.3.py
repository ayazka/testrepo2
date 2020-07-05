'''trunk_mode_template = [
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
'''
#####################################

conf_name = "config_sw1.txt"

def get_int_vlan_map(filename):
	f = open(filename, 'r')
	file_content_list = f.read().rstrip().split('!')
	access_dict = {}
	trunk_dict = {}
	for line in file_content_list:
		if "interface FastEthernet" in line:
			interface_temp_list = line.split('\n')
			for line_int in interface_temp_list:
				if "interface FastEthernet" in line_int:
					int_name = line_int.split(' ')[1]
				elif "switchport access vlan" in line_int:
					vlan_name = int(line_int.split(' ')[4])
					access_dict[int_name] = vlan_name
				elif "switchport trunk allowed vlan" in line_int:
					vlan_list_str = line_int.split(' ')[5]
					vlan_list = vlan_list_str.split(',')
					trunk_dict[int_name] = vlan_list
	finale_tuple = (access_dict, trunk_dict)
	return finale_tuple

print(get_int_vlan_map(conf_name))

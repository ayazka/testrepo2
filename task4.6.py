ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
listofstr = ospf_route.split()
iptemplate = '''
Protocol:    {}
Prefix:      {}
'''


print(iptemplate.format('OSPF', listofstr[1]))

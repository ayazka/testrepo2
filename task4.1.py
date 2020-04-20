nat = "ip nat inside source list ACL interface FastEthernet0/0 overload"
print(nat)
nat = nat.replace("Fast", "Gigabit")
print(nat)

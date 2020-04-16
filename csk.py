
dict_interfaces = {}
Port = [1,2,3,4,]
Name = [1,2,3,4,5]
Status = [up,up, up ,up,down,down]
Duplex = [auto,auto,half,half,auto]
Speed = [100,10,100,100,10,10]
Type = [basetx,baseTX,basesfp,basesfp]


dict_interfaces[Port] = {"Name": Name, "Status": Status, "Vlan": Vlan, "Duplex": Duplex, "Speed": Speed, "Type": Type}

print(dict_interfaces)

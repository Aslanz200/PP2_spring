import json

with open("/Users/azenilmes/Desktop/git/lab4/sample-data.json" , "r") as f:
    data = json.load(f)
    print("Interface status")
    print("=" * 84)
    print("DN" , " "*49 , "Description" , " "*11 , "Speed" , " "*2 , "MTU")
    print("-"*50 , " " , "-"*20 , "  " , "-"*6  , " " , "-"*6)
    for name in data["imdata"]:
        dn = name['l1PhysIf']['attributes']['dn']
        description = name['l1PhysIf']['attributes']["descr"]
        speed = name['l1PhysIf']['attributes']["speed"]
        mtu = name['l1PhysIf']['attributes']["mtu"]
        print(dn , ' '*15 , description , ' '*15 , speed , ' '*2 , mtu)

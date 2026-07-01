#lab3
data3 = [
    "arun-blr-10,40,30",
    "ravi-mum-40,50,60",
    "hari-chn-70,80,90",
    "john-del-10,50,40"
]

n= input("Student name: ")

found= False

for i in data3:
    det= i.split("-")
    
    if det[0]== n:
        found= True
        cty= det[1]
        m= det[2].split(",")
        tot= int(m[0])+int(m[1])+int(m[2])
        
        print("Found")
        print("City= ", cty)
        print("Total= ", tot)
        break

if found== False:
    print("Not found")
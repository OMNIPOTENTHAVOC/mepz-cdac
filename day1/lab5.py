#lab5
data = {
    "north": "10,20,30,40",
    "south": "50,60,70,80",
    "west": "90,100,110,120",
    "east": "130,140,150,160"
}

z=input("Enter zone: ").lower()

if z in data:
    print("found")
    sales=list(map(int, data[z].split(",")))
    print("sales =", sales)
else:
    print("Zone not found")
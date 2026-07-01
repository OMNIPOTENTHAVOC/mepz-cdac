#lab1.py

data1=[
       "arun-blr-10,40,3",
       "ravi-mum-40,50,60",
       "hari-chn-70,80,90",
       "john-del-10,50,40"
      ]

data = [i.replace(",", "-") for i in data1]
print(data, "\n")
for k in data:
    n, c, *m= k.split("-")
    m= list(map(int, m))
    print(m, "\n")

    print(f"Row sum= {sum(m)}\n")
    print(f"Row max= {max(m)}\n")
    print(f"Col sum= {sum(m[0])}")
    print(f"Col max= {max(m[0])}")
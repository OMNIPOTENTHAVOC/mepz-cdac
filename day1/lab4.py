data4 = ["arun=60", "sunil=80", "ravi=75", "manoj=88", "elan=70", "hari=5"]

srt= sorted(data4, v=lambda x: int(x.split("=")[1]))

for i in srt:
    n= i.split("=")[0]
    m= int(i.split("=")[1])
    print(f"{n}:{m}")
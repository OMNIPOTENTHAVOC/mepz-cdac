#lab2
data2 = [
    "arun-blr-10,40,30",
    "ravi-mum-40,50,60",
    "hari-chn-70,80,90",
    "john-del-10,50,40"
]

all_marks = []

print("Row 2nd Max = ", end=" ")

for record in data2:
    name, city, marks = record.split("-")
    marks = list(map(int, marks.split(",")))
    all_marks.append(marks)

    marks.sort(reverse=True)
    print(marks[1], end=" ")

print()

print("Col 2nd Max = ", end=" ")

for col in range(3):
    temp = []
    for row in range(len(all_marks)):
        temp.append(all_marks[row][col])

    temp.sort(reverse=True)
    print(temp[1], end=" ")
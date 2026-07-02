from Person import Person
p1 = Person(name= 'rahul', age= 18)
p2 = Person(name= "ravi", age= 20)
p3 = Person(name="ronit", age= 19)
p4 = Person(name="rohit", age= 21)
p5 = Person(name="raunak", age= 23)

arr = [p1,p2,p3,p4,p5]

for elem in arr:
    arr.sort(key=lambda x: x.age)
    elem.show()
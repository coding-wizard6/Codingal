class birds:
    species="bird"

    def __init__(self,name,age):
        self.name=name
        self.age=age

p=birds("Parrot",10)
q=birds("Sparrow",7)

print("Parrot is a ",p.species)
print("Sparrow is a ",p.species)

print(f"{p.name} is a {p.age} year old {p.species}")
print(f"{q.name} is a {q.age} year old {q.species}")

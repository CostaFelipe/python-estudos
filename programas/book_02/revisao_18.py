List1 = []

Avengers = ['Hulk', 'Iron-Man', 'Captain', 'Thor']

a, b = [1, 2]
print(a)
print(b)

Avengers = ['Hulk', 'Iron-Man', 'Captain', 'Thor']
print(Avengers[0])
print(Avengers[1])
print(Avengers[1:3])

Avengers = ['Hulk', 'Iron-Man', 'Captain', 'Thor']
Avengers[2] = "Captain-America"
print(Avengers)

C_W_team = ['Hulk', 'iron-man', 'Captain-American', 'Thor', "Vision"]
del C_W_team[0]
print(C_W_team)
del C_W_team[2:4]
print(C_W_team)

Avengers1 = ['hulk', 'iron-man', 'Captain-America', 'Thor']
Avengers2 = ["Vision","sam"]
Avengers = Avengers1 + Avengers2
print(Avengers)

Av = ['Vision', 'sam']
new_Av = Av * 2
print(new_Av)

Avengers= ['hulk', 'iron-man', 'Captain-America', 'Thor']
if "iron-man" in Avengers:
    print("Yes")

print(len(Avengers))

lista = [1, 2, 6, 45, 100]
print(max(lista))

lista = ["1", "2"]
print(max(lista))

#method list()
name = "Esther"
print(list(name))

#method sorted()
list1 = [2, 3, 0, 3, 1, 4, 7, 1]
print(sorted(list1))
print(list1)

#tuple in sorted()
tuple = (100, 5, 7, 9)
print(sorted(tuple))

#method append()

Avengers = []
Avengers.append("Captain American")
print(Avengers)

#extend() method
Avengers1 = ["Hulk"]
Avengers2 = ["iron-man", 'sam']
Avengers1.extend(Avengers2)
print(Avengers1)

list1 = ["mohit", "Bhaskar"]
name = "Linda"
list1.extend(name)
print(list1)

#tuple + list in extend() method
Avengers1 = ['hulk', 'iron-man', 'Captain-America', 'Thor']
team2 = ("vision", "Clint")
Avengers1.extend(team2)
print(Avengers1)

# extend() x append() method
Linux = ["kali", "Ubuntu", "debian"]
Linux2 = ["RHEL", "Centos"]
Linux.extend(Linux2)
print(Linux)

Linux = ["kali", "Ubuntu", "debian"]
Linux2 = ["RHEL", "Centos"]

Linux.append(Linux2)
print(Linux)

#count() method
list1 = ["a","c","b","c","a","h","l", 1, 2, 3, 4]
print(list1.count("c"))

#index() method
OS = ['kali', 'Ubuntu', 'debian', 'RHEL', 'Centos']
print(OS.index("debian"))

print(OS.index("RHEL"))

#insert() method
A = ['iron-man', 'hulk', 'Thor']
A.insert(1, "Captain-America")
print(A)

#remove() method
Avengers1 = ["Iron-man","Thor","Loki","hulk"]
Avengers1.remove("Thor")
print(Avengers1)

num = [1,2,3,4,5,6,4,1,7]
num.remove(1)
print(num)

#pop() method
GoT = ["Tyrion","Sansa", "Arya","Joffrey","Ned-Stark"]
GoT.pop()
print(GoT)




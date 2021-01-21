friends_lists = ['Ruth', 'Levi', 'Sueli', 'Raimundo', 'Felipe']
message = "Eu felipe convido-os ao jantar"
print(message + " " + friends_lists[0])
print(message + " " + friends_lists[1])
print(message + " " + friends_lists[2])
print(message + " " + friends_lists[3])
print(message + " " + friends_lists[4])

print(friends_lists.pop())
friends_lists.append('Linda')
print(friends_lists)
print("______________________________________________")
friends_lists = ['Ruth', 'Levi', 'Sueli', 'Raimundo', 'Felipe']
friends_lists.insert(1, "Linda")
friends_lists.insert(2, "Esther")
friends_lists.insert(3, "Naomi")
friends_lists.append("Paulo")
print(friends_lists)

friends_lists.pop(1)
friends_lists.pop(2)
friends_lists.pop(3)
friends_lists.pop(4)
friends_lists.pop(2)
friends_lists.pop(-1)
friends_lists.pop(-2)
del friends_lists[0]
del friends_lists[-1]
print(friends_lists)
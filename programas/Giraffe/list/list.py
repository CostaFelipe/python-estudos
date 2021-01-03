friends = ["Ruth", "Levi", "Diego"]
print(friends)
print(friends[0])
print(friends[1])
print(friends[2])
print(friends[-1])
print(friends[-2])
print(friends[-3])
print(friends[1:3])
print(friends[1:])
print(friends[:2])

friends[2] = "Mike"
print(friends)

#list functions
luck_numbers = [111, 22, 3, 7, 8]
friends = ["Ruth", "Levi", "Diego"]
#friends.extend(luck_numbers)
print(friends)
friends.append("Linda")
print(friends)

friends.insert(1, "Esther")
print(friends)

friends.remove("Diego")
print(friends)

friends.clear()
print(friends)

friends = ["Kevin", "Karen", "Jim", "Oscar"]
friends.pop()
print(friends)
print(friends.index("Jim"))

friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Anne"]
print(friends.count("Karen"))

friends.sort()
print(friends)

luck_numbers.sort()
print(luck_numbers)

luck_numbers.reverse()
print(luck_numbers)

numbers = luck_numbers.copy()
print(numbers)
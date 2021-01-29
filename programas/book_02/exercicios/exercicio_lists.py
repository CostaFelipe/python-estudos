# string == avengers
list1 = ["abc",[2,3,("mohit","the avengers")],1,2,3]
print(list1[1][2][1][4:])

#With the for loop, take the following list and sort it based on the sum of the
#values of the tuples of the list:
list1 = [(1,5),(9,0),(12,3),(5,4),(13,6),(1,1)]

def sum1(tup1):
	a,b = tup1
	c = a+b
	return c

list1.sort(key=sum1)
print(list1)
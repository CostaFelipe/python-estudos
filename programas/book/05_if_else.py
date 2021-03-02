#if and else == !=
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies")

age = 18
print(age == 18)

answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")

age = 19
print(age <= 21)
print(age >= 21)
print(age < 19)

#Testando varias condicoes
#and
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)

age_1 = 22
print(age_0 >= 21 and age_1 >= 21)

#or
age_1 = 18
print(age_0 >= 21 or age_1 >= 21)
age_0 = 18
print(age_0 > 21 or age_1 >= 21)



#for if else
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

car = 'bmw'
print(car == 'bmw')

car = 'audi'
print(car == 'bmw')

car = 'Audi'
print(car == 'audi')

car = 'Audi'
print(car.lower() == 'audi')

#difirenca !=
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")

age = 18
print(age == 18)

answer = 17
if answer != 42:
    print('That is not the correct answer. Please try again!')

print(age <= 15)
print(age >= 18)
print(age > 15)
print(age < 15)

# and
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)
age_1 = 22
print(age_0 >= 21 and age_1 >= 21)

# or
age_0 = 22
age_1 = 18
print(age_0 >= 21 or age_1 >= 21)
age_0 = 18
print(age_0 >= 21 or age_1 >= 21)

#in
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)
print('pepperoni' in requested_toppings)

#not in
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")

#faca voce mesmo
#5.1
car = 'subaru'
if car == 'subaru':
    print("Is car == 'subaru'? I predict True.")
    print(car == 'subaru')

car = 'ford'
if car != 'audi':
    print("\n car == 'audi'? I predict False.")
    print(car == 'audi')

#5.2
name = 'Esther'
print(name == 'esther')
print(name == 'Esther')
print(name.lower() == 'esther')

number_0 = 33
number_1 = 31
print(number_0 >= 30 and number_1 >= 30)
print(number_0 <= 30 and number_1 <= 30)
number_1 = 18
print(number_0 >= 30 and number_1 >= 30)
print(number_0 <= 30 and number_1 <= 30)
print(number_0 <= 30 or number_1 <= 30)

medicos = ['Henrique', 'Paulo', 'Paula', 'Esther']
print('felipe' in medicos)
print('Paula' in medicos)
name = 'felipe'
if name.title() not in medicos:
    print("O medico " + name.title() + " nao existe")

#Instrucoes if simples
age = 19
if age >= 18:
    print("You are old enough to vote")

age = 19
if age >= 18:
    print("You are old enough to vote")
    print("Have you registered to vote yet?")

print("\n")
#if-else
age = 17
if age >= 18:
    print("You are old enough to vote")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

print("\n")
#if-elif-else
age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")

print("\n")

age = 12
if age < 4: price = 0
elif age < 18: price = 5
else: price = 10
print("Your admission cost is $" + str(price) + ".")

print("\n")
#Usando varios blocos elif
age = 64
if age < 4: price = 0
elif age < 18: price = 5
elif age > 65: price = 5
else: price = 10
print("Your admission cost is $" + str(price) + ".")

print("\n")
age = 19
if age < 4: price = 0
elif age < 18: price = 5
elif age < 65: price = 10
elif age >= 65: price = 5

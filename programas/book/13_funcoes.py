#coding=utf-8
#Passando uma lista para uma função

def greet_users(names):
    for name in names:
        msg = "hello, " + name.title() + "!"
        print(msg)

usernames = ['felipe', 'ruth', 'levi']
greet_users(usernames)

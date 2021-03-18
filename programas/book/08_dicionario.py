#coding=utf-8
#Um dicionário em um dicionário
users = {
    'aeinstein': {
                 'first': 'albert', 'last': 'einstein',
                 'location': 'princeton', },
    'felipe': {'first': 'lima', 'last': 'martins',
                'location': 'sao paulo'},
    'ruth': {'first':'silva', 'last': 'gomes',
              'location': 'santa catarina'}
}
for username, bio in users.items():
    print(username.title() + " " + bio['first'] + " " + bio['last'])


accounts = {
            'felipe' : {'username': 'felipe', 'lastname': 'lima'},
            'ruth' : {'username': 'ruth', 'lastname': 'lima'},
            'levi' : {'username': 'levi', 'lastname': 'lima'}
           }

for account, profile in accounts.items():
    print(account.title() + " Profile {" + profile['username'] + " " + profile['lastname'] + "}" )

#exercicios
people_01 = {'first_name': 'linda', 'last_name': 'rita', 'age': 27,'city': 'sao paulo'}
people_02 = {'first_name': 'mulder', 'last_name': 'johny', 'age': 34 ,'city': 'santa catarina'}
people_03 = {'first_name': 'esther', 'last_name': 'Akino', 'age': 32,'city': 'mato grosso'}
peoples = [people_01, people_02, people_03]

for people in peoples:
    print(people)

yaika = {'tipo': 'cachorro', 'dono': 'felipe'}
misuki = {'tipo': 'cachorro', 'dono': 'ruth'}
naninha = {'tipo': 'gato', 'dono': 'levi'}
pets = [yaika, misuki, naninha]

for pet in pets:
    print(pet)

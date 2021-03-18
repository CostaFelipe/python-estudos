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

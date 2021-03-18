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

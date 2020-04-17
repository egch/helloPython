phonebook = {}
phonebook['Enrico'] = 56546354635
phonebook['Maria'] = 673647364
print(phonebook)

addressbook = {
    'Basel': 'badenerstrasse 19',
    'Ascoli': 'via Roma 40'
}
# print(addressbook)

for key, value in addressbook.items():
    print('key: %s - value: %s' % (key, value))

del addressbook['Basel']
print(addressbook)
addressbook.pop('Ascoli')
print(addressbook)

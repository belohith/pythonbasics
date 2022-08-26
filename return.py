def greet(lang):
    if lang =='es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'

print (greet('en'), 'Genny')
print(greet('fr'), 'Harry')
print(greet('es'), 'Alex')
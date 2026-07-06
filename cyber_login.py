#Project: Cyber Login System

maintenance = True
adm_passwo = "Admin555"
reqiured_level = 3
owner = 'Sergey'

name = input('Enter your name:')
passwo = input('Enter your password:')
lvl = int(input('Enter your lvl:'))

if not maintenance and passwo == adm_passwo and lvl >= reqiured_level:
    print('Access granted!')
    if name == owner:
        print('Welcome back!, Owner!')
        print("========")
        print('Name:', name)
        print('Lvl:', lvl)
        print("========")
    else:
        print('Welcome back!', name)
        print("========")
        print('Name:', name)
        print('Lvl:', lvl)
        print("========")
else:
    print('Access denied')


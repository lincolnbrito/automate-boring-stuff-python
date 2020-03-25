password_file = open('pass.txt')
secret_password = password_file.read()

print('Enter your password')
typed_password = input()

if typed_password == secret_password:
    print('Access Granted')
    if typed_password == '12345':
        print('That password sucks')
else:
    print('Acess Denied')
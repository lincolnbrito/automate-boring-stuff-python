# This program say Hello and ask your name and age

print('Hello World!')
print('What is your name?')
my_name = input()

print('It is good to meet you, ' + my_name)
print('The length of your name is: ', len(my_name))

print('What is your age?')
my_age = input()
print('You will be ' + str(int(my_age)+1) + ' in a year.')

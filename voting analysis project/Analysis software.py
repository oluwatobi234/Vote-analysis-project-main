options = ['List Constituency names','Name of regions','Countries information']
print('Welcome: I am here to help you. Pls pick from this option:')
option_num = 0
for option in options:
    option_num +=1
    print(option_num, option)

while True:
    user_input = input(f'please pick a number: ')
    if user_input.isdigit():
        user_input = int(user_input)
        if 1<=user_input <= len(options):
            print('this work')
            break
        else:
            print('Invalid option, please pick a number') 
    
    else:
        print('Invalid option, please pick a number')
    


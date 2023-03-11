from replit import clear
elements = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', ',', '?', "'", '!', '/',
            '(', ')', '&', ':', ';', '=', '+', '-', '_', '"', '$', '@', ' ']

signs = ['▄ ▄▄▄ ', '▄▄▄ ▄ ▄ ▄', '▄▄▄ ▄ ▄▄▄ ▄', '▄▄▄ ▄ ▄', '▄', '▄ ▄ ▄▄▄ ▄', '▄▄▄ ▄▄▄ ▄', '▄ ▄ ▄ ▄', '▄ ▄',
         '▄ ▄▄▄ ▄▄▄ ▄▄▄', '▄▄▄ ▄ ▄▄▄', '▄ ▄▄▄ ▄ ▄', '▄▄▄ ▄▄▄', '▄▄▄ ▄', '▄▄▄ ▄▄▄ ▄▄▄', '▄ ▄▄▄ ▄▄▄ ▄', '▄▄▄ ▄▄▄ ▄ ▄▄▄ ',
         '▄ ▄▄▄ ▄', '▄ ▄ ▄', '▄▄▄', '▄ ▄ ▄▄▄', '▄ ▄ ▄ ▄▄▄', '▄ ▄▄▄ ▄▄▄', '▄▄▄ ▄ ▄ ▄▄▄', '▄▄▄ ▄ ▄▄▄ ▄▄▄', '▄▄▄ ▄▄▄ ▄ ▄ ',
         '▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄', '▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄', '▄ ▄ ▄▄▄ ▄▄▄ ▄▄▄', '▄ ▄ ▄ ▄▄▄ ▄▄▄', '▄ ▄ ▄ ▄ ▄▄▄', '▄ ▄ ▄ ▄ ▄ ',
         '▄▄▄ ▄ ▄ ▄ ▄', '▄▄▄ ▄▄▄ ▄ ▄ ▄', '▄▄▄ ▄▄▄ ▄▄▄ ▄ ▄', '▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄', '▄ ▄▄▄ ▄ ▄▄▄ ▄ ▄▄▄',
         '▄▄▄ ▄▄▄ ▄ ▄ ▄▄▄ ▄▄▄ ', '▄ ▄ ▄▄▄ ▄▄▄ ▄ ▄', '▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄', '▄▄▄ ▄ ▄▄▄ ▄ ▄▄▄ ▄▄▄', '▄▄▄ ▄ ▄ ▄▄▄ ▄',
         '▄▄▄ ▄ ▄▄▄ ▄▄▄ ▄', '▄▄▄ ▄ ▄▄▄ ▄▄▄ ▄ ▄▄▄', '▄ ▄▄▄ ▄ ▄ ▄', '▄▄▄ ▄▄▄ ▄▄▄ ▄ ▄ ▄', '▄▄▄ ▄ ▄▄▄ ▄ ▄▄▄ ▄',
         '▄▄▄ ▄ ▄ ▄ ▄▄▄ ', '▄ ▄▄▄ ▄ ▄▄▄ ▄', '▄▄▄ ▄ ▄ ▄ ▄ ▄▄▄', '▄ ▄ ▄▄▄ ▄▄▄ ▄ ▄▄▄', '▄ ▄▄▄ ▄ ▄ ▄▄▄ ▄',
         '▄ ▄ ▄ ▄▄▄ ▄ ▄ ▄▄▄', '▄ ▄▄▄ ▄▄▄ ▄ ▄▄▄ ▄', 'space']
print('!!!!Welcome to MorseCode converter!!!!')
is_on = True
while is_on:
    sentence = input("write down below what you like to convert, and hit enter:\n")
    sent = sentence.upper()
    char_list = list(sent)
    for char in char_list:
        if char in elements:
            index = elements.index(char)
            print(signs[index])
        else:
            print("Error")
    print('End Of Work')
    choice = input('Do you want to continue converting? type "Y" or "n" and hit enter: ')
    if choice.upper() == "Y":
        clear()
    elif choice.upper() == "N":
        is_on = False
    else:
        print("Error!")
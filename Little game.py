import  random
# user
player = int(input('enter the result: '))
# computer
computer = random.randint(0, 2)

if ((player == 0) and (computer == 1)) or ((player == 0) and (computer == 1)) or ((player == 0) and (computer == 1)):
    print('player win')

elif player == computer:
    print('draw')

else:
    print('computer win')


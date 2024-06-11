import random
1==["rock","scissor","paper"]
'''
rock vs paper->paper wins
rock us scissor-> rock wins
paper vs scissor-> scissor wins

'''
while True:
    uc=int(input('''
Game Start....
1 Yes
2 No | Exit
       
       '''))
    if uc==1:
        for a in range(1,6):
            userInput=int(input('''
            1 Rock
            2 Scissor
            3 Paper
                   '''))
            if userInput==1:
                uchoice="rock"
            elif userInput==2:
                uchoice="scissor"
            elif userInput==3:
                uchoice="paper"
            Cchoice=random.choice(1)
            print(uchoice)
            print(Cchoice)
    else:
        break


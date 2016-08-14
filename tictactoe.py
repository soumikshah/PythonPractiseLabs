import random
from Tkinter import *

print '|', '?', '|',
print '|', '?', '|',
print '|', '?', '|'
print 'Hi, This is Text based Tic Tac Toe, You Get 4 chance to win. If you answer correctly thrice you win.'

question = {'Where is Bixby bridge?': 'California',
            'Where is Pyramid of Ghaza?': 'Egypt',
            'Where is Taj Mahal?': 'India',
            'Where is Eiffel Tower': 'Paris',
            'Where is Statue of Liberty':'New York',
            'What country has largest population?':'China'
            }
answers = ['California', 'Egypt', 'India', 'Paris','New York','China']
score = 0
machineScore = 0
play = True
while play is True:
    for i in range(6):
        if i % 2 == 0:
            a = question.keys().__getitem__(i)
            print a
            ans = str(raw_input("... ").capitalize())
            values = question.values().__getitem__(i)
            if ans == values.capitalize():
                score = score + 1
                if score == 1:
                    print '|', 'X', '|'
                if score == 2:
                    print '|', 'X', '|', '|', 'X', '|'
                if score == 3:
                    print '|', 'X', '|', '|', 'X', '|', '|', 'X', '|'
                    print "Wow, you're the winner. Hurray!!!!"
                    option = int(raw_input("press 1 to play again or 2 to exit."))
                    if option == 1:
                        score = 0
                        machineScore = 0
                        continue
                    elif option == 2:
                        play = False
                        break
            else:
                print "Sorry you're wrong."
        else:
            b=random.randrange(4)
            c = random.randrange(4)
            compGenerated = question.keys().__getitem__(b)
            compGeneratedAnswer = answers.__getitem__(c)
            print "Machine is playing, wait.."
            print compGenerated
            print "..."
            print "...."
            print "........"
            print compGeneratedAnswer
            quest = question.values().__getitem__(b)
            if quest is compGeneratedAnswer:
                machineScore = machineScore + 1
                if machineScore == 1:
                    print '|', 'O', '|'
                if machineScore == 2:
                    print '|', 'O', '|', '|', 'O', '|'
                if machineScore == 3:
                    print '|', 'O', '|', '|', 'O', '|', '|', 'O', '|'
                    print "Lol, Machine with less than 1% chance of winning against you has won!!!! Try harder"
                    break
            else:
                print "Machine age has not won upon us yet, keep playing soldier."
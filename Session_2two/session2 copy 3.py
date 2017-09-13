#three games

game_one="The Xbox __1__ is a home video game console developed by __2__. Announced on May 21, 2013, it isthe successor to the Xbox __3__ and the __4__ console in the Xbox family. It directly competes with Sony Computer Entertainment's PlayStation 4 and Nintendo's Wii U as part of the eighth generation of video game consoles."
game_two="__1__ 5: __2__ is a __3__ shooter video game developed by 343 Industries and published by __4__ Studios for the Xbox One. Part of the Halo franchise, the game was released on October 27, 2015."
game_three="John-117, or __1__ __2__, is a fictional character and the protagonist of the __3__ fictional universe created by __4__. Master Chief is a playable character in the series of science fiction first-person shooter video games: __3__: Combat Evolved, __3__ 2, __3__ 3, __3__ 4, and __3__ 5: Guardians."


answers_one=["one","Microsoft","360","third"]
answers_two=["Halo","Guardians","first-person","Microsoft"]
answers_three=["Master","Chief","Halo","Bungie"]







#functions

def user_choose_level():
        #show the prompt of choosing game level. It has no input, and output is the level (string) that user choose.
        level=raw_input("Please choose your level from 1, 2, 3: ") 
        return int(level)

def game_assign(level):# assing the game depends on level
        if level==1:
                return game_one
        elif level==2:
                return game_two
        return game_three

def answers_assign(level): #assign the answer depends on level
        if level==1:
                return answers_one
        elif level==2:
                return answers_two
        return answers_three

def user_input(index):
        user_input_answer=raw_input("What should go in blank number "+str(index)+" : ")
        return user_input_answer

def game_original(game):#show the original game
        print game

def game_replace(game,answer,index):#replace the __index__ by user's answer
        game_array=[]
        game=game.split()
        blank="__"+str(index)+"__"
        for s in game:
                if blank in s:
                        game_array.append(answer)
                else:
                        game_array.append(s)
        game=" ".join(game_array)
        return game



def win(game):
        print game
        print "Congratulation! You win the game."

#main programming
def main():
        level=user_choose_level()
        game=game_assign(level)
        answers=answers_assign(level)
        for a in answers:
                index_question=answers.index(a)+1#the ith question
                while True:
                        print game  #show the game before answer the ith question
                        user_input_answer=user_input(index_question) #user answer the ith question
                        if user_input_answer==a: #check the answer
                                game=game_replace(game,a,index_question)#if user answer correct, replace __index__ by answer
                                break
                        continue
        win(game)
                

main()
















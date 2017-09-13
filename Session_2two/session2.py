#three games

game_one="The Xbox __1__ is a home video game console developed by __2__. Announced on May 21, 2013, it isthe successor to the Xbox __3__ and the __4__ console in the Xbox family. It directly competes with Sony Computer Entertainment's PlayStation 4 and Nintendo's Wii U as part of the eighth generation of video game consoles."
game_two="__1__ 5: __2__ is a __3__ shooter video game developed by 343 Industries and published by __4__ Studios for the Xbox One. Part of the Halo franchise, the game was released on October 27, 2015."
game_three="John-117, or __1__ __2__, is a fictional character and the protagonist of the __3__ fictional universe created by __4__. Master Chief is a playable character in the series of science fiction first-person shooter video games: __3__: Combat Evolved, __3__ 2, __3__ 3, __3__ 4, and __3__ 5: Guardians."

#three answers
answers_one=["one","Microsoft","360","third"]
answers_two=["Halo","Guardians","first-person","Microsoft"]
answers_three=["Master","Chief","Halo","Bungie"]


def user_choose_level():#show the prompt of choosing game level. It has no input Output is the level (string) that user choose.
        level=raw_input("Please choose your level from 1, 2, 3: ") 
        return int(level)

def user_input(index):#show the questions. The input is the index of answer arry, and return user's input
        user_input_answer=raw_input("What should go in blank number "+str(index)+" : ")
        return user_input_answer

def game_assign(level):# assign the game and answer depends on level that user choose. Input is the level. Output are the game and answer in that level.
        if level==1:
                return game_one,answers_one
        elif level==2:
                return game_two,answers_two
        return game_three,answers_three



def game_replace(game,answer,index):#replace the __index__ by user's answer. The input is the game, the correct answer, and the index of question. The output is the game with blank replaced by user's answer
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

def win(game):#show user win the game. The input is the game with all correct answer. The output is the game, and also congratulation.
        print game
        print "Congratulation! You win the game."

def main():#main programming. There is no input. The output is: first, the user chooses the level, second, the game shows, and waiting user's answer. Third, user answers questions one by one. Finaly it shows the user win.  
        level=user_choose_level()
        game,answers=game_assign(level)
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
                

main()#run the program. The game is run from this function. There is no input. Output is the game.
















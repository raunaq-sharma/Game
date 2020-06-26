import Mood
from sys import exit
from random import randint

setting = Mood.Mood(1, 1, 1)
def calc(setting):
        return setting.stability * (setting.HMULT/setting.SMULT) * 100/randint(5, 10)
            
def RPG(set_mood):
    if set_mood == "Happy":
        print ("100% stability achieved!")
    else:
        print(f"Your mental stability is: {round(calc(setting), 2)}%.")
    
def FPS(set_mood):
    if set_mood == "Angry":
       print("100% stability achieved!")
    else:
        print(f"Your mental stability is: {round(calc(setting), 2)}%.")
        
def PnC(set_mood):
    if set_mood == "Stressed":
        print ("100% stability achieved!")
    else:
        print(f"Your mental stability is: {round(calc(setting), 2)}%.")
        
def Sim(set_mood):
    if set_mood == "Sad":
        print ("100% stability achieved!")
    else:
        print(f"Your mental stability is: {round(calc(setting), 2)}%.") 
            
def output(set_mood, set_games):

    if set_mood == "Happy": 
        setting = Mood.Happy()
    elif set_mood == "Angry":
        setting = Mood.Angry()
    elif set_mood == "Stressed":
        setting = Mood.Stressed()
    elif set_mood == "Sad":
        setting = Mood.Sad()
        
    if set_games == "RPG":
        RPG()
    elif set_games == "FPS":
        FPS(set_mood)
    elif set_games == "PnC":
        PnC()
    elif set_games == "Sim":
        Sim()
        
    # print(setting.HMULT)
    # print(setting.SMULT)
            
# output("Angry", "FPS")

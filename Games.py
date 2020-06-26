import Mood
from sys import exit
from random import randint

setting = Mood.Mood(1, 1, 1) #initialized for calc

def calc(setting):
        return setting.stability * (setting.HMULT/setting.SMULT) * 100/randint(5, 10)
            
def RPG(set_mood):
    if set_mood == "Happy":
        data = "100% stability achieved!"
    else:
        data = f"Your mental stability is: {round(calc(setting), 2)}%."
    return data
    
def FPS(set_mood):
    if set_mood == "Angry":
       data = "100% stability achieved!"
    else:
        data = f"Your mental stability is: {round(calc(setting), 2)}%."
    return data
        
def PnC(set_mood):
    if set_mood == "Stressed":
        data = "100% stability achieved!"
    else:
        data = f"Your mental stability is: {round(calc(setting), 2)}%."
    return data   
    
def Sim(set_mood):
    if set_mood == "Sad":
        data = "100% stability achieved!"
    else:
        data = f"Your mental stability is: {round(calc(setting), 2)}%."
    return data 
    
def output(set_mood, set_games):
    
    global setting  #reassign values to setting in global scope
    if set_mood == "Happy": 
        setting = Mood.Happy()
    elif set_mood == "Angry":
        setting = Mood.Angry()
    elif set_mood == "Stressed":
        setting = Mood.Stressed()
    elif set_mood == "Sad":
        setting = Mood.Sad()
        
    if set_games == "RPG":
        games_result = RPG(set_mood)
    elif set_games == "FPS":
        games_result = FPS(set_mood)
    elif set_games == "PnC":
        games_result = PnC(set_mood)
    elif set_games == "Sim":
        games_result = Sim(set_mood)
    
    return games_result   

#print(output("Angry", "RPG"))
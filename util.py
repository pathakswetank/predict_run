import pickle
import json
import numpy as np

__PLAYER = None
__data_columns = None
__model = None

def estimated_run(PLAYER, Avg, BF, SR,Fours, Six):
    try:
        loc_index = __data_columns.index(PLAYER.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = Avg
    x[1] = BF
    x[2] = SR
    x[3] = Fours
    x[4] = Six
    if loc_index >= 0:
        x[loc_index] = 1
    
    return round (__model.predict([x])[0])


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global  __data_columns
    global __locations

    with open("columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __PLAYER = __data_columns[5:]  

    global __model
    if __model is None:
        with open('ipl_individual.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")

def player_names():
    return __PLAYER

def get_data_columns():
    return __data_columns

if __name__ == '__main__':
    load_saved_artifacts()
    print(player_names())
    print(estimated_run("KL_Rahul", 80,20,125,10,4))
    
from game import Game
from cards import Deck
import numpy as np
import pandas as pd
import pickle
from tqdm.notebook import tqdm


def runSimulations(numberOfPlayers: int, numberOfSimulations: int, append: dict = None, verbose: bool = True) -> dict:

    if append is None:
        simulations = {item:np.array([0,0,0]) for item in Game.HAND_RANKINGS.keys()}
    else:
        simulations = append
    
    if(verbose):
        if append is None:
            print(f"Running {numberOfSimulations} simulations for a game of {numberOfPlayers} players")
        else:
            print(f"Adding {numberOfSimulations} simulations for a game of {numberOfPlayers} players")

    for _ in tqdm(range(numberOfSimulations)):
        game = Game(numberOfPlayers)
        res = game.simulateGame()
        for item in res:
            simulations[item]=np.add(simulations[item],res[item])

    return simulations

def saveRaw(results: dict, numberOfPlayers: int, verbose: bool = True):

    fileName = 'results/winrate_'+str(numberOfPlayers)+"_raw.pickle"
    with open(fileName, 'wb') as handle:
        pickle.dump(results, handle, protocol=pickle.HIGHEST_PROTOCOL)
    
    if(verbose):
        print(f"Raw data file saved at {fileName}!")

def clean(results: dict, numberOfPlayers: int, verbose: bool = True) -> pd.DataFrame:

    names = list(Game.HAND_NAMES.values())

    cleaned = pd.DataFrame.from_dict(results,orient='index', columns = ['wins','ties','total_games'])
    cleaned.index.name = 'hand'
    cleaned.insert(0, 'name', names)
    cleaned['winrate'] = cleaned['wins']/cleaned['total_games']
    cleaned['winrate'] = round(cleaned['winrate'], 4)
    cleaned.index = [", ".join(list(item)) for item in cleaned.index]

    if(verbose):
        print("Converted dictionary to DataFrame and cleaned it!")

    return cleaned

def saveCleaned(results: pd.DataFrame, numberOfPlayers: int, verbose: bool = True):

    fileName = 'results/winrate_'+str(numberOfPlayers)+"_cleaned.csv"
    results.to_csv(fileName)

    if(verbose):
        print(f"Cleaned data file saved at {fileName}!")

def loadRaw(numberOfPlayers: int, verbose: bool = True) -> dict:

    fileName = 'results/winrate_'+str(numberOfPlayers)+"_raw.pickle"
    with open(fileName, 'rb') as handle:
        res = pickle.load(handle)

    if(verbose):
        print(f"Data loaded from {fileName}!")
    
    return res

def simulationsRun(numberOfPlayers: int, verbose: bool = True):

    df = pd.read_csv('results/winrate_'+str(numberOfPlayers)+"_cleaned.csv")
    num = int(df['total_games'].sum()/numberOfPlayers)

    if(verbose):
        print(f"{num} simulations have been run for {numberOfPlayers} players")
    else:
        return num


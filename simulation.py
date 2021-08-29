from game import Game
from cards import Deck
import numpy as np
import pandas as pd
import pickle
from tqdm.notebook import tqdm


def runSimulations(numberOfPlayers: int, numberOfSimulations: int, append: dict = None) -> dict:

    if append is None:
        simulations = {item:np.array([0,0,0]) for item in Game.HAND_RANKINGS.keys()}
    else:
        simulations = append

    for _ in tqdm(range(numberOfSimulations)):
        game = Game(numberOfPlayers)
        res = game.simulateGame()
        for item in res:
            simulations[item]=np.add(simulations[item],res[item])

    return simulations

def saveRaw(results: dict, numberOfPlayers: int):

    fileName = 'results/winrate_'+str(numberOfPlayers)+"_raw.pickle"
    with open(fileName, 'wb') as handle:
        pickle.dump(results, handle, protocol=pickle.HIGHEST_PROTOCOL)

def clean(results: dict, numberOfPlayers: int) -> pd.DataFrame:

    names = list(Game.HAND_NAMES.values())

    cleaned = pd.DataFrame.from_dict(results,orient='index', columns = ['wins','ties','total_games'])
    cleaned.index.name = 'hand'
    cleaned.insert(0, 'name', names)
    cleaned['winrate'] = cleaned['wins']/cleaned['total_games']
    cleaned['winrate'] = round(cleaned['winrate'], 4)
    cleaned.index = [", ".join(list(item)) for item in cleaned.index]

    return cleaned

def saveCleaned(results: pd.DataFrame, numberOfPlayers: int):

    fileName = 'results/winrate_'+str(numberOfPlayers)+"_cleaned.csv"
    results.to_csv(fileName)

def loadRaw(numberOfPlayers: int) -> dict:

    fileName = 'results/winrate_'+str(numberOfPlayers)+"_raw.pickle"
    with open(fileName, 'rb') as handle:
        res = pickle.load(handle)

    return res

def simulationsRun(numberOfPlayers: int):

    df = pd.read_csv('results/winrate_'+str(numberOfPlayers)+"_cleaned.csv")
    return int(df['total_games'].sum()/numberOfPlayers)


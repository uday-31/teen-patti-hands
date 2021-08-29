from .game import Game
from .cards import Deck
import numpy as np
import pandas as pd
import pickle
from tqdm.notebook import tqdm


def runSimulations(numberOfPlayers: int, numberOfSimulations: int, append: dict = None, verbose: bool = True) -> dict:
    """Run simulations of games

    Parameters
    ----------
    numberOfPlayers : int
        Number of players in each game
    numberOfSimulations : int
        Number of simulations of the game
    append : dict, optional
        Whether results are to be added to existing results, by default None
    verbose : bool, optional
        Whether debugging information is to be printed, by default True

    Returns
    -------
    dict
        Results for each possible hand
    """

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
    """Save the dictionary of results

    Parameters
    ----------
    results : dict
        Results for each hand
    numberOfPlayers : int
        Number of players in the game
    verbose : bool, optional
        Whether debugging information is to be printed, by default True
    """

    fileName = 'results/winrate_'+str(numberOfPlayers)+"_raw.pickle"
    with open(fileName, 'wb') as handle:
        pickle.dump(results, handle, protocol=pickle.HIGHEST_PROTOCOL)
    
    if(verbose):
        print(f"Raw data file saved at {fileName}!")

def clean(results: dict, numberOfPlayers: int, verbose: bool = True) -> pd.DataFrame:
    """Cleans the results and converts it to a DataFrame

    Parameters
    ----------
    results : dict
        Results for each hand
    numberOfPlayers : int
        Number of players in the game
    verbose : bool, optional
        Whether debugging information is to be printed, by default True

    Returns
    -------
    pd.DataFrame
        Cleaned DataFrame with the results for each hand
    """

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
    """Save the cleaned results to a CSV file

    Parameters
    ----------
    results : pd.DataFrame
        Cleaned DataFrame with the results for each hand
    numberOfPlayers : int
        Number of players in the game
    verbose : bool, optional
        Whether debugging information is to be printed, by default True
    """

    fileName = 'results/winrate_'+str(numberOfPlayers)+"_cleaned.csv"
    results.to_csv(fileName)

    if(verbose):
        print(f"Cleaned data file saved at {fileName}!")

def loadRaw(numberOfPlayers: int, verbose: bool = True) -> dict:
    """Load the dictionary of results

    Parameters
    ----------
    numberOfPlayers : int
        Number of players in the game
    verbose : bool, optional
        Whether debugging information is to be printed, by default True

    Returns
    -------
    dict
        Dictionary with results for each hand
    """

    fileName = 'results/winrate_'+str(numberOfPlayers)+"_raw.pickle"
    with open(fileName, 'rb') as handle:
        res = pickle.load(handle)

    if(verbose):
        print(f"Data loaded from {fileName}!")
    
    return res

def simulationsRun(numberOfPlayers: int, verbose: bool = True):
    """Get the number of simulations that have been run for games with a certain number of players

    Parameters
    ----------
    numberOfPlayers : int
        Number of players in the game
    verbose : bool, optional
        Whether debugging information is to be printed or returned, by default True

    Returns
    -------
    [type]
        [description]
    """

    df = pd.read_csv('results/winrate_'+str(numberOfPlayers)+"_cleaned.csv")
    num = int(df['total_games'].sum()/numberOfPlayers)

    if(verbose):
        print(f"{num} simulations have been run for {numberOfPlayers} players")
    else:
        return num


# teen-patti-winrates
Run Monte Carlo simulations to get win-rates for different Teen patti (three-card brag) hands

# Introduction
Teen Patti is a card game popular in South Asia. It is a derivative of poker and three-card brag, and is also called flush. Each player is dealt a hand of three cards, and the betting continues till one player remains: players can pack, or choose to 'show' with adjacent players, where the hands are compared and the player with the worse hand has to pack. More details can be found [here](https://en.wikipedia.org/wiki/Teen_patti).

The purpose of this project is to run Monte Carlo simulations to generate the win-rates of each possible hand, for games with a certain number of players. This is done by first simulating the running of a single game by defining hands for each player, and then comparing the hands to pick a winner. This is then run millions of times and the results are saved.

# Examples
See the file examples.ipynb for usage examples.

## Cards 
Cards can be created using the Card class in code/cards.py.

```python
# Creating a card
aceSpades = Card('S', 'A')

# Printing the full name of the card
aceSpades.printCard()
```

## Decks
Decks can be created using the Deck class in code/cards.py.

```python
# Creating a deck
deck = Deck()

cards = []
for card in deck.getDeck():
    cards.append(card.getShorthand())

print(cards)
print("Size of deck:",deck.size)
```

## Simulating games
Simulations for a game can be run using the Game class in code/game.py.

```python
# Creating a game of 5 players and generating hands
game = Game(5)

# Simulate a single game
results = game.simulateGame(saveResults=True)
game.printResults()
```

## Running Monte Carlo simulations
Functions from simulation.py can be used to run simulations, and manipulate the results.

```python
# Running 1000000 simulations for a game of 5 players
sim = runSimulations(5, 1000000)

# Adding 500000 simulations to the previous results
sim = runSimulations(5, 500000, append = sim)
```

Saving and loading the raw dictionary file:
```python
# Saving the dictionary with results
saveRaw(sim, 5)

# Loading the dictionary
sim = loadRaw(5)
```

Cleaning the raw dictionary and converting it to a DataFrame:
```python
# Cleaning the dictionary and converting it to a DataFrame
sim_cleaned = clean(sim, 5)

# Saving the cleaned DataFrame
saveCleaned(sim_cleaned, 5)
```

Retrieving the number of simulations run:
```python
# Retrieving the number of simulations run for games with 5 players
simulationsRun(5)
```

# Results
Simulation results are found in the results folder.

The CSV files are named according to the number of players in the game for which the simulations were run.

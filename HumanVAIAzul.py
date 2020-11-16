from MCTS import MCTS
from azul.AzulGame import AzulGame
from azul.AzulPlayers import HumanAzulPlayer, RandomPlayer
from azul.pytorch.NNet import NNetWrapper as NNet
from azul.AzulArena import AzulArena

import cProfile, pstats, io
from pstats import SortKey

import numpy as np
from utils import *

"""
use this script to play any two agents against each other, or play manually with
any agent.
"""

randPlayers = True

g = AzulGame(shouldRandomize=False)

# all players
hp = HumanAzulPlayer(g).play
rp1 = RandomPlayer(g).play
rp2 = RandomPlayer(g).play

n2 = NNet(g)
n2.load_checkpoint('./temp/', 'best.pth.tar')
args2 = dotdict({'numMCTSSims': 50, 'cpuct': 1.0})
mcts2 = MCTS(g, n2, args2)
n2p = lambda x: np.argmax(mcts2.getActionProb(x, temp=0))

player2 = n2p  # Player 2 is neural network if it's cpu vs cpu.

if randPlayers:
    arena = AzulArena(rp1, rp2, g, display=AzulGame.display)
else:
    arena = AzulArena(hp, player2, g, display=AzulGame.display)

print(arena.playFullGame(verbose=True))


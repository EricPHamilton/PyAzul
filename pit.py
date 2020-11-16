import Arena
from MCTS import MCTS
from azul.AzulGame import AzulGame
from azul.AzulPlayers import RandomPlayer, HumanAzulPlayer
from azul.pytorch.NNet import NNetWrapper as NNet

import cProfile, pstats, io
from pstats import SortKey


import numpy as np
from utils import *

"""
use this script to play any two agents against each other, or play manually with
any agent.
"""

human_vs_cpu = False
ai = False
profiling = True

g = AzulGame(shouldRandomize=False)

# all players
rp = RandomPlayer(g).play
rp2 = RandomPlayer(g).play
hp = HumanAzulPlayer(g).play

if human_vs_cpu:
    player2 = hp
else:
    if (ai):
        n2 = NNet(g)
        n2.load_checkpoint('./temp/', 'best.pth.tar')
        args2 = dotdict({'numMCTSSims': 50, 'cpuct': 1.0})
        mcts2 = MCTS(g, n2, args2)
        n2p = lambda x: np.argmax(mcts2.getActionProb(x, temp=0))

        player2 = n2p  # Player 2 is neural network if it's cpu vs cpu.
    else:
        player2 = rp2


if profiling:
    _output_file = 'perfTesting.prof'
    pr = cProfile.Profile()
    pr.enable()

arena = Arena.Arena(rp, player2, g, display=AzulGame.display)
print(arena.playGames(100, verbose=False))

if profiling:
    pr.disable()
    pr.dump_stats(_output_file)

    with open(_output_file, 'w') as f:
        ps = pstats.Stats(pr, stream=f)
        ps.strip_dirs()
        ps.sort_stats(SortKey.CUMULATIVE)
        ps.print_stats()
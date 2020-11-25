import cProfile, pstats, io
from azul.AzulPlayers import RandomPlayer
from azul.AzulArena import AzulArena
from azul.AzulGame import AzulGame

pr = cProfile.Profile()
pr.enable()

g = AzulGame(shouldRandomize=False)
rp1 = RandomPlayer(g).play
rp2 = RandomPlayer(g).play

for _ in range(100):
    arena = AzulArena(rp1, rp2, g, display=AzulGame.display)

    arena.playFullGame(verbose=False)

pr.disable()
s = io.StringIO()
ps = pstats.Stats(pr, stream=s).sort_stats('cumulative')
ps.print_stats()

with open('azulperf2.txt', 'w+') as f:
    f.write(s.getvalue())



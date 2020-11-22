import sqlite3

con = sqlite3.connect('AzulGamesSite/AzulGameViewer/db.sqlite3')

with con:
    cur = con.cursor()
    cur.execute("DELETE FROM games_game")
    cur.execute("DELETE FROM games_turn")
con.commit()
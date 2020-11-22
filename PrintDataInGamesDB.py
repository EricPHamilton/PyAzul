import sqlite3

con = sqlite3.connect('AzulGamesSite/AzulGameViewer/db.sqlite3')

with con:
    cur = con.cursor()
    cur.execute("SELECT * FROM games_game")
    rows = cur.fetchall()

    print("GAMES")
    for row in rows:
        print(row)

    cur.execute("SELECT * FROM games_turn")
    rows = cur.fetchall()

    print("TURNS")
    for row in rows:
        print(row)
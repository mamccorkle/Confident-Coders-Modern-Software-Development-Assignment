from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# Function to fetch all games from the database
def get_all_games():
    conn = sqlite3.connect('MSD-P01-LeaderBoard.sqlite')
    cursor = conn.cursor()
    cursor.execute("SELECT game_id, game_name, description FROM games")
    games = cursor.fetchall()
    conn.close()
    return games

@app.route('/')
def hello_world():  # put application's code here
    games = get_all_games()
    return render_template('index.html', games=games)


def get_leaderboard_data(game_name):
    conn = sqlite3.connect('MSD-P01-LeaderBoard.sqlite')
    cursor = conn.cursor()
    cursor.execute("""
        SELECT l.rank, l.player_name, l.score
        FROM leaderboard l
        JOIN games g ON l.game_id = g.game_id
        WHERE g.game_name = ?
        ORDER BY l.rank
    """, (game_name,))
    rows = cursor.fetchall()
    conn.close()
    return rows

@app.route('/leaderboard/<game_name>')
def leaderboard(game_name):
    data = get_leaderboard_data(game_name)
    return render_template('leaderboard.html', game_name=game_name, data=data)


if __name__ == '__main__':
    app.run(debug=True)

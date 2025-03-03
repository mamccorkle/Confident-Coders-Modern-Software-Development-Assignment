from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# This function will get a list of all games so that it can be displayed on the main landing page:
def get_all_games():
    conn = sqlite3.connect('MSD-P01-LeaderBoard.sqlite')
    cursor = conn.cursor()
    cursor.execute("SELECT game_id, game_name, description FROM games")
    games = cursor.fetchall()
    conn.close()
    return games

# This function will get a specific games details:
def get_game_details(game_id):
    conn = sqlite3.connect('MSD-P01-LeaderBoard.sqlite')
    cursor = conn.cursor()
    cursor.execute("SELECT game_name, description FROM games WHERE game_id = ?", (game_id,))
    game = cursor.fetchone()
    conn.close()
    return game

# This function will get a games leaderboard details:
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

# This function will add a new game to the database:
def add_game_to_db(game_name, description):
    conn = sqlite3.connect('MSD-P01-LeaderBoard.sqlite')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO games (game_name, description) VALUES (?, ?)", (game_name, description))
    conn.commit()
    conn.close()


## Routes:

# Main landing page route with GET and POST to allow for adding games to the database:
@app.route('/', methods=['GET', 'POST'])
def home():
    # Display all games
    games = get_all_games()  # Fetch all games from the database
    return render_template('index.html', games=games)


# Leaderboard for an individual game:
@app.route('/leaderboard/<game_name>')
def leaderboard(game_name):
    data = get_leaderboard_data(game_name)
    return render_template('leaderboard.html', game_name=game_name, data=data)

# Route to a games details page:
# Game Details page
@app.route('/game/<int:game_id>')
def game_details(game_id):
    game = get_game_details(game_id)
    if game:
        return render_template('game_details.html', game=game)
    else:
        return "Game not found", 404

@app.route('/add_game', methods=['GET', 'POST'])
def add_game():
    if request.method == 'POST':
        # Get form data for the new game
        game_name = request.form['game_name']
        description = request.form['description']

        # Insert new game into the database
        add_game_to_db(game_name, description)

        # Redirect to the homepage to show the updated list of games
        return redirect(url_for('home'))
    else:
        print("test")


if __name__ == '__main__':
    app.run(debug=True)

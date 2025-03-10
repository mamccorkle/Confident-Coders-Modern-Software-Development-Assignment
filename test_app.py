import app
import pytest
import sqlite3


@pytest.fixture
def setup_database():
    # Setting up an in-memory database with sample data
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()

    # Create tables
    cursor.execute('''
    CREATE TABLE games (
        game_id INTEGER PRIMARY KEY,
        game_name TEXT,
        description TEXT
    )''')

    cursor.execute('''
    CREATE TABLE leaderboard (
        leaderboard_id INTEGER PRIMARY KEY,
        game_id INTEGER,
        player_name TEXT,
        score INTEGER,
        rank INTEGER,
        FOREIGN KEY (game_id) REFERENCES games(game_id)
    )''')

    # Insert sample data
    cursor.execute("INSERT INTO games (game_name, description) VALUES ('Game A', 'A fun game')")
    cursor.execute("INSERT INTO leaderboard (game_id, player_name, score, rank) VALUES (1, 'Player1', 100, 1)")
    cursor.execute("INSERT INTO leaderboard (game_id, player_name, score, rank) VALUES (1, 'Player2', 90, 2)")
    cursor.execute("INSERT INTO leaderboard (game_id, player_name, score, rank) VALUES (1, 'Player3', 80, 3)")

    conn.commit()
    return conn, cursor

def test_get_leaderboard_ordered(setup_database):
    conn, cursor = setup_database

    # Call the function to get the leaderboard for game_id 1
    leaderboard = app.test_get_leaderboard_data(1)
    #leaderboard = app.get_leaderboard_data(1)

    # Assert the leaderboard is ordered correctly by rank (lowest rank first)
    assert leaderboard[0] == (1, 'Player1', 100)  # Player1 should have rank 1
    assert leaderboard[1] == (2, 'Player2', 90)  # Player2 should have rank 2
    assert leaderboard[2] == (3, 'Player3', 80)  # Player3 should have rank 3

def test_unique_rank_1(setup_database):
    conn, cursor = setup_database

    # Attempt to insert a second player with rank 1
    cursor.execute("INSERT INTO leaderboard (game_id, player_name, score, rank) VALUES (1, 'Player4', 95, 1)")
    conn.commit()

    # Fetch the leaderboard
    leaderboard = app.test_get_leaderboard_data(1)
    #leaderboard = app.get_leaderboard_data(1)

    # Assert only one player has rank 1
    rank_1_players = [player for player in leaderboard if player[0] == 1]
    assert len(rank_1_players) == 1  # There should only be one player with rank 1

    # Clean up: Delete player 4 to reset the data
    cursor.execute("DELETE FROM leaderboard WHERE player_name = 'Player4'")
    conn.commit()

def test_correct_data_for_players(setup_database):
    conn, cursor = setup_database

    # Fetch the leaderboard
    leaderboard = app.test_get_leaderboard_data(1)
    #leaderboard = app.get_leaderboard_data(1)

    # Assert the player names, scores, and ranks are correct
    assert leaderboard[0] == (1, 'Player1', 100)
    assert leaderboard[1] == (2, 'Player2', 90)
    assert leaderboard[2] == (3, 'Player3', 80)

    # Clean up database connection
    conn.close()
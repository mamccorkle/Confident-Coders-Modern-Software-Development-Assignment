# App Description

> Leaderboard App is an application that will allow you to see the top scores and rankings of popular games and users from around the world! This application will use Pythons Flask Framework and the Jinja v2 templating engine and SQLite as database storage.

# Feature List

> Add/Remove Games
> Add/Remove Scores

# Required Features

> (Must-have for minimum functionality)

> Add/Remove Games
> Add/Remove Scores

# Should Have Features

> (Adds more value but not critical)

# Nice to Have Features

> Graphic Images / Site-wide Themes

# User Stories

> Who is using the app and what they can do (e.g., “As a quiz creator, I want to add questions so others can take my quiz”).

> As a player, I would like to add my scores
> As a player, I would like to add the game I like to play that is not listed
> As a player, I would like to edit my scores
> As a player, I would like to edit my scores

# Database Schema (ERD)

> Tables, their columns, and relationships.

```mermaid
erDiagram
    GAMES {
        INTEGER game_id PK
        STRING game_name
        STRING description
    }
    LEADERBOARD {
        INTEGER leaderboard_id PK
        INTEGER game_id FK
        STRING player_name
        INTEGER score
        INTEGER rank
    }

    GAMES ||--o| LEADERBOARD: "has"
```

# User Flow Diagram

```mermaid
flowchart TD  
    A[Home Page] --> B[Select Game]
    B --> C[View Game Details]
    C --> F[Return to Home Page]
    C --> D[View Leaderboard]
    B --> D
    D --> G[Add Stats]
    D --> F[Return to Home Page]
    B --> E[Delete Game]
```

# List of Endpoints

| Route                      | Description                                | Method     | Input                               | Output                               
|----------------------------|--------------------------------------------|------------|-------------------------------------|--------------------------------------
| /                          | Main landing page                          | GET / POST | N\A                                 | render_template('index.html')        
| /leaderboard/<game_name>   | Stats for a given game                     | GET / POST | game_name, player_name, score, rank | render_template('leaderboard.html')  
| /game/<int:game_id>        | Route to a games details page              | GET / POST | game_id                             | render_template('game_details.html') 
| /add_game                  | Add a new game to the database             | GET / POST | game_name, description              | URL Redirect(Home)                   
| /delete_game/<int:game_id> | Delete the game selected from the database | POST       | game_id                             | URL Redirect(Home)
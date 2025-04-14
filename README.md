# Project name
> Leaderboard App is an application that will allow you to see the top scores and rankings of popular games and users from around the world! This application will use Pythons Flask Framework and the Jinja v2 templating engine and SQLite as database storage.and a short description

# Team:<br/>
> ## Confident Coders<br/>
> 
> &nbsp;&nbsp;Team Members:<br/>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Carson Alonzo<br/>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Estefania Ramirez<br/>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Mark McCorkle<br/>

# Software:<br/>
> &nbsp;&nbsp;&nbsp;&nbsp;Python<br/>
> &nbsp;&nbsp;&nbsp;&nbsp;PyCharm

# Framework(s):<br/>
> &nbsp;&nbsp;&nbsp;&nbsp;Flask<br/>
> &nbsp;&nbsp;&nbsp;&nbsp;Jinja2

# Database:<br />
> SQLite

# Python Dependencies:<br />
> Flask==3.1.0
>   - blinker [required: >=1.9, installed: 1.9.0]
>   - click [required: >=8.1.3, installed: 8.1.8]
>     - colorama [required: Any, installed: 0.4.6]
>   - itsdangerous [required: >=2.2, installed: 2.2.0]
>   - Jinja2 [required: >=3.1.2, installed: 3.1.6]
>     - MarkupSafe [required: >=2.0, installed: 3.0.2]
>   - Werkzeug [required: >=3.1, installed: 3.1.3]
>     - MarkupSafe [required: >=2.1.1, installed: 3.0.2]

# Setup instructions
> [!NOTE]  
> This app requires both Python, Flask, and PIP to run. The following instructions will guide you through this process:

> ## 1. Install Python
> 
> ### For Windows:
> 1. **Download Python:**
>    - Go to the official [Python download page](https://www.python.org/downloads/).
>    - Click on the "Download Python" button for the latest version.
> 
> 2. **Run the Installer:**
>    - Once the Python installer is downloaded, run it.
>    - **Important:** Make sure to check the box that says **"Add Python to PATH"** before clicking "Install Now."
>    - Follow the on-screen instructions to complete the installation.
> 
> 3. **Verify Installation:**
>    - Open the Command Prompt (`Win + R`, type `cmd`, and press Enter).
>    - Type `python --version` and press Enter. You should see the Python version installed, like `Python 3.x.x`.
> 
> ### For macOS:
> 1. **Install Homebrew (if not already installed):**
>    - Open Terminal and run the following command:
>      ```bash
>      /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
>      ```
> 
> 2. **Install Python:**
>    - After Homebrew is installed, you can install Python by running:
>      ```bash
>      brew install python
>      ```
> 
> 3. **Verify Installation:**
>    - Type `python3 --version` in the Terminal to verify that Python was installed.
> 
> ### For Linux:
> 1. **Use the Package Manager:**
>    - For Ubuntu/Debian-based systems, use the following commands:
>      ```bash
>      sudo apt update
>      sudo apt install python3
>      ```
>    - For Red Hat/Fedora-based systems:
>      ```bash
>      sudo dnf install python3
>      ```
> 
> 2. **Verify Installation:**
>    - Run `python3 --version` to verify that Python was installed.
> 
> ---
> 
> ## 2. Install pip (Python Package Installer)
> 
> `pip` is usually installed automatically with Python (for Python 3.4 and above), but if it's missing, you can install it manually:
> 
> ### For Windows/macOS/Linux:
> 1. Download `get-pip.py` from [this link](https://bootstrap.pypa.io/get-pip.py).
> 2. Open the terminal or command prompt in the folder where you downloaded `get-pip.py`.
> 3. Run the following command:
>    ```bash
>    python get-pip.py
> 
> ## 3. Set up a Virtual Environment (Recommended)
> 
> It's a good practice to create a virtual environment for your app to avoid conflicts between packages in your global Python installation.
> 
> ### 1. Create a Virtual Environment:
>    - Navigate to the folder where your app is located, and run the following command:
>      ```bash
>      python -m venv myenv
>      ```
>      Replace `myenv` with your desired virtual environment name.
> 
> ### 2. Activate the Virtual Environment:
>    - For **Windows**:
>      ```bash
>      myenv\Scripts\activate
>      ```
>    - For **macOS/Linux**:
>      ```bash
>      source myenv/bin/activate
>      ```
> 
> ### 3. Deactivate Virtual Environment:
>    - You can deactivate the virtual environment by running:
>      ```bash
>      deactivate
>      ```
> 
> ## 4. Install Required Packages Using `requirements.txt`
> 
> If your app has a `requirements.txt` file (which lists all the packages your app needs), you can install all the necessary dependencies with a single command.
> 
> ### 1. Navigate to Your Project Folder:
>    - Use the terminal or command prompt to navigate to the folder that contains the `requirements.txt` file.
> 
> ### 2. Install Packages:
>    - Ensure you have your virtual environment activated (if you're using one).
>    - Run the following command to install the packages:
>      ```bash
>      pip install -r requirements.txt
>      ```
> 
>    This will automatically download and install all the required packages listed in the `requirements.txt` file.
> 
> ## 5. Run the Application
> 
> Once you've installed the necessary packages, you can usually run your app with the following command:
> 
> ### 1. Run the Python Script:
>    - For Python scripts (e.g., `app.py`), you can run:
>      ```bash
>      python app.py
>      ```
> 
> This will start your application, assuming all dependencies are installed and the environment is properly set up.

# Project Structure:
```
├── flask/
    ├── app.py                          # Main Program
    ├── MSD-P01-LeaderBoard.sqlite      # Database
    ├── planning.md                     # Planning Document
    ├── README.md                       # Instructions/Intro
    ├── requirements.txt                # Python Dependencies
    ├── templates/
    │   ├── index.html                  # Main Page
    │   ├── game_details.html           # Game Details Page
    │   ├── leaderboard.html            # Leaderboard(Score) Page
    └── static/
        └── style.css                   # Sitewide Styles
        └── 10954552.jpg                # Header Image
        └── favicon.ico                 # Browser Tab Icon
        
```

# How to use the app
> * Once you arrive at the site you wil be presented with a list of games (presented as cards)
>  > Additionally, a user can add a new game by adding the following details (bottom of page):<br /><br />&nbsp;&nbsp;- Game Name<br />&nbsp;&nbsp;- Game Description<br />
> * For each game, click the button "View Game Details" to see the games description
> * For each game, click the button "View Leaderboard" to see the leaderboard for the selected game
>  > Additionally, a user can add new stats by adding the following details (bottom of page):<br /><br />&nbsp;&nbsp;- Player Name<br />&nbsp;&nbsp;- Score<br />&nbsp;&nbsp;- Rank<br />

# Screenshots

<img src="https://github.com/Cmalonzo1/Confident-Coders-Modern-Software-Development-Assignment/blob/master/Home.png">
<img src="https://github.com/Cmalonzo1/Confident-Coders-Modern-Software-Development-Assignment/blob/master/GameDetails.png">
<img src="https://github.com/Cmalonzo1/Confident-Coders-Modern-Software-Development-Assignment/blob/master/Leaderboard.png">


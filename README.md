# Twitter Search Dashboard

This is a simple **Twitter Search Dashboard** built using **Django** and **Bootstrap**. The dashboard allows users to search for tweets on Twitter using specific keywords or hashtags. The results are displayed in a user-friendly interface, leveraging the **Twitter API** for fetching tweet data.

## Features
- Search tweets by keyword or hashtag.
- Display tweet details such as username, text, likes, and retweets.
- Built with **Django** for backend and **Bootstrap** for frontend styling.
- User-friendly and responsive design.

## Technologies Used
- **Backend**: Django
- **Frontend**: HTML, CSS (Bootstrap)
- **API**: Twitter API (for fetching tweets)
- **Database**: SQLite 
- **Others**: JavaScript (for dynamic search functionality)

## Installation

Follow these steps to set up the project on your local machine.

### Prerequisites
1. Install Python (>= 3.7) from [python.org](https://www.python.org/).
2. Install **Git** for version control (optional, but recommended).

### Step 1: Clone the Repository
First, clone the repository to your local machine:

git clone https://github.com/your-username/twitter-search-dashboard.git
Navigate to the project folder:
cd twitter-search-dashboard

### Step 2: Set Up a Virtual Environment
Create and activate a Python virtual environment:


python -m venv env
Activate the environment:

On Windows:

env\Scripts\activate
On macOS/Linux:

source env/bin/activate

### Step 3: Install Dependencies
pip install -r requirements.txt

### Step 4: Set Up Twitter API Keys
Create a Twitter Developer account at the Twitter Developer Portal.
Set up a new app and obtain the following credentials:
API Key
API Secret Key
Access Token
Access Token Secret

TWITTER_API_KEY = 'your_api_key'

TWITTER_API_SECRET_KEY = 'your_api_secret_key'

TWITTER_ACCESS_TOKEN = 'your_access_token'

TWITTER_ACCESS_TOKEN_SECRET = 'your_access_token_secret'

### Step 5: Run Database Migrations
python manage.py migrate

### Step 6: Start the Development Server
python manage.py runserver
Open your browser and navigate to:
http://127.0.0.1:8000/


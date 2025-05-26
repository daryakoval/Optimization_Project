import os
from dotenv import load_dotenv
# Load environment variables (for API keys)
load_dotenv()

# Define a sample city to analyze
CITY = "Seattle, WA, USA"
# Alternative cities to try: "Portland, OR, USA", "San Francisco, CA, USA", "Austin, TX, USA"

# Budget constraint ($)
MAX_BUDGET = 1000000  # $1M budget for new stations
STATION_COST = 100000  # Cost per station

# Coverage parameters
MAX_COVERAGE_DISTANCE = 1000  # meters
MIN_DISTANCE_BETWEEN_STATIONS = 500  # meters

# Number of candidate locations to consider
NUM_CANDIDATE_LOCATIONS = 50

# NREL API key - Get from https://developer.nrel.gov/signup/
NREL_API_KEY = os.getenv("NREL_API_KEY", "DEMO_KEY")

# Census API key - Get from https://api.census.gov/data/key_signup.html
CENSUS_API_KEY = os.getenv("CENSUS_API_KEY", "")
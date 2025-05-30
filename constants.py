import os
from dotenv import load_dotenv
# Load environment variables (for API keys)
load_dotenv()

SEED = 42   # good for seatle - 15, portland - 35, austin - 47
# Define a sample city to analyze
CITY = "Chicago, IL, USA"
# Alternative cities to try: "Seattle, WA, USA", "Portland, OR, USA", "San Francisco, CA, USA", "Austin, TX, USA", "Los Angeles, CA, USA", "Chicago, IL, USA"

POPULATION_POINTS = 1000
# Budget constraint ($)
MAX_BUDGET = 10000000  # $10M budget for new stations
BASE_STATION_COST = 100000  # Cost per station

# Coverage parameters
MAX_COVERAGE_DISTANCE = 1000  # meters
MIN_DISTANCE_BETWEEN_STATIONS = 500  # meters

# Number of candidate locations to consider
NUM_CANDIDATE_LOCATIONS = 50

# NREL API key - Get from https://developer.nrel.gov/signup/
NREL_API_KEY = os.getenv("NREL_API_KEY", "g9a48djfLHVAyaM0dpcAHa7ocScZTfWnZUOrbCgf")

# Census API key - Get from https://api.census.gov/data/key_signup.html
CENSUS_API_KEY = os.getenv("CENSUS_API_KEY", "e370861af9700b96c64c482d989b412332513405")
import os
from dotenv import load_dotenv
# Load environment variables (for API keys)
load_dotenv()

SEED = 17   
CITY = "Chicago, IL, USA"
# Alternative cities to try: "Seattle, WA, USA", "Portland, OR, USA", "San Francisco, CA, USA", "Austin, TX, USA", "Los Angeles, CA, USA", "Chicago, IL, USA"

POPULATION_POINTS = 200
MAX_BUDGET = 1000000  
BASE_STATION_COST = 100000 

MAX_COVERAGE_DISTANCE = 1000  
MIN_DISTANCE_BETWEEN_STATIONS = 500  

NUM_CANDIDATE_LOCATIONS = 50

# NREL API key - Get from https://developer.nrel.gov/signup/
NREL_API_KEY = os.getenv("NREL_API_KEY", "g9a48djfLHVAyaM0dpcAHa7ocScZTfWnZUOrbCgf")

# Census API key - Get from https://api.census.gov/data/key_signup.html
CENSUS_API_KEY = os.getenv("CENSUS_API_KEY", "e370861af9700b96c64c482d989b412332513405")
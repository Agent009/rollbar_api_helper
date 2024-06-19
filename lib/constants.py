from dotenv import load_dotenv, find_dotenv
import os

# Load environment variables from .env file even if not in the current directory
load_dotenv(find_dotenv())
# Ensure environment variables are loaded
project_read_token = os.getenv('ROLLBAR_PROJECT_READ_TOKEN')
project_write_token = os.getenv('ROLLBAR_PROJECT_WRITE_TOKEN')

# We can't run the app with missing configurations.
if not project_read_token or not project_write_token:
    raise EnvironmentError(
        'Required environment variables are missing. '
        'Please copy/paste the .env.sample file and set your variables in the .env file.'
    )

# API Base URL
base_url = 'https://api.rollbar.com/api/1/'
# Default limit per page for pagination
default_limit_per_page = 100
# Header key for access tokens
access_token_header_key = 'X-Rollbar-Access-Token'

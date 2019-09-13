import os

# settings.py
from dotenv import load_dotenv
load_dotenv()



SECRET_KEY = os.getenv("EMAIL")
print(SECRET_KEY)
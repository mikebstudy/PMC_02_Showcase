import os
from dotenv import load_dotenv

load_dotenv(override=True)
pw = os.getenv("PMC_02_SHOWCASE_PW")
print(pw)


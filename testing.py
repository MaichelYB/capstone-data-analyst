from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.environ['TOKEN']

print(f'Length of TOKEN: {len(TOKEN)} characters')
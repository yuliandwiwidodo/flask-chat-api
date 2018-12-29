import os
from dotenv import load_dotenv
from pathlib import Path 

load_dotenv()
load_dotenv(verbose=True)
env_path = Path('../../') / '.env'
dotenv = load_dotenv(dotenv_path=env_path)



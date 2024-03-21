import sys
import os

# Add the 'backend' directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from config import Config


# Now you can import config.py

# Use Config class as needed
def foo():

    config = Config()
    print(config.SQLALCHEMY_DATABASE_URL)


if __name__ == '__main__':
    foo()

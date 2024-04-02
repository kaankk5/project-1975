import sys
import os


from backend.app.config import Settings


# Now you can import config.py

# Use Config class as needed
def foo():
    config = Settings()
    print(config.SQLALCHEMY_DATABASE_URL)


if __name__ == '__main__':
    foo()

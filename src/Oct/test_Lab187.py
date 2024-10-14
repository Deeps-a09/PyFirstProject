# PASSWORD - I store the pwd in the framework ?
# No, we will create environment variable
# env file we will create
# Env File-> .env(dot.env)
# How do you store your password or credentials in the framework
# pip install python- dotenv(.env)

from dotenv import load_dotenv
import os

def test_update_req():
    load_dotenv()
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")
    print(username)
    print(password)
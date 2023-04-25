import os


class Config:
    browser = os.getenv('TEST_BROWSER', "chrome")  # will take browser from env variables or use "chrome" as default
    app_host = "http://uitestingplayground.com/"

    api_host = "http://localhost:3000"



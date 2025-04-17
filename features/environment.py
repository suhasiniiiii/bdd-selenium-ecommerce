from selenium import webdriver
from dotenv import load_dotenv
import os

def before_scenario(context, scenario):
    load_dotenv()
    options = webdriver.ChromeOptions()
    #options.add_argument("--headless=new")  # Optional, remove to see browser
    context.driver = webdriver.Chrome(options=options)
    context.driver.maximize_window()
    context.base_url = os.getenv("BASE_URL")

def after_scenario(context, scenario):
    context.driver.quit()

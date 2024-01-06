from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Chrome()
actions = ActionChains(browser)

browser.get("https://twitter.com/")
time.sleep(3) # wait for page to load

# Locate and click on the login button
log_in = browser.find_element(By.XPATH, "/html/body/div/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[5]/a/div")
log_in.click()

# Wait for the login page to load
time.sleep(5)                                           

# Find the username input field and enter the username
username = browser.find_element(By.TAG_NAME, 'input')
username.send_keys("username")
time.sleep(5)

# Locate and click the 'Next' button
next_button = browser.find_element(By.XPATH,"//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]")
next_button.click()
time.sleep(5)

# Find the password input field and enter the password
pasword = browser.find_element(By.NAME, 'password')
pasword.send_keys("password")
time.sleep(3)

# Locate and click the 'Log in' button
login = browser.find_element(By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div")
login.click()
time.sleep(5)

# Wait for the main X page to load after login
################################################################

# Locate the search button and the search input field
searchButton = browser.find_element(By.XPATH, '//a[@aria-label="Search and explore"]')
searchArea = browser.find_element(By.TAG_NAME, 'input')

# Click the search button
searchButton.click()
time.sleep(7)
# Refresh the page to ensure search area is active
browser.refresh()
time.sleep(7)
# Find the search input field again and enter the search term
searchArea = browser.find_element(By.TAG_NAME, 'input')
searchArea.send_keys("robotics news") #you can change input field with text you want to search
time.sleep(5)
# Press Enter to start the search
actions.send_keys(Keys.ENTER)
actions.perform()
time.sleep(5)

# Scroll down the page and load more tweets
lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match=False
while(match==False):
    lastCount = lenOfPage
    time.sleep(3)
    lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    if lastCount == lenOfPage:
        match=True
time.sleep(5)

# Collect tweets from the page
tweets = []
elements = browser.find_elements(By.CSS_SELECTOR, 'div[data-testid="tweetText"]')
for element in elements:
    tweets.append(element.text)

tweetCount = 1

# Write the collected tweets to a text file
with open("tweets.txt","w",encoding = "UTF-8") as file:
    for tweet in tweets:
        file.write(str(tweetCount) + ".\n" + tweet + "\n")
        file.write("**************************\n")
        tweetCount += 1

# Close the browser
browser.close()

# <ins>Web_Scraping_X_Feed_Selenium</ins>

This project will provide practical insights into handling dynamic web content, enabling you to extract valuable data from one of the world’s most active online communities.

## <ins>Selenium</ins>
Selenium simply automates web browsers. It is an open-source suite of tools and libraries that is used for browser automation.

### <ins>Importance of Selenium</ins>
* In software development, it’s important to test things quickly and accurately. Doing tests by hand takes a lot of time and sometimes people make mistakes. Using Selenium Automation for testing, helps us do these tests faster and more correctly. This means we make fewer mistakes and get more reliable results every time we test.

* When we’re looking at websites, we want to find the information that we need as fast as possible and automating this process can be achievable with Selenium.

* A key feature we’ll explore is the reusability of scripts. By altering just the text input in a single script, we can efficiently collect a wide range of data from X. This showcases how one well-designed script can be versatile and adaptable for different data gathering needs.

>For more information related with Selenium you can check this [unofficial documentation](https://selenium-python.readthedocs.io/index.html)

You can install Selenium with this code line.
```python
pip install selenium
```

Selenium requires a driver to interface with the chosen browser. You can check the following websites for spesific driver you wanted to use.
* `Chrome` https://sites.google.com/chromium.org/driver/?source=post_page-----c10ceb4b1a12--------------------------------
  
* `Edge` https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/?source=post_page-----c10ceb4b1a12--------------------------------&form=MA13LH

* `Firefox` https://github.com/mozilla/geckodriver/releases?source=post_page-----c10ceb4b1a12--------------------------------

* `Safari` https://webkit.org/blog/6900/webdriver-support-in-safari-10/?source=post_page-----c10ceb4b1a12--------------------------------

for more information you can check [WebDriver | Selenium](https://www.selenium.dev/documentation/webdriver/) which is official documentation.

## <ins>Sample Code</ins>
With the following sample code I will be demonstrating how to obtain data from YouTube
```python
from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up the Chrome WebDriver
driver = webdriver.Chrome()

# Navigate to YouTube's top 50 global song page
driver.get("https://www.youtube.com/results?search_query=top+50+song+global+")

# Find all the links and names on the page
links = driver.find_elements(By.TAG_NAME, 'a')
names = driver.find_elements(By.TAG_NAME, 'yt-formatted-string')

videos = zip(names, links)
# Print the href attribute and title of each link
for name, link in videos:
    href = link.get_attribute('href')
    v_name = name.text

    if href and v_name:
        print("Name: {} Link: {}\n".format(v_name, href))

# Close the browser
driver.quit()
```
With this simple code I can obtain top 50 global song related data of youtube with its name and video link, I only printed them for now but we can store them in various ways from text to excel.

![image](https://github.com/yavuzCodiin/Web_Scraping_X_Feed_Selenium/assets/82445309/f13ef271-b6c2-47cb-aa04-2ea48ef4e8ab)

In the [`Web_Scraping_IMDB_Most_Popular_Movies`](https://github.com/yavuzCodiin/Web_Scraping_IMDB_Most_Popular_Movies) I explained basic html structure you can go and check how website is built and how we can interact with it.

## <ins>Finding Elements: XPath and CSS Selectors</ins>
XPath and CSS Selectors are two ways to find and select specific parts of a web page (like a search bar, button, or a piece of information) so we can interact with them or get information from them.

### <ins>What is XPath?</ins>
It’s a way to navigate through the HTML structure. It allows us to find elements by specifying a path through the structure. For example, we can tell Selenium to find a button and click it inside a certain section of the page.

![image](https://github.com/yavuzCodiin/Web_Scraping_X_Feed_Selenium/assets/82445309/a0fc7e6b-2bdc-4ab2-ab1e-91fc2385bef7)

![image](https://github.com/yavuzCodiin/Web_Scraping_X_Feed_Selenium/assets/82445309/f6e6fc88-acef-446d-9b87-383b27f777e8)

So from here you can select `Copy XPath` to copy it.

As a result, we get something like this:
```XML
//*[@id="id__se3bnt9344"]/span
```
### <ins>What is CSS Selector?</ins>
This is another way to find elements, but it uses the styling information of the page. For example, if you know a button has a certain class name used for its style, you can tell Selenium to find the button using that class name.

## | <ins>Importing Libraries</ins>
```python
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
```

## | <ins>Initialize the Chrome WebDriver & Open X’s homepage</ins>
```python
browser = webdriver.Chrome()
actions = ActionChains(browser)

browser.get("https://twitter.com/")
time.sleep(3) # wait for page to load
```

## | <ins>Locate Elements on the Login Page and Enter X</ins>
```python
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
```

## | <ins>Locate Elements on the Feed Page and Send Input</ins>
```python
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
```

## | <ins>Scrolling Through Content Page</ins>
```python
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
```

## | <ins>Collecting Tweets Through Content Page</ins>
```python
# Collect tweets from the page
tweets = []
elements = browser.find_elements(By.CSS_SELECTOR, 'div[data-testid="tweetText"]')
for element in elements:
    tweets.append(element.text)

tweetCount = 1
```

## | <ins>Writing Tweets To a Text File and Closing Browser</ins>
```python
# Write the collected tweets to a text file
with open("tweets.txt","w",encoding = "UTF-8") as file:
    for tweet in tweets:
        file.write(str(tweetCount) + ".\n" + tweet + "\n")
        file.write("**************************\n")
        tweetCount += 1

# Close the browser
browser.close()
```

## <ins>Project Video</ins>

[![Project Tweet Scraper](https://img.youtube.com/vi/gw5one6ocyo/0.jpg)](https://youtu.be/gw5one6ocyo "Project Tweet Scraper")

## <ins>Result</ins>

![image](https://github.com/yavuzCodiin/Web_Scraping_X_Feed_Selenium/assets/82445309/6881e7ef-11d4-4806-9b6b-48b186dda986)

If you want to understand this in a more simpler language you can check my Medium writing published on `Level Up Coding`

LINK => https://levelup.gitconnected.com/web-scraping-series-part-ii-x-feed-selenium-c10ceb4b1a12













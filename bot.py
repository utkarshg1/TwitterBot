from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import random

#Sleep Time
st = 4

#Login To Twitter page
driver = webdriver.Chrome()
driver.get("https://twitter.com/i/flow/login")
time.sleep(st)

#Entering Username
username = driver.find_element(By.TAG_NAME, "input")
username.send_keys("EmmaWin1995")

#Clicking Next button
all_buttons = driver.find_elements(By.XPATH, "//div[@role='button']")
all_buttons[-2].click()
time.sleep(st)

#Entering Password
password = driver.find_element(By.XPATH,"//input[@type='password']")
password.send_keys("Example@1234")
time.sleep(st)

#Click Login Button
login = driver.find_elements(By.XPATH, "//div[@role='button']")
login[-1].click()
time.sleep(st)

#Query search
keyword = "cat"
keyword = keyword.lower()
words = keyword.split(" ")
if len(words)>1:
    querystring="%20".join(words)
else:
    querystring=keyword
print(querystring)

driver.get("https://twitter.com/search?q="+querystring+"&src=typed_query&f=top")
time.sleep(st)

messages = ['Wow!','Incredible!!!','Amaziiinggg!!','So Cute!','I Like It!','This is awesome!', 'Fantastic!!!','Cutie Pie!','Sweet!!']

n_scrolls = 3

for scroll in range(n_scrolls):
    #Liking the post
    like=driver.find_elements(By.XPATH,"//span[@data-testid='app-text-transition-container']")
    driver.execute_script("arguments[0].click();",like[2])
    time.sleep(st)

    #Clicking on Retweet Button
    retweet=driver.find_elements(By.XPATH,"//span[@data-testid='app-text-transition-container']")
    driver.execute_script("arguments[0].click();",retweet[1])
    time.sleep(st)

    #Clicking on quote tweet
    quote_tweet = driver.find_element(By.XPATH,"//a[@role='menuitem']")
    quote_tweet.click()
    time.sleep(st)

    #Writing the quote
    quote = driver.find_element(By.XPATH,"//div[contains(@class,'public-DraftStyleDefault-block')]")
    quote.send_keys(random.choice(messages))
    time.sleep(st)

    #Clicking tweet button
    tweet = driver.find_element(By.XPATH,"//div[@data-testid='tweetButton']")
    tweet.click()
    time.sleep(st)

    #Scrolling
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    time.sleep(st)






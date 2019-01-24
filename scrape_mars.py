from splinter import Browser
from bs4 import BeautifulSoup
import time

def init_browser():
    # @note: replace the path with your actial path to the chromedriver
    # possibly /usr/local/bin/chromedriver if your running osx
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    browser = init_browser()
    mars_listings={}

    url= 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url)

    time.sleep(5)

    html = browser.html
    soup = BeautifulSoup(html,"html.parser")

    mars_listings["news_title"] = soup.find('div', class_='content_title').get_text()
    mars_listings["news_p"] = soup.find('div', class_='article_teaser_body').get_text()
    #listings["headline"] = soup.find("a", class_="result-title").get_text()
    #listings["price"] = soup.find("span", class_="result-price").get_text()
    #listings["hood"] = soup.find("span", class_="result-hood").get_text()

    # Close the browser after scraping
    browser.quit()

    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    
    time.sleep(5)

    html = browser.html
    soup1 = BeautifulSoup(html,"html.parser")

    featured_image_url= soup1.find('article', class_='carousel_item')
    #mars_listings["featured_image_url"] = featured_image_url = 'https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA16225_hires.jpg'

    # Close the browser after scraping
    browser.quit()

    # Url of twitter page to be scraped
    url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url)

    html = browser.html
    soup2 = BeautifulSoup(html,"html.parser")

    time.sleep(5)

    mars_listings["mars_weather"] = soup2.find('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text')

    # Close the browser after scraping
    browser.quit()

    url = 'http://space-facts.com/mars/'
    browser.visit(url)

    time.sleep(5)

    html = browser.html
    soup3 = BeautifulSoup(html,"html.parser")

    mars_listings["mars_tableData"] = soup3.find('table', class_='tablepress tablepress-id-mars')

    # Close the browser after scraping
    browser.quit()

    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    
    time.sleep(5)

    html = browser.html
    soup4 = BeautifulSoup(html,"html.parser")

    mars_listings["mars_hemisphere1"] = soup3.find('table', class_='tablepress tablepress-id-mars')


    # Close the browser after scraping
    browser.quit()


    return mars_listings

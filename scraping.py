# import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import datetime as dt

def scrape_all():
    # initiate headless driver for deployment
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)

    news_title, news_paragraph = mars_news(browser)
    hemisphere_img_urls = mars_hemispheres(browser)

    # Run all scraping funcitons and store results in dictionsary
    data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image(browser),
        "facts": mars_facts(),
        "hemispheres": hemisphere_img_urls,
        "last_modified": dt.datetime.now()        
        }

    # stop webdriver and return data
    browser.quit()
    return data


def mars_news(browser):
    #Scrape Mars News
    #Visit Nasa news site
    url = 'https://redplanetscience.com'
    browser.visit(url)
    # optional delay for loading the page
    browser.is_element_present_by_css('div.list_text', wait_time=1)

    # set up HTML parser
    html = browser.html
    news_soup = soup(html, 'html.parser')

    # add try-except for error handling
    try:
        slide_elem = news_soup.select_one('div.list_text')
        # using parent element to find the firs 'a' tage and save it
        news_title = slide_elem.find('div', class_='content_title').get_text()
        # fusing parent element to find the paragraph text
        news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
        
    except AttributeError:
        return None, None

    return news_title, news_p

# ### Featured Images Scrape
def featured_image(browser):
    # Visit URL
    url = 'https://spaceimages-mars.com'
    browser.visit(url)

    # find and click the full image button
    full_image_elem = browser.find_by_tag('button')[1]
    full_image_elem.click()

    # parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')

    try:
        # find the relative image url
        img_url_rel = img_soup.find('img', class_='headerimage').get('src')
    except AttributeError:
        return None

    img_url = f'https://spaceimages-mars.com/{img_url_rel}'

    return img_url
    

# ### Scraping for facts
def mars_facts():
    
    try:
        # scrape to find capture the table
        df = pd.read_html('https://galaxyfacts-mars.com')[0]
    except BaseException:
        return None
    
    df.columns=['description', 'Mars', 'Earth']
    df.set_index('description', inplace=True)

    return df.to_html()

# Scrape for hemisphere data
def mars_hemispheres(browser):
    # 1. Use browser to visit the URL 
    url = 'https://marshemispheres.com/'
    browser.visit(url)

    html = browser.html
    hemi_soup = soup(html, 'html.parser')

    # 2. Create a list to hold the images and titles.
    hemisphere_img_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
    for i in range(4):
        hemispheres = {}
        browser.find_by_css('a.product-item h3')[i].click()
        element = browser.links.find_by_text('Sample').first
        img_url = element['href']
        title = browser.find_by_css('h2.title').text
        hemispheres['img_url'] = img_url
        hemispheres['title'] = title
        hemisphere_img_urls.append(hemispheres)
        browser.back()

    # 5. Quit the browser
    #browser.quit()

    return hemisphere_img_urls

if __name__ == "__main__":
    # if running as script, print scraped data
    print(scrape_all())




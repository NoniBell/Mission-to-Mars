from splinter import Browser
from bs4 import BeautfiulSoup as bs
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager

def init_browser():
     executable_path = {'executable_path': "/usr/local/bin/chromedriver"}
     browser = Browser('chrome', **executable_path, headless=False)
     return browser


def scrape():
    browser = init_browser()
    mars_dict = {}

    #MARS NEWS
    
    #create url variable for website
    mars_url = "https://redplanetscience.com/#"
    #visit url
    browser.visit(mars_url)
    #create html object and parse with bs
    mars_html = browser.html
    mars_soup = bs(mars_html, 'html.parser')

    #find the first news title and paragraph body
    #save to variables
    news_title = mars_soup.find('div', class_='content_title').text
    news_text = mars_soup.find('div', class_='article_teaser_body').text

    #add variables to mars_dict
    mars_dict['news_title'] = news_title
    mars_dict['news_text'] = news_text

    #JPL MARS SPACE IMAGES - FEATURED IMAGE

    #create url for website
    #visit url
    #create html object and parse with bs
    space_url = "https://spaceimages-mars.com/"
    browser.visit(space_url)
    space_html = browser.html
    space_soup = bs(space_html, 'html.parser')

    #find the url for the featured image
    #save to variable
    pull = space_soup.find('img', class_='headerimage fade-in')
    featured_image_url = space_url + pull.get('src')

    #add variables to mars_dict
    mars_dict['featured_image'] = featured_image_url

    #MARS FACTS

    #creat url for website
    #read url with pandas
    facts_url = "https://galaxyfacts-mars.com/"
    facts_df = pd.read_html(facts_url)
    #set df to first table pull
    facts_df = facts_df[0]
    #set column names
    facts_df.columns = ['Facts', 'Mars', 'Earth']
    #drop top row, set index to first column
    facts_df = facts_df.drop([0])
    facts_df = facts_df.set_index('Facts')
    #convert df to html string
    facts_html = facts_df.to_html()

    #add html to mars_dict
    mars_dict['facts'] = facts_html

    #MARS HEMISPHERES
    #grab urls for all full res screenshots
    cerberus_url = "https://marshemispheres.com/cerberus.html"
    sch_url = "https://marshemispheres.com/schiaparelli.html"
    valles_url = "https://marshemispheres.com/valles.html"
    syrtis_url = "https://marshemispheres.com/syrtis.html"

    #visit urls and create html objects
    browser.visit(cerberus_url)
    cer_html = browser.html
    cer_soup = bs(cer_html, 'html.parser')

    browser.visit(sch_url)
    sch_html = browser.html
    sch_soup = bs(sch_html, 'html.parser')

    browser.visit(valles_url)
    valles_html = browser.html
    valles_soup = bs(valles_html, 'html.parser')

    browser.visit(syrtis_url)
    syrtis_html = browser.html
    syrtis_soup = bs(syrtis_html, 'html.parser')

    #create empty hem list
    hemisphere_image_urls = []

    #pull titles
    cer_title = cer_soup.find('h2').text
    sch_title = sch_soup.find('h2').text
    valles_title = valles_soup.find('h2').text
    syrtis_title = syrtis_soup.find('h2').text

    #pull img_urls
    cer_img = cer_soup.find('img', class_='wide-image').get('src')
    sch_img = sch_soup.find('img', class_='wide-image').get('src')
    valles_img = valles_soup.find('img', class_='wide-image').get('src')
    syrtis_img = syrtis_soup.find('img', class_='wide-image').get('src')

    #create dictionaries
    cer_dict = {'title': cer_title, 'url_img': cer_img}
    sch_dict = {'title': sch_title, 'url_img': sch_img}
    valles_dict = {'title': valles_title, 'url_img': valles_img}
    syrtis_dict = {'title': syrtis_title, 'url_img': syrtis_img}

    #append dicts to list
    hemisphere_image_urls.append(cer_dict)
    hemisphere_image_urls.append(sch_dict)
    hemisphere_image_urls.append(valles_dict)
    hemisphere_image_urls.append(syrtis_dict)

    #add hem list to mars_dict
    mars_dict['hemisphere_image_urls'] = hemisphere_image_urls

    return mars_dict

    browser.quit()




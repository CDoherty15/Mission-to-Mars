# Mission-to-Mars
Module 10: Mission to Mars - Web scraping with HTML/CSS

## Making a Mars Web App
We are helping a friend make a web app portfolio to hold information about Mars from multiple different sources. This app will be used to wright down recent and updated news and facts about mars. Since we only want the recent news facts and images showing, we need to fine tune our web scraping skills to only display that data. 
#### Scraping & Saving
- In the [mission_to_Mars_Challenge.ipynb](https://github.com/CDoherty15/Mission-to-Mars/blob/main/Mission_to_Mars_Challenge.ipynb) file, you will find all the code that we used to practice and edit our scraping tools to ensure we collected all the recent and correct information off the sites. 
- Once we knew that we collected all the correct information, it was time to export and downloand the jupyter notebook to a local file - [scraping.py](https://github.com/CDoherty15/Mission-to-Mars/blob/main/scraping.py). From here, we transformed our previous lines of codes into functions so that the code would run on all one command and more smoothly. 
- Next was to make sure that we saved the information gathered from the code into a mongo database to make sure it would display on our web app. We are able to run a Flask app and update our mongo database all on the same script of code, found here - [app.py](https://github.com/CDoherty15/Mission-to-Mars/blob/main/app.py).
#### Results
We then create and connect an html file to connect our app.py file, which runs our scraping.py file, to display our data in easy to read format. With all of the above steps completed properly, our web app will look like the following:
![mission_to_mars_app](https://user-images.githubusercontent.com/79118630/123860446-ea085800-d8f3-11eb-8136-b2696d4f2d94.png)
- The screenshot of the web app is slightly zoomed out to include the whole page. Displayed is the most recent featured news along with a featured image of mars. There is also a facts table that compares Earth to Mars and finally, at the bottom, there is a picture of all four hemispheres with their names. 
- Most importantly, there is a scrape button at the top to be pressed every so often to update the web app to stay up to date with recent mars news. 

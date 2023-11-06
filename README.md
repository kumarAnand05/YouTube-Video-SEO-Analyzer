# YouTube Video SEO Analyzer
<img align="right" width="100" height="100" src="https://github.com/kumarAnand05/YouTube-Video-SEO-Analyzer/assets/111251492/5ad34e9c-4318-406d-bb36-0ef4a8436255">
By Anand Kumar

## Features (As of Now)
* **Multiple Search Terms** : Can handle multiple search terms and analyse top video results for each query. 
* **Video Title SEO Analysis** : Check for most used keywords in title, average word usage and average length of title.
* **Video Description SEO Analysis** : Check for most used keywords in description, average length and word usage of description.
* **Basic NLP Implementation** :  Implements basic Natural Language Processing to analyse Title and Description


# Instructions
After you have downloaded the project files. Follow the insctructions below to setup your machine to make code functional.
## Downloading/Installing dependencies 
Of course you need [Python](https://www.python.org) and an IDE like [VSCode](https://code.visualstudio.com), [PyCharm](https://www.jetbrains.com/pycharm) etc. installed on your machine. Along with it you need to install/download some other packages on your machine which are mentioned below.

> Get a YouTube API Key (It has free quota):

If you already have your API key for YouTube Data API v3, that's great! If not, you can get one by following the instructions on the [Google Cloud Console](https://cloud.google.com/console) or search online for instructions.
Make sure you enable the YouTube Data API for your project.

> Install the Required Library:

You'll need to install the google-api-python-client library to interact with the YouTube Data API.
You can install it using pip, just run the command below in command prompt or terminal:

`pip install --upgrade google-api-python-client`

> Install NLTK

Run the command below in your command promt or terminal if you do not have NLTK library on your machine:

`pip install nltk`

###### Your machine is ready now!!!

Simply open the YouTube Video SEO Analyzer folder in your IDE and run the main.py file.
Enter the API key and other required input and wait for some time. Time to process will vary depending upon the number of search keywords that you have entered and the number of videos that you want to analyze.
Keep in mind that a single processing will make `v*v*q` requests to the api, where v is the number of videos that you want to analyse for each search query and q is the number of query that you have entered.

import os
import googleapiclient.discovery
import languageProcessing as lp
from collections import Counter


def provideKey():
    print('Enter your api key:')
    api_key = input()
    return api_key

def makeConnection(api_key):
    return googleapiclient.discovery.build('youtube', 'v3', developerKey=api_key)


title_words = []
description_words = []
exclusions = ['http', 'https', 'vs']


def startSearch(youtube, search_query,resCount):
    title_length = 0
    title_word_count = 0
    description_length = 0
    description_word_count = 0
    iterations = 0
    for query in search_query:
        search_term = query

        # Requesting videos
        request = youtube.search().list(q = search_term, type = 'video', part = 'snippet', maxResults = resCount)
        response = request.execute()
        video_ids = [search_result['id']['videoId'] for search_result in response.get('items', [])]
        for video_id in video_ids:
            video_request = youtube.videos().list(part = 'snippet,statistics', id=video_id)
            video_response = video_request.execute()
            if 'items' in video_response:
                video_info = video_response['items'][0]
                video_title = video_info['snippet']['title']
                video_description = video_info['snippet']['description']
                titles = lp.preprocess_text(video_title)
                description = lp.preprocess_text(video_description)

                title_word_count += len(titles)
                title_length += len(video_title)
                description_word_count += len(description)
                description_length += len(video_description)
                iterations+=1

                title_words.extend(titles)
                description_words.extend(description)
    publishFindings(title_words,description_words,exclusions, title_length, title_word_count, description_length, description_word_count, iterations)
    
    return

def publishFindings(title_words,description_words,exclusions, title_length, title_word_count, description_length, description_word_count, iterations):
    title_frequency = Counter(title_words)
    description_frequency = Counter(description_words)
    common_title_words = title_frequency.most_common()
    common_description_words = description_frequency.most_common()
    
    print('Analysis Report:\n\n')
    print(f"An average of {title_word_count/iterations} words were used with an average length of {title_length/iterations}\n")
    print(f"An average of {description_word_count/iterations} words were used with an average length of {description_length/iterations}\n\n")
    print('Common Keywords used in Title:\n')
    for word, frequency in common_title_words:
        if word not in exclusions and frequency>1:
            print(f'{word}: {frequency}')
    print('Common Keywords used in Description:\n')
    for word, frequency in common_description_words:
        if word not in exclusions and frequency>5:
            print(f'{word}: {frequency}')

    return


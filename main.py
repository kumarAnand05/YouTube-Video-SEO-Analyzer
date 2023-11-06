import videoAnalyzer

apiKey = videoAnalyzer.provideKey()
youtube = videoAnalyzer.makeConnection(api_key)

search_query = input('\n\nEnter search terms that you think viewers can use. Use comma "," to separate the search queries.\n').split(",")
resCount = int(input('\nEnter number of videos that you want to analyze for each search terms. Note: Higher videos means higher processing time:'))

print('\nAnalyzing Videos for your search terms\n')
videoAnalyzer.startSearch(youtube, search_query, resCount)
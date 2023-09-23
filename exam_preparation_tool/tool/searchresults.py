from googlesearch import search
import os
import googleapiclient.discovery


def searchresults(query):
    link = []
        # Perform the Google search and iterate through the results
    for result in search(query):  # You can adjust the number of results, stop, and pause as needed
        link.append(result)

    return link




def search_videos(query, max_results=10):
    # Set your API key here. Replace 'YOUR_API_KEY' with your actual API key.
    API_KEY = 'AIzaSyBAWuTa1QA8GP2-vTDBbYDiwzRCGfJdqBU'

    # Initialize the YouTube API client
    youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey=API_KEY)
    try:
        # Perform a YouTube search based on the query
        search_response = youtube.search().list(
            q=query,
            type='video',
            part='id,snippet',  # Include snippet to get video titles
            maxResults=max_results
        ).execute()

        # Extract video titles and video IDs from the search results
        video_results = [(item['snippet']['title'], item['id']['videoId']) for item in search_response.get('items', [])]

        return video_results

    except Exception as e:
        return []

def recomendvideos(query):
    topic = query
    search_results = search_videos(topic+"english")
    videos=[]
        
    if search_results:
        print("Videos related to the topic:")
        for video_title, video_id in search_results:
            try:
                # Encode video title in UTF-8 and decode any invalid characters
                video_title = video_title.encode('utf-8', 'ignore').decode('utf-8')
                video_url = f'https://www.youtube.com/watch?v={video_id}'
                videos.append(f"{video_title}: {video_url}")
            except UnicodeEncodeError:
                pass
    else:
        videos.append('Sorry no results found')

    return videos

def extractlink(videolist):
    video_link=[]

    for link in videolist:
        video_link.append(link[link.index(":"):].replace(":",""))

    return video_link
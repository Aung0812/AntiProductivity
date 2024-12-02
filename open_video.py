import json
import urllib.request
import string
from random import choice
import webbrowser

def open_random_video(API_KEY):
    count = 1
    API_KEY = API_KEY
    random = ''.join(choice(string.ascii_uppercase + string.digits) for _ in range(3))

    urlData = f"https://www.googleapis.com/youtube/v3/search?key={API_KEY}&maxResults={count}&part=snippet&type=video&q={random}"

    # sends a GET request to the YouTube API and gets a response
    webURL = urllib.request.urlopen(urlData)
    data = webURL.read()
    encoding = webURL.info().get_content_charset('utf-8')
    results = json.loads(data.decode(encoding))

    for data in results['items']:
        videoId = (data['id']['videoId'])
        webbrowser.open(f"youtube.com/watch?v={videoId}")
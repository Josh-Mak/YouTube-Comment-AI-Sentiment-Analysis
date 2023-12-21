from googleapiclient.discovery import build
import html
import pickle
import os

# api_key = os.getenv('')
api_key = 'AIzaSyB16wi07ODYIUtJy14TkVDCyPFnRjvb4ME'
channel_id = 'UCMiiehUAHfg7KrfaPAk4R0w'
all_videos_playlist_id = 'UUMiiehUAHfg7KrfaPAk4R0w'

youtube = build('youtube', 'v3', developerKey=api_key)

# region Grabbing Video Ids
list_of_ids = []
request = youtube.playlistItems().list(
    part='contentDetails',
    playlistId=all_videos_playlist_id,
    maxResults=50,
)
response = request.execute()
for item in response['items']:
    vid_id = item['contentDetails']['videoId']
    list_of_ids.append(vid_id)

while True:
    try:
        next_page_token = response['nextPageToken']
        next_request = youtube.playlistItems().list(
            part='contentDetails',
            playlistId=all_videos_playlist_id,
            maxResults=50,
            pageToken=next_page_token,
        )
        response = next_request.execute()
        for item in response['items']:
            vid_id = item['contentDetails']['videoId']
            list_of_ids.append(vid_id)
    except KeyError:
        print(f"Got key Error")
        break
# endregion

# region Getting Comments from Every Video
c = 0
comments_dictionary = {}
for video_id in list_of_ids:
    request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        maxResults=100,
    )
    response = request.execute()

    list_of_comments = []
    for item in response['items']:
        comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
        cleaned_comment = html.unescape(comment)
        list_of_comments.append(cleaned_comment)

    while True:
        try:
            next_page_token = response['nextPageToken']
            next_request = youtube.commentThreads().list(
                part="snippet",
                videoId=video_id,
                maxResults=100,
                pageToken=next_page_token,
            )
            response = next_request.execute()
            for item in response['items']:
                comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
                cleaned_comment = html.unescape(comment)
                list_of_comments.append(cleaned_comment)
        except KeyError:
            break
    comments_dictionary[video_id] = list_of_comments
    c += 1
    if c % 5 == 0:
        print(f"Finished video: {video_id}. Total Complete: {c}")
# endregion
with open('comments_dictionary.pickle', 'wb') as handle:
    pickle.dump(comments_dictionary, handle, protocol=pickle.HIGHEST_PROTOCOL)
with open('comments_dictionary_to_edit.pickle', 'wb') as handle:
    pickle.dump(comments_dictionary, handle, protocol=pickle.HIGHEST_PROTOCOL)
# empty dict for app to use
analyzed_comments = {"6": "Base Data Comment"}
with open('analyzed_comments.pickle', 'wb') as handle:
    pickle.dump(analyzed_comments, handle, protocol=pickle.HIGHEST_PROTOCOL)


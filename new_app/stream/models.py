import os, json
from dotenv import load_dotenv
from oauth2client.client import GoogleCredentials
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from ..models import Favorite, Streamer
from django.contrib.auth.models import User

load_dotenv()
scopes = ["https://www.googleapis.com/auth/youtube.readonly"] # View your Youtube account
api_service_name = os.environ.get("API_SERVICE_NAME")
api_version = os.environ.get("API_VERSION")
client_secrets_file =  './client_secret_456715957369-o0epqn9ha9m2hme6r6qmiavo47ehm05v.apps.googleusercontent.com.json'


class CheckYoutubeAuth:
    pass


class StreamClass:
    def __init__(self, credentials = None):
        self.credentials = credentials
        self.youtube_service = None


    def get_credentials(self):
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
        credentials = flow.run_local_server(port=8001, prompt='consent').to_json() # return refresh-token everytime even for testing
        print('==== New credentials %s ======' % credentials)
        self.credentials = credentials
        return credentials

    def create_service(self):
        # print('self.credentials', self.credentials.replace("\'", "\""))
        self.credentials = json.loads(self.credentials.replace("\'", "\""))
        gCreds = GoogleCredentials( 
                self.credentials['token'], 
                self.credentials['client_id'],
                self.credentials['client_secret'],
                refresh_token=self.credentials['refresh_token'], 
                token_expiry=None,
                token_uri=self.credentials['token_uri'], 
                user_agent='Python client library',
                revoke_uri=None)        

        youtube_service = googleapiclient.discovery.build(
            api_service_name, api_version, credentials=gCreds)
        print('======= youtube service is  built: %s ========' % (youtube_service))
        self.youtube_service = youtube_service
        return
    
    def getSubscribeList(self):
        request = self.youtube_service.subscriptions().list(
            part="snippet,contentDetails",
            mine=True,
            maxResults=10
        )
        response = request.execute()

        return response, self.credentials
    
    def getStreamPlaylistList(self, streamer_key):
        request = self.youtube_service.playlists().list(
            part="snippet",
            channelId=streamer_key,
            maxResults=25
        )
        response = request.execute()

        return response, self.credentials
    
    def getStreamList(self, playlist_id):
        request = self.youtube_service.playlistItems().list(
            part="snippet",
            maxResults=1,
            playlistId=playlist_id
        )
        response = request.execute()

        return response, self.credentials
    
    
    

def store_favorite_streamer(stream_id, user_id):
    user_obj = User.objects.get(pk=user_id)
    streamer_obj, created = Streamer.objects.get_or_create(streamer_api_key = stream_id)
    favorite_obj, created = Favorite.objects.get_or_create(users_oid=user_obj, streamer_oid=streamer_obj)
    return favorite_obj.favorite_oid
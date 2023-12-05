import os
from dotenv import load_dotenv
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from django.http import JsonResponse

load_dotenv()
scopes = ["https://www.googleapis.com/auth/youtube.readonly"]
api_service_name = os.environ.get("API_SERVICE_NAME")
api_version = os.environ.get("API_VERSION")
client_secrets_file =  './client_secret_456715957369-o0epqn9ha9m2hme6r6qmiavo47ehm05v.apps.googleusercontent.com.json'



class StreamClass:
    async def create_service():
        os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
        # Get credentials and create an API client
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
            client_secrets_file, scopes)
        credentials = flow.run_local_server(port=8001)
        youtube_service = googleapiclient.discovery.build(
            api_service_name, api_version, credentials=credentials)
        print('======= youtube service is  built ========')
        return youtube_service
    
    async def getSubscribeList(youtube_service):
        request = youtube_service.subscriptions().list(
            part="snippet,contentDetails",
            mine=True
        )
        response = request.execute()

        return response
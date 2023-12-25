from ..models import Favorite
from ..users.models import get_user_obj
from django.core import serializers
from ..stream.models import DevelopYoutubeClass

def getFavoriteStreamer(user_oid):
    content = Favorite.objects.filter(
        users_oid=get_user_obj(user_oid)
    ).exclude(
        streamer_oid=None
    )
    streamer_list = []
    youtube_serv = DevelopYoutubeClass()
    for streamer_item in content:
        print('streamer_item', streamer_item.streamer_oid.streamer_api_key)
        detail_content = youtube_serv.getStreamerDetail(streamer_item.streamer_oid.streamer_api_key)
        for item in detail_content['items']:
            streamer_dict = {
                'streamer_title':item['snippet']['title'],
                'streamer_api_key':streamer_item.streamer_oid.streamer_api_key,
                'thumbnails_url':item['snippet']['thumbnails']['medium']['url'],

            }
        streamer_list.append(streamer_dict)
    return streamer_list
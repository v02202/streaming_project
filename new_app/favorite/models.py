from ..models import Favorite
from ..users.models import get_user_obj
from django.core import serializers
from ..stream.models import DevelopYoutubeClass, get_subscribe_list

def getFavoriteStreamer(user_oid):
    content = Favorite.objects.filter(
        users_oid=get_user_obj(user_oid)
    ).exclude(
        streamer_oid=None
    )
    content_list = [streamer_item.streamer_oid.streamer_api_key for streamer_item in content]
    return content_list


def mergeFavoriteAndSub(user_oid, youtube_oauth):
    reponse_list, credentials = get_subscribe_list(youtube_oauth)
    content_list = getFavoriteStreamer(user_oid)
    for item in reponse_list:
        if item['streamer_api_key'] in content_list:
            item['is_favorite'] = True
        else:
            item['is_favorite'] = False
    print('------ reponse_list ------ ', reponse_list)
    return reponse_list, credentials
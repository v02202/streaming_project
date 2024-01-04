import json, time
from django import forms
from ..models import Label
from ..stream.models import DevelopYoutubeClass
from django.db.models.expressions import RawSQL

class LableForm(forms.ModelForm):
    timestamp_url = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
            attrs={
                "placeholder": "Please paste url here...",
            }
        ),
        label="timestamp url",
    )
    is_share = forms.BooleanField(required=False)

    class Meta:
        model = Label
        exclude = ("stream_oid", "owner", "timestamp")


 

def get_label_list(owner_id):
    subquery = Label.objects.raw(
        '''
        SELECT label_oid, stream_oid_id, json_group_array(
            json_object(
                'label_name',label_name,
                'timestamp', timestamp,
                'is_share',is_share
            )
        ) AS aggre_list
        FROM new_app_label
        WHERE owner_id = %s GROUP BY stream_oid_id
        '''
        , [owner_id]
    )
    detail_list = []
    for item in subquery:
        print('item ---- stream_api_key %s aggre_list %s' % (item.stream_oid.stream_api_key, item.aggre_list))
        stream_api_key = item.stream_oid.stream_api_key
        service = DevelopYoutubeClass()
        response = service.getStreamDetail(stream_api_key)
        label_lis= json.loads(item.aggre_list)
        for label_item in label_lis:
            label_item.update(
                {
                    'timestamp':time.strftime('%H:%M:%S', time.gmtime(label_item['timestamp']))
                }
            )
        detail_dict = {
            'channel_title': response['items'][0]['snippet']['channelTitle'],
            'stream_title': response['items'][0]['snippet']['title'],
            'thumbnails_url': response['items'][0]['snippet']['thumbnails']['medium']['url'],
            'label_list': label_lis
        }
        detail_list.append(detail_dict)
    return detail_list
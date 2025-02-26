from django.urls import  re_path
from api.consumers import ChatConsumer


# Here, "" is routing to the URL ChatConsumer which 
# will handle the chat functionality.
websocket_urlpatterns = [
    re_path(r'^ws/(?P<room_name>[^/]+)/$', ChatConsumer.as_asgi()),
    


] 
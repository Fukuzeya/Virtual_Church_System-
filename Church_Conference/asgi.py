import os

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
import video.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Church_Conference.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    'websocket':AuthMiddlewareStack(
        URLRouter(
            video.routing.websocket_urlpatterns
        )
    )
})


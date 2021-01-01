from django.apps import AppConfig
from exo_mentions.registry import register


class ExoappConfig(AppConfig):
    name = 'exoapp'

    def ready(self):
        model = Post
        field = 'description'
        callback = post_detect_mention_callback

        register(model, field, callback)
from django.dispatch import receiver
from django.core.signals import request_finished

@receiver(request_finished)
def post_detect_mention_callback(sender, **kwargs):
    """ You will receive information of the mention
    user_from: kwargs.get('user_from')
        User that mentions
    object_pk: kwargs.get('object_pk')
        User's Pk that has been mentioned
    target: kwargs.get('target')
        The object where the mention was made
    """
    print("I am here")
    # Your code here
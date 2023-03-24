from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.db import models

from likes.models import Like
from tweets.models import Tweet
from utils.memcached_helper import MemcachedHelper


class Comment(models.Model):
    #ForeignKey(to, on_delete, **options)
    #to: class of connected model, 
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    tweet = models.ForeignKey(Tweet, on_delete=models.SET_NULL, null=True)
    content = models.TextField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # joint index
        index_together = (('tweet', 'created_at'), )

    @property
    def like_set(self):
        return Like.objects.filter(
            content_type=ContentType.objects.get_for_model(Comment),
            object_id=self.id,
        ).order_by('-created_at')

    @property
    def cached_user(self):
        return MemcachedHelper.get_object_through_cache(User, self.user_id)

    #display
    def __str__(self):
        return '{} - {} says at tweet {}'.format(
            self.created_at,
            self.user,
            self.content,
            self.tweet_id,
        )


from django.contrib.auth.models import User, AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.template.defaultfilters import slugify

class User(AbstractUser):
    followers = models.ManyToManyField('self', related_name='followees', symmetrical=False)


class Post(models.Model):
    author = models.ForeignKey(User, related_name='posts')
    title = models.CharField(name="title", unique=True, max_length=255, db_index=True)
    body = models.TextField(name="content")
    slug = models.SlugField(max_length=255, db_index=True)
    created_date = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        unique_together = ('author', 'title')
        ordering = ('created_date',)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    # @models.permalink
    # def get_absolute_url(self):
    #     return reverse('api:post-detail', kwargs={'pk': self.pk})
        # return reverse('api:post-detail', kwargs={'pk': self.slug})


class Comment(models.Model):
    name = models.CharField(max_length=100)
    email_address = models.EmailField(max_length=75)
    website = models.URLField(max_length=255, null=True, blank=True)
    body = models.CharField(max_length=200)
    post_id = models.ForeignKey(Post, related_name='comments')
    created_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.body


class Photo(models.Model):
    post_id = models.ForeignKey(Post, related_name='photos')
    image = models.ImageField(upload_to="%Y/%m/%d")

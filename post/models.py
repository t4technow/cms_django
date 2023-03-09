from django.db import models
from author.models import Author
from user.models import User

# Create your models here.

class Tag(models.Model):
    title = models.CharField(max_length = 30)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


VISIBILITY = (
    ('publish', 'publish'),
    ('draft', 'draft')
)

CONTENT_TYPE = (
    ('post', 'post'),
    ('page', 'page')
)

ALLOW_COMMENTS = (
    ('allow', 'allow'),
    ('no comments', 'no comments')
)

class Post(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField(unique=True, blank=True)
    featured_image = models.ImageField(upload_to='post/thumbnails')
    body = models.TextField()
    excerpt = models.TextField(null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name= 'post_category', on_delete=models.CASCADE, default='un_categorized')
    tags = models.ManyToManyField(Tag, related_name='post_tags')
    visibility = models.CharField(max_length=30, choices = VISIBILITY, default='publish')
    content_type = models.CharField(max_length=30, choices=CONTENT_TYPE, default='post')
    allow_comments = models.CharField(max_length=30, choices=ALLOW_COMMENTS, default='allow')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title

class Comment(models.Model):

    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:

        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return self.body

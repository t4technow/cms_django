from .models import Post, Category, Tag
from author.models import Author

def commonContext(request):
    trending_posts = Post.objects.filter(content_type = 'post').order_by('updated_at')
    categories = Category.objects.all().order_by('title')
    tags = Tag.objects.all().order_by('title')
    authors = Author.objects.all()[:6]
    pages = Post.objects.filter(content_type = 'page')

    return {
        'trending_posts': trending_posts,
        'categories': categories,
        'contributors': authors,
        'pages': pages,
        'tags': tags,
    }
from .models import Post, Category, Tag
from author.models import Author
from django.db.models import Count, Q

def commonContext(request):
    
    trending_posts = Post.objects.filter(content_type = 'post').order_by('-updated_at')

    categories = Category.objects.filter(Q(post_category__content_type = 'post') | Q(post_category__content_type = None)).annotate(no_of_posts = Count('post_category')).order_by('title')
    most_posted_cat = categories.order_by('-no_of_posts')[0:1]

    tags = Tag.objects.filter(Q(post_tags__content_type = 'post') | Q(post_tags__content_type = None)).annotate(no_of_posts = Count('post_tags')).order_by('title')
    authors = Author.objects.all()[:6]
    pages = Post.objects.filter(content_type = 'page')


    return {
        'trending_posts': trending_posts,
        'categories': categories,
        'contributors': authors,
        'pages': pages,
        'tags': tags,
        'most_posted_cat': most_posted_cat,
    }
    
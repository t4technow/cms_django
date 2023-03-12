from django.db.models import Count
from datetime import date, timedelta
from .models import PageVisit
from post.models import Post, Category, Tag
from author.models import Author

def page_visit_context_processor(request):

    visits = PageVisit.objects.values('url').annotate(count=Count('id')).order_by('-count')
    current_url = request.path
    
    current_user = request.user.id
    
    
    today = date.today()
    seven_days_before = today - timedelta(7)
    
    post_urls = visits.filter(url__startswith = '/post/')
    category_urls = visits.filter(url__startswith = '/category/')
    tag_urls = visits.filter(url__startswith = '/category/')
    
    most_visited_cat = category_urls[0:1]
    trending_urls = visits.filter(visited_at__gte = seven_days_before)
    
    trending_post_urls = []
    trending_cat_urls = []
    trending_tag_urls = []
    trending_author_urls = []
    
    
    for x in trending_urls:
        if x['url'].startswith('/post/'):
            trending_post_urls.append(x['url'].replace('/post/', ''))
        elif x['url'].startswith('/category/'):
            trending_cat_urls.append(x['url'].replace('/category/', ''))
        elif x['url'].startswith('/tag/'):
            trending_tag_urls.append(x['url'].replace('/tag/', ''))
        elif x['url'].startswith('/author/'):
            trending_author_urls.append(x['url'].replace('/author/', ''))

    
    trending_posts = Post.objects.filter(slug__in = trending_post_urls)
    trending_cats = Category.objects.filter(slug__in = trending_cat_urls)
    trending_tags = Tag.objects.filter(slug__in = trending_tag_urls)
    # trending_authors = Author.objects.filter(user_id__id__in = trending_author_urls)
    
    # print(trending_posts, 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
    # print(trending_cats, 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
    # print(trending_tags, 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
    # # print(trending_authors, 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
    
    
    
    return {
        'visits': visits,
        'current_url': current_url,
        'most_visited_cat': most_visited_cat,
        
        }




# urls = []
    # post_urls = []
    # categories_urls = []
    
    # for item in visits:
    #     if item.url.startswith('/post/'):
    #         post_urls.append(item.url)
    #     elif item.url.startswith('/category/'):
    #         categories_urls.append(item.url)
    #     else:
    #         urls.append(item.url)
            

    # print(urls, '--------------------------------------------')
    # print(post_urls, '--------------------------------------------')
    # print(categories_urls, '--------------------------------------------')

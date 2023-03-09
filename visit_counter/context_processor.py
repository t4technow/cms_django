from django.db.models import Count

from .models import PageVisit


def page_visit_context_processor(request):
    visits = PageVisit.objects.values('url').annotate(count=Count('id')).order_by('-count')
    current_url = request.path
    return {'visits': visits, 'current_url': current_url}




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

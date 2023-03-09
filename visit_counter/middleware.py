
from django.contrib.sessions.middleware import SessionMiddleware

from .models import PageVisit


class PageVisitMiddleware(SessionMiddleware):
    def process_response(self, request, response):
        if request.method == 'GET':
            session_key = request.session.session_key
            if not session_key:
                request.session.save()
                session_key = request.session.session_key

            url = request.get_full_path()

            if (
                url == '/'
                or '/post/' in url
                or '/page/' in url
                or '/category/' in url
                or '/categories/' in url
                or '/tag/' in url
                or '/tags/' in url
                or '/author/' in url
            ) and '/media/' not in url:

                # count requests
                if not PageVisit.objects.filter(session_key=session_key, url=url).exists():
                    if request.user.id:
                        x = PageVisit.objects.create(session_key=session_key, url=url, user_id=request.user.id)
                    else:
                        x = PageVisit.objects.create(session_key=session_key, url=url)

                    x.save()


        return response
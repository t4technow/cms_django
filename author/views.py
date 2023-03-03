from django.views.generic import DetailView
from .models import Author

class Profile(DetailView):
    model = Author
    context_object_name = 'author'
    template_name = "author/profile.html"

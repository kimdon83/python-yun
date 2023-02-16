from django.shortcuts import render

from django.views.generic  import ListView, DetailView,TemplateView

from .models import publication
# # from .models import conference

# # Create your views here.
# class PubDetailView(DetailView):
#     model = publication
#     context_object_name = "publication"
#     template_name = 'research/pub_detail.html'

# class ConfDetailView(DetailView):
#     model = conference
#     context_object_name = "conference"
#     template_name = 'research/conf_detail.html'

class HomeView(ListView):
    model = publication
    template_name = 'research/home.html'
    context_object_name= 'publications'
    queryset = publication.objects.all()
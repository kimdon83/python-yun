from django.urls import path

from . import views

urlpatterns= [
    path('',views.HomeView.as_view(),name=''),
    # path('gift/',views.GiftListView.as_view(),name='gift'),
    # path('publication/<int:pk>',views.PubDetailView.as_view(),name='pub.detail'),
    # path('publication/<int:pk>',views.ConfDetailView.as_view(),name='conf.detail')
    
]    


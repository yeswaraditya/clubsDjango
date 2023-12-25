
from django.urls import path

from innovationclub.views import InnovationHomePageView



urlpatterns = [
    
    path('inno/',InnovationHomePageView.as_view(),name='innovation.html'),
    
]

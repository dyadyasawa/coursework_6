

from django.views.decorators.cache import cache_page
from django.urls import path

from mailings.apps import MailingsConfig
from mailings.views import StartPageView

app_name = MailingsConfig.name


urlpatterns = [
    path('', StartPageView.as_view(), name='start_page'),

]

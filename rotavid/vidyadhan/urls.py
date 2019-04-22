from django.urls import path
from vidyadhan.views import IndexPage 

urlpatterns = [
	path('', IndexPage , name='index' ),
]

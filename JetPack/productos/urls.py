from django.conf.urls import url
from . import views

urlpatterns = [

	url(r'^todos/$',
    	views.HomeView.as_view(),
    	name = 'todos'
    	),
    
]
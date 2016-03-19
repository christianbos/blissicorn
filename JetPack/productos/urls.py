from django.conf.urls import url
from . import views

urlpatterns = [

	url(r'^todos/$',
    	views.HomeView.as_view(),
    	name = 'todos'
    	),

	url(r'^detalle/(?P<id>\d+)',
		views.ProductDetailView.as_view(),
		name = 'detalle'
		),
    
]
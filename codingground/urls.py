from django.conf.urls import url
from .import views

app_name = "codingground"

urlpatterns = [
	
	url(r'^$', views.home_page, name='index'),
	url(r'^about/$', views.about_page, name='about'),
	url(r'^form/$', views.form_page, name='form'),
	#url(r'^syntaxdb/$', views.syntaxdb_page, name='syntaxdb'),

	#iFrame Urls Here:-

	#url(r'^syntaxdb/syntaxdb.com$', views.syntaxdb_iFrame, name='syntaxdb'),

	#Form Processing Urls Here:-

	url(r'^getdata/$', views.get_data, name='get_data'),

	url(r'^cleardata/$', views.clear_data, name='clear_data')
]
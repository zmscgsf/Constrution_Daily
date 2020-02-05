#!/usr/bin/python
from django.urls import path
from django.conf.urls import url
from . import views

app_name='note'
urlpatterns = [
	path('admin/',views.index,name='admin'),
	path('',views.index,name='index'),
	path('topics/',views.topics,name='topics'),
	path('entries/',views.entries,name='entries'),
	path('topic/',views.topic,name='topic'),
	path('topics/<topic_id>',views.topic,name='topic'),

	path('new_topic/' , views.new_topic,name='new_topic'),
]

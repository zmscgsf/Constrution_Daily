from django.shortcuts import render
from . models import Topic,Entry

from django.http import HttpResponseRedirect
from django.urls import reverse
from . forms import TopicForm

# Create your views here.
def index(request):
	#施工日志的主页
	return render(request,'note/index.html')
def topics(request):
	#显示所有单位工程
	topics = Topic.objects.order_by('date_added')
	context = {'topics':topics}
	return render(request,'note/topics.html',context)
def topic(request,topic_id):
	#显示一个单位工程及施工日志
	topic = Topic.objects.get(id=topic_id)
	entries = topic.entry_set.order_by('-date_added')
	context = {'topic':topic,'entries':entries}
	return render(request,'note/topic.html',context)

def entries(request):
	#显示所有施工日志
	entries = Entry.objects.order_by('-date_added')
	context = {'entries':entries}
	return render(request,'note/entries.html',context)


def new_topic(request):
	#添加新主题
	if request.method != 'POST':
		#未提交数据：创建一个新表单
		form = TopicForm()

	else:
		#POST提交的数据，对数据进行处理
		form = TopicForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('note:topics'))
	context = {'form':form}
	return render(request,'note/new_topic.html',context)
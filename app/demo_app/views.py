import redis
import celery.states as states

from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.urls import reverse


from .models import Member
from mysite.settings import celery

# Redis連線
cache = redis.Redis(host='redis', port=6379)

# Create your views here.
def main(request):
	context = {
		'count': get_hit_count(),
		'member_list': Member.objects.all(),
	}
	return render(request, 'main.html', context)

def get_hit_count():
	retries = 5
	while True:
		try:
			return cache.incr('hits')
		except redis.exceptions.ConnectionError as exc:
			# 此處為連線斷掉的情況
			if retries == 0:
				raise exc
			retries -= 1
			time.sleep(0.5)

# class view demo
class MemberView(View):
	def get(self, request, name):
		Member.objects.create(name=name)
		return HttpResponse("create member %s success !" % name)

def add(request, param1, param2):
    task = celery.send_task('tasks.add', args=[param1, param2], kwargs={})
    return HttpResponse(f"<a href='{reverse('check_task', kwargs={'task_id':task.id})}'>check status of {task.id} </a>")

def check_task(request, task_id):
    res = celery.AsyncResult(task_id)
    if res.state == states.PENDING:
        return HttpResponse("%s" % res.state)
    else:
        return HttpResponse("%s" % str(res.result))
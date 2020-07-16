from django.urls import path
from .views import main, MemberView, add, check_task

urlpatterns = [
	path('', main, name='main'),
	path('addmember/<str:name>', MemberView.as_view(), name='MemberView'),
	path('add/<int:param1>/<int:param2>', add, name='addnumber'),
	path('check/<str:task_id>', check_task, name='check_task'),
]
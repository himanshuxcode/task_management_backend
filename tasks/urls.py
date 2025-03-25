from django.urls import path
from .views import TaskCreateView, TaskAssignView, UserTaskListView

urlpatterns = [
    path('create/', TaskCreateView.as_view(), name='task-create'),
    path('<int:pk>/assign/', TaskAssignView.as_view(), name='task-assign'),
    path('user/<int:user_id>/', UserTaskListView.as_view(), name='user-tasks'),
]
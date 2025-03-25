from rest_framework import generics, status
from rest_framework.response import Response
from .models import Task, User
from .serializers import TaskSerializer, TaskCreateSerializer, TaskAssignSerializer
from task_management.utils import custom_response

class TaskCreateView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskCreateSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return custom_response(
            data=TaskSerializer(serializer.instance).data,
            message="Task created successfully",
            status=status.HTTP_201_CREATED
        )

class TaskAssignView(generics.GenericAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskAssignSerializer
    
    def post(self, request, *args, **kwargs):
        task = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user_ids = serializer.validated_data['user_ids']
        users = User.objects.filter(id__in=user_ids)
        task.assigned_users.add(*users)
        
        return custom_response(
            data=TaskSerializer(task).data,
            message="Task assigned successfully"
        )

class UserTaskListView(generics.ListAPIView):
    serializer_class = TaskSerializer
    
    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Task.objects.filter(assigned_users__id=user_id)
    
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return custom_response(data=response.data)
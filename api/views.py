from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from api.models import Task
from api.serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])      
def getRoutes(request): # get all routes
    routes = [
        '/api/tasks/',      # get all tasks
        '/api/tasks/<id>/',   # get single task
    ]
    return Response(routes)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getTasks(request):
    tasks = Task.objects.all()
    if not tasks.exists():
        return Response({'message': 'No tasks found'})
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getTask(request, pk): # get single task
    try:
        task = Task.objects.get(id=pk)  # get single task
        serializer =TaskSerializer(task, many=False)            # convert to json
        return Response(serializer.data)
    except Task.DoesNotExist:   # if task does not exist
        return Response({'message': f'Task {pk} not found'})
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createTask(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response({'errors': serializer.errors, 'message': 'Task not created. Please fix the above fields.'},
            status=400)
    

            
            
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response({'errors': serializer.errors, 'message': 'Task not Updated. Please fix the above fields.'},
            status=400)
    

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteTask(request, pk):
    try:
        task = Task.objects.get(id=pk)
        task.delete()
        return Response({'message': 'Task deleted'})
    except:
        return Response({'message': f'Task {pk} not found'})
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Notification
from django.contrib.auth.decorators import login_required

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@login_required
def get_notifications(request):
    notifications = Notification.objects.filter(recipient=request.user).order_by('-timestamp')
    serialized_notifications = NotificationSerializer(notifications, many=True)
    return Response(serialized_notifications.data)

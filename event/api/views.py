from rest_framework.response import Response
from rest_framework.decorators import api_view
from event.models import Event_Table as Event
from .serializers import EventTableSerializer
from django.contrib.auth.decorators import login_required

@login_required(login_url='auth')
@api_view(['GET'])
def events_list(request):
    events = Event.objects.all().order_by('event_date')
    serializer = EventTableSerializer(events, many=True)
    return Response(serializer.data)
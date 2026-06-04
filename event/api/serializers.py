from rest_framework import serializers
from event.models import Event_Table

class EventTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event_Table
        fields = '__all__'
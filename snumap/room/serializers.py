from rest_framework import serializers, status
from place.models import Place
from room.models import Room
from place.serializers import TagSerializer, PlaceInRoomSerializer


class RoomSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)
    number = serializers.IntegerField()
    # type = serializers.IntegerField()
    floor = serializers.IntegerField()
    building = PlaceInRoomSerializer()
    information = serializers.CharField(max_length=500, allow_null=True)
    tags = TagSerializer(many=True)

    class Meta:
        model = Room
        fields = (
            'id',
            'name',
            'number',
            'type',
            'floor',
            'building',
            'information',
            'tags'
        )

    def validate(self, data):
        data['type'] = self.instance.get_type_display()
        
        return data
from rest_framework import serializers
from .models import Board
from icecream import ic

class BooardSerializers(serializers.Serializer):
    title = serializers.CharField(max_length=30)
    content = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Board.objects.create(**validated_data)

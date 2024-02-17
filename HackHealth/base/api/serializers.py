from rest_framework.serializers import ModelSerializer
from base.models import UploadedFile
from rest_framework import serializers


class RoomSerializer(ModelSerializer):
    class Meta:
        model = UploadedFile
        fields = '__all__'


class NLPResultSerializer(serializers.Serializer):
    result = serializers.CharField()


class DIPResultSerializer(serializers.Serializer):
    result = serializers.BooleanField()

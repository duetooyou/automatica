from rest_framework import serializers
from .models import Worker, Store, Visit


class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = "__all__"


class StoreSerializer(serializers.ModelSerializer):

    worker = WorkerSerializer()

    class Meta:
        model = Store
        fields = "__all__"


class VisitSerializer(serializers.ModelSerializer):

    store = serializers.StringRelatedField

    class Meta:
        model = Visit
        fields = "__all__"

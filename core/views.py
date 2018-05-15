from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import serializers
from core.models import WorkOrder


def test_bower_staticfiles(request):
    template = 'core/test_bower_staticfiles.html'
    return render(request, template, {})


class WorkOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkOrder
        fields = "__all__"


class WorkOrderViewSet(viewsets.ModelViewSet):
    queryset = WorkOrder.objects.all()
    serializer_class = WorkOrderSerializer

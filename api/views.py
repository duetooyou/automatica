from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_201_CREATED
from .models import Worker, Store
from .serializers import (StoreSerializer,
                          VisitSerializer)


class StoreView(APIView):

    def get(self, request):
        if request.headers.get('phone-number'):
            store_list = Store.objects.filter(worker__phone_number=self.request.headers['phone-number']). \
                select_related('worker')
            serializer = StoreSerializer(store_list, many=True)
            return Response(serializer.data)
        else:
            content = "Введите номер в заголовок запроса"
            return Response(content, HTTP_400_BAD_REQUEST)

    def get_view_name(self):
        return f"Список точек работника"


class VisitCreateView(CreateAPIView):

    def create(self, request, *args, **kwargs):
        queryset = Worker.objects.filter(phone_number=
                                         request.headers.get('phone-number'))
        store = get_object_or_404(Store, id=request.data['store'])
        if queryset.exists():
            serializer = VisitSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, HTTP_201_CREATED)
        else:
            content = "Отсутствует или неверный номер телефона в заголовке " \
                      "или работник c таким номером телефона не зарегистрирован."
            return Response(content, HTTP_400_BAD_REQUEST)

    def get_view_name(self):
        return f"Создать посещение"

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.status import HTTP_400_BAD_REQUEST
from .models import Worker, Store, Visit
from .serializers import (StoreSerializer,
                          VisitSerializer)


class StoreView(APIView):

    def get(self, request):
        try:
            self.request.data['phone_number']
        except KeyError:
            return Response({"Введите номер в тело запроса"}, HTTP_400_BAD_REQUEST)
        else:
            store_list = Store.objects.filter(worker__phone_number=self.request.data['phone_number']). \
                select_related('worker')
            serializer = StoreSerializer(store_list, many=True)
            return Response(serializer.data)

    def get_view_name(self):
        return f"Список точек работника"


class VisitCreateView(CreateAPIView):
    serializer_class = VisitSerializer
    queryset = Visit.objects.all()

    def get_view_name(self):
        return f"Создать посещение"

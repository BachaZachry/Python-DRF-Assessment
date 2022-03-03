from rest_framework import generics
from rest_framework.response import Response


class ViewA(generics.GenericAPIView):
    pass


class ViewC(generics.GenericAPIView):
    pass


class ViewAPI(generics.GenericAPIView):

    def get(self, request):
        return Response({"test": "test"})

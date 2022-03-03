from rest_framework import generics, mixins
from rest_framework.response import Response


class ViewA(generics.GenericAPIView):
    pass


class ViewB(mixins.CreateModelMixin):
    pass

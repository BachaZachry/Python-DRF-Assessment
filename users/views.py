from rest_framework import generics, mixins


class ViewA(generics.GenericAPIView):
    pass


class ViewB(mixins.CreateModelMixin):
    pass

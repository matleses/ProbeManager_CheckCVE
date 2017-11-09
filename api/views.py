from rest_framework import viewsets
from checkcve.api.serializers import CheckcveSerializer, CveSerializer, WhiteListSerializer, SoftwareSerializer
from checkcve.models import Cve, Checkcve, WhiteList, Software
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin


class CheckcveViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Checkcve.objects.all()
    serializer_class = CheckcveSerializer


class CveViewSet(ListModelMixin, RetrieveModelMixin, viewsets.GenericViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Cve.objects.all()
    serializer_class = CveSerializer


class WhiteListViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = WhiteList.objects.all()
    serializer_class = WhiteListSerializer


class SoftwareViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Software.objects.all()
    serializer_class = SoftwareSerializer
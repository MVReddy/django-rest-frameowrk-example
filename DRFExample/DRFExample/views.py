from django.conf import settings
from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


def home(request):
    """ Renders the home page. """
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'DRFExample/index.html',
        context = RequestContext(request, { 'title': 'Drfexample' })
    )


def page2(request):
    """ Renders page 2. """
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'DRFExample/page2.html',
        context = RequestContext(request, { 'title': 'Drfexample' })
    )
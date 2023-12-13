from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed

from django.db.models import Count

from .models import Server, Category, Channel
from .serializers import ServerSerializer
# Create your views here.


class ServerView(viewsets.ViewSet):

    queryset = Server.objects.all()

    def list(self, request):
        category = request.query_params.get('category')
        if (category):
            try:
                category = Category.objects.get(name=category)
            except Category.DoesNotExist:
                return Response("Category did not found!!", status=status.HTTP_404_NOT_FOUND)
            self.queryset = self.queryset.filter(category=category)

        channel = request.query_params.get('channel')
        if (channel):
            try:
                channel = Channel.objects.get(name=channel)
            except Channel.DoesNotExist:
                return Response("Channel did not found!!", status=status.HTTP_404_NOT_FOUND)
            self.queryset = self.queryset.filter(channel_server__in=[channel])

        my_servers = request.query_params.get('my_servers')
        if (my_servers == "true"):
            if (not request.user.is_authenticated):
                raise AuthenticationFailed()
            self.queryset = self.queryset.filter(owner=request.user)

        quantity = request.query_params.get('qty')
        if (quantity):
            self.queryset = self.queryset[:int(quantity)]

        num_of_members = request.query_params.get("num_of_members")
        if (num_of_members):
            self.queryset = self.queryset.annotate(num_members=Count("member"))

        serialized_data = ServerSerializer(self.queryset, many=True)
        return Response(serialized_data.data, status=status.HTTP_200_OK)

from rest_framework import serializers
from .models import Destination, UpcomingOffers


class DestinationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Destination
        fields = ('id','name', 'descr', 'image', 'price', 'offers', 'rating')

class UpcomingOfferSerializer(serializers.ModelSerializer):

    class Meta:
        model = UpcomingOffers
        fields = ('id','Place', 'decr', 'pic', 'amt', 'offr', 'ratings')

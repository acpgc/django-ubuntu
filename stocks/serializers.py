from rest_framework import serializers

from .models import Stocks

class StocksSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Stocks
		fields = ('name', 'description', 'ticker', 'created_at')
		
from rest_framework import serializers
from p4_app.p4_api.models import Category, Game


class GameSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Game
        fields = ('id', 'title', 'category', 'owner', 'image_url', 'game_url',
                  'description', 'additional_info', 'added', 'is_public')


class CategorySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    games = GameSerializer(many=True, required=False)

    class Meta:
        model = Category
        fields = ('id', 'name', 'owner', 'games', 'created_at', 'updated_at')

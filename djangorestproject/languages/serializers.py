from rest_framework import serializers

from .models import Language, Popularity, Programmer


class LanguageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Language
        fields = ("id", "url", "name", "paradigm", "rank", "popularity")


class PopularitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Popularity
        fields = ("id", "url", "previousrank", "rank")


class ProgrammerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Programmer
        fields = ("id", "url", "name", "languages")

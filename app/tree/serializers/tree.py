from rest_framework import serializers
from tree.models import Tree


class TreeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tree
        fields = (
            'id',
            'name',
            'data',
        )
        read_only_fields = (
            'id',
        )

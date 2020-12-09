from rest_framework import serializers
from nav.models import Nav

class SubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nav
        fields ='__all__'

class Serializer(serializers.ModelSerializer):
    sub_product=SubSerializer(many=True,read_only=True)
    class Meta:
        model = Nav
        fields = '__all__'

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        # self.fields['sub_product'] =  SubProductSerializer(read_only=True)
        return Nav.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.name_product = validated_data.get('name_nav', instance.name_product)
        instance.code = validated_data.get('code', instance.code)
        instance.color = validated_data.get('color', instance.color)
        instance.parent = validated_data.get('parent', instance.parent)
        instance.save()
        return instance
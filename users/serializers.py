from rest_framework import serializers

from users.models import Book


class BookSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    # 定义需要提取的序列化字段,名称和model中定义的字段相同
    title = serializers.CharField(required=True, max_length=100)
    isbn = serializers.CharField(required=True, max_length=100)
    author = serializers.CharField(required=True, max_length=100)
    publish = serializers.CharField(required=True, max_length=100)
    rate = serializers.FloatField(default=0)
    add_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=True)


class BookModelSerializer(serializers.ModelSerializer):
    add_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=True)

    class Meta:
        model = Book
        fields = "__all__"  # 将所有的字段都序列化
        # fields = ('title', 'isbn') # 指定某些字段序列化

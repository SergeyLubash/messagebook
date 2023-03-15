from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from messagebook.models import Users, Posts, Comments
from messagebook.validators import Сensorshipvalidator, Phonevalidator, Emailvalidator, Passwordvalidator


class PostsSerializer(serializers.ModelSerializer):
    title = serializers.CharField(validators=[Сensorshipvalidator()])

    def create(self, validated_data):
        if validated_data['user_post']:
            import datetime
            age = validated_data['user_post']
            if age.dateofbirth:
                if (datetime.date.today() - age.dateofbirth) > datetime.timedelta(days=18 * 365):
                    age.save()
                    return super().create(validated_data)
                else:
                    raise serializers.ValidationError("Создание поста запрещено, Вам нет 18 лет")

    class Meta:
        model = Posts
        fields = '__all__'


class CommentsSerializer(serializers.ModelSerializer):
    user_comment = serializers.SlugRelatedField(
        queryset=Users.objects.all(),
        slug_field='username'
    )

    class Meta:
        model = Comments
        fields = '__all__'


class UsersSerializer(serializers.ModelSerializer):
    phone = serializers.IntegerField(validators=[Phonevalidator()])
    email = serializers.CharField(validators=[Emailvalidator()])
    password = serializers.CharField(validators=[Passwordvalidator()])

    def create(self, validated_data):
        users = super().create(validated_data)
        users.set_password(users.password)
        users.save()
        return users

    class Meta:
        model = Users
        fields = '__all__'

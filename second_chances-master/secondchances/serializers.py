from rest_framework import serializers
from .models import *

from directmessages.apps import Inbox
from directmessages.models import Message
from directmessages.services import MessagingService


class User_ProfileSerializer(serializers.ModelSerializer):
    # user = serializers.PrimaryKeyRelatedField(many=False, read_only=False)
    class Meta:
        model = User_Profile
        fields = ('user', 'firstname', 'lastname', 'emailaddress', 'bio', 'created', 'last_login')

    # def create(self, validated_data):
    #     # return User_Profile.objects.create_user(**validated_data)
    #     new = User_Profile(**validated_data)
    #     new.save()
    #     return new


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('password', 'id', 'email', 'username')

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class JobSerializer(serializers.ModelSerializer):
   #  url = serializers.HyperlinkedIdentityField(
   #     view_name='job',
   # )
    class Meta:
        model = Job
        fields = ('id', 'owner', 'title', 'description', 'created', 'location')


# class JobMatchSerializer(serializers.ModelSerializer):
#     # url = serializers.HyperlinkedIdentityField(
#     #     view_name='jobmatch',
#     # )
#     class Meta:
#         model = Job
#         fields = ('owner', 'title', 'description', 'created', 'location')


class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = ('id', 'skill')


class Provided_SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provided_Skill
        fields = ('id', 'owner', 'skill', 'skill_string')


class Required_SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Required_Skill
        fields = ('id', 'owner', 'skill', 'skill_string')


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'city', 'state', 'location_string')


class User_LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Location
        fields = ('id', 'owner', 'location', 'location_string')


class NeedsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Needs
        fields = ('id', 'need')


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('id', 'owner', 'title', 'description', 'created', 'location')


class User_NeedsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Needs
        fields = ('id', 'owner', 'need', 'need_string')


class Provided_NeedsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provided_Needs
        fields = ('id', 'owner', 'need', 'need_string')


class ConnectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connection
        fields = ('id', 'user_1', 'user_2', 'created')


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'sender', 'recipient', 'content', 'sent_at', 'read_at')


class ConversationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('sender', 'recipient')

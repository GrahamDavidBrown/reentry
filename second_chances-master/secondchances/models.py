from django.db import models
from django.contrib.auth.models import User


class User_Profile(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    firstname = models.CharField(max_length=30, blank=True, null=True)
    lastname = models.CharField(max_length=30, blank=True, null=True)
    emailaddress = models.CharField(max_length=50, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now=True)
    last_login = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Location(models.Model):
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    location_string = models.CharField(max_length=54, null=True)

    def __str__(self):
        return self.city + ", " + self.state

    class Meta:
        unique_together = ('city', 'state')


class Job(models.Model):
    owner = models.ForeignKey(User_Profile)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created = models.DateTimeField(auto_now=True)
    location = models.ForeignKey(Location, null=True)

    def __str__(self):
        return self.title


class Skills(models.Model):
    skill = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.skill


class Provided_Skill(models.Model):
    owner = models.ForeignKey(User_Profile)
    skill = models.ForeignKey(Skills)
    skill_string = models.CharField(max_length=25, null=True)

    def __str__(self):
        return self.skill.skill

    class Meta:
        unique_together = ('owner', 'skill')


class Required_Skill(models.Model):
    owner = models.ForeignKey(Job)
    skill = models.ForeignKey(Skills)
    skill_string = models.CharField(max_length=25, null=True)

    def __str__(self):
        return self.skill.skill

    class Meta:
        unique_together = ('owner', 'skill')


class User_Location(models.Model):
    owner = models.ForeignKey(User_Profile)
    location = models.ForeignKey(Location)
    location_string = models.CharField(max_length=54, null=True)

    def __str__(self):
        return str(self.location)

    class Meta:
        unique_together = ('owner', 'location')


class Needs(models.Model):
    need = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.need


class User_Needs(models.Model):
    owner = models.ForeignKey(User_Profile)
    need = models.ForeignKey(Needs)
    need_string = models.CharField(max_length=25, null=True)


class Service(models.Model):
    owner = models.ForeignKey(User_Profile)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created = models.DateTimeField(auto_now=True)
    location = models.ForeignKey(Location, null=True)

    def __str__(self):
        return self.title


class Provided_Needs(models.Model):
    owner = models.ForeignKey(Service)
    need = models.ForeignKey(Needs)
    need_string = models.CharField(max_length=25, null=True)

    def __str__(self):
        return self.need.need

    class Meta:
        unique_together = ('owner', 'need')


class Connection(models.Model):
    user_1 = models.ForeignKey(User_Profile, related_name='Connection_user_1')
    user_2 = models.ForeignKey(User_Profile, related_name='Connection_user_2')
    created = models.DateTimeField(auto_now=True)


# class Conversation(models.Model):
#     from_user = models.ForeignKey(User_Profile, related_name='Conversation_from_user')
#     to_user = models.ForeignKey(User_Profile, related_name='Conversation_to_user')
#     created = models.DateTimeField(auto_now=True)
#
#
# class Message(models.Model):
#     conversation = models.ForeignKey(Conversation)
#     text_body = models.TextField()
#     created = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.text_body[:50]

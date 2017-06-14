from django.shortcuts import render, redirect
from rest_framework import viewsets
# consider changing to clear up namespace
from .models import *
from django.contrib.auth.models import User
# consider changing to clear up namespace
from .serializers import *
from django.http import HttpResponse
from django.views.generic import View  #
from django.contrib.auth import authenticate, login, logout  #
from .forms import UserForm  #
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import list_route
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from os import sys
from django.db.models import Q
from directmessages.apps import Inbox
from directmessages.services import MessagingService



class User_ProfileViewSet(viewsets.ModelViewSet):
    queryset = User_Profile.objects.all()
    serializer_class = User_ProfileSerializer
    permission_classes = [AllowAny]

    # def get_queryset(self):
    #     user_id = self.kwargs['user_id']
    #     # user_id = self.request.user.id
    #     user_profile = User_Profile.objects.get(user=user_id)
    #     # user = User.objects.get(id=user_id)
    #     # login(request, user)
    #     # user_profile_list = []
    #     # user_profile_list.append(user_profile)
    #     return user_profile

    # def update(self, request, pk):
    #     profile = User_Profile.objects.get(user_id=20)
    #     profile.firstname="anything"
    #     return response
    #
    # def perform_update(self, request):
    #     pass

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return self.queryset.all()

    def create(self, request):
        response = super(UserViewSet, self).create(request)
        # login user via session
        login(request, self.user)
        # user_profile = User_Profile(user=self.user.id)
        user_profile = User_Profile(user=self.request.user)
        user_profile.save()
        # return Response({'id': self.request.user.id})
        return response

    def perform_create(self, serializer):
        # calls save on the serializer
        self.user = serializer.save()

    @list_route(methods=['post'])
    def login(self, request):
        user = authenticate(username=request.data['username'], password=request.data['password'])

        if user:
            if user.is_active:
                login(request, user)
                return Response({'id': user.id})
        return Response({}, status=401)



class JobMatchViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    def get_queryset(self):
        """
            This will return all job matches for a user based first on whether
            any one of their provided skills matches any one of the of job's
            required skills and then secondarily on whether the locations
            they are willing to work includes the job location
        """
        try:
            jobs = []
            user_id = self.kwargs['user_id']
            # user_id = self.request.user.id
            user_profile = User_Profile.objects.get(user=user_id)
            provided_skills = Provided_Skill.objects.filter(owner=user_profile)
            required_skills = Required_Skill.objects.all()
            user_locations = User_Location.objects.filter(owner=user_profile)

            print("*** {}  in Try block***".format(len(user_locations)))

            for owned_skill in provided_skills:
                for job_skill in required_skills:
                    if (owned_skill.skill == job_skill.skill):
                        # print("\n*** Here I am ***\n")
                        print("\n*** {} ***\n".format(len(user_locations)))
                        if len(user_locations) == 0:
                            #  append job object
                            jobs.append(job_skill.owner)

                        else:
                            print("\n*** INSIDE ELSE ***\n")

                            for spot in user_locations:
                                print(spot)
                                print(str(job_skill.owner.location) == str(spot))

                                if str(job_skill.owner.location) == str(spot):
                                    #  append job object
                                    jobs.append(job_skill.owner)
                                    print("\n*** {} ***\n".format(jobs))

            sorted_jobs = sorted(jobs, key=lambda x: x.created, reverse=True)
            return sorted_jobs

        except:
            print("*** something broke ****")
            print("** In JobMatchViewSet **")
            return Job.objects.all()


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer



class OwnedJobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        user_profile = User_Profile.objects.get(user=user_id)
        return Job.objects.filter(owner=user_profile)


class SkillsViewSet(viewsets.ModelViewSet):
    queryset = Skills.objects.all()
    serializer_class = SkillsSerializer


class Provided_SkillBaseViewSet(viewsets.ModelViewSet):
    queryset = Provided_Skill.objects.all()
    serializer_class = Provided_SkillSerializer


class Provided_SkillViewSet(viewsets.ModelViewSet):
    queryset = Provided_Skill.objects.all()
    # queryset = Provided_Skill.objects.filter(owner=user_id)
    serializer_class = Provided_SkillSerializer

    def get_queryset(self):
        try:
            user_id = self.kwargs['user_id']
            # user_id = self.request.user.id
            user_profile = User_Profile.objects.get(user=user_id)
            # provided_skill = user_profile.provided_skill_set.all()
            provided_skills = Provided_Skill.objects.filter(owner=user_profile)
            for owned_skill in provided_skills:
                owned_skill.skill_string = owned_skill.skill.skill
                owned_skill.save()

            return provided_skills  # .filter(owner=user_profile)
        except:
            return Provided_Skill.objects.all()


class Required_SkillBaseViewSet(viewsets.ModelViewSet):
    queryset = Required_Skill.objects.all()
    serializer_class = Required_SkillSerializer


class Required_SkillViewSet(viewsets.ModelViewSet):
    queryset = Required_Skill.objects.all()
    serializer_class = Required_SkillSerializer

    def get_queryset(self):
        try:
            job_id = self.kwargs['job_id']
            job = Job.objects.get(id=job_id)
            required_skills = Required_Skill.objects.filter(owner=job)
            for owned_skill in required_skills:
                owned_skill.skill_string = owned_skill.skill.skill
                owned_skill.save()
            return required_skills
        except:
            return Required_Skill.objects.all()


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class User_LocationBaseViewSet(viewsets.ModelViewSet):
    queryset = User_Location.objects.all()
    serializer_class = User_LocationSerializer


class User_LocationViewSet(viewsets.ModelViewSet):
    queryset = User_Location.objects.all()
    # queryset = Provided_Skill.objects.filter(owner=user_id)
    serializer_class = User_LocationSerializer

    def get_queryset(self):
        try:
            user_id = self.kwargs['user_id']
            user_profile = User_Profile.objects.get(user=user_id)
            user_locations = User_Location.objects.filter(owner=user_profile)
            for owned_location in user_locations:
                owned_location.location_string = str(owned_location.location)
                owned_location.save()
            return user_locations
        except:
            return User_Location.objects.all()


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def get_queryset(self):
        try:
            services = []
            user_id = self.kwargs['user_id']
            user_profile = User_Profile.objects.get(user=user_id)
            user_needs = User_Needs.objects.filter(owner=user_profile)
            provided_needs = Provided_Needs.objects.all()
            user_locations = User_Location.objects.filter(owner=user_profile)
            for owned_need in user_needs:
                for service_need in provided_needs:
                    if (owned_need.need == service_need.need):
                        if len(user_locations) == 0:
                            services.append(service_need.owner)
                        else:
                            for spot in user_locations:
                                if str(service_need.owner.location) == str(spot):
                                    services.append(service_need.owner)
            return services.sort(key=created, reverse=True)
        except:
            return Service.objects.all()


class NeedsViewSet(viewsets.ModelViewSet):
    queryset = Needs.objects.all()
    serializer_class = NeedsSerializer


class User_NeedsBaseViewSet(viewsets.ModelViewSet):
    queryset = User_Needs.objects.all()
    serializer_class = User_NeedsSerializer


class User_NeedsViewSet(viewsets.ModelViewSet):
    queryset = User_Needs.objects.all()
    # queryset = Provided_Skill.objects.filter(owner=user_id)
    serializer_class = User_NeedsSerializer

    def get_queryset(self):
        try:
            user_id = self.kwargs['user_id']
            user_profile = User_Profile.objects.get(user=user_id)
            # provided_skill = user_profile.provided_skill_set.all()
            user_needs = User_Needs.objects.filter(owner=user_profile)
            for owned_need in user_needs:
                owned_need.need_string = owned_need.need.need
                owned_need.save()
            return user_needs
        except:
            return User_Needs.objects.all()


class Provided_NeedsViewSet(viewsets.ModelViewSet):
    queryset = Provided_Needs.objects.all()
    serializer_class = Provided_NeedsSerializer

    def get_queryset(self):
        try:
            service_id = self.kwargs['service_id']
            service = Service.objects.get(id=service_id)
            provided_needs = Provided_Needs.objects.filter(owner=job)
            for owned_need in provided_needs:
                owned_need.need_string = owned_need.need.need
                owned_need.save()
            return provided_needs
        except:
            return Provided_Needs.objects.all()


class ConnectionViewSet(viewsets.ModelViewSet):
    queryset = Connection.objects.all()
    serializer_class = ConnectionSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        user_profile = User_Profile.objects.get(user=user_id)
        return self.queryset.filter(Q(sender=user_profile.user) | Q(recipient=user_profile.user))

    def list(self, request):
        user_id = self.kwargs['user_id']
        user_profile = User_Profile.objects.get(user=user_id)
        queryset = Message.objects.all().filter(Q(sender=user_profile.user) | Q(recipient=user_profile.user))
        serializer = MessageSerializer(queryset, many=True)
        return Response(serializer.data)


class ConversationViewSet(viewsets.ModelViewSet):

    queryset = Message.objects.all()
    # queryset =  Message.objects.all().filter(Q(sender=request.user) | Q(recipient=request.user))
    serializer_class = ConversationSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        user_profile = User_Profile.objects.get(user=user_id)
        all_conversations = self.queryset.filter(Q(sender=user_profile.user) | Q(recipient=user_profile.user))
        contacts = []
        for conversation in all_conversations:
            if conversation.sender.id != user_id:
                contacts.append(conversation.sender)
            elif conversation.recipient != user_profile.user:
                contacts.append(conversation.recipient)

        # To abolish duplicates
        # This sends a list... Can you make it a filtered queryset?
        # return list(set(contacts))

        return self.queryset.filter(Q(sender=self.request.user) | Q(recipient=self.request.user))


class UserFormView(View):
    form_class = UserForm
    template_name = 'secondchances/registration_form.html'  # html template where registration form is
    # template_name = 'build/index.html'  # html template where registration form is


    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)  # creates object from form but does not save to db

            #  cleaned, normalized data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            #  return user object if credentials are correct

            user = authenticate(username=username, password=password)

            if user:
                if user.is_active:
                    # print("here I am")
                    login(request, user)
                    userprofile = User_Profile(user_id=user.id, bio="Your Bio Goes Here")
                    userprofile.save()
                    return redirect('/secondchances/profile/' + str(user.id) + '/')  # or redirect to any page

        # if not here is a blank form
        return render(request, self.template_name, {'form': form})


def logout(request):
    logout(request)
    return render(request, 'secondchances/')


def profile(request, user_id):
    userprofile = User_Profile.objects.get(user=request.user)
    context = {'userprofile': userprofile}
    return render(request, 'secondchances/profile.html', context)

#
# def loginx(request):
#     return HttpResponse('login')
#

def messages(request, user_id):
    user = User.objects.get(pk=user_id)
    all_conversations = Inbox.get_conversations(user)  # List of users (with IDs)
    unread_messages = Inbox.get_unread_messages(user)

    context = {'user': user,
               'all_conversations': all_conversations,
               'num_of_convos': len(all_conversations),
               'num_of_unread': unread_messages
               }
    return render(request, 'secondchances/messages.html', context)


def conversation(request, sender_id, recipient_id):
    sender = User.objects.get(pk=sender_id)
    recipient = User.objects.get(pk=recipient_id)
    full_conversation = Inbox.get_conversation(sender, recipient)

    for msg in full_conversation:
        Inbox.mark_as_read(msg)

    context = {'user1': sender,
               'user2': recipient,
               'full_conversation': full_conversation,
    }
    return render(request, 'secondchances/conversation.html', context)


def posting_detail(request, posting_id):
    return HttpResponse('posting detail')


def index(request):
    return render(request, 'secondchances/index.html')


def message_detail(request, conversation_id):
    return HttpResponse('message detail')


def myskills(request, user_id):
    return HttpResponse('skill tag editor')


def posting_search(request, user_id):
    return HttpResponse('seach posting by tags')

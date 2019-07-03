from django.contrib import admin

# Register your models here.
from schoolteam.models import Team, RecommendContest, Users, Message

admin.site.register(Users)
admin.site.register(Team)
admin.site.register(Message)
admin.site.register(RecommendContest)

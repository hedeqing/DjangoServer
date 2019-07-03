from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

import base64
# Create your models here.
class Users(models.Model):
    sex = (
        ("male","男"),
        ("female","女"),
        )
    username = models.CharField(max_length=128,default='Aris',blank=False)
    password = models.CharField(max_length=256,blank=False)
    gender  = models.CharField(max_length=32,choices=sex,default="男")
    dynamic = models.CharField(max_length=256,default="这家伙很懒，没有留下什么！")#动态;
    number = models.CharField(max_length=128,blank = False,default="123456",unique=True)
    picture = models.ImageField(upload_to="avatars/",verbose_name= "头像",blank=False,default="avatars/1.jpg")
    def __str__(self):
        return self.number

    class Meta:
        verbose_name = "用户"
        verbose_name_plural="用户"

@receiver(pre_delete, sender=Users)
def user_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.picture.delete(False)

class Team(models.Model):
    contest = {
        ("contest","比赛"),
        ('study','学习'),
        ('traval','出行'),
        ('game','游戏'),

    }
    team_id = models.ForeignKey(
        'Users',
        on_delete= models.CASCADE,
    )#队长id
    # team_id = models.CharField(max_length=32)#队伍id(主码)
    menber_id = models.CharField(max_length=128,blank=False,default= "") #成员id
    menber_quantity = models.CharField(max_length=32,default= "1")
    category = models.CharField(max_length= 128,choices= contest,blank=False)
    description = models.CharField(max_length=256,blank=False,default="没有任何描述")
    team_picture = models.ImageField(upload_to='cover/',verbose_name="封面",default='avatars/2.jpg')
    start_time = models.CharField(max_length=128)
    end_time = models.CharField(max_length=128)
    location = models.CharField(max_length=128)
    fare = models.CharField(max_length=128)
    favor_quantity = models.CharField(max_length=32,default= "0")
    # comment_ID = models.CharField(max_length=128,unique=True)
    def __str__(self):
        return  self.description
    class Meta:
        verbose_name_plural = "队伍"
        verbose_name  = '队伍'

@receiver(pre_delete, sender=Team)
def team_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.team_picture.delete(False)

class RecommendContest(models.Model):
    contest = {
        ("Freshman", "大一"),
        ('Sophomore', '大二'),
        ('Junior', '大三'),
        ('Senior', '大四'),

    }
    name = models.CharField(max_length=128,default="推荐比赛",primary_key=True,unique=True)#比赛名字
    sign_up_time = models.CharField(max_length= 128)
    deadline = models.CharField(max_length=128)
    category = models.CharField(max_length= 128,choices= contest,blank=False)
    context = models.CharField(max_length=256,blank=False,default='暂时没有比赛相关内容')
    file = models.FileField(upload_to='file/',verbose_name='比赛相关文件',default='avatars/2.jpg')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '推荐比赛'
        verbose_name_plural = '推荐比赛'

@receiver(pre_delete, sender=RecommendContest)
def recommend_contest_delete(sender, instance, **kwargs):
    # pass false so FileField doesn't save the model.
    instance.file.delete(False)


class Message(models.Model):
    fromName = models.CharField(max_length=128)
    room = models.CharField(max_length=32)
    content = models.CharField(max_length=256)
#
# class Comments(models.Model):
#     # comment_id = models.ForeignKey(
#     #     'Team',
#     #     on_delete=models.CASCADE,
#     # )
#
#     from_user = models.ForeignKey(
#         "User",
#         on_delete=models.CASCADE)
#     to_user = models.ForeignKey(
#         "User",
#         on_delete=models.CASCADE)
#     c_time = models.DateField(auto_now_add=True)
#     text = models.CharField(max_length=256,default="暂时没有评论")
#     content = models.ManyToManyField("Team")
#     def __str__(self):
#         return self.text
#     class Meta:
#         verbose_name_plural = "评论"
#         verbose_name = "评论"
#
#
# class Reply(models.Model):
#     # comment_id = models.ForeignKey(
#     #     'Team',
#     #     on_delete=models.CASCADE,
#     # )
#     from_user = models.ForeignKey(
#         "User",
#         on_delete=models.CASCADE)
#     to_user = models.ForeignKey(
#         "User",
#         on_delete=models.CASCADE)
#     c_time = models.DateField(auto_now_add=True)
#     text = models.CharField(max_length=256,default="暂时没有评论")
#     content = models.ForeignKey(
#         "Comments",
#     on_delete=models.CASCADE,
#     )
#     def __str__(self):
#         return self.text
#     class Meta:
#         verbose_name_plural = "回复"
#         verbose_name = "回复"
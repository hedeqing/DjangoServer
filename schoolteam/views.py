
from django.contrib import auth
from django.db import connection
from django.db.models import Q
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
# Create your views here.
from django.utils.safestring import mark_safe
from schoolteam import forms, models
from schoolteam.models import RecommendContest, Team, Users, Message

# Create your views here.
import  json
from django.core import serializers



from schoolteam.consumers import ChatConsumer


def login(request):
    pass
    return render(request, "schoolteam/web_login.html")

def index(request):
    return render(request, 'schoolteam/index.html')


def room(request, room_name):

    return render(request, 'schoolteam/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })




def judge_login(request):
    data = {}
    users = serializers.serialize("json",Users.objects.all())
    return HttpResponse(users)

def get_data(request):
    number = request.POST.get("号码")
    password = request.POST.get('密码')
    data_ok = {}
    data_not_ok = {}
    users =  Users.objects.get(number = number)
    # print(Users)
    data = {}
    # judge = check_password(str(password),str(Users.password))
    judge = password == users.password
    users1 = serializers.serialize("json",Users.objects.filter(number = number))
    print(users)
    print(judge)
    data_ok['stata'] = {'status': '1'}
    data_not_ok['stata'] = {'status': '0'}
    data = users1
    if judge:
        return  HttpResponse(data)
    else:
        return  HttpResponse(data_not_ok)

    # data_ok['stata'] = {'status': '1'}
    # data_not_ok['stata'] = {'status': '0'}
    # if judge:
    #     return HttpResponse(json.dumps(data_ok))
    # else:
    #     return  HttpResponse(json.dumps(data_not_ok))

    # else:
    #     return HttpResponse(json.dumps(data__not_ok))
    # Users = serializers.serialize("json",data1)
    # data1['response'] = Users
def sign_up(request):
    errors = []
    name = None
    password = None
    number = None
    gender = None
    status = {}
    if request.method == 'POST':
        if not request.POST.get('name'):
            errors.append('用户名不能为空')
        else:
            name = request.POST.get('name')

        if not request.POST.get('password'):
            errors.append('密码不能为空')
        else:
            password = request.POST.get('password')
        # if not request.POST.get('password2'):
        #     errors.append('确认密码不能为空')
        # else:
        #     password2 = request.POST.get('password2')
        if not request.POST.get('number'):
            errors.append('号码不能为空')
        else:
            number = request.POST.get('number')
        if not request.POST.get('gender'):
            errors.append('性别不能为空')
        else:
            gender = request.POST.get('gender')

        # if password is not None:
        #     if password == password2:
        #         gender = True
        #     else:
        #         errors.append('两次输入密码不一致')
        print(name,password,number,gender,"code_password"+make_password(password,'Password','pbkdf2_sha256'))

        if name is not None and password is not None and number is not None and gender is not None:
            users = Users.objects.create(username=name,number = number,password =password,gender = gender)
            users.save()
            print(users.save())
            if users.save():
                status['stata'] = {'status': '1'}
                return HttpResponse(json.dumps(status))
            # Userslogin = auth.authenticate(Usersname=name,password=password,number = number,gender = gender)
            # auth.login(request, Userslogin)
            else:
                status['stata'] = {'status': '0'}
                return HttpResponse(json.dumps(status))
            # return HttpResponseRedirect('/blog')


def show_recommend(request):
        education  =request.POST.get('education')
        data = {}
        contest = serializers.serialize("json",RecommendContest.objects.filter(category=education))
        print(RecommendContest.objects.filter(category=education))
        # print(contest)
        data = contest
        print(json.dumps(data))
        return HttpResponse(data)

def  get_team(request):
    team = serializers.serialize("json",Team.objects.all())
    print(team)
    return  HttpResponse(team)

def updata_avator(request):
    number  = request.POST.get("number")
    avator = request.POST.get("avator")
    print(avator)
    print(number)
    data = {}
    try:
        user = Users.objects.get(number = number)
        print(user)
        user.picture = avator
        print(user.picture)
        user.save()
        print(user)
        data['stata'] = {"status": "2"}
        print("修改头像成功")
        return HttpResponse(json.dumps(data))
    except :
        print("找不到该用户")

def get_team_by_category(request):
    if request.method == "POST":
        category = request.POST.get("category")
        data = {}
        print(category)
        team = serializers.serialize("json",Team.objects.filter(category=category))
        data = team
        print(data)
        return HttpResponse(data)

def release_team(request):
    team_id = request.POST.get("team_id")
    users = Users.objects.get(number = team_id)
    description = request.POST.get("description")
    start_time = request.POST.get("startTime")
    end_time = request.POST.get("endTime")
    location = request.POST.get("location")
    fare = request.POST.get("fareDescription")
    category = request.POST.get("category")
    imagePath = request.POST.get("image_path")
    print(imagePath)
    menber_id = users.id
    print(users.id)
    data_ok = {}
    data_not_ok = {}
    team = Team(team_id = users,description = description, start_time= start_time, end_time=end_time, location = location,fare=fare,category=category,menber_id = menber_id,team_picture=imagePath)
    team.save()
    print(team)
    data_ok['stata'] =  {'status':'1'}
    data_not_ok['stata'] =  {'status':'0'}
    if team:
        return  HttpResponse(json.dumps(data_ok))
    else:
        return  HttpResponse(json.dumps(data_not_ok))
def update(request):
    oldnumber = request.POST.get("old_number")
    oldPassword = request.POST.get("oldPassword")
    newPassword = request.POST.get("newPassword")
    new_gender = request.POST.get("new_gender")
    new_dynamic = request.POST.get("new_dynamic")
    new_name = request.POST.get("new_name")
    new_number = request.POST.get("new_number")
    # print(oldPassword)
    # print(oldnumber)
    # print(new_number)
    # print(new_dynamic)
    # print(new_gender)
    # print(new_name)
    # print(newPassword)
    users = Users.objects.get(number =oldnumber)
    print(users)
    data_ok = {}
    data_not_ok = {}
    judge = oldPassword == users.password
    # print(encode_password)
    # print("oldnumber"+oldnumber);
    # print(Users.password)
    # print(check_password(str(oldPassword), str(Users.password)))
    data_ok['stata'] = {'status': '1'}
    data_not_ok['stata'] = {'status': '0'}
    if judge:
        Users.objects.filter(number=oldnumber).update(password=newPassword, gender=new_gender,number=new_number, username=new_name, dynamic=new_dynamic)
        # print("status " + Users.update(oldPassword = newPassword,gender = new_gender,number = new_number,name = new_name,dynamic = new_dynamic))
        if Users.objects.filter(number=oldnumber).update(password=newPassword, gender=new_gender, number=new_number,
                                                     username=new_name, dynamic=new_dynamic):
            return HttpResponse(json.dumps(data_ok))
    else:
        return HttpResponse(json.dumps(data_not_ok))

def get_message(request):
    room = request.POST.get("room")
    message = Message.objects.filter(room=room)
    print(serializers.serialize("json",message))
    return HttpResponse(serializers.serialize("json",message))

def get_myteam(request):
    number  =request.POST.get('number')
    print(number)
    # number1 = '1'
    user = Users.objects.filter(number=number)
    user_id = ""
    for i in user:
        print(i.id)
        user_id = i.id
    print(user_id)
    team=Team.objects.filter(menber_id__contains=number)
    print(team)
    data = {}
    list = []
    for i in team:
        list1 = []
        str = i.menber_id
        list1 = str.split(',')
        if  number in list1:
            team = Team.objects.get(pk = i.pk)
            list.append(i.pk)
    print(list)
    return HttpResponse(serializers.serialize("json", Team.objects.filter(id__in=list)|Team.objects.filter(team_id = user_id)))

def get_name_by_id(request):
    user_id = request.POST.get("user_id")
    print(user_id)
    # user = Users.objects.get(pk_in =  )
    return  HttpResponse(serializers.serialize("json",Users.objects.get(pk__in = user_id)))

def join_team(request):
    team_id = request.POST.get("team_id")
    my_id = request.POST.get("my_id")
    # team_id = Team.objects.get(id =team_id)
    print(team_id)
    print(my_id)
    data_ok = {}
    data_not_ok = {}
    data_ok['stata'] = {'status': '1'}
    data_not_ok['stata'] = {'status': '0'}
    team=Team.objects.get(id = team_id)
    list1 = []
    id = team.menber_id
    list1 = id.split(',')
    print(list1)
    if my_id in list1:
        return HttpResponse(json.dumps(data_not_ok))
    else:
        team.menber_quantity = int(team.menber_quantity)+1
        team.menber_id = team.menber_id+","+str(my_id)
        team.save()
        return  HttpResponse(json.dumps(data_ok))
def search(request):
    text = request.POST.get("text")
    # text = '找对象'
    print(text)
    team = Team.objects.filter(description__contains=text)
    team = serializers.serialize("json",team)
    print(team)
    return HttpResponse(team)
#web server
def web_admin(request):
    pass
    return  render(request,"schoolteam/web_admin.html")
def web_index(request):
    pass
    return  render(request,"schoolteam/web_index.html")

def web_login(request):
    if request.session.get("is_login",None):#不允许重复登陆
        return  redirect("/index/")
    if request.method == 'POST':
        login_form = forms.UserForm(request.POST)
        message = '请检查填写的内容！'
        print(login_form)
        print(login_form.is_valid())

        if login_form.is_valid():
            number = login_form.cleaned_data.get('number')
            password = login_form.cleaned_data.get('password')

            try:
                user = models.Users.objects.get(number=number)
            except :
                message = '用户不存在！'
                # return render(request, 'schoolteam/web_admin.html', locals())

            if user.password == password:
                request.session['is_login'] = True
                request.session['user_id'] =user.id
                request.session['user_username'] = user.username
                return redirect('/web_admin/')
            else:
                message = '密码不正确！'
                # return render(request, 'schoolteam/web_admin.html', locals())
        else:
            return render(request, 'schoolteam/web_login.html',{"login_form":login_form}, locals())

    login_form = forms.UserForm()
    return render(request, 'schoolteam/web_login.html',{"login_form":login_form}, locals())

def web_register(request):
    if request.session.get('is_login',None):
        return  redirect("/web_index/")
    if request.method=="POST":
        register_form = forms.MyRegisterForm(request.POST)
        print(register_form)
        print(register_form.is_valid())
        # message = "请检查填写的内容"
        if register_form.is_valid():
            name = register_form.cleaned_data.get("username")
            number = register_form.cleaned_data.get("number")
            password1 = register_form.cleaned_data.get("password1")
            password2 = register_form.cleaned_data.get('password2')
            # email = register_form.cleaned_data.get('email')
            dynamic = register_form.cleaned_data.get('dynamic')
            gender = register_form.cleaned_data.get('sex')

            if password1 != password2:
                message = "两次输入的密码不同"
                return  render(request, 'schoolteam/web_register.html', locals())
            else:
                same_name_user = models.Users.objects.filter(number=number)
                if same_name_user:
                    message  = "用户已经存在"
                    return  render(request, 'schoolteam/web_register.html', locals())
                # same_email_user  = models.Users.objects.filter(email = email)
                # if same_email_user:
                #     message = "该邮箱已经被注册"
                #     return  render(request, 'schoolteam/web_register.html', locals())

                new_user = models.Users()
                new_user.username = name
                new_user.number = number
                new_user.password = password1
                new_user.dynamic =dynamic
                new_user.gender = gender
                new_user.save()
                print(new_user)
                message = "注册成功"
                return render(request,"schoolteam/web_login.html",locals())
        else:
            return  render(request, 'schoolteam/web_register.html')
    register_form = forms.MyRegisterForm()
    return render(request, 'schoolteam/web_register.html',{"register_form":register_form})


def logout_web(request):
    if not request.session.get('is_login',None):
        return redirect('/web_index/')
    request.session.flush()
    return redirect("/web_login/")

def test(request):
    user = Users.objects.all()
    return  render(request,"schoolteam/test.html",{"user":user})
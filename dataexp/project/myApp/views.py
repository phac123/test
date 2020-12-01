from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth import logout
from django.http import HttpResponseRedirect,JsonResponse
from django.shortcuts import redirect

# Create your views here.
from django.http import HttpResponse
from .models import Users

#主页
def index(request):   #请求：浏览器给服务器的东西
    #取session
    username = request.session.get('name','游客')  #如果没有取出来name的数值，则为后面的”游客“
    account = request.session.get('account', '123')
    return render(request, 'myApp/index.html', {
        'username':username, 'account':account
    })

def index1(request):   #请求：浏览器给服务器的东西
    # print("sdfdsf")
    return redirect('/dataex/index')

#注册
def to_register(request):   #转到用户注册
    return render(request, "myApp/register.html")
def register(request):     #注册页面点击注册
    account = request.POST.get('account')
    password = request.POST.get('password')
    name = request.POST.get('username')
    age = request.POST.get('age')
    gender = request.POST.get('gender')
    hobby = "无"
    isDelete = False

    users = Users.objects.all()
    f = False
    for user1 in users:
        if(user1.uaccount == account):
            f = True
            break

    if(f == True):
        return redirect('/dataex/to_register')
    print("sss")
    user = Users.createUser(account, password, name, age, gender, hobby, isDelete)
    user.save()
    # return HttpResponse(user.uage + "  "  + user.ugender)
    return redirect('/dataex/index')

#登录
def to_login(request):
    return render(request, "myApp/login.html")
def login(request):
    userAccount = request.POST.get('account')
    userPassword = request.POST.get('password')
    users = Users.objects.all()
    f = False
    for user in users :
        if(userAccount == user.uaccount):
            if(userPassword == user.upassword):
                f = True

    if(f):
        return redirect('/dataex/to_dataset')
    return redirect('/dataex/to_login')

#数据集选择
def to_dataset(request):
    return render(request, "myApp/datasetSelect.html")

#数据属性选择
def to_dataAttr(request):
    return render(request, "myApp/dataAttr.html")

#样本反馈
def to_feedback(request):
    return render(request, "myApp/feedback.html")

#打标签后的数据发聩
def dataFeedback(request):
    return render(request, 'myApp/ends.html')

#退出登录
from django.contrib.auth import logout
def quit(request):
    #清除session
    logout(request)  #方式1
    # request.session.clear()  #方式2
    # request.session.flush()  #方式3
    return redirect('/dataex/index')



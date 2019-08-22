from django.http import HttpResponse

def login(request):
    if request.method == 'POST':
        code=request.GET.get("code")
        # if no this code in database:
        #   return regist
        return HttpResponse("code: %s"%(code))

def regist(request):
    if request.method == 'POST':
        code=request.GET.get("code")
        #use wechat api to get openid
        openid="testtestets"
        nickname=request.GET.get("nickname")
        avatarUrl="default.def"
        description=request.GET.get("description")
        school=request.GET.get("school")
        grade=request.GET.get("grade")
        coin=30
        new_user = {'openid':openid,'nickname':nickname,'avatarUrl':avatarUrl,'description':description,'school':school,'grade':grade,'coin':coin}
        models.User.objects.create(**new_user)
        return HttpResponse("OK ")

from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from django.template import RequestContext, loader
from .models import Verify_number, User_phone_number
from django.http import Http404


def index(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/home')
    template = loader.get_template('login_page/index.html')
    context = RequestContext(request, {
        'request': request,
    })
    return HttpResponse(template.render(context)) 

def first_page_phone(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/home')
    template = loader.get_template('login_page/index.html')
    context = RequestContext(request, {
        'request': request,
    })
    return HttpResponse(template.render(context)) 

# /usr/bin/env python
# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import TwilioRestClient
import random, string

def send_sms_verification_code(to_num,from_num,code):
    # Find these values at https://twilio.com/user/accoun
    account_sid = twilio_sid #put your own
    auth_token = twilio_password #put your own
    client = TwilioRestClient(account_sid, auth_token)
    msg = " Your Code is "+ code
    message = client.messages.create(to=to_num, from_=from_num, body=msg) #client.messages.create(to="2132907861", from_="+18187228353", body="Verification Code")
    


def check_number(request,country_code,numb):
    phone_number = '+'+country_code+numb
    user_num = User_phone_number.objects.filter(phone_number=phone_number).first()
    
    #if no register user with this num
    if not user_num:
        #check if waiting for validation:
        verifible_number = Verify_number.objects.filter(phone_number=phone_number).first()
        if verifible_number:
            #delete it 
            verifible_number.delete()
        #generate verification code
        code=''.join(random.choice(string.digits) for _ in range(5))#string.ascii_lowercase + 
        #create new one
        new_numb = Verify_number(phone_number=phone_number,is_verified=False, verification_code=code)
        new_numb.save()

        
        #send via sms
        from_num="+18187228353"
        #send_sms_verification_code(phone_number,from_num,code)
        print "text sent - remove # for actually sending"

        #verification page
        url='/verification_page/'+country_code+numb
        return HttpResponseRedirect(url)

    else:
        #verification page
        url='/login/'+country_code+numb
        return HttpResponseRedirect(url)


def verification_page(request,phone_num):
    template = loader.get_template('login_page/verification_page.html')
    context = RequestContext(request, {
        'request': request,
        'phone_number':phone_num,
    })
    return HttpResponse(template.render(context)) 


def verify_code(request,numb,code):
    phone_number='+'+numb
    verifible_number = Verify_number.objects.filter(phone_number=phone_number).first()
    if not verifible_number:
        raise Http404("No number matches the given query.") 
    if verifible_number.verification_code!=code:
        raise Http404("Wrong Code") 
    elif False:#if too long has passed
        pass
    else:
        verifible_number.is_verified=True
        verifible_number.save()
        #create account
        url='/register/'+numb
        return HttpResponseRedirect(url) 




from django.contrib import auth
#from django.core.context_processors import csrf #deprecated
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response

@csrf_protect
def login(request,numb):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/home')
    else:
        phone_number='+'+numb
        user_phone_numb= User_phone_number.objects.filter(phone_number=phone_number).first()
        username= user_phone_numb.user.username
        c = {'username':username}
        #c.update(csrf(request))
        return render(request, "login_page/enter_password.html", c)
       # return render_to_response('login_tab/login.html', context_instance=RequestContext(request))

def auth_view(request):
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    user = auth.authenticate(username=username,password=password)
    
    if user is not None:
        auth.login(request,user)
        return HttpResponseRedirect('/')
    else:
        raise Http404("Invalid password") 


from forms import MyRegistrationForm

def register(request,numb):
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        if form.is_valid():

            u_name = form.cleaned_data.get('email')#('username')
            u_pass = form.cleaned_data.get('password2')
            new_user = form.save()
            user = auth.authenticate(username=u_name,
                                     password=u_pass)
            #login after registration
            auth.login(request, user)

            #create phone number related field
            phone_number='+'+numb
            user_phone_numb= User_phone_number(phone_number=phone_number,user=user)
            user_phone_numb.save()

            return HttpResponseRedirect("/home")
    else:
        form = MyRegistrationForm()
    return render(request, "login_page/register.html", {
        'form': form,
        'request': request,
    })


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")
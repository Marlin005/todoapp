from accounts.forms import LoginForm, ProfileEditForm, RegistrationForm, UserEditForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.views import View
# from django.shortcuts import render, redirect, reverse
# from django.urls import reverse_lazy
# from django.views import generic
#from django.core.mail import EmailMessage
#from django.core.email import send_mail
#from django.core.mail import BadHeaderError, send_mail
#from django.core.mail import get_connection, send_mail
#from django.core.mail.message import EmailMessage
#import smtplib


class LoginView(View):
    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password']
                                )
            if user is None:
                return HttpResponse('Неправильный логин и/или пароль')
            if not user.is_active:
                return HttpResponse('Ваш аккаунт заблокирован')

            login(request, user)
            return HttpResponse('Добро пожаловать! Успешный вход')
        return render(request, 'accounts/login.html', {'form': form})

    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, 'accounts/login.html', {'form': form})


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data["password"])
            new_user.save()
            #Profile.objects.create(user=new_user)

            return render(request, "accounts/registration_complete.html",
                          {"new_user": new_user})
    else:
        form = RegistrationForm()
    return render(request, "accounts/register.html", {"user_form": form})


# class SignUpView(generic.CreateView):
 #   form_class = UserCreationForm
  #  success_url = reverse_lazy('login')
# template_name = 'accounts/signup.html'

@login_required
def edit(request):
    if request.method == "POST":
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(
            instance=request.user.profile, data=request.POST,
            files=request.FILES
        )
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    return render(
        request,
        "accounts/edit.html",
        {"user_form": user_form, "profile_form": profile_form},
    )


# send_mail(
 #   'Subject',
  #  'Message.',
   # 'from@example.com',
   # ['john@example.com', 'jane@example.com'],
# )

# send_mail("Привет от django", "Письмо отправленное из приложения",
# settings.EMAIL_HOST_USER, ["zgozgo500@gmail.com"], fail_silently=False)

# def send_email(request):
 #   subject = request.POST.get('subject', '')
  #  message = request.POST.get('message', '')
   # from_email = request.POST.get('from_email', '')
    # if subject and message and from_email:
    #   try:
    #      send_mail(subject, message, from_email, ['admin@example.com'])
    # except BadHeaderError:
    #    return HttpResponse('Invalid header found.')
    # return HttpResponseRedirect('/contact/thanks/')
   # else:
    # In reality we'd use a form class
    # to get proper validation errors.
    #    return HttpResponse('Make sure all fields are entered and valid.')


# msg = EmailMessage(
 # subject=u'Тема письма',
  #body=u'тело сообщения тут',
  # from_email='yandexUser@ya.ru',
  # to=('email_to@gmail.com',),
  #headers={'From': 'email_from@me.com'}
# )
#msg.content_subtype = 'html'
# msg.send()

# send_mail('Django mail', 'This e-mail was send with Django.',
#          'yandexUser@ya.ru', ['mySecondMail@gmail.com'], fail_silently=False)


# def sendMail(email_from, email_to, subject, text):
 #   server = smtplib.SMTP("smtp.yandex.ru", 587)
  #  server.ehlo()
   # server.starttls()
    #server.login("myYandexAccount", "o_MyPassword")
   # message = "\r\n".join([ \
    #    "From: {}".format(email_from), \
    #   "To: {}".format(email_to), \
    #  "Subject: {}".format(subject), \
    # "", \
    #"{}".format(text) \
    # ])
   # server.sendmail("myYandexAccount@ya.ru", email_to, message)
   # server.quit()

# sendMail(
 #   'email_from@gmail.com',
  #  'email_to@gmail.com',
   # 'subject message',
    #'body text here...'
# )

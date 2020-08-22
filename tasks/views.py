from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from tasks.forms import AddTaskForm, TodoItemExportForm, TodoItemForm
from tasks.models import TodoItem


#import smtplib
"""
Class-based views
"""
# #Создаём класс, наследуемый от ListView
# class TaskListView(ListView):
# Указываем запрос, по которому будем доставать элементы из базы (поле queryset)
#     queryset = TodoItem.objects.all()
# # Указываем, как в шаблоне будут называться объекты,
# # которые мы достали из базы (context_object_name)
#     context_object_name = "tasks"
# #Указываем, как называется шаблон (template_name)
#     template_name = "tasks/list.html"

# нераспределённые таски в админке
# class TaskListView(ListView):
#    queryset = TodoItem.objects.all()
#    context_object_name = "tasks"
#    template_name = "tasks/list.html"
# Создаем и наследуем класс от View


#@ login_required
def index(request):
    return HttpResponse("Примитивный ответ из приложения tasks")


def complete_task(request, uid):
    t = TodoItem.objects.get(id=uid)
    t.is_completed = True
    t.save()
    return HttpResponse("OK")


def delete_task(request, uid):
    t = TodoItem.objects.get(id=uid)
    t.delete()
    messages.success(request, "Задача удалена")
    return redirect(reverse("tasks:list"))


def add_task(request):
    if request.method == "POST":
        desc = request.POST["description"]
        t = TodoItem(description=desc)
        t.save()
    return reverse("tasks:list")
    # return redirect("/tasks/list")


class TaskListView(LoginRequiredMixin, ListView):
    model = TodoItem
    context_object_name = "tasks"
    template_name = "tasks/list.html"

    def get_queryset(self):
        u = self.request.user
        qs = super().get_queryset()
        return qs.filter(owner=u)

    # def get_queryset(self):
    #   qs = super().get_queryset()
    #  u = self.request.user
    # if u.is_anonymous:
    #    return []
    #   return qs.filter(owner=u)

# 2способ  мы находимся внутри защищённого логином окружения с mixin, мы можем
# убрать проверку на анонимность пользователя

    #def get_queryset(self):
     #   u = self.request.user
      #  if u.is_anonymous:
       #     return []
        #return u.tasks.all()

# форма без owner
# class TaskCreateView(View):
    # def my_render(self, request, form):
        # return render(request, "tasks/create.html", {"form": form})

 #   def post(self, request, *args, **kwargs):
  #      form = TodoItemForm(request.POST)
   #     if form.is_valid():
    #        form.save()
     #       #return reverse("/tasks/list")
      #      return reverse("tasks:list")
       # #return render(request, "tasks/list.html")
        # return render(request, "tasks/create.html", {"form": form})

#    def get(self, request, *args, **kwargs):
 #       form = TodoItemForm()
  #      #return self.my_render(request, form)
   #     return render(request, "tasks/create.html", {"form": form})

        # )


class TaskCreateView(View):
    def post(self, request, *args, **kwargs):
        form = TodoItemForm(request.POST)
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.owner = request.user
            new_task.save()
            return redirect(reverse("tasks:list"))

        return render(request, "tasks/create.html", {"form": form})

    def get(self, request, *args, **kwargs):
        form = TodoItemForm()
        return render(request, "tasks/create.html", {"form": form})


class TaskDetailsView(DetailView):
    model = TodoItem
    template_name = 'tasks/details.html'


"""
Function based view
"""


class TaskEditView(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        t = TodoItem.objects.get(id=pk)
        form = TodoItemForm(request.POST, instance=t)
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.owner = request.user
            new_task.save()
            return redirect(reverse("tasks:list"))

        return render(request, "tasks/edit.html", {"form": form, "task": t})

    def get(self, request, pk, *args, **kwargs):
        t = TodoItem.objects.get(id=pk)
        form = TodoItemForm(instance=t)
        return render(request, "tasks/edit.html", {"form": form, "task": t})


# def tasks_list(request):
#    all_tasks = TodoItem.objects.all()
#    return render(
#        request,
#        'tasks/list.html',
#        {'tasks': all_tasks}
#    )


# Модельная форма


# Обычная форма
# def task_create(request):
#     if request.method == "POST":
#         form=AddTaskForm(request.POST)
#         if form.is_valid():
#             cd=form.cleaned_data
#             desc=cd["description"]
#             t=TodoItem(description = desc)
#             t.save()
#             return redirect("/tasks/list")
#     else:
#        form=AddTaskForm()
#     return render(request, "tasks/create.html", {"form": form})


# def sendMail(email_from, email_to, subject, text):
    #server = smtplib.SMTP("smtp.yandex.ru", 587)
 #   server = smtplib.SMTP("z@gmail.com", 587)
  #  server.ehlo()
   # server.starttls()
    #server.login("х@yandex.com", "")
    #server.login("х@gmail.com", "")
   # message = "\r\n".join([
    #    "From: {}".format(email_from),
    #   "To: {}".format(email_to),
    #  "Subject: {}".format(subject),
    # "",
    # "{}".format(text)
    # ])
    #server.sendmail("х@gmail.com", email_to, message)
    # server.quit()


# sendMail(
    # 'х@gmail.com',
   # 'х@gmail.com',
  #  'subject message',
 #   'body text here...'
# )

class TaskExportView(LoginRequiredMixin, View):
    def generate_body(self, user, priorities):
        q = Q()
        if priorities["prio_high"]:
            q = q | Q(priority=TodoItem.PRIORITY_HIGH)
        if priorities["prio_med"]:
            q = q | Q(priority=TodoItem.PRIORITY_MEDIUM)
        if priorities["prio_low"]:
            q = q | Q(priority=TodoItem.PRIORITY_LOW)
        tasks = TodoItem.objects.filter(owner=user).filter(q).all()

        body = "Ваши задачи и приоритеты:\n"
        for t in list(tasks):
            if t.is_completed:
                body += f"[x] {t.description} ({t.get_priority_display()})\n"
            else:
                body += f"[ ] {t.description} ({t.get_priority_display()})\n"

        return body

    def post(self, request, *args, **kwargs):
        form = TodoItemExportForm(request.POST)
        if form.is_valid():
            email = request.user.email
            body = self.generate_body(request.user, form.cleaned_data)
            send_mail("Задачи", body, settings.EMAIL_HOST_USER, [email])
            messages.success(
                request, "Задачи были отправлены на почту %s" % email)
        else:
            messages.error(request, "Что-то пошло не так, попробуйте ещё раз")
        return redirect(reverse("tasks:list"))

    def get(self, request, *args, **kwargs):
        form = TodoItemExportForm()
        return render(request, "tasks/export.html", {"form": form})


#send_mail("Привет от django", "Письмо отправленное из приложения",
#settings.EMAIL_HOST_USER, ["х@gmail.com"], fail_silently=False)


#EMAIL_HOST = os.environ.get("EMAIL_HOST")
#EMAIL_PORT = int(os.environ.get("EMAIL_PORT"))
#EMAIL_USE_TLS = True
#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
#!/usr/bin/env python
from django import forms
from tasks.models import TodoItem


class AddTaskForm(forms.Form):
    description = forms.CharField(max_length=64, label="")


class TodoItemForm(forms.ModelForm):
    class Meta:
        model = TodoItem
        fields = ("description", "priority")
        labels = {"description": "Описание", "priority": ""}


class TodoItemExportForm(forms.Form):
    prio_high = forms.BooleanField(
        label="высокая важность", initial=True, required=False
    )
    prio_med = forms.BooleanField(
        label="средней важности", initial=True, required=False
    )
    prio_low = forms.BooleanField(
        label="низкой важности", initial=False, required=False
    )


#class Profile(models.Model):
 #   user = models.OneToOneField(User, on_delete=models.CASCADE)
  #  birthdate = models.DateField(blank=True, null=True)

   # def __str__(self):
    #    return "Профиль пользователя %s" % self.user.username

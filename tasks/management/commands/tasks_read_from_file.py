#!/usr/bin/env python
# coding: utf-8
from django.core.management import BaseCommand
from datetime import datetime
from tasks.models import TodoItem


class Command(BaseCommand):
    help = u"Read tasks from file (one line = one task)and save them to db"


    def add_arguments(self, parser):
        parser.add_argument('--file', dest='input_file', type=str)


    def handle(self, *args, **options):
        now = datetime.now(timezone.utc)
        file_path = "/Library/Frameworks/Python.framework/Versions/3.8/bin/todoapp/tasks/management/commands/input.txt"
        my_file = open(file_path, 'r')
        for t in my_file:
            t = TodoItem(description = t, created = now)
            t.safe()
            response = HttpResponse(my_file.read(), mimetype='text/plain')
            response['Content-Disposition'] = 'inline;filename=input.txt'
        return response
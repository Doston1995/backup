from django.shortcuts import render
import contextlib
from django.core.management import call_command
from django.http import HttpResponse
import subprocess


def index(request):
    return render(request, 'index.html')


def backup(request):
    call_command('dbbackup', compress=True, interactive=False)
    return HttpResponse('success')

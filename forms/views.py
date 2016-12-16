from django.shortcuts import render, redirect
from django.http import HttpResponse
from forms import TitleForm, UploadFileForm
from channels.handler import AsgiHandler
import time


def handle_upload_file(f):
    with open('forms/storage/{}'.format(f.name), 'wb+') as dest:
        for chunk in f.chunks():
            dest.write(chunk)


def index(request):
    time.sleep(1)
    return HttpResponse('Ok!')


def custom_form_view(request):
    if request.method == 'POST':
        form = TitleForm(request.POST)
        if form.is_valid():
            # form.save()
            return redirect('/forms')
    else:
        form = TitleForm()
    time.sleep(2)
    return render(request, 'forms/form.html', {'form': form.as_p(),
                                               'action': '/forms/custom'})


def upload_form_view(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_upload_file(request.FILES['file'])
            return redirect('/forms')
    else:
        form = UploadFileForm()
    return render(request, 'forms/form.html', {'form': form.as_ul(),
                                               'action': '/forms/upload'})


def http_consumer(message):
    response = HttpResponse("Hello world! You asked for {}"
                            .format(message.content['path']))
    for chunk in AsgiHandler.encode_response(response):
        message.reply_chanel.send(chunk)

from django.shortcuts import get_object_or_404, redirect, render
from landing.models import *
from .forms import *
from landing.models import *
from .storage_backends import PublicMediaStorage as MediaStorage
import os
from django.contrib.auth.decorators import login_required

@login_required(redirect_field_name='landing-index')
def index(request):
    content = {
        'title':'Dashboard Web Alive',
        #'visitantes': Visitante.objects.all()
    }
    return render(request, 'admin2/dashboard.html', content)

@login_required(redirect_field_name='index')
def landing(request):
    carrocel = Carrocel.objects.all()
    landing = get_object_or_404(Landing, id = 1)
    content = {
        'title' :'Admin - Landing Page',
        'landing' : landing,
        'carrocel': carrocel,
    }
    return render(request, "admin2/landing.html", content)

@login_required(redirect_field_name='landing-index')
def addLanding(request):
    
    forma = addLandingForm()
    content = {
        'title':'Add Landing',
        'form': forma,
    }
    if request.method == "POST":
        formss = addLandingForm(request.POST, request.FILES )
        if formss.is_valid:
            title = request.POST['title']
            mensagemFlayer1 = request.POST['mensagemFlayer1']
            mensagemFlayer2 = request.POST['mensagemFlayer2']
            file_obj = request.FILES['imagem']

            # do your validation here e.g. file size/type check

            # organize a path for the file in bucket
            file_directory_within_bucket = 'user_upload_files/{username}'.format(username=request.user)

            # synthesize a full file path; note that we included the filename
            file_path_within_bucket = os.path.join(
                file_directory_within_bucket,
                file_obj.name
            )

            media_storage = MediaStorage()
            media_storage.save(file_path_within_bucket, file_obj)
            file_url = media_storage.url(file_path_within_bucket)

            landing = Landing(id = 1, title = title, mensagemFlayer1 = mensagemFlayer1 , mensagemFlayer2 = mensagemFlayer2, imagem = file_url)
            landing.save()

            return redirect('https://192.168.15.4:80/administration')
    return render(request, 'admin2/addLanding.html', content)

@login_required(redirect_field_name='landing-index')
def addCarrocel(request):
    
    forma = addCarrocelForm()
    content = {
        'title':'Add Landing',
        'form': forma,
    }
    if request.method == "POST":
        formss = addCarrocelForm(request.POST, request.FILES )
        if formss.is_valid:
            nome = request.POST['nome']
            file_obj = request.FILES['imagem']

            # do your validation here e.g. file size/type check

            # organize a path for the file in bucket
            file_directory_within_bucket = 'user_upload_files/{username}'.format(username=request.user)

            # synthesize a full file path; note that we included the filename
            file_path_within_bucket = os.path.join(
                file_directory_within_bucket,
                file_obj.name
            )

            media_storage = MediaStorage()
            media_storage.save(file_path_within_bucket, file_obj)
            file_url = media_storage.url(file_path_within_bucket)

            carrocel = Carrocel( nome = nome, imagem = file_url)
            carrocel.save()

            return redirect('https://192.168.15.4:80/administration')
    return render(request, 'admin2/addCarrocel.html', content)

@login_required(redirect_field_name='landing-index')
def delCarrocel(request, id):
    carrocel = get_object_or_404(Carrocel, id = id)
    carrocel.delete()
    return redirect(index)

@login_required(redirect_field_name='landing-index')
def addService(request):
    if request.method == 'POST':
        form = addServiceForm(request.POST, request.FILES)
        if form.is_valid:
            file_obj = request.FILES['imagem']

            # do your validation here e.g. file size/type check

            # organize a path for the file in bucket
            file_directory_within_bucket = 'user_upload_files/{username}'.format(username=request.user)

            # synthesize a full file path; note that we included the filename
            file_path_within_bucket = os.path.join(
                file_directory_within_bucket,
                file_obj.name
            )

            media_storage = MediaStorage()
            media_storage.save(file_path_within_bucket, file_obj)
            file_url = media_storage.url(file_path_within_bucket)
            url = request.POST['url']
            nome = request.POST['nome']
            descricao = request.POST['descricao']
            icon = request.POST['icon']
            texto = request.POST['texto']
            service = Servicos(url = url, nome = nome, descricao = descricao, icon = icon, texto = texto, imagem = file_url)
            service.save()
            return redirect(index)
    return render(request, 'admin2/addService.html')

@login_required(redirect_field_name='landing-index')
def delService(request, id):
    service = get_object_or_404(Servicos, id = id)
    service.delete()
    return redirect(index)

@login_required(redirect_field_name='landing-index')
def service(request):
    servicos = Servicos.objects.all()
    content = {
        'title':'Serviços / Admin',
        'servicos':servicos,
        
    }
    return render(request, 'admin2/service.html', content)

@login_required(redirect_field_name='landing-index')
def addTag(request):
    if request.method == 'POST':
        form = addTagServiceForm(request.POST)
        if form.is_valid:
            tag = request.POST['tag']
            tagS = Tag(tag=tag)
            tagS.save()

            return redirect(index)
    return render(request, 'admin2/addTag.html')
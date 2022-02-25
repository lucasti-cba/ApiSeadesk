from django import forms


class addLandingForm(forms.Form):
    title =  forms.CharField(max_length=50)
    mensagemFlayer1 =  forms.CharField(max_length=250)
    mensagemFlayer2 =  forms.CharField(max_length=250)
    imagem =  forms.ImageField()

class addCarrocelForm(forms.Form):
    nome =  forms.CharField(max_length=50)
    imagem =  forms.ImageField()

class DeletionForm(forms.Form):
    id = forms.IntegerField()

class addServiceForm(forms.Form):
    url =  forms.CharField(max_length=20)
    nome =  forms.CharField(max_length=50)
    descricao =  forms.CharField(max_length=500)
    icon =  forms.CharField(max_length=30)
    texto =  forms.CharField(max_length=5000)


class addTagServiceForm(forms.Form):
    tag =  forms.CharField(max_length=50)
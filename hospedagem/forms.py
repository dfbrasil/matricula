from django.forms import ModelForm
from django import forms
from .models import Hospedagem

class HospedagemForm(ModelForm):

    class Meta:
        model = Hospedagem
        fields = '__all__'
        widgets = {
            'cliente' : forms.TextInput(attrs={'class': 'form-control' }),
            'data_entrada' : forms.TextInput(attrs={'class': 'form-control' }),
            'data_saida' : forms.EmailInput(attrs={'class': 'form-control' }),
            'quarto': forms.Select(attrs={'class': 'form-control' }),
            'valor': forms.Select(attrs={'class': 'form-control' })
        }

class HospedagemFilterForm(forms.Form):
    cliente = forms.CharField(max_length=150, required=False)
    # cidade = forms.ModelChoiceField(queryset=Cidade.objects.all(), required=False)
    # curso = forms.ModelChoiceField(queryset=Curso.objects.all(), required=False)
    
    # adicionar a classe form-control para todos os campos
    def __init__(self, *args, **kwargs):
        super(HospedagemFilterForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

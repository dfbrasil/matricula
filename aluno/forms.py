from django.forms import ModelForm
from django import forms
from .models import Aluno,Curso

class AlunoForm(ModelForm):

    class Meta:
        model = Aluno
        fields = '__all__'
        widgets = {
            'nome_aluno' : forms.TextInput(attrs={'class': 'form-control' }),
            'endereco' : forms.TextInput(attrs={'class': 'form-control' }),
            'email' : forms.EmailInput(attrs={'class': 'form-control' }),
            'cidade': forms.Select(attrs={'class': 'form-control' }),
            'curso': forms.Select(attrs={'class': 'form-control' }),
            'imagem' : forms.FileInput(attrs={'class': 'form-control' }),
            'valor' : forms.TextInput(attrs={
                'class': 'mask-money form-control',
                'maxlength': 500,
                'placeholder': '00,00'
            }),
        }

class CursoForm(ModelForm):
    class Meta:
        model = Curso
        fields='__all__'
        widgets = {
            'nome' : forms.TextInput(attrs={'class': 'form-control' }),
        }
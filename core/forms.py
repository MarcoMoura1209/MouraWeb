from django import forms
from .models import Cliente


class Form(forms.ModelForm):
    class Meta:
        model = Cliente

        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'campo-nome campo',
                'placeholder': 'Seu nome'}),

            'email': forms.EmailInput(attrs={
                'class': 'campo-email campo',
                'placeholder': 'seu@email.com'}),

            'mensagem': forms.Textarea(attrs={
                'class': 'campo-mensagem campo',
                'placeholder': 'Descreva o que você tem em mente...',
                'maxlength': '1500'}),
        }

        def clean_mensagem(self):
            mensagem = self.cleaned_data.get('mensagem')
            if len(mensagem) > 1500:
                raise forms.ValidationError(
                    'A mensagem deve ter no máximo 1500 caracteres.')
            return mensagem

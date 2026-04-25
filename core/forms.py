from django import forms
from .models import Cliente


class Form(forms.ModelForm):
    class Meta:
        model = Cliente

        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'campo-nome',
                'placeholder': 'Seu nome'}),

            'email': forms.EmailInput(attrs={
                'class': 'campo-email',
                'placeholder': 'seu@email.com'}),

            'mensagem': forms.Textarea(attrs={
                'class': 'campo-mensagem',
                'placeholder': 'Descreva o que você tem em mente...'})
        }

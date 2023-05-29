from django import forms

class ArticuloFormulario(forms.Form):
    titulo = forms.CharField(max_length=200)
    subtitulo = forms.CharField(max_length=200)
    cuerpo = forms.CharField(widget=forms.Textarea(attrs={'class': 'ArchivoFormulario'}))
    autor = forms.CharField(max_length=64)
    fecha = forms.DateField(
        input_formats=['%Y-%m-%d'],
        widget=forms.DateInput(format='%Y-%m-%d'),
        label='Fecha (YYYY-MM-DD)'
    )
    imagen = forms.ImageField(required=False)
    descripcion = forms.CharField(widget=forms.Textarea(attrs={'class': 'ArchivoFormulario'}))

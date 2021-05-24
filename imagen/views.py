from imagen.forms.imagenForm import DocumentForm
from django.shortcuts import render, redirect


def create(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            return render(request, 'formsImagen.html', {'form': form, 'img_obj': img_obj})
    else:
        form = DocumentForm()
    return render(request, 'formsImagen.html', {'form': form})


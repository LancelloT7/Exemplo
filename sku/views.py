from django.shortcuts import render, redirect
from .models import Sku, ModeloSufixo
from django.contrib import messages



def cadSku(request):
    sku_instance = None
    sufixos = []
    
    if request.method == 'POST':
        sku_input = request.POST.get('sku').strip()  # Captura o SKU digitado
        try:
            sku_instance = Sku.objects.get(sku=sku_input)
            sufixos = sku_instance.sufixos.all()  # Acesso aos sufixos existentes

            if 'modelo_sufixo' in request.POST:
                modelo_sufixo_input = request.POST.get('modelo_sufixo').strip()
                new_sufixo = ModeloSufixo(sku=sku_instance, sufixo=modelo_sufixo_input)
                new_sufixo.save()
                messages.success(request, 'Novo sufixo cadastrado com sucesso!')

        except Sku.DoesNotExist:
            if 'modelo_revenda' in request.POST and 'modelo_sufixo' in request.POST:
                modelo_revenda = request.POST.get('modelo_revenda').strip()
                new_sku = Sku(sku=sku_input, modelo_revenda=modelo_revenda)
                new_sku.save()
                
                modelo_sufixo_input = request.POST.get('modelo_sufixo').strip()
                new_sufixo = ModeloSufixo(sku=new_sku, sufixo=modelo_sufixo_input)
                new_sufixo.save()
                messages.success(request, 'SKU, modelo revenda e sufixo cadastrados com sucesso!')

    return render(request, 'cadastro_sku.html', {
        'sku_instance': sku_instance,
        'sufixos': sufixos,
    })
    

  
from django.shortcuts import render

def base_view(request):
    """
    Renderiza a página inicial.
    """
    return render(request, 'base.html')

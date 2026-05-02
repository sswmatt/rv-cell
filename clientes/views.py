from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Cliente


def home(request):
    if request.method == 'POST':
        Cliente.objects.create(
            nome_completo=request.POST.get('nome'),
            idade=request.POST.get('idade'),
            telefone=request.POST.get('telefone')
        )

    return render(request, 'home.html')

def lista_clientes(request):
    return render(request, 'lista.html')


def api_clientes(request):
    clientes = list(Cliente.objects.values())
    return JsonResponse(clientes, safe=False)



def deletar_cliente(request, id):
    if request.method == "POST":
        cliente = get_object_or_404(Cliente, id=id)
        cliente.delete()
        return JsonResponse({"status": "ok"})

    return JsonResponse({"status": "erro"}, status=400)


def editar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)

    if request.method == "GET":
        return JsonResponse({
            "nome": cliente.nome_completo,
            "idade": cliente.idade,
            "telefone": cliente.telefone
        })

    if request.method == "POST":
        cliente.nome_completo = request.POST.get("nome")
        cliente.idade = request.POST.get("idade")
        cliente.telefone = request.POST.get("telefone")
        cliente.save()

        return JsonResponse({"status": "ok"})
    


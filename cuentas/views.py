from multiprocessing import context
from django.shortcuts import render, redirect
from django.urls import reverse
from . import forms
from database import models as models_db

# Create your views here.
def paquetes(request):
    form = forms.SelectorForm
    if request.method == "POST":
        form = form(data=request.POST)

        if form.is_valid():
            # Tipo Cliente solicitado
            tipo_cliente_id = request.POST.get("tipo_cliente", "")

            # recuperamos el último cliente
            cliente_id = (
                models_db.Cliente.objects.using("homebanking")
                .values("customer_id")
                .all()
                .last()
            )

            # Cargamos el tipo de cliente seleccionado
            models_db.Cliente.objects.using("homebanking").filter(
                customer_id=cliente_id["customer_id"]
            ).update(tipo_cliente=tipo_cliente_id)

            return redirect(reverse("login"))
    return render(request, "cuentas/paquetes.html", {"form": form})

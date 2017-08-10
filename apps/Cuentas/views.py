from django.shortcuts import render
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.core.urlresolvers import reverse_lazy
from django.views.generic.detail import DetailView
import json
import requests

from apps.Cuentas.models import Tipos_Documentos, Clientes, Asientos_Contables, Transacciones
from apps.Cuentas.forms import TiposDocumentosForm, ClientesForm, TransaccionesForm, AsientosContablesForm
from apps.Cuentas.filter import TiposDocumentos_Filter

#---------------------------------------------------Estan son las Views pertenecientes a Tipos de documentos---------------------------------------------------
class TiposDocumentosCreate(CreateView):
    model = Tipos_Documentos
    form_class = TiposDocumentosForm
    template_name = 'Cuenta/TiposDocumentos_Create.html'
    success_url = reverse_lazy('Cuentas:TiposDocumentos_List')


class TiposDocumentosList(ListView):
    queryset = Tipos_Documentos.objects.order_by('id')
    template_name = 'Cuenta/TiposDocumentos_List.html'
    paginate_by = 5
    
class TiposDocumentosDelete(DeleteView):
    model = Tipos_Documentos
    template_name = 'Cuenta/TiposDocumentos_Delete.html'
    success_url = reverse_lazy('Cuentas:TiposDocumentos_List')
    
class TiposDocumentosUpdate(UpdateView):
    model = Tipos_Documentos
    form_class = TiposDocumentosForm
    template_name = 'Cuenta/TiposDocumentos_Create.html'
    success_url = reverse_lazy('Cuentas:TiposDocumentos_List')
    
class TiposDocumentosDetail(DetailView):
	model = Tipos_Documentos
	template_name = 'Cuenta/TiposDocumentos_Show.html'
    
def Search(request):
    TD_list= Tipos_Documentos.objects.all()
    filtro = TiposDocumentos_Filter(request.GET, queryset = TD_list)
    return render(request, 'Cuenta/TiposDocumentos_List.html', {'filter':filtro})


#--------------------------------Estan son las Views pertenecientes a Clientes---------------------------------------------------------

class ClientesCreate(CreateView):
    model = Clientes
    form_class = ClientesForm
    template_name = 'Cuenta/Clientes_Create.html'
    success_url = reverse_lazy('Cuentas:Clientes_List')
    
class ClientesList(ListView):
    queryset = Clientes.objects.order_by('id')
    template_name = 'Cuenta/Clientes_List.html'
    paginate_by = 5
    
class ClientesDelete(DeleteView):
    model = Clientes
    template_name = 'Cuenta/Clientes_Delete.html'
    success_url = reverse_lazy('Cuentas:Clientes_List')
    
class ClientesUpdate(UpdateView):
    model = Clientes
    form_class = ClientesForm
    template_name = 'Cuenta/Clientes_Create.html'
    success_url = reverse_lazy('Cuentas:Clientes_List')
    
class ClientesDetail(DetailView):
	model = Clientes
	template_name = 'Cuenta/Clientes_Show.html'

#--------------------------------Estan son las Views pertenecientes a Transacciones----------------------------------------------------

class TransaccionesCreate(CreateView):
    model = Transacciones
    form_class = TransaccionesForm
    template_name = 'Cuenta/Transacciones_Create.html'
    success_url = reverse_lazy('Cuentas:Transacciones_List')
    
class TransaccionesList(ListView):
    queryset = Transacciones.objects.order_by('id')
    template_name = 'Cuenta/Transacciones_List.html'
    paginate_by = 5
    
class TransaccionesDelete(DeleteView):
    model = Transacciones
    template_name = 'Cuenta/Transacciones_Delete.html'
    success_url = reverse_lazy('Cuentas:Transacciones_List')
    
class TransaccionesUpdate(UpdateView):
    model = Transacciones
    form_class = TransaccionesForm
    template_name = 'Cuenta/Transacciones_Create.html'
    success_url = reverse_lazy('Cuentas:Transacciones_List')
    
class TransaccionesDetail(DetailView):
	model = Transacciones
	template_name = 'Cuenta/Transacciones_Show.html'
    
#--------------------------------Estan son las Views pertenecientes a Asientos Contables-----------------------------------------------

class AsientosContablesCreate(CreateView):
    model = Asientos_Contables
    form_class = AsientosContablesForm
    template_name = 'Cuenta/AsientosContables_Create.html'
    success_url = reverse_lazy('Cuentas:AsientosContables_List')
    
class AsientosContablesList(ListView):
    queryset = Asientos_Contables.objects.order_by('id')
    template_name = 'Cuenta/AsientosContables_List.html'
    paginate_by = 5
    
class AsientosContablesDelete(DeleteView):
    model = Asientos_Contables
    template_name = 'Cuenta/AsientosContables_Delete.html'
    success_url = reverse_lazy('Cuentas:AsientosContables_List')
    
class AsientosContablesUpdate(UpdateView):
    model = Asientos_Contables
    form_class = AsientosContablesForm
    template_name = 'Cuenta/AsientosContables_Create.html'
    success_url = reverse_lazy('Cuentas:AsientosContables_List')
    
class AsientosContablesDetail(DetailView):
	model = Transacciones
	template_name = 'Cuenta/AsientosContables_Show.html'
#-------------------------------------------------------------------------
class AsientosContables(ListView):
    queryset = Transacciones.objects.order_by('id')
    template_name = 'Cuenta/AsientosContables.html'
    paginate_by = 5


class Enviar_AsientosContables(DetailView):
    model = Transacciones
    template_name = 'Cuenta/Enviar.html'
#-------------------------------------------------------------------------------------------------------------------
    def ws(request):
        url = "http://accountingintegration.azurewebsites.net/api/accountingentry"
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

        data = {

        "description": "Allahu Akbar",
        "auxiliary": {
            "id": 5
        },
        "transactions":
            [
            {
                "accountingAccount": {
                    "id": 13
                },
                "origin": "CREDIT",
                "amount": 3000
            },
            {
                "accountingAccount": {
                    "id": 8
                },
                "origin": "DEBIT",
                "amount": 3000
                }
            ]
        }
        r = requests.post(url, data=json.dumps(data), headers=headers)

        print(r.text)

        return render(request, {"Envio":r})
#     return render_to_response('Enviar.html', {'j': r},)

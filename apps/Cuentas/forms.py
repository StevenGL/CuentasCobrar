from django import forms
from apps.Cuentas.models import Tipos_Documentos, Clientes, Transacciones, Asientos_Contables


# Este es el form de Tipos de documentos  
class TiposDocumentosForm(forms.ModelForm):

    def clean_Cuenta_Contable(self):
        cuenta = self.cleaned_data['Cuenta_Contable']
        largo = len(cuenta.__str__())
        if  not largo == 4:
            raise forms.ValidationError("La cuenta debe tener 4 digitos")
        return cuenta
    class Meta:
        model = Tipos_Documentos
        fields =[
            'Descripcion',
            'Cuenta_Contable',
            'Estado',
        ]
        
        labels ={
            'Descripcion':'Descripcion',
            'Cuenta_Contable': 'Cuenta contable',
            'Estado': 'Estado',
        }
        
        widgets ={
            'Descripcion': forms.Textarea(attrs={'class':'form-control'}),
            'Cuenta_Contable': forms.TextInput(attrs={'class':'form-control'}),
            'Estado':forms.Select(attrs={'class':'form-control'}),
        }
# Este es el form de Clientes       
class ClientesForm(forms.ModelForm):

    def clean_Limite_Credito(self):
        monto = self.cleaned_data['Limite_Credito']
        if not monto > 1:
            raise forms.ValidationError("El monto debe se positivo")
        return monto

    class Meta:
        model = Clientes
        fields =[
            'Nombre',
            'Cedula',
            'Limite_Credito',
            'Estado',
        ]
        
        labels ={
            'Nombre':'Nombre',
            'Cedula':'Cedula',
            'Limite_Credito':'Limite de credito',
            'Estado': 'Estado',
        }
        
        widgets ={
            'Nombre': forms.TextInput(attrs={'class':'form-control'}),
            'Cedula': forms.TextInput(attrs={'class':'form-control'}),
            'Limite_Credito': forms.TextInput(attrs={'class':'form-control'}),
            'Estado':forms.Select(attrs={'class':'form-control'}),
        }
        
# Este es el form de Transacciones
class TransaccionesForm(forms.ModelForm):

    def clean_Monto(self):
        monto = self.cleaned_data['Monto']
        if not monto > 1:
            raise forms.ValidationError("El monto debe se positivo")
        return monto
    class Meta:
        model = Transacciones
        fields =[
            'Descripcion',
            'TipoDocumento',
            'Tipo_Movimiento',
            'Numero_Documento',
            'Cliente',
            'Fecha',
            'Monto',
        ]
        
        labels ={
            'Descripcion':'Descripcion',
            'TipoDocumento':'Tipos de documento',
            'Tipo_Movimiento': 'Tipo de movimiento',
            'Numero_Documento':'Numero de documento',
            'Cliente':'Cliente',
            'Fecha':'Fecha',
            'Monto':'Monto',
        }
        
        widgets ={
            'Descripcion': forms.Textarea(attrs={'class':'form-control'}),
            'TipoDocumento':forms.Select(attrs={'class':'form-control'}),
            'Tipo_Movimiento':forms.Select(attrs={'class':'form-control'}),
            'Numero_Documento': forms.TextInput(attrs={'class':'form-control'}),
            'Cliente':forms.Select(attrs={'class':'form-control'}),
            'Fecha': forms.TextInput(attrs={'class':'form-control', 'placeholder':'mm/dd/yyyy'}),
            'Monto': forms.TextInput(attrs={'class':'form-control'}),
        }

# Este es el form de Asientos Contables 

class AsientosContablesForm(forms.ModelForm):

    def clean_Monto(self):
        monto = self.cleaned_data['Monto']
        if not monto > 1:
            raise forms.ValidationError("El monto debe se positivo")
        return monto

    class Meta:
        model = Asientos_Contables
        fields =[
            'Descripcion',
            'Cliente',
            'Tipo_Movimiento',
            'Cuenta',
            'Fecha',
            'Monto',
            'Estado',
        ]



        labels ={
            'Descripcion':'Descripcion',
            'Cliente':'Cliente',
            'Tipo_Movimiento': 'Tipo de movimiento',
            'Cuenta':'Cuenta',
            'Fecha':'Fecha',
            'Monto':'Monto',
            'Estado':'Estado',
        }


        
        widgets ={
            'Descripcion': forms.Textarea(attrs={'class':'form-control'}),
            'Cliente':forms.Select(attrs={'class':'form-control'}),
            'Tipo_Movimiento':forms.Select(attrs={'class':'form-control'}),
            'Cuenta': forms.TextInput(attrs={'class':'form-control'}),
            'Fecha': forms.TextInput(attrs={'class':'form-control', 'placeholder':'mm/dd/yyyy'}),
            'Monto': forms.TextInput(attrs={'class':'form-control'}),
            'Estado':forms.Select(attrs={'class':'form-control'}),
        
        
        }



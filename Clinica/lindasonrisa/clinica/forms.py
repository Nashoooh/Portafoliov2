from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from django.core.exceptions import ValidationError

from .models import User, Paciente

from django.db.models.signals import post_save
from django.dispatch import receiver

from django.forms import Textarea

""" class DateInput(forms.DateInput):
    input_type = 'date'
    input_formats=['%Y/%m/%d'] """

class ContactoForm(forms.Form):
    correo = forms.EmailField(required=True)
    asunto = forms.CharField(required=True)
    mensaje = forms.CharField(widget=forms.Textarea, required=True)
    nombre = forms.CharField(required=True)
    apellido_paterno = forms.CharField(required=True)
    apellido_materno = forms.CharField(required=True)

class CreacionUsuarioPersonalizada(forms.Form):
    username = forms.CharField(label='Nombre de Usuario:', min_length=4, max_length=150)
    first_name = forms.CharField(label='Nombre:', min_length=4, max_length=150)
    last_name = forms.CharField(label='Apellidos:', min_length=4, max_length=150)
    email = forms.EmailField(label='Email:')
    password1 = forms.CharField(label='Contraseña:', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirme Contraseña:', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username","first_name","last_name","email","password"]

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name'].capitalize()
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name'].capitalize()
        return last_name

    def clean_username(self):
        username = self.cleaned_data['username'].capitalize()
        r = User.objects.filter(username=username)
        if r.count():
            raise  ValidationError("Usuario ya existe")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise  ValidationError("Correo ya esta vinculado a un usuario")
        return email
 
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
 
        if password1 and password2 and password1 != password2:
            raise ValidationError("Las contraseñas ingresadas no coinciden")
 
        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password1']
        )
        return user

class PacienteForm(forms.Form):

    COMUNA = (
        ("BUIN", 'Buin'),
        ("CALERA_DE_TANGO", 'Calera de Tango'),
        ("CERRILLOS", 'Cerrillos'),
        ("CERRO_NAVIA", 'Cerro Navia'),
        ("COLINA", 'Colina'),
        ("CONCHALI", 'Conchali'),
        ("EL_BOSQUE", 'El Bosque'),
        ("EL_MONTE", 'El Monte'),
        ("ESTACION_CENTRAL", 'Estacion Central'),
        ("HUECHURABA", 'Huechuraba'),
        ("ISLA_DE_MAIPO", 'Isla de Maipo'),
        ("INDEPENDENCIA", 'Independencia'),
        ("LAMPA", 'Lampa'),
        ("LA_CISTERNA", 'La Cisterna'),
        ("LA_FLORIDA", 'La Florida'),
        ("LA_GRANJA", 'La Granja'),
        ("LA_PINTANA", 'La Pintana'),
        ("LA_REINA", 'La Reina'),
        ("LAS_CONDES", 'Las Condes'),
        ("LO_BARNECHEA", 'Lo Barnechea'),
        ("LO_ESPEJO", 'Lo Espejo'),
        ("LO_PRADO", 'Lo Prado'),
        ("MACUL", 'Macul'),
        ("MAIPU", 'Maipu'),
        ("ÑUÑOA", 'Ñuñoa'),
        ("PAINE", 'Paine'),
        ("PADRE_HURTADO", 'Padre Hurtado'),
        ("PEDRO_AGUIRRE_CERDA", 'Pedro Aguirre Cerda'),
        ("PEÑAFLOR", 'Peñaflor'),
        ("PEÑALOLEN", 'Peñalolen'),
        ("PROVIDENCIA", 'Providencia'),
        ("PUDAHUEL", 'Pudahuel'),
        ("PUENTE_ALTO", 'Puente Alto'),
        ("QUILICURA", 'Quilicura'),
        ("QUINTA_NORMAL", 'Quinta Normal'),
        ("RECOLETA", 'Recoleta'),
        ("RENCA", 'Renca'),
        ("SAN_BERNARDO", 'San Bernardo'),
        ("SAN_JOAQUIN", 'San Joaquin'),
        ("SAN_JOSE_DE_MAIPO", 'San Jose de Maipo'),
        ("SAN_MIGUEL", 'San Miguel'),
        ("SAN_RAMON", 'San Ramon'),
        ("SANTIAGO", 'Santiago'),
        ("TALAGANTE", 'Talagante'),
        ("VITACURA", 'Vitacura'),
    )

    SEXO = (
        ("MASCULINO", "Masculino"),
        ("FEMENINO", "Femenino"),
    )

    rut = forms.CharField(label='Rut:', min_length=7, max_length=12, required=True)
    nacionalidad = forms.CharField(label='Nacionalidad:', min_length=4, max_length=150)
    edad = forms.IntegerField(label='Edad:', max_value=99, required=True)
    sexo = forms.ChoiceField(choices=SEXO)
    direccion = forms.CharField(label='Dirección:', required=True)
    numeracion = forms.CharField(label='Numeración:', required=True)
    casa_o_depto = forms.CharField(label='Numero Casa o Depto:', required=False)
    comuna = forms.ChoiceField(choices=COMUNA)
    numero_celular = forms.CharField(label='Celular:', min_length=9, max_length=12, required=True)

    class Meta:
        model = Paciente
        fields = ('rut',
            'fecha_nacimiento',
            'nacionalidad',
            'edad',
            'sexo',
            'direccion',
            'numeracion',
            'casa_o_depto',
            'comuna',
            'numero_celular',)
    
    def save(self, commit=True):
        rut=self.rut,
        edad=self.edad,
        sexo=self.sexo,
        direccion=self.direccion,
        numeracion=self.numeracion,
        casa_o_depto=self.casa_o_depto,
        comuna=self.comuna,
        numero_celular=self.numero_celular

        return paciente

class LoginForm(forms.Form):
    username = forms.CharField(label='Ingrese Usuario', min_length=4, max_length=150)
    password = forms.CharField(label='Ingrese Contraseña', widget=forms.PasswordInput)
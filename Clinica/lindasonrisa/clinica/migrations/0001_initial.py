# Generated by Django 3.0.8 on 2020-07-23 13:16

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Especialista',
            fields=[
                ('rut', models.CharField(default=0, max_length=40, primary_key=True, serialize=False)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
                ('especialidad', models.CharField(max_length=30, null=True)),
                ('usuario', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FamiliaProducto',
            fields=[
                ('id_familia', models.CharField(default=0, max_length=3, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator(code='nomatch', message='Length has to be 3', regex='^.{3}$')])),
                ('familia', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('rut', models.CharField(default=0, max_length=12, primary_key=True, serialize=False)),
                ('nacionalidad', models.CharField(max_length=40, null=True)),
                ('edad', models.IntegerField(null=True)),
                ('sexo', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=40, null=True)),
                ('numeracion', models.CharField(max_length=8, null=True)),
                ('casa_o_depto', models.CharField(max_length=8, null=True)),
                ('comuna', models.CharField(max_length=50)),
                ('numero_celular', models.CharField(max_length=9, null=True)),
                ('usuario', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TipoProducto',
            fields=[
                ('id_tipo_producto', models.CharField(default=0, max_length=3, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator(code='nomatch', message='Length has to be 3', regex='^.{3}$')])),
                ('tipo_producto', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reservahora',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_reserva', models.DateTimeField(blank=True, null=True)),
                ('fecha_agendamiento', models.DateTimeField(auto_now=True, null=True)),
                ('Especialista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinica.Especialista')),
                ('Paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinica.Paciente')),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id_proveedor', models.CharField(default=0, max_length=3, primary_key=True, serialize=False)),
                ('rut', models.CharField(max_length=40, null=True, unique=True)),
                ('nombre', models.CharField(max_length=40, null=True)),
                ('apellido_paterno', models.CharField(max_length=40, null=True)),
                ('apellido_materno', models.CharField(max_length=40, null=True)),
                ('rubro', models.CharField(max_length=40, null=True)),
                ('direccion', models.CharField(max_length=40, null=True)),
                ('numeracion', models.CharField(max_length=8, null=True)),
                ('casa_o_depto', models.CharField(max_length=8, null=True)),
                ('comuna', models.CharField(choices=[('Buin', 'Buin'), ('Calera_de_Tango', 'Calera de Tango'), ('Cerrillos', 'Cerrillos'), ('Cerro Navia', 'Cerro Navia'), ('Colina', 'Colina'), ('Conchali', 'Conchali'), ('El Bosque', 'El Bosque'), ('El Monte', 'El Monte'), ('Estacion Central', 'Estacion Central'), ('Huechuraba', 'Huechuraba'), ('Isla de Maipo', 'Isla de Maipo'), ('Independencia', 'Independencia'), ('Lampa', 'Lampa'), ('La Cisterna', 'La Cisterna'), ('La Florida', 'La Florida'), ('La Granja', 'La Granja'), ('La Pintana', 'La Pintana'), ('La Reina', 'La Reina'), ('Las Condes', 'Las Condes'), ('Lo Barnechea', 'Lo Barnechea'), ('Lo Espejo', 'Lo Espejo'), ('Lo Prado', 'Lo Prado'), ('Macul', 'Macul'), ('Maipu', 'Maipu'), ('Ñuñoa', 'Ñuñoa'), ('Paine', 'Paine'), ('Padre Hurtado', 'Padre Hurtado'), ('Pedro Aguirre Cerda', 'Pedro Aguirre Cerda'), ('Peñaflor', 'Peñaflor'), ('Peñalolen', 'Peñalolen'), ('Providencia', 'Providencia'), ('Pudahuel', 'Pudahuel'), ('Puente Alto', 'Puente Alto'), ('Quilicura', 'Quilicura'), ('Quinta Normal', 'Quinta Normal'), ('Recoleta', 'Recoleta'), ('Renca', 'Renca'), ('San Bernardo', 'San Bernardo'), ('San Joaquin', 'San Joaquin'), ('San Jose de Maipo', 'San Jose de Maipo'), ('San Miguel', 'San Miguel'), ('San Ramon', 'San Ramon'), ('Santiago', 'Santiago'), ('Talagante', 'Talagante'), ('Vitacura', 'Vitacura')], max_length=50)),
                ('numero_celular', models.CharField(max_length=9, null=True)),
                ('correo', models.CharField(max_length=30, null=True)),
                ('usuario', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.CharField(default='N', max_length=20, primary_key=True, serialize=False)),
                ('fecha_vencimiento', models.DateField(blank=True, null=True)),
                ('descripcion_producto', models.CharField(max_length=100, null=True)),
                ('precio_compra', models.IntegerField(null=True)),
                ('precio_venta', models.IntegerField(null=True)),
                ('stock', models.IntegerField(null=True)),
                ('stock_critico', models.IntegerField(null=True)),
                ('FamiliaProducto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinica.FamiliaProducto')),
                ('Proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinica.Proveedor')),
                ('TipoProducto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinica.TipoProducto')),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('rut', models.CharField(default=0, max_length=12, primary_key=True, serialize=False)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
                ('nacionalidad', models.CharField(max_length=40, null=True)),
                ('edad', models.IntegerField(null=True)),
                ('sexo', models.CharField(choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino')], max_length=30)),
                ('direccion', models.CharField(max_length=40, null=True)),
                ('numeracion', models.CharField(max_length=8, null=True)),
                ('casa_o_depto', models.CharField(max_length=8, null=True)),
                ('comuna', models.CharField(choices=[('Buin', 'Buin'), ('Calera de Tango', 'Calera de Tango'), ('Cerrillos', 'Cerrillos'), ('Cerro Navia', 'Cerro Navia'), ('Colina', 'Colina'), ('Conchali', 'Conchali'), ('El Bosque', 'El Bosque'), ('El Monte', 'El Monte'), ('Estacion Central', 'Estacion Central'), ('Huechuraba', 'Huechuraba'), ('Isla de Maipo', 'Isla de Maipo'), ('Independencia', 'Independencia'), ('Lampa', 'Lampa'), ('La Cisterna', 'La Cisterna'), ('La Florida', 'La Florida'), ('La Granja', 'La Granja'), ('La Pintana', 'La Pintana'), ('La Reina', 'La Reina'), ('Las Condes', 'Las Condes'), ('Lo Barnechea', 'Lo Barnechea'), ('Lo Espejo', 'Lo Espejo'), ('Lo Prado', 'Lo Prado'), ('Macul', 'Macul'), ('Maipu', 'Maipu'), ('Ñuñoa', 'Ñuñoa'), ('Paine', 'Paine'), ('Padre Hurtado', 'Padre Hurtado'), ('Pedro Aguirre Cerda', 'Pedro Aguirre Cerda'), ('Peñaflor', 'Peñaflor'), ('Peñalolen', 'Peñalolen'), ('Providencia', 'Providencia'), ('Pudahuel', 'Pudahuel'), ('Puente Alto', 'Puente Alto'), ('Quilicura', 'Quilicura'), ('Quinta Normal', 'Quinta Normal'), ('Recoleta', 'Recoleta'), ('Renca', 'Renca'), ('San Bernardo', 'San Bernardo'), ('San Joaquin', 'San Joaquin'), ('San Jose de Maipo', 'San Jose de Maipo'), ('San Miguel', 'San Miguel'), ('San Ramon', 'San Ramon'), ('Santiago', 'Santiago'), ('Talagante', 'Talagante'), ('Vitacura', 'Vitacura')], max_length=50)),
                ('numero_celular', models.CharField(max_length=9, null=True)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

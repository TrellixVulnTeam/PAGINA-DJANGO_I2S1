# Generated by Django 2.0.1 on 2018-01-30 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoriaseries',
            fields=[
                ('codigo', models.IntegerField(primary_key=True, serialize=False)),
                ('nombrecaregoria', models.CharField(help_text='máximo 20 caracteres', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Comentarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(help_text='máximo 400 caracteres', max_length=400)),
                ('fecha', models.DateField(unique=True)),
                ('hora', models.DateField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Enlace',
            fields=[
                ('codigo', models.IntegerField(primary_key=True, serialize=False)),
                ('url', models.CharField(help_text='máximo 100 caracteres(mega)', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Estilo',
            fields=[
                ('codigo', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(help_text='máximo 20 caracteres', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Hilos',
            fields=[
                ('codigo', models.IntegerField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(help_text='máximo 200 caracteres', max_length=200)),
                ('fecha', models.DateField(unique=True)),
                ('hora', models.DateField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Juegos',
            fields=[
                ('codigo', models.IntegerField(primary_key=True, serialize=False)),
                ('portada', models.ImageField(upload_to='')),
                ('size', models.FloatField()),
                ('titulo', models.CharField(help_text='máximo 100 caracteres', max_length=100)),
                ('fechalanzamiento', models.CharField(help_text='formato:00/00/0000', max_length=10, null=True)),
                ('desarrolladora', models.CharField(help_text='máximo 30 caracteres', max_length=30)),
                ('distribuidora', models.CharField(help_text='máximo 30 caracteres', max_length=30)),
                ('sinopsis', models.CharField(help_text='máximo 300 caracteres', max_length=300)),
                ('personajes', models.CharField(help_text='máximo 200 caracteres', max_length=200)),
                ('numjugadores', models.ImageField(upload_to='')),
                ('enlace', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='webbody.Enlace')),
            ],
        ),
        migrations.CreateModel(
            name='Musica',
            fields=[
                ('codigo', models.IntegerField(primary_key=True, serialize=False)),
                ('portada', models.ImageField(upload_to='')),
                ('size', models.FloatField()),
                ('tituloalbum', models.CharField(help_text='máximo 100 caracteres', max_length=100)),
                ('fechalanzamiento', models.CharField(help_text='formato:00/00/0000', max_length=10, null=True)),
                ('artista', models.CharField(help_text='máximo 30 caracteres', max_length=30)),
                ('numcanciones', models.IntegerField()),
                ('enlace', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='webbody.Enlace')),
                ('estilomusical', models.ManyToManyField(to='webbody.Estilo')),
                ('titulohilo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webbody.Hilos')),
            ],
        ),
        migrations.CreateModel(
            name='Peliculas',
            fields=[
                ('codigo', models.IntegerField(primary_key=True, serialize=False)),
                ('portada', models.ImageField(upload_to='')),
                ('size', models.FloatField()),
                ('titulo', models.CharField(help_text='máximo 100 caracteres', max_length=100)),
                ('fechalanzamiento', models.CharField(help_text='formato:00/00/0000', max_length=10, null=True)),
                ('director', models.CharField(help_text='máximo 30 caracteres', max_length=30)),
                ('duracion', models.CharField(help_text='máximo 50 caracteres', max_length=50)),
                ('sinopsis', models.CharField(help_text='máximo 300 caracteres', max_length=300)),
                ('personajes', models.CharField(help_text='máximo 200 caracteres', max_length=200)),
                ('enlace', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='webbody.Enlace')),
            ],
        ),
        migrations.CreateModel(
            name='Plataforma',
            fields=[
                ('codigo', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(help_text='máximo 20 caracteres', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('codigo', models.IntegerField(primary_key=True, serialize=False)),
                ('portada', models.ImageField(upload_to='')),
                ('size', models.FloatField()),
                ('titulo', models.CharField(help_text='máximo 100 caracteres', max_length=100)),
                ('fechalanzamiento', models.CharField(help_text='formato:00/00/0000', max_length=10, null=True)),
                ('creador', models.CharField(help_text='máximo 30 caracteres', max_length=30)),
                ('numcapitulos', models.IntegerField()),
                ('numtemporadas', models.IntegerField()),
                ('sinopsis', models.CharField(help_text='máximo 300 caracteres', max_length=300)),
                ('personajes', models.CharField(help_text='máximo 200 caracteres', max_length=200)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webbody.Categoriaseries')),
                ('enlace', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='webbody.Enlace')),
                ('titulohilo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webbody.Hilos')),
            ],
        ),
        migrations.CreateModel(
            name='Tipopelicula',
            fields=[
                ('codigo', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(help_text='máximo 20 caracteres', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('nombreusuario', models.CharField(help_text='máximo 50 caracteres', max_length=50, primary_key=True, serialize=False)),
                ('email', models.CharField(help_text='este campo no puede estar vacío', max_length=100, unique=True)),
                ('nombre', models.CharField(help_text='máximo 30 caracteres', max_length=30, null=True)),
                ('apellidos', models.CharField(help_text='máximo 50 caracteres', max_length=50, null=True)),
                ('imgprincipal', models.ImageField(null=True, upload_to='')),
                ('fnacimiento', models.CharField(help_text='formato:00/00/0000', max_length=10, null=True)),
                ('nacionalidad', models.CharField(help_text='máximo 30 caracteres', max_length=30, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='peliculas',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webbody.Tipopelicula'),
        ),
        migrations.AddField(
            model_name='peliculas',
            name='titulohilo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webbody.Hilos'),
        ),
        migrations.AddField(
            model_name='juegos',
            name='plataforma',
            field=models.ManyToManyField(to='webbody.Plataforma'),
        ),
        migrations.AddField(
            model_name='juegos',
            name='titulohilo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webbody.Hilos'),
        ),
        migrations.AddField(
            model_name='hilos',
            name='comen',
            field=models.ManyToManyField(through='webbody.Comentarios', to='webbody.Usuario'),
        ),
        migrations.AddField(
            model_name='comentarios',
            name='codigohilo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webbody.Hilos'),
        ),
        migrations.AddField(
            model_name='comentarios',
            name='nombreusuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webbody.Usuario'),
        ),
        migrations.AlterUniqueTogether(
            name='hilos',
            unique_together={('fecha', 'hora')},
        ),
        migrations.AlterUniqueTogether(
            name='comentarios',
            unique_together={('fecha', 'hora')},
        ),
    ]

# Generated by Django 3.0.4 on 2020-03-12 19:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.DateField()),
                ('horario', models.TimeField()),
                ('disponivel', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Especialidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=120)),
                ('crm', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=50)),
                ('telefone', models.CharField(max_length=13)),
                ('especialidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicar.Especialidade')),
            ],
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_agendamento', models.DateTimeField(auto_now=True)),
                ('agenda', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='medicar.Agenda')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='agenda',
            name='medico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicar.Medico'),
        ),
        migrations.AlterUniqueTogether(
            name='agenda',
            unique_together={('medico', 'dia', 'horario')},
        ),
    ]

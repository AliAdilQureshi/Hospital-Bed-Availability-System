# Generated by Django 4.0.3 on 2022-03-13 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=300)),
                ('phone', models.CharField(max_length=20)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hospitals', to='covid.city')),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('hospital', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='covid.hospital')),
                ('oxygen_beds_totals', models.IntegerField(default=0)),
                ('oxygen_beds_available', models.IntegerField(default=0)),
                ('oxygen_cylinder_total', models.IntegerField(default=0)),
                ('oxygen_cylinder_available', models.IntegerField(default=0)),
                ('ventilator_total', models.IntegerField(default=0)),
                ('ventilator_available', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cities', to='covid.state'),
        ),
    ]

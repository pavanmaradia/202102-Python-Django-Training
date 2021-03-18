# Generated by Django 3.1.7 on 2021-03-15 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='emp.city'),
        ),
    ]

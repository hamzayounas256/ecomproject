# Generated by Django 4.1.13 on 2025-04-16 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0007_roles_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logout',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('token', models.CharField(max_length=500)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecomapp.users')),
            ],
        ),
    ]

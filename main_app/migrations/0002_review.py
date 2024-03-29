# Generated by Django 4.0.6 on 2022-07-07 03:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('opinion', models.CharField(choices=[('L', 'Like'), ('D', "Don't like"), ('N', 'Never played')], default='L', max_length=1)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.game')),
            ],
        ),
    ]

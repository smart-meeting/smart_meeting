# Generated by Django 2.1 on 2020-01-11 04:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('post', '0012_auto_20200111_0327'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('join', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.Join')),
            ],
        ),
    ]

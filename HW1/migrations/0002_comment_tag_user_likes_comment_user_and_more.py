# Generated by Django 4.2.7 on 2023-11-14 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HW1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.TextField()),
                ('isuseful', models.BooleanField()),
                ('likenum', models.IntegerField()),
                ('dislikenum', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='tag',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tag', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('login', models.CharField(max_length=25)),
                ('avatar', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=50)),
                ('nickname', models.CharField(max_length=25)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='likes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('like', models.BooleanField()),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HW1.comment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HW1.user')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HW1.user'),
        ),
        migrations.AddField(
            model_name='question',
            name='commentlist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HW1.comment'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='taglist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HW1.tag'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HW1.user'),
            preserve_default=False,
        ),
    ]

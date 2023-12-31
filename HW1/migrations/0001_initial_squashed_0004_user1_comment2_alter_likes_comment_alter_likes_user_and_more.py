# Generated by Django 4.2.7 on 2023-11-14 20:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('HW1', '0001_initial'), ('HW1', '0002_comment_tag_user_likes_comment_user_and_more'), ('HW1', '0003_alter_comment_user_alter_likes_comment_and_more'), ('HW1', '0004_user1_comment2_alter_likes_comment_alter_likes_user_and_more')]

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tag',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tag', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='user1',
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
            name='comment2',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.TextField()),
                ('isuseful', models.BooleanField()),
                ('likenum', models.IntegerField()),
                ('dislikenum', models.IntegerField()),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='HW1.user1')),
            ],
        ),
        migrations.CreateModel(
            name='likes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('like', models.BooleanField()),
                ('comment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='HW1.comment2')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='HW1.user1')),
            ],
        ),
        migrations.CreateModel(
            name='question',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('question_name', models.CharField(max_length=200)),
                ('question_description', models.TextField()),
                ('likenum', models.IntegerField()),
                ('dislikenum', models.IntegerField()),
                ('commentlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HW1.comment2')),
                ('taglist', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='HW1.tag')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='HW1.user1')),
            ],
        ),
    ]

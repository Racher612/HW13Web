# Generated by Django 4.2.7 on 2023-11-14 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HW1', '0003_alter_comment_user_alter_likes_comment_and_more'),
    ]

    operations = [
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
        migrations.AlterField(
            model_name='likes',
            name='comment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='HW1.comment2'),
        ),
        migrations.AlterField(
            model_name='likes',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='HW1.user1'),
        ),
        migrations.AlterField(
            model_name='question',
            name='commentlist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HW1.comment2'),
        ),
        migrations.AlterField(
            model_name='question',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='HW1.user1'),
        ),
        migrations.DeleteModel(
            name='comment',
        ),
        migrations.DeleteModel(
            name='user',
        ),
    ]

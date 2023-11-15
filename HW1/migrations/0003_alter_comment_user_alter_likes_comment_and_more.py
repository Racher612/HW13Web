# Generated by Django 4.2.7 on 2023-11-14 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HW1', '0002_comment_tag_user_likes_comment_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='HW1.user'),
        ),
        migrations.AlterField(
            model_name='likes',
            name='comment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='HW1.comment'),
        ),
        migrations.AlterField(
            model_name='likes',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='HW1.user'),
        ),
        migrations.AlterField(
            model_name='question',
            name='taglist',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='HW1.tag'),
        ),
        migrations.AlterField(
            model_name='question',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='HW1.user'),
        ),
    ]
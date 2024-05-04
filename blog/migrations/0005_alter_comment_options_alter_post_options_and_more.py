# Generated by Django 4.2.11 on 2024-05-03 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['created_on']},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_on']},
        ),
        migrations.AddField(
            model_name='comment',
            name='challenge',
            field=models.SlugField(default='this_is_a_slug'),
            preserve_default=False,
        ),
    ]

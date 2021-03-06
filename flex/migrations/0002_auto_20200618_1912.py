# Generated by Django 3.0.4 on 2020-06-18 18:12

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0001_squashed_0021'),
        ('flex', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flexpage',
            name='body',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(blank=True, icon='title', null=True)), ('paragraph', wagtail.core.blocks.RichTextBlock(blank=True, icon='pilcrow', null=True)), ('embed', wagtail.embeds.blocks.EmbedBlock(blank=True, icon='media', null=True))], blank=True, null=True),
        ),
        migrations.AddField(
            model_name='flexpage',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='wagtailimages.Image'),
        ),
        migrations.AlterField(
            model_name='flexpage',
            name='subtitle',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]

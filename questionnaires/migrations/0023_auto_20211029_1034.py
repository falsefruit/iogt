# Generated by Django 3.1.13 on 2021-10-29 10:34

from django.db import migrations
import home.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks
import wagtailmarkdown.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaires', '0022_auto_20211029_0633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='description',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(form_classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'image'])), ('html', home.blocks.RawHTMLBlock(help_text='Paragraph (V1 Legacy)', icon='code')), ('image', wagtail.images.blocks.ImageChooserBlock()), ('list', wagtailmarkdown.blocks.MarkdownBlock(icon='code')), ('numbered_list', home.blocks.NumberedListBlock(wagtailmarkdown.blocks.MarkdownBlock(icon='code'))), ('page_button', wagtail.core.blocks.StructBlock([('page', wagtail.core.blocks.PageChooserBlock()), ('text', wagtail.core.blocks.CharBlock(max_length=255, required=False))]))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='description',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(form_classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'image'])), ('html', home.blocks.RawHTMLBlock(help_text='Paragraph (V1 Legacy)', icon='code')), ('image', wagtail.images.blocks.ImageChooserBlock()), ('list', wagtailmarkdown.blocks.MarkdownBlock(icon='code')), ('numbered_list', home.blocks.NumberedListBlock(wagtailmarkdown.blocks.MarkdownBlock(icon='code'))), ('page_button', wagtail.core.blocks.StructBlock([('page', wagtail.core.blocks.PageChooserBlock()), ('text', wagtail.core.blocks.CharBlock(max_length=255, required=False))]))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='survey',
            name='description',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(form_classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'image'])), ('html', home.blocks.RawHTMLBlock(help_text='Paragraph (V1 Legacy)', icon='code')), ('image', wagtail.images.blocks.ImageChooserBlock()), ('list', wagtailmarkdown.blocks.MarkdownBlock(icon='code')), ('numbered_list', home.blocks.NumberedListBlock(wagtailmarkdown.blocks.MarkdownBlock(icon='code'))), ('page_button', wagtail.core.blocks.StructBlock([('page', wagtail.core.blocks.PageChooserBlock()), ('text', wagtail.core.blocks.CharBlock(max_length=255, required=False))]))], blank=True, null=True),
        ),
    ]
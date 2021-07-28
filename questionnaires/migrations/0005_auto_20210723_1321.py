# Generated by Django 3.1.13 on 2021-07-23 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaires', '0004_auto_20210723_0906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizformfield',
            name='field_type',
            field=models.CharField(choices=[('checkbox', 'Checkbox'), ('checkboxes', 'Checkboxes'), ('date', 'Date'), ('datetime', 'Date/time'), ('dropdown', 'Drop down'), ('email', 'Email'), ('hidden', 'Hidden field'), ('singleline', 'Single line text'), ('multiline', 'Multi-line text'), ('multiselect', 'Multiple select'), ('number', 'Number'), ('positivenumber', 'Positive number'), ('radio', 'Radio buttons'), ('url', 'URL')], max_length=16, verbose_name='field type'),
        ),
        migrations.AlterField(
            model_name='surveyformfield',
            name='field_type',
            field=models.CharField(choices=[('checkbox', 'Checkbox'), ('checkboxes', 'Checkboxes'), ('date', 'Date'), ('datetime', 'Date/time'), ('dropdown', 'Drop down'), ('email', 'Email'), ('hidden', 'Hidden field'), ('singleline', 'Single line text'), ('multiline', 'Multi-line text'), ('multiselect', 'Multiple select'), ('number', 'Number'), ('positivenumber', 'Positive number'), ('radio', 'Radio buttons'), ('url', 'URL')], max_length=16, verbose_name='field type'),
        ),
    ]
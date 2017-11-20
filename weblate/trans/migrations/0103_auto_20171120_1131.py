# -*- coding: utf-8 -*-
# Generated by Django 1.11.5.dev20170816164241 on 2017-11-20 10:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trans', '0102_auto_20171013_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='change',
            name='action',
            field=models.IntegerField(choices=[(0, 'Resource update'), (1, 'Translation completed'), (2, 'Translation changed'), (5, 'New translation'), (3, 'Comment added'), (4, 'Suggestion added'), (6, 'Automatic translation'), (7, 'Suggestion accepted'), (8, 'Translation reverted'), (9, 'Translation uploaded'), (10, 'Glossary added'), (11, 'Glossary updated'), (12, 'Glossary uploaded'), (13, 'New source string'), (14, 'Component locked'), (15, 'Component unlocked'), (16, 'Detected duplicate string'), (17, 'Committed changes'), (18, 'Pushed changes'), (19, 'Reset repository'), (20, 'Merged repository'), (21, 'Rebased repository'), (22, 'Failed merge on repository'), (23, 'Failed rebase on repository'), (28, 'Failed push on repository'), (24, 'Parse error'), (25, 'Removed translation'), (26, 'Suggestion removed'), (27, 'Search and replace'), (29, 'Suggestion removed during cleanup'), (30, 'Source string changed')], default=2),
        ),
        migrations.AlterField(
            model_name='subproject',
            name='file_format',
            field=models.CharField(choices=[('aresource', 'Android String Resource'), ('auto', 'Automatic detection'), ('csv', 'CSV file'), ('csv-simple', 'Simple CSV file'), ('csv-simple-iso', 'Simple CSV file (ISO-8859-1)'), ('dtd', 'DTD file'), ('i18next', 'i18next JSON file'), ('joomla', 'Joomla Language File'), ('json', 'JSON file'), ('json-nested', 'JSON nested structure file'), ('php', 'PHP strings'), ('po', 'Gettext PO file'), ('po-mono', 'Gettext PO file (monolingual)'), ('poxliff', 'XLIFF Translation File with PO extensions'), ('properties', 'Java Properties (ISO-8859-1)'), ('properties-utf16', 'Java Properties (UTF-16)'), ('properties-utf8', 'Java Properties (UTF-8)'), ('resx', '.Net resource file'), ('ruby-yaml', 'Ruby YAML file'), ('strings', 'OS X Strings'), ('strings-utf8', 'OS X Strings (UTF-8)'), ('ts', 'Qt Linguist Translation File'), ('webextension', 'WebExtension JSON file'), ('xliff', 'XLIFF Translation File'), ('yaml', 'YAML file')], default='auto', help_text='Automatic detection might fail for some formats and is slightly slower.', max_length=50, verbose_name='File format'),
        ),
    ]

# Generated by Django 5.0.2 on 2025-03-02 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('q', '0014_alter_quizresult_options_remove_question_image_loc_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to='pdfs/'),
        ),
    ]

# Generated by Django 3.2.9 on 2021-12-29 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('AcadeMeData', '0010_merge_20211229_1454'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='board',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE,
                                    to='AcadeMeData.messageboards'),
        ),
        migrations.AlterField(
            model_name='messageboards',
            name='courseName',
            field=models.ForeignKey(blank=True, default=0, on_delete=django.db.models.deletion.CASCADE,
                                    to='AcadeMeData.course'),
        ),
    ]
# Generated by Django 5.0.2 on 2024-02-13 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('content', '0002_tag_article'),
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visual_selection', models.CharField(choices=[('standard', 'Standard'), ('horizontal', 'Horizontal'), ('vertical', 'Vertical')], max_length=20)),
                ('position', models.CharField(max_length=255)),
                ('order', models.PositiveIntegerField(default=0)),
                ('title', models.CharField(max_length=250)),
                ('show_title', models.BooleanField(default=False)),
                ('link_and_rearrange', models.ManyToManyField(blank=True, to='content.article')),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
            },
        ),
    ]

# Generated by Django 5.0.7 on 2024-07-30 20:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Detector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100, unique=True, verbose_name='Code')),
                ('fine_gain', models.DecimalField(decimal_places=4, max_digits=10, verbose_name='Fine Gain')),
                ('coarse_gain', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Coarse Gain')),
                ('detector_type', models.CharField(choices=[('HPGE', 'HPGE'), ('NAI', 'NaI(Tl)')], default='HPGE', max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Detector',
                'verbose_name_plural': 'Detectors',
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='Nuclide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('energy', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Energy')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Nuclide',
                'verbose_name_plural': 'Nuclides',
            },
        ),
        migrations.CreateModel(
            name='SessionData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sample_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Sample Name')),
                ('roi_file', models.CharField(max_length=255, verbose_name='ROI File')),
                ('qa_prep', models.CharField(max_length=255, verbose_name='QA Prep')),
                ('lifetime', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Lifetime')),
                ('description', models.TextField(blank=True, help_text='Description of the measurement session e.g. sample id in the logbook', null=True, verbose_name='Description')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('detector', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='session_detector', to='qa.detector')),
            ],
            options={
                'verbose_name': 'Session Data',
                'verbose_name_plural': 'Session Data',
            },
        ),
        migrations.CreateModel(
            name='Roi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('centroid', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Centroid')),
                ('net_count', models.PositiveBigIntegerField(verbose_name='Net Count')),
                ('roi_type', models.CharField(choices=[('ROI', 'ROI'), ('INSERT', 'Insert')], default='ROI', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('nuclide', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='roi', to='qa.nuclide')),
                ('session_data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='spectrum', to='qa.sessiondata')),
            ],
            options={
                'verbose_name': 'ROI',
                'verbose_name_plural': 'Spectra',
                'ordering': ['created_at'],
            },
        ),
    ]

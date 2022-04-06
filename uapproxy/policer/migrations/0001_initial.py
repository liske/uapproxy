# Generated by Django 4.0.3 on 2022-04-06 10:42

from django.db import migrations, models
import django.db.models.deletion
import policer.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('description', models.CharField(blank=True, help_text='description', max_length=255, null=True)),
                ('brand', models.CharField(help_text="ua's device brand", max_length=48)),
                ('family', models.CharField(blank=True, default='', help_text="ua's device family", max_length=48)),
                ('model', models.CharField(blank=True, default='', help_text="ua's device model", max_length=48)),
            ],
        ),
        migrations.CreateModel(
            name='OperatingSystem',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('description', models.CharField(blank=True, help_text='description', max_length=255, null=True)),
                ('family', models.CharField(help_text="ua's os family", max_length=48)),
                ('major', models.PositiveIntegerField(blank=True, null=True)),
                ('minor', models.PositiveIntegerField(blank=True, null=True)),
                ('patch', models.PositiveIntegerField(blank=True, null=True)),
                ('patch_minor', models.PositiveIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Prefix',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('description', models.CharField(blank=True, help_text='description', max_length=255, null=True)),
                ('prefix', models.GenericIPAddressField(unpack_ipv4=True)),
                ('length', models.PositiveSmallIntegerField()),
            ],
            options={
                'verbose_name_plural': 'prefixes',
            },
        ),
        migrations.CreateModel(
            name='UserAgent',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('description', models.CharField(blank=True, help_text='description', max_length=255, null=True)),
                ('family', models.CharField(help_text="ua's device family", max_length=48)),
                ('major', models.PositiveIntegerField(blank=True, null=True)),
                ('minor', models.PositiveIntegerField(blank=True, null=True)),
                ('patch', models.PositiveIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Policy',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('priority', models.IntegerField(default=policer.models.Policy.get_free_priority, unique=True)),
                ('permit', models.BooleanField(default=True)),
                ('ua_comparator', models.CharField(choices=[('LT', '<'), ('LE', '≤'), ('EQ', '='), ('NE', '≠'), ('GE', '≥'), ('GT', '>')], default='LT', max_length=2)),
                ('os_comparator', models.CharField(choices=[('LT', '<'), ('LE', '≤'), ('EQ', '='), ('NE', '≠'), ('GE', '≥'), ('GT', '>')], default='EQ', max_length=2)),
                ('device_equal', models.BooleanField(default=True, help_text='If TRUE the device must match, if FALSE it must not match.')),
                ('prefix_inside', models.BooleanField(default=True, help_text='If TRUE the client ip address must be inside the prefix, if FALSE it must not be inside.')),
                ('matches', models.PositiveIntegerField(default=0)),
                ('device', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='policer.device')),
                ('os', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='policer.operatingsystem')),
                ('prefix', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='policer.prefix')),
                ('ua', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='policer.useragent')),
            ],
            options={
                'verbose_name_plural': 'policies',
                'ordering': ['priority'],
            },
        ),
    ]
# Generated by Django 5.2.1 on 2025-05-25 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aturangejala',
            fields=[
                ('id_aturangejala', models.BigIntegerField(db_column='id_aturanGejala', primary_key=True, serialize=False)),
                ('id_detailaturan', models.BigIntegerField(blank=True, db_column='id_detailAturan', null=True)),
            ],
            options={
                'db_table': 'aturangejala',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Detailaturan',
            fields=[
                ('id_detailaturan', models.BigIntegerField(db_column='id_detailAturan', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'detailaturan',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Diagnosis',
            fields=[
                ('id_diagnosis', models.BigIntegerField(primary_key=True, serialize=False)),
                ('nama_diagnosis', models.CharField(blank=True, max_length=255, null=True)),
                ('deskripsi_diagnosis', models.TextField(blank=True, null=True)),
                ('gambar_diagnosis', models.TextField(blank=True, null=True)),
                ('solusi_diagnosis', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'diagnosis',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Gejala',
            fields=[
                ('id_gejala', models.BigIntegerField(primary_key=True, serialize=False)),
                ('nama_gejala', models.CharField(blank=True, max_length=255, null=True)),
                ('kode_gejala', models.CharField(blank=True, max_length=100, null=True)),
                ('pertanyaan_gejala', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'gejala',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Laporandiagnosis',
            fields=[
                ('id_laporandiagnosis', models.BigIntegerField(db_column='id_laporanDiagnosis', primary_key=True, serialize=False)),
                ('tanggal_diagnosis', models.DateField(blank=True, null=True)),
                ('probabilitas', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'laporandiagnosis',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Laporangejala',
            fields=[
                ('id_laporangejala', models.BigIntegerField(db_column='id_laporanGejala', primary_key=True, serialize=False)),
                ('value', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'laporangejala',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pengguna',
            fields=[
                ('id_pengguna', models.BigIntegerField(primary_key=True, serialize=False)),
                ('nama_pengguna', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('password', models.CharField(blank=True, max_length=255, null=True)),
                ('role', models.CharField(blank=True, max_length=5, null=True)),
            ],
            options={
                'db_table': 'pengguna',
                'managed': False,
            },
        ),
    ]

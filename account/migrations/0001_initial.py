# Generated by Django 2.1.7 on 2020-03-03 05:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Access',
            fields=[
                ('accessid', models.AutoField(primary_key=True, serialize=False)),
                ('accname', models.CharField(blank=True, max_length=25, null=True, verbose_name='role name')),
                ('accdescription', models.CharField(blank=True, max_length=100, null=True, verbose_name='description')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('createdby', models.CharField(max_length=20)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('updatedby', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='BA',
            fields=[
                ('baid', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('bttrplce_vendorid', models.CharField(default='no data', max_length=60, verbose_name='Vendor Id')),
                ('bttrplce_vendorname', models.CharField(default='no data', max_length=100, verbose_name='Vendor Name')),
                ('bacode', models.CharField(blank=True, max_length=5, null=True, verbose_name='ba code')),
                ('baname', models.CharField(blank=True, max_length=150, null=True)),
                ('bacontactname', models.CharField(blank=True, max_length=30, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('mobileno', models.CharField(blank=True, max_length=15, null=True)),
                ('pancard', models.CharField(blank=True, max_length=10, null=True)),
                ('status', models.CharField(blank=True, max_length=50, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('createdby', models.CharField(max_length=20)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('updatedby', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('custid', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('custcode', models.CharField(blank=True, max_length=5, null=True, verbose_name='customer code')),
                ('custname', models.CharField(blank=True, max_length=200, null=True)),
                ('custcontactname', models.CharField(blank=True, max_length=30, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('mobileno', models.CharField(blank=True, max_length=15, null=True)),
                ('status', models.CharField(blank=True, max_length=50, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('createdby', models.CharField(max_length=20)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('updatedby', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userid', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('firstname', models.CharField(blank=True, max_length=15, null=True, verbose_name='First Name')),
                ('lastname', models.CharField(blank=True, max_length=15, null=True, verbose_name='Last Name')),
                ('mobileno', models.CharField(blank=True, max_length=10, null=True, verbose_name='MobileNo.')),
                ('worklocation', models.CharField(blank=True, max_length=20, null=True, verbose_name='worklocation')),
                ('status', models.CharField(blank=True, max_length=5, null=True)),
                ('version', models.CharField(blank=True, max_length=10, null=True)),
                ('password', models.CharField(default='123456', max_length=15)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('createdby', models.CharField(max_length=20)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('updatedby', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='UserAccess',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('createdby', models.CharField(max_length=20)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('updatedby', models.CharField(max_length=20)),
                ('access', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Access')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='location.OperationLocation')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.User')),
            ],
        ),
        migrations.CreateModel(
            name='UserLocationCustomer',
            fields=[
                ('ulcpkey', models.AutoField(max_length=10, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('createdby', models.CharField(max_length=20)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('updatedby', models.CharField(max_length=20)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='location.OperationLocation')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.User')),
            ],
        ),
    ]
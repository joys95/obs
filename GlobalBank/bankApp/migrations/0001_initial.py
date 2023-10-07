# Generated by Django 4.2.1 on 2023-09-04 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cust_Info',
            fields=[
                ('account_no', models.BigIntegerField(max_length=10, primary_key=True, serialize=False)),
                ('addhar', models.BigIntegerField(max_length=12)),
                ('cust_name', models.CharField(max_length=30)),
                ('cust_email', models.EmailField(max_length=50)),
                ('cust_city', models.CharField(max_length=15)),
                ('cust_dob', models.DateField(auto_now_add=True)),
                ('cust_pass', models.CharField(max_length=10)),
                ('img_url', models.ImageField(upload_to='images/')),
                ('acct_st', models.CharField(default='False', max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='Master_Account',
            fields=[
                ('ms_id', models.BigIntegerField(max_length=10, primary_key=True, serialize=False)),
                ('deposit_amount', models.BigIntegerField(default=0)),
                ('master_balance', models.BigIntegerField(default=0)),
                ('withdraw_amount', models.BigIntegerField(default=0)),
                ('ts_dt', models.DateTimeField(auto_now_add=True)),
                ('account_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankApp.cust_info')),
            ],
        ),
        migrations.CreateModel(
            name='Account_Info',
            fields=[
                ('ts_id', models.BigIntegerField(max_length=10, primary_key=True, serialize=False)),
                ('deposit_amount', models.BigIntegerField(default=0)),
                ('balance_amount', models.BigIntegerField(default=0)),
                ('withdraw_amount', models.BigIntegerField(default=0)),
                ('ts_dt', models.DateTimeField(auto_now_add=True)),
                ('ts_st', models.CharField(default=False, max_length=6)),
                ('account_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankApp.cust_info')),
            ],
        ),
    ]

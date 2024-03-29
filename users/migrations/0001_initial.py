# Generated by Django 2.2.7 on 2019-11-13 03:45

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('accountNumber', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(default='', max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(default='', max_length=50)),
                ('city', models.CharField(default='', max_length=50)),
                ('state', models.CharField(default='', max_length=2)),
                ('zipCode', models.CharField(default='', max_length=5)),
                ('phoneNumber', models.CharField(default='1112223333', max_length=10)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='ATM_Card',
            fields=[
                ('atmCardNumber', models.AutoField(primary_key=True, serialize=False)),
                ('pin', models.CharField(default='', max_length=4)),
                ('name', models.CharField(default='', max_length=50)),
                ('dateOfIssue', models.CharField(default='', max_length=50)),
                ('expirationDate', models.CharField(default='', max_length=50)),
                ('address', models.CharField(default='', max_length=50)),
                ('phoneNumber', models.CharField(default='1112223333', max_length=10)),
                ('cardStatus', models.BooleanField(default=True)),
                ('twoFactorAuthenticationStatus', models.BooleanField(default=True)),
                ('accountNumber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ATMachine',
            fields=[
                ('ATMachineUID', models.AutoField(primary_key=True, serialize=False)),
                ('currentBalance', models.PositiveIntegerField(default=0)),
                ('location', models.CharField(default='', max_length=100)),
                ('minimumBalance', models.PositiveIntegerField(default=1000)),
                ('status', models.CharField(default='', max_length=50)),
                ('lastRefillDate', models.DateField(default='', max_length=50)),
                ('nextMaintenanceDate', models.DateField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='BalanceEnquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balanceAmount', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='CashTransfer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beneficiaryAccountNumber', models.CharField(default='', max_length=50)),
                ('beneficiaryName', models.CharField(default='', max_length=50)),
                ('amountTransferred', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='CashWithdrawal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amountTransferred', models.PositiveIntegerField(default=0)),
                ('denomination', models.CharField(default='', max_length=50)),
                ('currentBalance', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='PhoneChange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('newPhoneNumber', models.CharField(default='1112223333', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='PinChange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('previousPin', models.CharField(default='', max_length=4)),
                ('newPin', models.CharField(default='', max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('transactionId', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(default='', max_length=50)),
                ('status', models.CharField(default='', max_length=50)),
                ('responseCode', models.CharField(default='', max_length=50)),
                ('transactionType', models.CharField(default='', max_length=50)),
                ('ATMCardNumber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.ATM_Card')),
                ('ATMachineUID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.ATMachine')),
            ],
        ),
        migrations.CreateModel(
            name='ATMachineRefill',
            fields=[
                ('refillId', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.PositiveIntegerField(default=0)),
                ('atmBranch', models.CharField(default='', max_length=50)),
                ('refillDate', models.DateField(default='', max_length=50)),
                ('previousBalance', models.PositiveIntegerField(default=0)),
                ('ATMachineUID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.ATMachine')),
            ],
        ),
        migrations.CreateModel(
            name='AccountExtension',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('phoneNumber', models.CharField(default='1112223333', max_length=10)),
                ('balance', models.IntegerField(default=0)),
                ('accountNumber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

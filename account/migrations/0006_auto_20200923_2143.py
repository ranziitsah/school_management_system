# Generated by Django 3.0 on 2020-09-23 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_expense_income'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='paid',
            new_name='bus_fee',
        ),
        migrations.RenameField(
            model_name='account',
            old_name='remaining_due',
            new_name='remaining',
        ),
        migrations.RemoveField(
            model_name='account',
            name='prev_balance',
        ),
        migrations.AddField(
            model_name='account',
            name='laboratory_fee',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='miscellaneous',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='tuition_fee',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paid', models.DecimalField(decimal_places=2, max_digits=10)),
                ('remaining', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('discount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('cash', models.BooleanField(default=False)),
                ('cheque', models.BooleanField(default=False)),
                ('online_banking', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Account')),
            ],
        ),
    ]
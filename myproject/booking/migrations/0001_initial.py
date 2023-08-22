# Generated by Django 4.0 on 2022-12-03 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(help_text='Probably your name.', max_length=100)),
                ('Service', models.CharField(choices=[('Hair Rebond', 'HAIR REBOND-$20'), ('Hair Dye', 'HAIR DYE-$20'), ('Hair Cut', 'HAIR CUT-$7'), ('Face Mask', 'FACE MASK-$8'), ('Extraction', 'EXTRACTION-$12'), ('Massage', 'MASSAGE-$15'), ('Cut/Clean', 'CUT/CLEAN-$9'), ('Foot Spa', 'FOOT SPA-$10')], max_length=255)),
                ('Time', models.CharField(choices=[('9:00 - 9:30', '9:00 - 9:30'), ('9:31 - 10:00', '9:31 - 10:00'), ('10:31 - 11:00', '10:31 - 11:00'), ('11:01 - 11:30', '11:01 - 11:30'), ('11:31 - 12:30', '11:31 - 12:30'), ('12:31 - 13:00', '12:31 - 13:00'), ('13:01 - 13:30', '13:01 - 13:30'), ('13:31 - 14:00', '13:31 - 14:00'), ('14:01 - 14:30', '14:01 - 14:30'), ('14:31 - 15:00', '14:31 - 15:00'), ('15:01 - 15:30', '15:01 - 15:30'), ('15:31 - 16:00', '15:31 - 16:00'), ('16:01 - 16:30', '16:01 - 16:30'), ('16:31 - 17:00', '16:31 - 17:00'), ('17:01 - 17:30', '17:01 - 17:30'), ('17:31 - 18:00', '17:31 - 18:00')], default='09:00', help_text='Please select a time in 24hr clock format (HH:MM) from the drop down.', max_length=13)),
                ('Email', models.EmailField(help_text='Please provide email in case of cancellation.', max_length=254)),
                ('Day', models.CharField(choices=[('Monday', 'MONDAY'), ('Tuesday', 'TUESDAY'), ('Wednesday', 'WEDNESDAY'), ('Thursday', 'THURSDAY'), ('Friday', 'FRIDAY'), ('Saturday', 'SATURDAY'), ('Sunday', 'SUNDAY')], default='MONDAY', max_length=9)),
            ],
        ),
    ]
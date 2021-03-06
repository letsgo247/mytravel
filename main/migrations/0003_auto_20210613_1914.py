# Generated by Django 3.2.3 on 2021-06-13 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210525_0052'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entity',
            old_name='hkg',
            new_name='AFG',
        ),
        migrations.RenameField(
            model_name='entity',
            old_name='jpn',
            new_name='AGO',
        ),
        migrations.RenameField(
            model_name='entity',
            old_name='kor',
            new_name='ALB',
        ),
        migrations.RenameField(
            model_name='entity',
            old_name='usa',
            new_name='ARE',
        ),
        migrations.AddField(
            model_name='entity',
            name='ARG',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='ARM',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='ATA',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='ATF',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='AUS',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='AUT',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='AZE',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='BDI',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='BEL',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='BEN',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='BFA',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='BGD',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='BGR',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='BHS',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='BIH',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='BLR',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='BLZ',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='BOL',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='BRA',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='BRN',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='BTN',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='BWA',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='CAF',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='CAN',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='CHE',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='CHL',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='CHN',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='CIV',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='CMR',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='COD',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='COG',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='COL',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='CRI',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='CUB',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='CYP',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='CZE',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='DEU',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='DJI',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='DNK',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='DOM',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='DZA',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='ECU',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='EGY',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='ERI',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='ESH',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='ESP',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='EST',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='ETH',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='FIN',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='FJI',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='FLK',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='FRA',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='GAB',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='GBR',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='GEO',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='GHA',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='GIN',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='GMB',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='GNB',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='GNQ',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='GRC',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='GRL',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='GTM',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='GUY',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='HND',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='HRV',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='HTI',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='HUN',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='IDN',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='IND',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='IRL',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='IRN',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='IRQ',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='ISL',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='ISR',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='ITA',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='JAM',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='JOR',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='JPN',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='KAZ',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='KEN',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='KGZ',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='KHM',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='KOR',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='KWT',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='LAO',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='LBN',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='LBR',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='LBY',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='LKA',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='LSO',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='LTU',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='LUX',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='LVA',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='MAR',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='MDA',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='MDG',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='MEX',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='MKD',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='MLI',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='MMR',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='MNE',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='MNG',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='MOZ',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='MRT',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='MWI',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='MYS',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='NAM',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='NCL',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='NER',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='NGA',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='NIC',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='NLD',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='NOR',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='NPL',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='NZL',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='OMN',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='PAK',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='PAN',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='PER',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='PHL',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='PNG',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='POL',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='PRI',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='PRK',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='PRT',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='PRY',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='PSE',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='QAT',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='ROU',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='RUS',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='RWA',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='SAU',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='SDN',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='SEN',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='SLB',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='SLE',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='SLV',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='SOM',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='SRB',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='SSD',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='SUR',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='SVK',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='SVN',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='SWE',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='SWZ',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='SYR',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='TCD',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='TGO',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='THA',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='TJK',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='TKM',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='TLS',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='TTO',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='TUN',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='TUR',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='TWN',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='TZA',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='UGA',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='UKR',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='URY',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='USA',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='UZB',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='VEN',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='VNM',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='VUT',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='YEM',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='ZAF',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='ZMB',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='ZWE',
            field=models.BooleanField(default=False),
        ),
    ]

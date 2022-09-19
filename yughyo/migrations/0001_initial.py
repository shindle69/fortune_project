# Generated by Django 4.1.1 on 2022-09-18 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Iching',
            fields=[
                ('g_id', models.IntegerField(primary_key=True, serialize=False)),
                ('g_name', models.CharField(max_length=30)),
                ('g_content', models.CharField(max_length=500)),
                ('h_content_1', models.CharField(max_length=500)),
                ('h_content_2', models.CharField(max_length=500)),
                ('h_content_3', models.CharField(max_length=500)),
                ('h_content_4', models.CharField(max_length=500)),
                ('h_content_5', models.CharField(max_length=500)),
                ('h_content_6', models.CharField(max_length=500)),
                ('hope', models.CharField(max_length=500)),
                ('consult', models.CharField(max_length=500)),
                ('business', models.CharField(max_length=500)),
                ('trade', models.CharField(max_length=500)),
                ('contract', models.CharField(max_length=500)),
                ('law', models.CharField(max_length=500)),
                ('job', models.CharField(max_length=500)),
                ('promotion', models.CharField(max_length=500)),
                ('school', models.CharField(max_length=500)),
                ('move', models.CharField(max_length=500)),
                ('travel', models.CharField(max_length=500)),
                ('love', models.CharField(max_length=500)),
                ('marry', models.CharField(max_length=500)),
            ],
            options={
                'ordering': ['g_name'],
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('hope', '소원'), ('consult', '상담'), ('business', '사업'), ('trade', '매매'), ('contract', '계약'), ('law', '소송'), ('job', '취업'), ('promotion', '승진/진급'), ('school', '입학'), ('move', '이사'), ('travel', '여행'), ('love', '연애/사랑'), ('marry', '결혼')], max_length=10)),
                ('question_text', models.CharField(max_length=200)),
                ('jum', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

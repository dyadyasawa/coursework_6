# Generated by Django 4.2.2 on 2024-05-10 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Примечание')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True, verbose_name='Тема сообщения')),
                ('message', models.TextField(verbose_name='Сообщение')),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщения',
            },
        ),
        migrations.CreateModel(
            name='Mailing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_start', models.TimeField(verbose_name='Время начала')),
                ('time_end', models.TimeField(verbose_name='Время окончания')),
                ('period', models.CharField(choices=[('daily', 'Ежедневная'), ('weekly', 'Еженедельная'), ('monthly', 'Ежемесячная')], default='daily', max_length=20, verbose_name='Период')),
                ('status', models.CharField(choices=[('created', 'Создана'), ('started', 'Запущена'), ('done', 'Выполнена')], default='created', max_length=20, verbose_name='Статус')),
                ('clients', models.ManyToManyField(to='mailings.client', verbose_name='Клиенты')),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailings.message', verbose_name='Сообщение')),
            ],
            options={
                'verbose_name': 'Рассылка',
                'verbose_name_plural': 'Рассылки',
            },
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата и время')),
                ('status', models.CharField(choices=[('ok', 'Успешно'), ('failed', 'Ошибка')], default='ok', max_length=20, verbose_name='Статус')),
                ('answer_server', models.TextField(blank=True, null=True, verbose_name='Ответ сервера')),
                ('mailing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailings.mailing', verbose_name='Рассылка')),
            ],
            options={
                'verbose_name': 'Лог',
                'verbose_name_plural': 'Логи',
            },
        ),
    ]

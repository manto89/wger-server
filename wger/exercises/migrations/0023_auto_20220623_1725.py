# Generated by Django 3.2.10 on 2022-06-23 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0022_auto_20220529_0029'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historicalalias',
            options={
                'get_latest_by': 'history_date',
                'ordering': ('-history_date', '-history_id'),
                'verbose_name': 'historical alias'
            },
        ),
        migrations.AlterModelOptions(
            name='historicalexercise',
            options={
                'get_latest_by': 'history_date',
                'ordering': ('-history_date', '-history_id'),
                'verbose_name': 'historical exercise'
            },
        ),
        migrations.AlterModelOptions(
            name='historicalexercisebase',
            options={
                'get_latest_by': 'history_date',
                'ordering': ('-history_date', '-history_id'),
                'verbose_name': 'historical exercise base'
            },
        ),
        migrations.AlterModelOptions(
            name='historicalexercisecomment',
            options={
                'get_latest_by': 'history_date',
                'ordering': ('-history_date', '-history_id'),
                'verbose_name': 'historical exercise comment'
            },
        ),
        migrations.AlterField(
            model_name='exercise',
            name='exercise_base',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='exercises',
                to='exercises.exercisebase',
                verbose_name='ExerciseBase'
            ),
        ),
        migrations.AlterField(
            model_name='historicalalias',
            name='history_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='historicalexercise',
            name='exercise_base',
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name='+',
                to='exercises.exercisebase',
                verbose_name='ExerciseBase'
            ),
        ),
        migrations.AlterField(
            model_name='historicalexercise',
            name='history_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='historicalexercisebase',
            name='history_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='historicalexercisecomment',
            name='history_date',
            field=models.DateTimeField(),
        ),
    ]

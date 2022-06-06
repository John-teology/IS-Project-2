# Generated by Django 4.0.4 on 2022-06-06 08:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0011_delete_ranks_profile_leadb_alter_profile_aboutme'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='leadB',
        ),
        migrations.AddField(
            model_name='leaderboards',
            name='userProfile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_leaderboard', to='portfolio.profile'),
        ),
    ]

# Generated by Django 4.2.3 on 2024-06-17 21:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0005_alter_project_profile"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="profile",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="projects",
                to="projects.profile",
            ),
        ),
    ]
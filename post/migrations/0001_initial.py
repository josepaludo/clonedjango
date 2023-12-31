# Generated by Django 4.2.5 on 2023-10-03 18:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('group', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=2000)),
                ('downvoters', models.ManyToManyField(related_name='downvoteds', to=settings.AUTH_USER_MODEL)),
                ('upvoters', models.ManyToManyField(related_name='upvoteds', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MainPost',
            fields=[
                ('post_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='post.post')),
                ('title', models.CharField(max_length=120)),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='group.group')),
            ],
            options={
                'ordering': ['-id'],
            },
            bases=('post.post',),
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('post_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='post.post')),
                ('related_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='post.post')),
            ],
            options={
                'ordering': ['-id'],
            },
            bases=('post.post',),
        ),
    ]

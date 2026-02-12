from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save, pre_delete
from django.dispatch import receiver
from task.models import Task

# simple signal logic for creating user
@receiver(post_save, sender=User)
def user_created_signal(sender, instance, created, **kwargs):
    if created:
        print(f'new user created: {instance.username}')
        
@receiver(post_save, sender=Task)
def task_created_signal(sender, instance, created, **kwargs):
    if created:
        print(f'new task created: {instance.title} by user {instance.user.username}')
        
@receiver(pre_save, sender=Task)
def task_update_signal(sender, instance, **kwargs):
    if not instance.pk:
        return
    try:
        old_task = Task.objects.get(pk=instance.pk)
    except Task.DoesNotExist:
        return
    if old_task.status != instance.status:
        print(f'task {instance.title} the status is changed from {old_task.status} to {instance.status}')
        
@receiver(pre_delete, sender=Task)
def task_delete_signal(sender, instance, **kwargs):
    print(f'task {instance.title} is deleted by {instance.user.username}')
        
        
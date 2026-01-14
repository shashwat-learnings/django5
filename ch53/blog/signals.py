from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed 
from django.db.models.signals import  pre_init,  pre_save, post_save, pre_delete, post_delete, post_init, post_migrate, post_save, pre_migrate    

from django.core.signals import request_started, request_finished, got_request_exception

from django.dispatch import receiver
from django.db.backends.signals import connection_created

# Connecting signals using the connect method
def log_user_login(sender, request, user, **kwargs):
    print(f"User {user.username} logged in. Sender: {sender} and Request: {request} and kwargs: {kwargs}")

user_logged_in.connect(log_user_login,sender=User)


# Using the receiver decorator to connect signals
@receiver(user_logged_out, sender=User)
def log_user_logout(sender, request, user, **kwargs):
    print(f"User {user.username} logged out. Sender: {sender} and Request: {request} and kwargs: {kwargs}")

@receiver(user_login_failed)
def log_user_login_failed(sender, credentials, request, **kwargs):
    print(f"User {credentials.get('username')} failed to log in. Sender: {sender} and Request: {request} and kwargs: {kwargs}")


@receiver(pre_save, sender=User) # Before a User instance is saved, this signal is sent. it will also be sent when a new User logs in as last login date time get updated. or if any field is updated.
def before_user_save(sender, instance, **kwargs):
    print(f"About to save User: {instance.username}. Sender: {sender} and kwargs: {kwargs}")

@receiver(post_save, sender=User) 
def after_user_save(sender, instance, created, **kwargs):
    if created:
        print(f"New User created: {instance.username}. Sender: {sender} and kwargs: {kwargs}")
    else:
        print(f"User updated: {instance.username}. Sender: {sender} and kwargs: {kwargs}")

@receiver(pre_delete, sender=User)
def before_user_delete(sender, instance, **kwargs):
    print(f"About to delete User: {instance.username}. Sender: {sender} and kwargs: {kwargs}")  


@receiver(post_delete, sender=User)
def after_user_delete(sender, instance, **kwargs):
    print(f"Deleted User: {instance.username}. Sender: {sender} and kwargs: {kwargs}")

@receiver(pre_init, sender=User)
def before_user_init(sender, *args, **kwargs):
    print(f"User instance about to be initialized. Sender: {sender} and args: {args} and kwargs: {kwargs}")

@receiver(post_init, sender=User)
def after_user_init(sender, *args, **kwargs):
    print(f"User instance initialized: {args}. Sender: {sender} and kwargs: {kwargs}")

@receiver(pre_migrate)
def before_migration(sender, app_config, verbosity, interactive, using, plan, apps, **kwargs):
    print(f"Migration about to start. Sender: {sender} and kwargs: {kwargs}")

@receiver(post_migrate)
def after_migration(sender, app_config, verbosity, interactive, using, plan, apps, **kwargs):
    print(f"Migration completed. Sender: {sender} and kwargs: {kwargs}")

@receiver(request_started)
def log_request_started(sender, environ, **kwargs):
    print(f"Request started. Sender: {sender} and environ: {environ} and kwargs: {kwargs}")

@receiver(request_finished)
def log_request_finished(sender, **kwargs):
    print(f"Request finished. Sender: {sender} and kwargs: {kwargs}")

@receiver(got_request_exception)
def log_request_exception(sender, request, **kwargs):
    print(f"Request exception occurred. Sender: {sender} and Request: {request} and kwargs: {kwargs}")

@receiver(connection_created)
def log_connection_created(sender, connection, **kwargs):
    print(f"Database connection created. Sender: {sender} and Connection: {connection} and kwargs: {kwargs}")

from django.dispatch import Signal, receiver

# Create your signals here

notification = Signal()


#Rec function
@receiver(notification)
def show_notification(sender, **kwargs):
    print("Notification signal received with kwargs:", kwargs)


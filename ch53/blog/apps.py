from django.apps import AppConfig


class BlogConfig(AppConfig):
    name = 'blog'

    def ready(self):
        '''
        This method is called when the Django app is ready. It imports the signals module to ensure that
        signal handlers are connected we also have to add {default_app_config = 'blog.apps.BlogConfig'} in __init__.py file to complete the configuration.
        
        The import statement inside this method ensures that the signal handlers defined in blog/signals.py are registered
        when the application starts.

        The ready method is a good place to put initialization code for your application.

        The second method is to directly put "blog.apps.BlogConfig" in the INSTALLED_APPS list in settings.py file.
        instead of just "blog".

        '''
        import blog.signals  

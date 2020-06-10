from django.apps import AppConfig


class AppsConfig(AppConfig):
    name = 'apps'
    verbose_name = "Nuestros apps"

    def ready(self):
        import apps.signals.handlers
    
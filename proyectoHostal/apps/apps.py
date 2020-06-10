from django.apps import AppConfig


class AppsConfig(AppConfig):
    name = 'apps'
    verbose_name = "Apps"

    def ready(self):
        import app.signals.handlers
    
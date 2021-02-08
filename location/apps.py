from django.apps import AppConfig


class LocationConfig(AppConfig):
    name = 'location'


    def ready(self):
        from contract import updater
        # updater.start()
        updater.start1()
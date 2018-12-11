from importlib import import_module

from django.apps import AppConfig as BaseAppConfig


class AppConfig(BaseAppConfig):

    name = "Django_VeriTure"

    def ready(self):
        import_module("Django_VeriTure.receivers")

from django.apps import AppConfig

class RelationshipAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'relationship_app'

    # This ensures signals are registered when the app is ready
    def ready(self):
        import relationship_app.signals

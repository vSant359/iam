from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Cria um superusuário padrão se ainda não existir'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser(
                username="admin",
                email="admin@example.com",
                password="senha123"
            )
            self.stdout.write(self.style.SUCCESS("Superusuário criado com sucesso."))
        else:
            self.stdout.write(self.style.WARNING("Superusuário já existe."))

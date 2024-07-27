from django.test import TestCase
from restaurant.models import Menu
from rest_framework import status
from rest_framework.test import APIClient
from django.urls import reverse
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):  # Conformité à la convention de nommage
    def setUp(self):
        # Créez des instances du modèle Menu pour les tests
        self.menu1 = Menu.objects.create(title="Ice Cream", price=80.00, inventory=100)
        self.menu2 = Menu.objects.create(title="Cake", price=50.00, inventory=200)
        self.client = APIClient()  # Utilisez APIClient pour les tests de l'API

    def test_getall(self):
        # Accédez à l'URL qui retourne tous les objets Menu
        url = reverse('menu-list')  # Assurez-vous que 'menu-list' est l'URL appropriée pour votre vue

        # Envoyez une requête GET
        response = self.client.get(url)

        # Vérifiez que la réponse a un code de statut 200
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Sérialisez les objets Menu pour comparaison
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)  # Assurez-vous que MenuSerializer est défini
        self.assertEqual(response.data, serializer.data)
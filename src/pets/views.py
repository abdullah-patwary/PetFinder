#cloud_journey/src/pets/views.py

from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView
from pets.models import Pet


class PetsListView(ListView):
    model = Pet
    
class PetCreateView(CreateView):
    model = Pet
    fields = ["author", "title", "text", "text", "description", "created_date", "published_date"]

# class PetDetailView(DetailView):
#     model = Pet
#     template_name = "pet_detail.html"

#     # Get the pet details based on the ID from the URL
#     def get_object(self, queryset=None):
#         pet_id = self.kwargs['pk']  # 'pk' is the captured parameter name
#         return Pet.objects.get(pk=pet_id)
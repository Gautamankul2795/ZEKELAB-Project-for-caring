from django.contrib import admin
from . models import Caretaker
from .models import Careneeder
from .models import Contact

# Register your models here.
admin.site.register(Caretaker)
admin.site.register(Careneeder)
admin.site.register(Contact)

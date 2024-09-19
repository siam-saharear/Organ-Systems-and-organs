from django.db import models

# Create your models here.



class Organ_systems(models.Model):
    organ_system = models.CharField(max_length=19)
    def __str__(self):
        return self.organ_system

class Organs(models.Model):
    organ_name = models.CharField(max_length=29)
    organ_function = models.CharField(max_length=1000)
    organ_system = models.ForeignKey(Organ_systems, on_delete=models.CASCADE)
    def __str__(self):
        return self.organ_name
    
    def save(self, *args, **kwargs):
        if self.pk is None:
            self.id = self.get_next_id()
        super().save(*args, **kwargs)

    def get_next_id(self):
        # Find the smallest available ID
        used_ids = set(Organs.objects.values_list('id', flat=True))
        all_ids = set(range(1, max(used_ids, default=0) + 2))
        available_ids = sorted(all_ids - used_ids)
        return available_ids[0] if available_ids else max(used_ids, default=0) + 1
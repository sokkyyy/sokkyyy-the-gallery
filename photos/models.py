from django.db import models
from django_countries.fields import CountryField
import pyperclip
from django.conf import settings




# Create your models here.
class Location(models.Model):
    country = CountryField(blank="select country")

    @classmethod
    def find_location(cls,country):
        location = cls.objects.filter(country=country).all()
        return location
    


class Category(models.Model):
    IMAGE_CATEGORIES = (
        ('travel',"Travel"),
        ('food',"Food"),
        ('places',"Places"),
        ('people','People'),
        ('sports','Sports'),
    )
    category = models.CharField(max_length=20, choices=IMAGE_CATEGORIES)

    @classmethod
    def search_by_category(cls,category):
        category = cls.objects.filter(category =category)
        return category
    
    @classmethod
    def find_category_id(cls,category):
        category = cls.objects.filter(category=category)
        return category

    def __str__(self):
        return self.category

class Image(models.Model):
    image = models.ImageField(upload_to='gallery/')
    name = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='img_category')
    description = models.TextField()
    location = models.ForeignKey(Location,on_delete=models.CASCADE, related_name='img_location')


    def save_image(self):
        self.save()
    
    def delete_image(self):
        self.delete()

    @classmethod
    def search_image(cls,category):
        images = cls.objects.filter(category = category)
        return images
    
    @classmethod
    def filter_by_location(cls,location):

        images = cls.objects.all()
        loc_images=[]

        for image in images:
            for country in location:
                if image.location_id == country.id:
                    loc_images.append(image)
        
        return loc_images
    
    @classmethod
    def copy_image_url(cls,image_id):
        image = cls.objects.filter(id=image_id)
        print(image[0].name)
        image_url = f'{settings.BASE_DIR}{image[0].image.url}'
        pyperclip.copy(image_url)

    @classmethod
    def get_image_by_id(cls, id):
        image = Image.objects.get(pk=id)
        return image        

    def __str__(self):
        return self.name





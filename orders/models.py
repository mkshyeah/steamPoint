from django.db import models
from users.models import Saunas
from registration.models import Registration
from django.conf import settings

class Order(models.Model):
  user = models.ForeignKey(to=Registration, on_delete=models.SET_DEFAULT,
                           blank=True, null=True, default=None)
  
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  email = models.EmailField()
  city = models.CharField(max_length=100)
  address = models.CharField(max_length=250)
  postal_code = models.CharField(max_length=20)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
  paid = models.BooleanField(default=False)
  stripe_id = models.CharField(max_length=255,blank=True)
  
  class Meta:
    ordering = ['-created']
    indexes = [
      models.Index(fields=['-created'])
    ]
    
  
  def __str__(self):
    return f'Заказ {self.id}'
  
  def get_total_cost(self):
    return sum(item.get_cost() for item in self.items.all())
  
  def get_stripe_url(self):
        if not self.stripe_id:
            return ''
        if '_test_' in settings.STRIPE_SECRET_KEY:
            path = '/test/'
        else:
            path = '/'
        return f'https://dashboard.stripe.com{path}payments/{self.stripe_id}'
  
class OrderItem(models.Model):
  order = models.ForeignKey(Order,
                            related_name='items',
                            on_delete=models.CASCADE)
  saunas = models.ForeignKey(Saunas,
                             related_name="order_items",
                             on_delete=models.CASCADE)  
  price_per_hour = models.DecimalField(max_digits=10,
                                       decimal_places=2)
  
  quantity = models.PositiveIntegerField(default=1)
  
  def __str__(self):
    return str(self.id)
  
  def get_cost(self):
    return self.price_per_hour*self.quantity
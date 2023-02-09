from decimal import Decimal
from django.conf import settings
from summercamp.models import Camp 

class Cart(object):
    
    def __init__(self, request):
    #Initializing Cart
        self.session=request.session
        shopping_cart = self.session.get(settings.CART_SESSION_ID)
        if not shopping_cart:
            shopping_cart = self.session[settings.CART_SESSION_ID]={}
        self.shopping_cart=shopping_cart    
        
    def add(self,camp,quantity=1,override_quantity=False):
        camp_id = str(camp.id)
        if camp_id not in self.shopping_cart:
            self.shopping_cart[camp_id]={'quantity':0, 'fees':str(camp.fees)}
            
        if override_quantity:
            self.shopping_cart[camp_id]['quantity']=quantity
        else:
            self.shopping_cart[camp_id]['quantity'] += quantity 
        self.save() 
        
    def save(self):
        self.session.modified = True 
        
    def remove(self, camp):
        camp_id = str(camp.id)
        if camp_id in self.shopping_cart:
            del self.shopping_cart[camp_id]
            self.save()
            
    def __iter__(self):
        camp_ids = self.shopping_cart.keys()
        camps = Camp.objects.filter(id__in=camp_ids)
        
        shopping_cart = self.shopping_cart.copy()
        for camp in camps:
            shopping_cart[str(camp.id)]['camp'] = camp
        
        for item in shopping_cart.values():
            item['fees'] = Decimal(item['fees'])
            item['total_fees'] = item['fees'] * item['quantity']
            yield item
            
    def __len__(self):
        return sum(item['quantity'] for item in self.shopping_cart.values())
    
    def get_total_fees(self):
        return sum(Decimal(item['fees']* item['quantity']) for item in self.shopping_cart.values())
    
    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()
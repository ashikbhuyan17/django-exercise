from django.db import models
#-------------------------timezone----------------
from django.utils.timezone import now
#-------------------------image----------------
from PIL import Image
#-------------------------slugify----------------
from django.utils.text import slugify
#-------------------------------MultiSelectField----------
from multiselectfield import MultiSelectField
#-------------------------------user can post multiple time ----------
from django.contrib.auth.models import User

class contact(models.Model):
    name = models.CharField(max_length = 150)
    message = models.CharField(max_length = 150)
    subject = models.CharField(max_length = 150)
    

    def __str__(self):
        return self.name


class post(models.Model):
    CATEGORY=(
        ('T','T'),
        ('S','S'),
        
    )
    MEDIUM=(
        ('bangla','bangla'),
        ('eng','eng'),
        ('urdu','urdu'),
        ('hindi','hindi'),
    )
#-------------------------------user can post multiple time ----------
    User = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
#-------------------------------blank=True,null=True => default value pass korar jonno  ----------
 
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length = 150)
    slug = models.CharField(max_length = 150,default=title)
    # default=title means title value slug e cole asbe
    email = models.EmailField()
    available = models.BooleanField()
    details = models.TextField()
# choices field ---------------------------
    category = models.CharField(max_length=50, choices=CATEGORY)
    created_at = models.DateTimeField(default=now)
#-------------------------image----------------

    image = models.ImageField(default='default.jpg',upload_to='tuition/images')

#-------------------------------MultiSelectField----------
    medium =MultiSelectField(max_length = 300,max_choices=5,choices=MEDIUM,default='bangla')
    



    def save(self,*args, **kwargs):

# sluging ----------------------------------------------------
        self.slug=slugify(self.title)

#-------------------------image size convert ----------------        
        super(post,self).save(*args,**kwargs)
        img=Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size=(300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
    
#--------------------------------------------------------------------------------------------------------------------------
    
 
    


       
        

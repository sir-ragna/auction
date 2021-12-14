from django.contrib.auth.models import AbstractUser
from django.db import models

class Listing(models.Model):
    title = models.CharField(max_length=140, null=False)
    description = models.CharField(max_length=280, null=False)
    date_created = models.DateTimeField(auto_now_add=True, null=False)
    date_modified = models.DateTimeField(auto_now=True, null=False)
    starting_bid = models.PositiveIntegerField(null=False)
    seller = models.ForeignKey('User', on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.id}:{self.title}"
    def __repr__(self):
        return f"<Listing {str(self)}>"

class User(AbstractUser):
    watchlist = models.ManyToManyField(Listing)
    def __repr__(self):
        return f"<User {self.username}>"

# class Bid(models.Model):
#     listing = models.ForeignKey(Listing, on_delete=models.CASCADE, null=False)
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
#     amount = models.PositiveIntegerField(null=False)

#     def __repr__(self):
#         return f"<Bid '{self.user.username}' bid '{self.amount}' on '{self.listing.title}'>"

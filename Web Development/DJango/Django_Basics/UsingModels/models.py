from django.db import models
from django.urls import reverse
# it is also possible to use models across files by importing the model we want to use
from PollsApp.models import Question

# Create your models here.
# here is a simple table of user

# creating an abstract class to hold the common information that is shared across different models
class UserBaseInfo(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    class Meta:
        abstract = True

class Person(UserBaseInfo):
    SHIRT_SIZES = (
        ('S', 'small'),
        ('M', 'Medium'),
        ('L', 'Large')
    )
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)
    
    def __str__(self):
        return self.first_name + " " + self.last_name

class Musician(UserBaseInfo):
    instrument = models.CharField(max_length=100)

    # adding model methods to define row level functionality to model instance
    @property
    def full_name(self):
        return self.first_name + " " + self.last_name 
    
    @property
    def full_details(self):
        return f"{self.full_name} plays {self.instrument} and belongs to {self.group_set.count()} Groups"


class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    release_date = models.DateField()
    name = models.CharField(max_length=100)
    num_stars = models.IntegerField(default=0)

class Group(models.Model):
    name = models.CharField(max_length=100)
    date_created = models.DateField()
    members = models.ManyToManyField(Musician)

    def __str__(self):
        return self.name

# making use of Meta Options
# Meta Options are used to set or provide more information about a particular table
# for example
class Drummers(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(default=8)

    class Meta:
        db_table = 'Drummers'


# creating and making use of multi table inheritance is also another way to link tables together
# for example
class Place(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)

# now we can create a Restaurant Model and also make it a place
class Restaurant(Place):
    restaurant_type = models.CharField(max_length=200)
    serves_hot_dot = models.BooleanField(default=True)
    serves_pizza = models.BooleanField(default=True)


# Proxy models
# Proxy models are an extension of an original model, by extending the real model methods, functionalites and behavior
# All the query that passes through the proxy is relayed to the original model making it look like ae are interacring with the original model
class MyPerson(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class SuperPerson(MyPerson):
    def name(self):
        print("name cannot be assessed")
    class Meta:
        proxy = True
        

# ## Making Queries in django
class Blog(models.Model):
    name = models.CharField(max_length=200)
    tagline = models.TextField()
    
    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    age = models.IntegerField(default=15)
    
    def __str__(self):
        return self.name
        
class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=200)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField(default=0)
    number_of_likes = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)

class Publisher(models.Model):
    name = models.CharField(max_length=50)

class Book(models.Model):
    title = models.CharField(max_length=50)
    pages = models.IntegerField(default=10)
    price = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    review = models.IntegerField(default=0)
    authors = models.ManyToManyField(Author)
    pub_date = models.DateField()
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, null=True)

    def get_absolute_url(self):
        return reverse("edit-book", kwargs={"book_index": self.pk})
    
    

class Store(models.Model):
    name = models.CharField(max_length=50)
    books = models.ManyToManyField(Book)

# Learning about custom Managers in Django
class SiteUserManager(models.Manager):
    def get_usernames(self):
        return self.get_queryset().values('user_name')

class SiteUsers(models.Model):
    name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    email = models.EmailField()

    people = SiteUserManager()
    objects = models.Manager()


# this is to test the use of custom manager and multi-table inheritance in Django
class OrderManager(models.Manager):
    def active_orders(self):
        return self.get_queryset().filter(order_type="active")
    
    def pending_order(self):
        return self.get_queryset().filter(order_type='pending')
    
    def completed_orders(self):
        return self.get_queryset().filter(order_type='completed')

class Orders(models.Model):
    ORDER_STATUSES = (
        ('A', 'Active'),
        ('P', 'Pending'),
        ('C', 'Completed')
    )
    order_id = models.IntegerField()
    order_type = models.CharField(max_length=200)  # this is used to know how the user has placed the order
    status = models.CharField(max_length=1, choices=ORDER_STATUSES)

    orders = OrderManager()

    class Meta:
        abstract = True  # this is to make the Orders model an abstract model, so it can be inherited by other models

class BusinessOrders(models.Model):
    company_name = models.CharField(max_length=200)

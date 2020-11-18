from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Create your views here.


def index(request):    
    categories = Category.objects.all()
    restaurants = Restaurant.objects.all()
    content = {'categories' : categories, 'restaurants' : restaurants}
    # return HttpResponse("index")    
    
    return render(request, 'shareRes/index.html', content)

def restaurantCreate(request):
    # return HttpResponse("restaurantCreate")
    categories = Category.objects.all()
    content = {'categories': categories}
	
    return render(request, 'shareRes/restaurantCreate.html', content)

def Create_restaurant(request):
    category_id = request.POST['resCategory']
    category = Category.objects.get(id = category_id)
    restaurant_name = request.POST['resTitle']
    restaurant_link = request.POST['resLink']
    restaurant_content = request.POST['resContent']
    restaurant_keyword = request.POST['resLoc']
    new_restaurant = Restaurant(category = category, restaurant_name = restaurant_name, restaurant_link =                 restaurant_link, restaurant_content=restaurant_content, restaurant_keyword=restaurant_keyword)
    new_restaurant.save()
    
    return HttpResponseRedirect(reverse('index'))

def Delete_restaurant(request):
    res_id = request.POST['resId']
    restaurant = Restaurant.objects.get(id = res_id)
    restaurant.delete()
    return HttpResponseRedirect(reverse('index'))

def restaurantDetail(request,res_id):
    restaurant = Restaurant.objects.get(id=res_id)
    content = {'restaurant' : restaurant}
    
    return render(request, 'shareRes/restaurantDetail.html', content)

def restaurantUpdate(request,res_id):
	categories=Category.objects.all()
	restaurant = Restaurant.objects.get(id = res_id)
	content={'categories':categories, 'restaurant':restaurant}
    
	return render(request,'shareRes/restaurantUpdate.html',content)
	
    
def Update_restaurant(request):
    resId = request.POST['resId']
    category_id = request.POST['resCategory']
    category = Category.objects.get(id = category_id)
    restaurant_name = request.POST['resTitle']
    restaurant_link = request.POST['resLink']
    restaurant_content = request.POST['resContent']
    restaurant_keyword = request.POST['resLoc']
    
    restaurant = Restaurant.objects.get(id= resId)
    restaurant.category=category
    restaurant.restaurant_name=restaurant_name
    restaurant.restaurant_link=restaurant_link
    restaurant.restaurant_content=restaurant_content
    restaurant.restaurant_keyword=restaurant_keyword
    
    restaurant.save()
    
    
    

    return HttpResponseRedirect(reverse('resDetailPage', kwargs={'res_id':resId}))

def categoryCreate(request):
    categories = Category.objects.all()
    content = {'categories': categories}
    # return HttpResponse("categoryCreate")
    return render(request, 'shareRes/categoryCreate.html', content)

def Create_category(request):
    category_name = request.POST['categoryName']
    new_category = Category(category_name = category_name)
    new_category.save()
    
    return HttpResponseRedirect(reverse('index'))
    # return HttpResponse("여기서 category Create 기능을 구현할 거야.")
    
def Delete_category(request):
    category_id = request.POST['categoryId']
    delete_category = Category.objects.get(id = category_id)
    delete_category.delete()
    
    return HttpResponseRedirect(reverse('cateCreatePage'))


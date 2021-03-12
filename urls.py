
from django.urls import path
from .import views
from django.contrib.auth.decorators import login_required
urlpatterns = [

    path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"), 
    path('logout/', views.logoutUser, name="logout"),
    

    path('', views.dashboard,name="dashboard"),
    path('/category<str:name>/', views.category,name="category"),
    

    path("add-to-cart-<int:pro_id>/",login_required( views.AddToCartView.as_view()), name="addtocart"),
    path("manage-cart/<int:cp_id>/", views.ManageCartView.as_view(), name="managecart"),
    path("my-cart/", views.MyCartView.as_view(), name="mycart"),
    path("search/", views.SearchView.as_view(), name="search"),
   
    
    
   

   
    
 
   
    
    

    
   
   
    
]

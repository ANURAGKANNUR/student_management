
from django.urls import path,include
from . import views

urlpatterns = [
    path('register/',views.register,name="register"),
    path("view/<int:id>", views.student_view, name="view"),
    path('list/', views.studentlist,name="list"),
    path('search/',views.search,name='search'),
    path('',views.start),
    path('load/',views.loadregister,name='load')

    # path('admin/', admin.site.urls),

]

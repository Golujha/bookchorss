from django.contrib import admin
from django.urls import path
from book.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path ("", homepage,name="homepage"),
    path ("insert/", insert,name="insertpage"),
    path ("generous/<int:cat_id>/", viewPost,name="generous"),
    path ("show/<int:post_id>/", singlePost,name="singlePost"),
    path ("search/", search,name="search"),
    
    
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
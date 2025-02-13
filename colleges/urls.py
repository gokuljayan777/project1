from django.urls import path
from . import views

urlpatterns = [
    path('visit/stc.html/', views.stc, name='stc'),
    path('visit/kv.html/', views.kv, name='kv'),
    path('visit/alocyus.html/', views.alocyus, name='alocyus'),
    path('visit/christ.html/', views.christ, name='christ'),
    path('visit/littleflower.html/', views.littleflower, name='littleflower'),
    path('visit/mar.html/', views.mar, name='mar'),
    path('visit/naipunya.html/', views.naipunya, name='naipunya'),
    path('visit/nehru.html/', views.nehru, name='nehru'),
    path('visit/sahurdaya.html/', views.sahurdaya, name='sahurdaya'),
    path('visit/sreenarayana.html/', views.sreenarayana, name='sreenarayana'),
    path('visit/stmarys.html/', views.stmarys, name='stmarys'),
    path('visit/universal.html/', views.universal, name='universal'),
    path('visit/vidhya.html/', views.vidhya, name='vidhya'),
    path('visit/vimala.html/', views.vimala, name='vimala'),
    path('visit/holy.html/', views.holy, name='holy'),

]

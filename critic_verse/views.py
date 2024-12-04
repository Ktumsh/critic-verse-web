from io import BytesIO
from django.http import HttpResponse
from django.shortcuts import render
from django_user_agents.utils import get_user_agent
import qrcode

def index_view(request):
    user_agent = get_user_agent(request)
    
    is_mobile = user_agent.is_mobile or user_agent.is_tablet
    is_pc = not is_mobile
    
    app_link = "https://drive.usercontent.google.com/download?id=1Tdo9F2pazWVkCX06mWZS2D5P6lAHcl1p&export=download&authuser=1"
    
    context = {
        'is_mobile': is_mobile,
        'is_pc': is_pc,
        'app_link': app_link,
    }
    
    return render(request, 'index.html', context)

def generate_qr(request):
    qr_url = "https://drive.usercontent.google.com/download?id=1Tdo9F2pazWVkCX06mWZS2D5P6lAHcl1p&export=download&authuser=1"
    
    qr = qrcode.make(qr_url)
    
    qr_image = BytesIO()
    qr.save(qr_image)
    qr_image.seek(0)
    
    return HttpResponse(qr_image, content_type="image/png")
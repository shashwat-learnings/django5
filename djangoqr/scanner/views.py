from django.shortcuts import render
from .models import QRCode
import qrcode
from django.core.files.storage import FileSystemStorage
from io import BytesIO
from django.core.files.base import ContentFile
from django.conf import settings
from pathlib import Path
from pyzbar.pyzbar import decode
from PIL import Image


# Create your views here.

def generate_qr(request):
    qr_image_url=None
    if request.method =='POST':
        mobile_number = request.POST.get('mobile_number')
        data = request.POST.get('qr_data')

        if not mobile_number or len(mobile_number)!=10 or not mobile_number.isdigit():
            return render(request,'scanner/generate.html',{'error':'Invalid mobile number'})
        
        qr_content = f"{data}|{mobile_number}"
        qr = qrcode.make(qr_content)
        qr_image_io = BytesIO()
        qr.save(qr_image_io,format='PNG')
        qr_image_io.seek(0)
        qr_storage_path = settings.MEDIA_ROOT / 'qr_codes'
        fs = FileSystemStorage(location=qr_storage_path,base_url='/media/qr_codes/')
        filename = f"{data}_{mobile_number}.png"
        qr_image_content = ContentFile(qr_image_io.read( ),name=filename)
        file_path = fs.save(filename,qr_image_content)
        qr_image_url = fs.url(filename)

        QRCode.objects.create(data=data,mobile_number=mobile_number)
    return render(request,'scanner/generate.html',{'qr_image_url':qr_image_url})

def scan_qr(request):
    result=None
    if request.method == 'POST' and request.FILES.get('qr_image'):
        qr_image = request.FILES['qr_image']
        mobile_number = request.POST.get('mobile_number')
    
        if not mobile_number or len(mobile_number)!=10 or not mobile_number.isdigit():
            return render(request,'scanner/scan.html',{'error':'Invalid mobile number'})
        
        fs = FileSystemStorage()
        filename = fs.save(qr_image.name, qr_image)
        image_path = Path(fs.location) / filename
        try:
            image = Image.open(image_path)
            decoded_object = decode(image)

            if decoded_object:
                qr_content = decoded_object[0].data.decode('utf-8').strip()
                qr_data, qr_mobile_number = qr_content.split('|')

                qr_entry = QRCode.objects.filter(data=qr_image,mobile_number=qr_mobile_number).first()

                if qr_entry and qr_mobile_number==mobile_number:
                    result = "Scan Sucess: Valid Qr Code"

                    qr_entry.delete()

                    qr_image_path = settings.MEDIA_ROOT / 'qr_codes' / f"{qr_data}_{qr_mobile_number}.png"
                    if image_path.exists():
                        image_path.unlink()
                else:
                    result = "Scan Failed: Invalid QR Code or mobile number mismatch"

            else:
                result = "No QR Code detected in the image"
        except Exception as e:
            result = f"Error processing the image: {str(e)}"
        finally:
            pass

    return render(request,'scanner/scanner.html',{'result':result})
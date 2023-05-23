# import base64
#
# import numpy as np
# import pytesseract
# from django.contrib import messages
# from django.shortcuts import render
# from PIL import Image
#
# # you have to install tesseract module too from here - https://github.com/UB-Mannheim/tesseract/wiki
# pytesseract.pytesseract.tesseract_cmd = (
#     r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # Path to tesseract.exe
# )
#
#
# def homepage(request):
#     if request.method == "POST":
#         form = ImageForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             obj = form.instance
#
#             return render(request, "index.html", {"obj": obj})
#     else:
#         form = ImageForm()
#     img = Image.objects.all()
#
#     return render(request, "index.html", {"img": img, "form": form})
#     # if request.method == "POST":
#         # try:
#         #     image = request.FILES["imagefile"]
#         #     # encode image to base64 string
#         #     image_base64 = base64.b64encode(image.read()).decode("utf-8")
#         # except:
#         #     messages.add_message(
#         #         request, messages.ERROR, "No image selected or uploaded"
#         #     )
#         #     return render(request, "home.html")
#         # lang = request.POST["language"]
#         # img = np.array(Image.open(image))
#         # text = pytesseract.image_to_string(img, lang=lang)
#         # return text to html
#         return render(request, "result.html", {"ocr": text, "image": image_base64})
#
#     return render(request, "home.html")


from django.shortcuts import render

from django.shortcuts import render
from PIL import Image
import pytesseract
import re

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

data = {}
def homepage(request):
    if request.method == 'POST' and request.FILES.get('image'):
        image = request.FILES['image']
        image = Image.open(image)
        res = pytesseract.image_to_string(image)
        result = res.split('\n')
        for text in result:
            if re.findall('^Ma|^Maung|^Daw|^U',text):
                data['name'] = text[0:len(text)-11]
            if re.findall('^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[012])/(19|20)',text):
                data['date'] = text
            if (re.findall('Ks$',text)):
                data['amount'] = text[1:]
            if re.findall('^\d{10}',text):
                data['id'] = text
        return render(request, 'result.html',{'data':data})
    return render(request,'home.html')
# Create your views here.
from pytesseract import pytesseract
import re
from PIL import Image

# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


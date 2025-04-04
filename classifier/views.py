from django.shortcuts import render
from django.conf import settings
from .forms import ImageUploadForm
from image_classifier import ImageClassifier
import os

def home(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the uploaded image
            image = form.cleaned_data['image']
            image_path = os.path.join(settings.MEDIA_ROOT, 'uploads', image.name)
            os.makedirs(os.path.dirname(image_path), exist_ok=True)
            
            with open(image_path, 'wb') as f:
                for chunk in image.chunks():
                    f.write(chunk)
            
            # Load and predict
            classifier = ImageClassifier()
            classifier.load_model()  # Load the trained model
            
            from PIL import Image
            img = Image.open(image_path)
            
            # Resize image to match model input size
            img = img.resize((32, 32))
            
            # Make prediction
            prediction, confidence = classifier.predict(img)
            
            return render(request, 'classifier/result.html', {
                'prediction': prediction,
                'confidence': confidence * 100,
                'image_url': os.path.join(settings.MEDIA_URL, 'uploads', image.name)
            })
    else:
        form = ImageUploadForm()
    
    return render(request, 'classifier/home.html', {'form': form})

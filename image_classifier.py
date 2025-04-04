import numpy as np
from sklearn.ensemble import RandomForestClassifier
from PIL import Image
import joblib
import os

class ImageClassifier:
    def __init__(self):
        self.model = None
        self.class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer',
                           'dog', 'frog', 'horse', 'ship', 'truck']
    
    def preprocess_image(self, image):
        """Preprocess image for prediction"""
        # Resize image to 32x32
        image = image.resize((32, 32))
        # Convert to grayscale and flatten
        image = image.convert('L')
        # Convert to numpy array and normalize
        img_array = np.array(image).flatten() / 255.0
        return img_array
    
    def train_model(self, train_images, train_labels):
        """Train the model"""
        # Preprocess all training images
        X_train = np.array([self.preprocess_image(img) for img in train_images])
        y_train = np.array(train_labels)
        
        # Create and train the model
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.model.fit(X_train, y_train)
    
    def save_model(self, path='saved_model'):
        """Save the trained model"""
        if not os.path.exists(path):
            os.makedirs(path)
        joblib.dump(self.model, os.path.join(path, 'model.joblib'))
    
    def load_model(self, path='saved_model'):
        """Load a saved model"""
        model_path = os.path.join(path, 'model.joblib')
        if os.path.exists(model_path):
            self.model = joblib.load(model_path)
        else:
            raise Exception("Model file not found")
    
    def predict(self, image):
        """Make prediction on a single image"""
        if self.model is None:
            raise Exception("Model not loaded or trained")
        
        # Preprocess the image
        img_array = self.preprocess_image(image)
        
        # Make prediction
        prediction = self.model.predict([img_array])[0]
        probabilities = self.model.predict_proba([img_array])[0]
        confidence = probabilities[prediction]
        
        return self.class_names[prediction], confidence 
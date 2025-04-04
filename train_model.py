import numpy as np
from PIL import Image
import os
from image_classifier import ImageClassifier

def create_synthetic_data(n_samples=100):
    """Create synthetic image data for training"""
    images = []
    labels = []
    
    for i in range(n_samples):
        # Create a random 32x32 grayscale image
        img_array = np.random.randint(0, 255, (32, 32), dtype=np.uint8)
        img = Image.fromarray(img_array)
        images.append(img)
        
        # Assign a random label (0-9)
        label = np.random.randint(0, 10)
        labels.append(label)
    
    return images, np.array(labels)

def main():
    # Create saved_model directory if it doesn't exist
    if not os.path.exists('saved_model'):
        os.makedirs('saved_model')
    
    # Create synthetic data
    print("Creating synthetic data...")
    train_images, train_labels = create_synthetic_data(100)
    
    # Create and train the model
    print("Training model...")
    classifier = ImageClassifier()
    classifier.train_model(train_images, train_labels)
    
    # Save the model
    print("Saving model...")
    classifier.save_model()
    
    print("Model training completed and saved successfully!")

if __name__ == "__main__":
    main() 
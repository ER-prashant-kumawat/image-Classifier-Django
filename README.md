# Image Classification Web App

A Django web application that uses machine learning to classify images into different categories.

## Features

- Upload images through a web interface
- Real-time image classification
- Support for multiple image formats
- Simple and intuitive user interface

## Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/yourusername/image-classifier.git
cd image-classifier
```

2. Create and activate virtual environment:
```bash
python -m venv venv
# On Windows
.\venv\Scripts\activate
# On Linux/Mac
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Train the model:
```bash
python train_model.py
```

5. Run migrations:
```bash
python manage.py migrate
```

6. Start the development server:
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser.

## Deployment

### Deploying to Heroku

1. Create a Heroku account and install Heroku CLI
2. Login to Heroku:
```bash
heroku login
```

3. Create a new Heroku app:
```bash
heroku create your-app-name
```

4. Add PostgreSQL addon:
```bash
heroku addons:create heroku-postgresql:hobby-dev
```

5. Configure environment variables:
```bash
heroku config:set SECRET_KEY=your-secret-key
heroku config:set DEBUG=False
```

6. Deploy:
```bash
git push heroku main
```

7. Run migrations:
```bash
heroku run python manage.py migrate
```

## Technologies Used

- Python 3.10
- Django 4.2
- scikit-learn
- Pillow
- NumPy
- Matplotlib

## License

This project is licensed under the MIT License - see the LICENSE file for details. 
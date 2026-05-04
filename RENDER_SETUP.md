# Render पर Deploy करने के लिए Setup Guide

## Step 1: Render पर नया Web Service बनाएं

1. https://render.com पर जाएं
2. **New +** → **Web Service** क्लिक करें
3. अपना GitHub repository connect करें

## Step 2: Build और Start Commands

**Build Command:**
```bash
bash build.sh
```

**Start Command:**
```bash
gunicorn Auth_Project.wsgi:application --bind 0.0.0.0:$PORT
```

## Step 3: Environment Variables

Render Dashboard पर जाएं और ये variables add करें:

### Development/Testing:
```
DEBUG=True
ALLOWED_HOSTS=your-service-name.onrender.com,localhost
```

### Production (Security):
```
DEBUG=False
SECURE_SSL_REDIRECT=True
SECURE_HSTS_SECONDS=31536000
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True
```

### Database & Email:
```
MONGODB_URI=mongodb+srv://vt464670_db_user:tGWT0e9Wdl6tCiC2@cluster0.hlj8gb9.mongodb.net/djongo_mongo_auth?retryWrites=true&w=majority&tlsAllowInvalidCertificates=true

EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
DEFAULT_FROM_EMAIL=Your Name <your-email@gmail.com>
```

### CORS Configuration:
```
CORS_ALLOWED_ORIGINS=https://your-frontend-domain.com,https://your-service-name.onrender.com
```

### Secret Key (production me zaroori):
```
SECRET_KEY=your-new-secret-key-here
```

## Step 4: Render Dashboard Settings

1. **Deploy Hook** enable करें (optional)
2. **Auto Deploy** enable करें (GitHub changes पर auto deploy)
3. **Instance Type**: Free plan से start करें ya Paid

## Step 5: Logs Check करें

```
Render Dashboard → Logs tab में errors देखें
```

## Common Issues

### 500 Internal Server Error:
- Environment variables check करें
- `MONGODB_URI` सही है क्या?
- `DEBUG=False` पर logs देखें

### 404 Not Found:
- `ALLOWED_HOSTS` में आपका Render domain है क्या?
- Static files collected हैं क्या?

### Database Connection Error:
- MongoDB Atlas connection string verify करें
- IP whitelist में Render IP add करें (MongoDB Atlas → Network Access)

### Email Not Working:
- App Password use करें (Google के लिए)
- EMAIL_HOST_USER और EMAIL_HOST_PASSWORD correct हैं?

## Testing

Deploy के बाद:

```bash
https://your-service-name.onrender.com/docs/
```

यहाँ Swagger UI खुल जाएगा। API test करें।

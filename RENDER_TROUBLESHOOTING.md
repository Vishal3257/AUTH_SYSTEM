# Render पर 500 Internal Server Error - Troubleshooting Guide

## अगर 500 error आ रहा है तो यह check करें:

### 1️⃣ Render Dashboard Logs Check करें

```bash
Render Dashboard → Logs (अपना service select करें)
```

**Common Error Messages और उनके Solutions:**

#### ❌ "ModuleNotFoundError: No module named 'dotenv'"
**Solution:**
```
pip install python-dotenv
```

#### ❌ "MongoServerError: authentication failed"
**Solution:**
- MongoDB Atlas जाएं → Network Access
- Render का IP whitelist में add करें
- या फिर सभी IPs allow करें: `0.0.0.0/0`

#### ❌ "MONGODB_URI environment variable not set"
**Solution:**
- Render Dashboard → Environment
```
MONGODB_URI=mongodb+srv://vt464670_db_user:password@cluster0...
```

#### ❌ "ALLOWED_HOSTS verification failed"
**Solution:**
```
ALLOWED_HOSTS=your-service-name.onrender.com
```
(Render dashboard से अपना URL check करें)

#### ❌ "Email backend error"
**Solution:**
```
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=app-password-not-regular-password
```
(Google ke liye App Password use करें!)

---

### 2️⃣ Environment Variables Setup

Render Dashboard पर जाएं:
1. Select your service
2. **Environment** tab
3. ये सब variables add करें:

```
DEBUG=False
ALLOWED_HOSTS=your-service-name.onrender.com
MONGODB_URI=mongodb+srv://vt464670_db_user:tGWT0e9Wdl6tCiC2@cluster0.hlj8gb9.mongodb.net/djongo_mongo_auth?retryWrites=true&w=majority&tlsAllowInvalidCertificates=true
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
DEFAULT_FROM_EMAIL=Your Name <your-email@gmail.com>
CORS_ALLOWED_ORIGINS=https://your-service-name.onrender.com
SECRET_KEY=your-generated-secret-key
SECURE_SSL_REDIRECT=False
SESSION_COOKIE_SECURE=False
CSRF_COOKIE_SECURE=False
```

---

### 3️⃣ Build Command Verify करें

यह होना चाहिए:
```
bash build.sh
```

अगर `build.sh` नहीं है तो:
```
pip install -r requirements.txt && python manage.py collectstatic --no-input && python manage.py migrate
```

---

### 4️⃣ Start Command Verify करें

```
gunicorn Auth_Project.wsgi:application --bind 0.0.0.0:$PORT
```

---

### 5️⃣ requirements.txt Complete है?

ये packages होने चाहिए:
```
Django
djangorestframework
djangorestframework-simplejwt
drf-spectacular
django-cors-headers
gunicorn
python-dotenv
djongo
pymongo
certifi
```

---

### 6️⃣ Database Migration Status

Render logs में देखें:
```
Running migrations... ✓
```

अगर migration fail हो तो कुछ models में issue है।

---

### 7️⃣ Static Files

Logs में check करें:
```
collectstatic... ✓
```

---

## 🔧 Production Settings सही हैं?

Check करें कि `DEBUG=False` पर error details नहीं show हो रहे।

---

## ✅ Testing करने के लिए:

अगर सब ठीक है तो:

```
https://your-service-name.onrender.com/docs/
```

यहाँ Swagger UI खुल जाएगा।

---

## 📝 Step by Step Checklist:

- [ ] Environment variables सब add किए?
- [ ] ALLOWED_HOSTS में अपना Render domain है?
- [ ] MONGODB_URI सही है?
- [ ] EMAIL credentials सही हैं?
- [ ] build.sh file GitHub repo में है?
- [ ] requirements.txt updated है?
- [ ] .env file .gitignore में है? (credentials leak न हो)
- [ ] Render restart किया?

---

## 🚨 अगर फिर भी 500 error है:

1. Logs में पूरा error message देखें
2. उस error को Google करें
3. या इस guide में उसे ढूंढें
4. फिर solution apply करें
5. Render restart करें: Dashboard → Service → Restart

---

**Important:** डेवलपमेंट में `DEBUG=True` और Production में `DEBUG=False` रखें!

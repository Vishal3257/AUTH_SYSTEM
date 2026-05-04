# Render Deployment - Quick Reference

## Files Created/Updated:

✅ `.env.example` - Environment variables template
✅ `build.sh` - Build script for Render
✅ `render.yaml` - Render configuration
✅ `requirements.txt` - Updated with all dependencies
✅ `Auth_Project/settings.py` - Updated for environment variables
✅ `Auth_Project/wsgi.py` - Updated to load .env file

## Your Render Service URL:

```
https://your-service-name.onrender.com
```

## API Endpoints:

```
POST   /api/register/                  - Register new user
POST   /api/send-otp/                  - Send OTP to email
POST   /api/login-verify-otp/          - Verify OTP and login
POST   /api/logout/                    - Logout user
GET    /docs/                          - Swagger API Documentation
GET    /api/schema/                    - OpenAPI Schema
```

## Swagger UI Location:

```
https://your-service-name.onrender.com/docs/
```

## Environment Variables You MUST Set:

**On Render Dashboard:**

1. `DEBUG=False` (production setting)
2. `ALLOWED_HOSTS=your-service-name.onrender.com`
3. `MONGODB_URI=` (your MongoDB connection string)
4. `EMAIL_HOST_USER=` (your Gmail)
5. `EMAIL_HOST_PASSWORD=` (Gmail App Password)
6. `SECRET_KEY=` (generate new one!)
7. `CORS_ALLOWED_ORIGINS=https://your-service-name.onrender.com`

## Local Testing Before Deploying:

```bash
# 1. Create .env file with your values
cp .env.example .env

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run migrations
python manage.py migrate

# 4. Start server
python manage.py runserver

# 5. Test on Swagger
http://localhost:8000/docs/
```

## Deploy to Render:

1. Push code to GitHub
2. Create new Web Service on Render
3. Connect GitHub repo
4. Add Environment Variables
5. Deploy!

## Check Logs:

```
Render Dashboard → Logs → See errors
```

## If 500 Error:

→ See `RENDER_TROUBLESHOOTING.md`

## MongoDB Atlas Setup:

1. Go to MongoDB Atlas
2. Network Access → Add 0.0.0.0/0 (or Render IPs)
3. Copy connection string
4. Set as MONGODB_URI on Render

## Support:

For detailed troubleshooting: `RENDER_SETUP.md` and `RENDER_TROUBLESHOOTING.md`

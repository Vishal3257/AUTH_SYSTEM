# Django SECRET_KEY Generation for Production

## Production के लिए नया SECRET_KEY कैसे generate करें:

### Option 1: Django Shell से

```bash
python manage.py shell
```

फिर:

```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

Output को copy करें और Render environment variables में add करें।

### Option 2: Python से directly

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### Option 3: Online Generator

https://djecrety.ir/

⚠️ **Warning:** Online tools का use production के लिए safe नहीं है!

---

## Render Dashboard पर SECRET_KEY Add करें:

1. Render Dashboard जाएं
2. अपना Service select करें
3. **Environment** tab click करें
4. **Add Environment Variable** click करें
5. Key: `SECRET_KEY`
6. Value: Generated key को paste करें
7. **Deploy** करें

---

## Important Security Tips:

✅ हमेशा नया SECRET_KEY production के लिए बनाएं
✅ SECRET_KEY को GitHub पर commit न करें
✅ .env file को .gitignore में रखें
✅ हर 6 महीने में SECRET_KEY change करें
✅ Local development के लिए अलग SECRET_KEY रखें

---

## देखें:

```
RENDER_SETUP.md               - Full Render setup guide
RENDER_TROUBLESHOOTING.md     - Common errors और solutions
DEPLOYMENT_CHECKLIST.md       - Quick reference
```

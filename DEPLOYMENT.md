# StudySpend Deployment Guide

## Quick Start - Deploy in 5 Minutes

### **Option 1: Deploy to Render (RECOMMENDED)**

1. **Prepare GitHub:**
   ```powershell
   cd "cs50 Finall Project"
   git init
   git add .
   git commit -m "StudySpend - CS50 Final Project"
   git remote add origin https://github.com/YourUsername/StudySpend.git
   git push -u origin main
   ```

2. **Deploy to Render:**
   - Go to render.com
   - Sign up with GitHub
   - Click "New +" → Web Service
   - Connect your GitHub repo
   - Fill in:
     - **Name:** studyspend
     - **Environment:** Python 3
     - **Build Command:** `pip install -r requirements.txt`
     - **Start Command:** `gunicorn app:app`
   - Click Deploy
   - Wait 2-3 minutes
   - Share the URL!

3. **Access Your App:**
   - Public link: `studyspend-xxxxx.onrender.com`
   - Works on phone, tablet, computer
   - Anyone can access without downloading

---

### **Option 2: Deploy to PythonAnywhere (Easier Setup)**

1. Go to pythonanywhere.com
2. Sign up (free account)
3. Upload your files
4. Create new Flask app
5. Configure WSGI file
6. Reload
7. Get link: `yourname.pythonanywhere.com`

---

### **Option 3: Local Network (For Testing)**

Edit `app.py`:
```python
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
```

Find your IP:
```powershell
ipconfig
```

Others on WiFi access: `http://192.168.1.XXX:5000`

---

## What Gets Deployed

- ✅ app.py (all routes)
- ✅ templates/ (all HTML files)
- ✅ static/styles.css (styling)
- ✅ database.db (created on first run)
- ✅ requirements.txt (dependencies)
- ✅ Procfile (deployment config)

---

## After Deployment

Users can:
- ✅ Register new accounts
- ✅ Track expenses
- ✅ Manage study tasks
- ✅ Filter by category
- ✅ View dashboard
- ✅ Everything works!

---

## Important Notes

- Database is created automatically on first run
- Each user has isolated data
- Free tier may have slight delays on first access
- App sleeps after 15 mins of inactivity (free Render tier)

---

## Troubleshooting

**App won't start?**
- Check requirements.txt has correct versions
- Check Procfile syntax (no extra spaces)

**Database errors?**
- Render creates fresh database on deploy
- No need to include database.db in git

**Port issues?**
- Render automatically assigns port
- Don't hardcode port in app.py

---

## Share Your App!

After deployment, share URL:
- Email: "Check out my CS50 project: [URL]"
- Social media: Post the link
- QR code: Generate from URL

Anyone can access without downloading anything! 🎉

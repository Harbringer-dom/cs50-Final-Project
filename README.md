# StudySpend 📚💰

Hey! This is my CS50 Final Project - a web app I built using Flask to help students like me track expenses and manage study tasks. It's been a great learning experience working with Python, databases, and web development!

## What It Does

### Dashboard
- Shows your total spending this month
- Tracks how many study tasks you have and how many are done
- Breaks down expenses by category
- Quick overview of your money and study progress

### Expense Tracker
- Add expenses with categories like Food, Travel, Study, etc.
- Filter to see spending in specific categories
- See total amounts spent
- Delete expenses if you made a mistake
- Everything sorted by date

### Study Planner
- Create study tasks with titles, descriptions, and due dates
- Mark tasks as completed
- Tasks sorted by what's done and what's due soon
- Delete tasks when you're done with them

### User Accounts
- Register with a username and password
- Login securely (passwords are hashed)
- Each person only sees their own data

### Nice Touches
- Shows success/error messages for everything you do
- Works on phone, tablet, and computer
- Checks your inputs and shows helpful messages
- Friendly messages when you have no data yet
- Smooth animations for a nice feel

## What I Used

This was my first time building a full web app! I learned:
- **Flask**: Python framework for web apps
- **SQLite**: Simple database that stores data in a file
- **Werkzeug**: For secure password handling
- **HTML/CSS**: For the pages and styling
- **Jinja2**: Flask's template system
- **ChatGPT**: I got help from ChatGPT for debugging and learning concepts
- **GitHub Copilot**: I used this to get explanations and understand changes in the project, especially for error handling

## Database Design

I kept it simple with three tables:

### Users
```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    hash TEXT NOT NULL
);
```

### Study Tasks
```sql
CREATE TABLE study_tasks2 (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    description TEXT,
    due_date DATE,
    completed INTEGER DEFAULT 0,
);

### Expenses
```sql
CREATE TABLE expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    category TEXT NOT NULL,
    amount REAL NOT NULL,
    date DATE NOT NULL,
    note TEXT,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
```

## How to Run It

You'll need Python 3.7+ installed.

### Quick Setup
1. Download or clone this project
2. Open terminal in the project folder
3. Create a virtual environment (optional but good practice):
   ```
   python -m venv .venv
   .\.venv\Scripts\activate  # Windows
   ```
4. Install the requirements:
   ```
   pip install -r requirements.txt
   ```
5. Run the app:
   ```
   python app.py
   ```
6. Open http://localhost:5000 in your browser

## Project Files

```
cs50 Finall Project/
├── app.py              # The main app file
├── requirements.txt    # List of packages needed
├── static/styles.css   # CSS for styling
└── templates/          # HTML templates
    ├── layout.html     # Base page with nav
    ├── dashboard.html  # Home page
    ├── login.html      # Login form
    ├── register.html   # Signup form
    ├── study.html      # Study tasks page
    └── expenses.html   # Expense page
```

## How to Use

### Getting Started
1. Register a new account with username/password
2. Login to see your dashboard

### Adding Expenses
- Go to Expense Tracker
- Pick a category (Food, Travel, etc.)
- Enter amount, date, and optional note
- Click Add Expense
- Use category buttons to filter what you see
- Delete button removes expenses

### Study Tasks
- Go to Study Planner
- Add tasks with title, description, due date
- Mark as done when finished
- Delete when no longer needed

### Dashboard
- Shows your spending this month
- Counts your study tasks
- Breaks down expenses by category

## Routes in the App

| Route | Method | Purpose |
|-------|--------|---------|
| `/` | GET | Dashboard |
| `/register` | GET, POST | Sign up |
| `/login` | GET, POST | Sign in |
| `/logout` | GET | Sign out |
| `/study` | GET, POST | Study tasks |
| `/delete_task/<id>` | GET | Delete task |
| `/toggle_task/<id>` | GET | Mark task done |
| `/expenses` | GET, POST | Expenses |
| `/delete_expense/<id>` | GET | Delete expense |

## Security & Checks

- Passwords are securely hashed
- Users can only see their own data
- Forms check for required fields and valid inputs
- Uses safe SQL queries to prevent issues

## Error Messages

- Green messages for success
- Red messages for errors
- Helpful hints for what went wrong

## What I Learned

This was my first big Flask project! I learned a lot about:
- Building web apps with Python
- Working with databases
- User authentication
- Making responsive designs
- Deploying to the web

## Future Ideas

If I had more time, I might add:
- Charts to visualize spending
- Export data to CSV
- Budget goals and alerts
- Email reminders for tasks

## Having Issues?

### Database Issues
If you encounter database errors:
1. Delete `database.db`
2. Restart the application
3. Create a new database by registering

### Port Already in Use
If port 5000 is busy:
1. Edit `app.py` and change `port=5000` to `port=5001`
2. Go to `http://localhost:5001`

### Virtual Environment Problems
```bash
# Exit current env
deactivate

# Delete and remake
rm -r .venv
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## About This Project

This was my CS50 final project. I learned a ton about web development!

**Made by**: Chitvan Suri  
**Date**: January 2026  
**Course**: CS50

## 🚀 Want to Share It Online?

Check out [DEPLOYMENT.md](DEPLOYMENT.md) for easy ways to put it on the internet:
- Render (free option)
- PythonAnywhere (super easy)
- Local network (for friends)

## 📂 Get the Code

The code is on GitHub. To run it yourself:
```bash
git clone https://github.com/Harbringer-dom/cs50-Final-Project.git
cd cs50-Final-Project
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

## Why I Built This

I wanted to make something useful that combines two things students deal with: money and studying. It was challenging but fun to learn Flask and databases!

# StudySpend 📚💰

A Flask-based web application for managing study tasks and personal expenses. Track your spending by category while organizing your study schedule efficiently.

## Features

### 📊 Dashboard
- **Monthly Expense Overview**: View your total spending for the current month
- **Study Progress**: Track total tasks, completed tasks, and pending tasks
- **Category Breakdown**: See expense distribution across categories
- **Quick Summary**: At-a-glance insights into your spending and productivity

### 💸 Expense Tracker
- **Add Expenses**: Record expenses with category, amount, date, and notes
- **Category Filtering**: Filter expenses by Food, Travel, Study, Shopping, Entertainment, or Other
- **Track Totals**: View total spending overall or by category
- **Delete Expenses**: Remove expenses with confirmation
- **Date-based Sorting**: Expenses sorted by date for easy navigation

### 📚 Study Planner
- **Create Study Tasks**: Add tasks with title, description, and due date
- **Task Status**: Mark tasks as completed or pending
- **Priority Sorting**: Tasks automatically sorted by completion status and due date
- **Task Management**: Delete completed or unnecessary tasks
- **Task Details**: Include descriptions and track due dates

### 🔐 User Authentication
- **Register**: Create a new account with username and password
- **Login**: Secure login with password hashing (Werkzeug)
- **Logout**: Session management and secure logout
- **User Isolation**: Each user sees only their own data

### 💬 User Experience
- **Flash Messages**: Real-time feedback for all actions (success/error)
- **Responsive Design**: Works on desktop, tablet, and mobile devices
- **Form Validation**: Client and server-side validation with helpful error messages
- **Empty States**: Friendly messages when no data exists
- **Smooth Animations**: Visual feedback for messages and interactions

## Technology Stack

- **Backend**: Flask (Python web framework)
- **Database**: SQLite3
- **Authentication**: Werkzeug password hashing
- **Frontend**: HTML5, Jinja2 templates
- **Styling**: Custom CSS with responsive grid layout
- **Session Management**: Flask sessions with secure secret key

## Database Schema

### Users Table
```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    hash TEXT NOT NULL
);
```

### Study Tasks Table
```sql
CREATE TABLE study_tasks2 (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    description TEXT,
    due_date DATE,
    completed INTEGER DEFAULT 0,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
```

### Expenses Table
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

## Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Steps

1. **Clone or Download the Project**
```bash
cd "cs50 Finall Project"
```

2. **Create a Virtual Environment**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1    # PowerShell
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the Application**
```bash
python app.py
```

5. **Access the Application**
Open your browser and go to: `http://localhost:5000`

## File Structure

```
cs50 Finall Project/
├── app.py                 # Main Flask application
├── database.db           # SQLite database file
├── requirements.txt      # Python dependencies
├── static/
│   └── styles.css       # Main stylesheet
└── templates/
    ├── layout.html      # Base template with navigation
    ├── dashboard.html   # Dashboard/home page
    ├── login.html       # Login page
    ├── register.html    # Registration page
    ├── study.html       # Study planner page
    └── expenses.html    # Expense tracker page
```

## Usage Guide

### Registration & Login
1. Click "Register" to create a new account
2. Enter a username and password
3. Click "Login" to access your dashboard

### Managing Expenses
1. Go to **Expense Tracker**
2. Select a category (Food, Travel, Study, etc.)
3. Enter the amount and date
4. Optionally add a note
5. Click "Add Expense"
6. Filter by category using the category buttons
7. Click "Delete" to remove an expense

### Managing Study Tasks
1. Go to **Study Planner**
2. Enter task title and due date
3. Optionally add a description
4. Click "Add Task"
5. Click "Mark Done" to complete a task
6. Click "Delete" to remove a task

### Viewing Dashboard
- Dashboard shows real-time statistics
- Monthly expense total
- Study task progress
- Category-wise expense breakdown
- Quick summary of your activities

## Key Routes

| Route | Method | Purpose |
|-------|--------|---------|
| `/` | GET | Dashboard |
| `/register` | GET, POST | User registration |
| `/login` | GET, POST | User login |
| `/logout` | GET | User logout |
| `/study` | GET, POST | Study planner |
| `/delete_task/<id>` | GET | Delete study task |
| `/toggle_task/<id>` | GET | Mark task complete/pending |
| `/expenses` | GET, POST | Expense tracker |
| `/delete_expense/<id>` | GET | Delete expense |

## Validation & Security

- **Password Security**: Passwords hashed using Werkzeug
- **Session Management**: User authentication via Flask sessions
- **User Isolation**: SQL queries filter by user_id
- **Input Validation**: 
  - Amount must be positive number
  - Required fields validated
  - Category selection from dropdown
- **SQL Injection Prevention**: Parameterized queries with `?` placeholders

## Error Handling

The application provides user-friendly error messages:
- ✅ Success messages for completed actions
- ❌ Error messages for invalid inputs
- 💬 Validation feedback for required fields
- 🔔 Flash messages dismiss automatically

## Browser Compatibility

- Chrome/Edge (recommended)
- Firefox
- Safari
- Mobile browsers

## Future Enhancements

Potential features for future versions:
- [ ] Data export (CSV/PDF)
- [ ] Spending charts and graphs
- [ ] Monthly/yearly reports
- [ ] Budget alerts
- [ ] Recurring expenses
- [ ] Email notifications
- [ ] Dark mode
- [ ] Multi-currency support

## Troubleshooting

### Database Issues
If you encounter database errors:
1. Delete `database.db`
2. Restart the application
3. Create a new database by registering

### Port Already in Use
If port 5000 is already in use:
1. Change port in `app.py`: `app.run(debug=True, port=5001)`
2. Access application at `http://localhost:5001`

### Virtual Environment Issues
```bash
# Deactivate current environment
deactivate

# Remove .venv folder
rm -r .venv

# Recreate
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## License

This project is created as a CS50 final project.

## Support

For issues or questions, refer to the code comments or review the Flask documentation at https://flask.palletsprojects.com/

---

**Version**: 1.0  
**Last Updated**: January 23, 2026  
**Developer**: Chitvan Suri  
**CS50 Final Project**: StudySpend

---

## 🚀 Deployment

Ready to share your app online? See [DEPLOYMENT.md](DEPLOYMENT.md) for step-by-step instructions to deploy on:
- **Render** (Recommended - Free tier available)
- **PythonAnywhere** (Easy setup)
- **Local Network** (For testing with friends on same WiFi)

## 📂 GitHub Repository

This project is available on GitHub. To get the code:
```bash
git clone https://github.com/YourUsername/StudySpend.git
cd StudySpend
python -m venv .venv
.venv\Scripts\Activate.ps1  #windows
source .venv/bin/activate   # Mac/Linux
pip install -r requirements.txt
python app.py
```

## ✅ What Makes This Project Great

- **Complete Full-Stack App**: Backend (Python/Flask) + Frontend (HTML/CSS/JS)
- **Database Design**: Proper schema with user isolation and relationships
- **Security**: Password hashing, parameterized queries, session management
- **UX/UI**: Responsive design, flash messages, form validation
- **Production Ready**: Can be deployed online and shared with anyone
- **Well Documented**: README, DEPLOYMENT guide, inline code comments

# Personal Expense Tracker & Budget Manager

A Python-based CLI tool for tracking daily expenses, categorizing spending, and managing personal budget efficiently.

## Overview

This project helps users manage their personal finances by:

- Tracking daily expenses with categories
- Setting and monitoring monthly budgets
- Generating spending reports
- Alerting when budget limits are exceeded

## Features

- ✅ Add and log daily expenses
- ✅ Categorize expenses (Food, Transport, Utilities, Entertainment, Health, Other)
- ✅ Set and track monthly budget
- ✅ View all expenses or filter by category
- ✅ Real-time budget status with alerts
- ✅ Category-wise spending breakdown
- ✅ Persistent data storage (JSON)
- ✅ User-friendly CLI interface

## Technologies Used

- Python 3.8+
- JSON for data storage
- Built-in libraries: json, datetime, os, pathlib

## Project Structure

```
expense-tracker/
├── main.py              # Entry point / CLI interface
├── requirements.txt     # Dependencies (none required)
├── README.md           # Project documentation
├── .gitignore
├── src/
│   ├── __init__.py
│   ├── expense.py      # Expense class
│   ├── budget.py       # Budget class
│   └── tracker.py      # Main tracker logic
├── data/
│   └── expenses.json   # Data storage (auto-generated)
└── output/
    └── (reports)
```

## Installation

1. Clone or download the project

```bash
git clone https://github.com/nivelone/Aman_Singh_Bhati_Personal_Expence_Tracker_&_Budget_Manager.git
cd Aman_Singh_Bhati_Personal_Expence_Tracker_&_Budget_Manager
```

2. No external dependencies required (uses only built-in Python libraries)

## How to Run

1. Open terminal/command prompt
2. Navigate to the project folder
3. Run the main script:

```bash
python main.py
```

## Usage

### Main Menu Options:

1. **Add Expense** - Log a new expense with amount, category, and description
2. **View All Expenses** - Display all recorded expenses
3. **View by Category** - Filter expenses by specific category
4. **View Budget Status** - Check budget usage and remaining amount
5. **Set Monthly Budget** - Configure your monthly budget limit
6. **Exit** - Close the application

### Sample Usage

```
==================================================
   PERSONAL EXPENSE TRACKER
==================================================
1. Add Expense
2. View All Expenses
3. View by Category
4. View Budget Status
5. Set Monthly Budget
6. Exit
==================================================

Enter your choice (1-6): 1

--- Add New Expense ---
Enter amount (₹): 500

Categories:
1. Food
2. Transport
3. Utilities
4. Entertainment
5. Health
6. Other
Select category (1-6): 1
Enter description: Lunch at restaurant

✅ Expense added: 2026-02-13 | Food            | ₹  500.00 | Lunch at restaurant

✅ Budget OK: 1.0% used. ₹49500.00 remaining
```

## Expected Input and Output

### Input:

- Amount: Positive number (e.g., 500, 1250.50)
- Category: Select from 6 predefined categories
- Description: Text description of expense

### Output:

- Formatted expense list with date, category, amount, and description
- Budget status with percentage used and remaining amount
- Category-wise spending breakdown
- Alerts when approaching or exceeding budget

## Features Implemented

✅ **Add Expense** - Add expenses with validation  
✅ **View Expenses** - Display all or filter by category  
✅ **Budget Management** - Set budget and track usage  
✅ **Budget Alerts** - Warning when 80%+ used, alert when exceeded  
✅ **Category Breakdown** - See spending distribution  
✅ **Data Persistence** - All data saved to JSON file  
✅ **Error Handling** - Input validation and error messages

## Objectives

1. Create a user-friendly CLI interface for expense management
2. Track expenses across multiple categories
3. Monitor budget usage with real-time alerts
4. Generate spending insights and reports
5. Store and retrieve data persistently

## Author Information

- **Name:** Aman Singh Bhati
- **Batch:** ITC Infotech Python Developer Course
- **Date:** 15 February 2026
- **Email:** amanbhati2004@email.com
- **GitHub:** https://github.com/nivelone

## License

This project is created for educational purposes as part of the ITC Infotech Python Developer training program.


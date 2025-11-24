 # Health-manager-application
A comprehensive Python-based console application designed to help users track their health and fitness journey through efficient meal and exercise logging. This robust system combines simplicity with powerful tracking capabilities, making health management accessible to everyone.
Health Manager - Console-Based Health Tracking Application
 # Overview
Health Manager is a comprehensive Python-based console application designed to help users track their health and fitness journey. This application provides a simple yet powerful solution for monitoring daily meals, exercise routines, and overall health progress through an intuitive text-based interface. With secure local data storage and no external dependencies, it's perfect for individuals who want to maintain their health records privately and efficiently.
# Features
 # User Management
•	Secure Registration & Login - Multi-user system with individual data isolation
•	Persistent Sessions - Maintain user data across application restarts
•	Privacy Focused - Each user's data stored separately in JSON files
 # Health Tracking
•	Meal Logging - Record food consumption with calorie information
•	Exercise Monitoring - Track workouts with duration and calories burned
•	Flexible Timestamps - Automatic or custom date/time recording
•	Data Validation - Input validation for calories and numerical data
# Analytics & Reports
•	Comprehensive Summaries - View meal and exercise history with totals
•	Calorie Analysis - Net calorie calculation (intake vs burned)
•	Progress Tracking - Records sorted by date with newest first
•	Health Insights - Calorie surplus/deficit status indicators
# Data Management
•	JSON Storage - Structured data storage using human-readable JSON files
•	Data Persistence - All records maintained between sessions
•	Backup Friendly - Easy to backup and restore user data files
# Technologies Used
•	Python 3.6+ - Core programming language
•	JSON - Data serialization and storage
•	datetime - Timestamp and date handling
•	os module - File system operations
•	Standard Library Only - No external dependencies required
## Installation & Setup
# Prerequisites
•	Python 3.6 or higher installed on your system
•	Basic terminal/command prompt knowledge
Step-by-Step Installation
1.	Download the Project
# Clone the repository or download the health_manager.py file
git clone <repository-url>
cd health-manager
2.	Verify Python Installation
python --version
# Should show Python 3.6 or higher
3.	Run the Application
python health_manager.py
4.	First-Time Setup
o	The application will automatically create a users directory
o	No additional configuration required
# Project Structure
health-manager/
│
├── health_manager.py          # Main application file
├── README.md                  # Project documentation
└── users/                     # User data directory (auto-created)
    ├── username1.json        # User-specific data files
    └── username2.json
# How to Use
Getting Started
1.	Launch the Application
python health_manager.py
2.	Create an Account
o	Select "Register" from the login screen
o	Choose a unique username
o	Your data file will be created automatically
3.	Start Tracking
o	Use the main menu to log meals and exercises
o	View your records to see progress
o	Monitor your net calorie balance
Basic Workflow
Logging a Meal:
1.	Select "Log Meal" from main menu
2.	Enter food description
3.	Input calorie count
4.	Choose current or custom date/time
5.	Save automatically
Logging an Exercise:
1.	Select "Log Exercise" from main menu
2.	Enter exercise description
3.	Input duration in minutes
4.	Enter calories burned
5.	Save automatically
Viewing Records:
•	View meals, exercises, or all records
•	See totals and summaries
•	Track your calorie balance



## Testing Instructions
# Manual Testing Steps
1.	User Registration Test
- Register a new user
- Try duplicate username registration
- Test empty username handling
2.	Login Test
- Login with valid credentials
- Attempt login with non-existent user
- Verify session persistence
3.	Data Logging Test
- Log meals with various calorie values
- Log exercises with different durations
- Test custom date/time entries
- Verify input validation
4.	Data Viewing Test
- View meal records
- View exercise records
- Check summary calculations
- Verify sorting functionality
5.	Error Handling Test
- Test invalid input handling
- Verify file operation safety
- Check menu navigation errors
Test Data Examples
Sample Meal Entry:
•	Food: "Oatmeal with fruits"
•	Calories: 350
•	Date: 2024-01-15
•	Time: 08:30
Sample Exercise Entry:
•	Exercise: "Running"
•	Duration: 30 minutes
•	Calories Burned: 300
•	Date: 2024-01-15
•	Time: 07:00

## Application Screenshots
Login Screen
 
Main Menu
 
Record Summary
 
# Customization
The application can be easily extended by modifying the health_manager.py file:
•	Add new health metrics
•	Modify data storage format
•	Enhance reporting features
•	Add new analysis calculations
# Contributing
Contributions are welcome! Please feel free to submit pull requests or open issues for:
•	Bug fixes
•	New features
•	Documentation improvements
•	Testing enhancements
# Support
If you encounter any issues:
1.	Check that Python 3.6+ is installed
2.	Verify file permissions in the application directory
3.	Ensure no other processes are using the user data files
4.	Check the users directory is created and accessible
# Future Enhancements
•	Data export functionality
•	Enhanced visualization
•	Meal and exercise templates
•	Water intake tracking
•	Goal setting features
•	Mobile application version




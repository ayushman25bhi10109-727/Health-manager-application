import os
import datetime
import json

class HealthManager:
    def __init__(self):
        self.current_user = None
        self.users_dir = "users"
        self.ensure_directories()
    
    def ensure_directories(self):
        """Create necessary directories if they don't exist"""
        if not os.path.exists(self.users_dir):
            os.makedirs(self.users_dir)
    
    def clear_screen(self):
        """Clear the console screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def display_header(self):
        """Display application header"""
        self.clear_screen()
        print("=" * 50)
        print("       HEALTH MANAGER APPLICATION")
        print("=" * 50)
        if self.current_user:
            print(f"Logged in as: {self.current_user}")
        print()
    
    def user_login(self):
        """Handle user login or registration"""
        self.display_header()
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        
        choice = input("\nChoose an option (1-3): ").strip()
        
        if choice == "1":
            self.login()
        elif choice == "2":
            self.register()
        elif choice == "3":
            print("Thank you for using Health Manager!")
            exit()
        else:
            input("Invalid choice! Press Enter to continue...")
            self.user_login()
    
    def register(self):
        """Register a new user"""
        self.display_header()
        print("=== USER REGISTRATION ===")
        username = input("Enter username: ").strip().lower()
        
        if not username:
            input("Username cannot be empty! Press Enter to continue...")
            self.register()
            return
        
        user_file = os.path.join(self.users_dir, f"{username}.json")
        
        if os.path.exists(user_file):
            input("Username already exists! Press Enter to continue...")
            self.register()
            return
        
        # Create user data structure
        user_data = {
            "username": username,
            "created_at": datetime.datetime.now().isoformat(),
            "meals": [],
            "exercises": []
        }
        
        # Save user data
        with open(user_file, 'w') as f:
            json.dump(user_data, f, indent=2)
        
        print(f"\nUser '{username}' registered successfully!")
        input("Press Enter to continue to login...")
        self.login()
    
    def login(self):
        """Login existing user"""
        self.display_header()
        print("=== USER LOGIN ===")
        username = input("Enter username: ").strip().lower()
        
        user_file = os.path.join(self.users_dir, f"{username}.json")
        
        if os.path.exists(user_file):
            self.current_user = username
            print(f"\nWelcome back, {username}!")
            input("Press Enter to continue...")
            self.main_menu()
        else:
            input("User not found! Press Enter to continue...")
            self.user_login()
    
    def get_user_data(self):
        """Load current user's data"""
        if not self.current_user:
            return None
        
        user_file = os.path.join(self.users_dir, f"{self.current_user}.json")
        try:
            with open(user_file, 'r') as f:
                return json.load(f)
        except:
            return {"meals": [], "exercises": []}
    
    def save_user_data(self, user_data):
        """Save user data to file"""
        if not self.current_user:
            return
        
        user_file = os.path.join(self.users_dir, f"{self.current_user}.json")
        with open(user_file, 'w') as f:
            json.dump(user_data, f, indent=2)
    
    def log_meal(self):
        """Log a meal entry"""
        self.display_header()
        print("=== LOG MEAL ===")
        
        food = input("What did you eat? ").strip()
        if not food:
            input("Food description cannot be empty! Press Enter to continue...")
            return
        
        try:
            calories = int(input("Calories: "))
        except ValueError:
            input("Invalid calories! Please enter a number. Press Enter to continue...")
            return
        
        # Get current date and time
        now = datetime.datetime.now()
        date_str = now.strftime("%Y-%m-%d")
        time_str = now.strftime("%H:%M")
        
        # Ask if user wants to use custom date/time
        use_custom = input("Use custom date/time? (y/n): ").strip().lower()
        if use_custom == 'y':
            date_str = input("Enter date (YYYY-MM-DD): ").strip()
            time_str = input("Enter time (HH:MM): ").strip()
        
        meal_entry = {
            "food": food,
            "calories": calories,
            "date": date_str,
            "time": time_str,
            "logged_at": now.isoformat()
        }
        
        # Save to user data
        user_data = self.get_user_data()
        user_data["meals"].append(meal_entry)
        self.save_user_data(user_data)
        
        print(f"\nMeal logged successfully!")
        input("Press Enter to continue...")
    
    def log_exercise(self):
        """Log an exercise entry"""
        self.display_header()
        print("=== LOG EXERCISE ===")
        
        exercise = input("What exercise did you do? ").strip()
        if not exercise:
            input("Exercise description cannot be empty! Press Enter to continue...")
            return
        
        try:
            duration = int(input("Duration (minutes): "))
            calories_burned = int(input("Calories burned: "))
        except ValueError:
            input("Invalid input! Please enter numbers for duration and calories. Press Enter to continue...")
            return
        
        # Get current date and time
        now = datetime.datetime.now()
        date_str = now.strftime("%Y-%m-%d")
        time_str = now.strftime("%H:%M")
        
        # Ask if user wants to use custom date/time
        use_custom = input("Use custom date/time? (y/n): ").strip().lower()
        if use_custom == 'y':
            date_str = input("Enter date (YYYY-MM-DD): ").strip()
            time_str = input("Enter time (HH:MM): ").strip()
        
        exercise_entry = {
            "exercise": exercise,
            "duration": duration,
            "calories_burned": calories_burned,
            "date": date_str,
            "time": time_str,
            "logged_at": now.isoformat()
        }
        
        # Save to user data
        user_data = self.get_user_data()
        user_data["exercises"].append(exercise_entry)
        self.save_user_data(user_data)
        
        print(f"\nExercise logged successfully!")
        input("Press Enter to continue...")
    
    def view_records(self):
        """View meal and exercise records"""
        self.display_header()
        print("=== VIEW RECORDS ===")
        
        user_data = self.get_user_data()
        meals = user_data.get("meals", [])
        exercises = user_data.get("exercises", [])
        
        print("\n1. View Meals")
        print("2. View Exercises")
        print("3. View All")
        print("4. Back to Main Menu")
        
        choice = input("\nChoose an option (1-4): ").strip()
        
        if choice == "1":
            self.view_meals(meals)
        elif choice == "2":
            self.view_exercises(exercises)
        elif choice == "3":
            self.view_all_records(meals, exercises)
        elif choice == "4":
            return
        else:
            input("Invalid choice! Press Enter to continue...")
            self.view_records()
    
    def view_meals(self, meals):
        """Display meal records"""
        self.display_header()
        print("=== MEAL RECORDS ===\n")
        
        if not meals:
            print("No meal records found.")
            input("\nPress Enter to continue...")
            return
        
        # Sort meals by date and time (newest first)
        sorted_meals = sorted(meals, key=lambda x: x.get('logged_at', ''), reverse=True)
        
        total_calories = 0
        for i, meal in enumerate(sorted_meals, 1):
            print(f"{i}. {meal['date']} {meal['time']}")
            print(f"   Food: {meal['food']}")
            print(f"   Calories: {meal['calories']}")
            print("-" * 30)
            total_calories += meal['calories']
        
        print(f"\nTotal Calories from {len(meals)} meals: {total_calories}")
        input("\nPress Enter to continue...")
    
    def view_exercises(self, exercises):
        """Display exercise records"""
        self.display_header()
        print("=== EXERCISE RECORDS ===\n")
        
        if not exercises:
            print("No exercise records found.")
            input("\nPress Enter to continue...")
            return
        
        # Sort exercises by date and time (newest first)
        sorted_exercises = sorted(exercises, key=lambda x: x.get('logged_at', ''), reverse=True)
        
        total_calories_burned = 0
        total_duration = 0
        for i, exercise in enumerate(sorted_exercises, 1):
            print(f"{i}. {exercise['date']} {exercise['time']}")
            print(f"   Exercise: {exercise['exercise']}")
            print(f"   Duration: {exercise['duration']} minutes")
            print(f"   Calories Burned: {exercise['calories_burned']}")
            print("-" * 30)
            total_calories_burned += exercise['calories_burned']
            total_duration += exercise['duration']
        
        print(f"\nTotal from {len(exercises)} exercises:")
        print(f"Calories Burned: {total_calories_burned}")
        print(f"Total Duration: {total_duration} minutes")
        input("\nPress Enter to continue...")
    
    def view_all_records(self, meals, exercises):
        """Display all records with summary"""
        self.display_header()
        print("=== ALL RECORDS SUMMARY ===\n")
        
        # Calculate totals
        total_calories_consumed = sum(meal['calories'] for meal in meals)
        total_calories_burned = sum(exercise['calories_burned'] for exercise in exercises)
        net_calories = total_calories_consumed - total_calories_burned
        
        print(f"Total Meals Logged: {len(meals)}")
        print(f"Total Exercises Logged: {len(exercises)}")
        print(f"Total Calories Consumed: {total_calories_consumed}")
        print(f"Total Calories Burned: {total_calories_burned}")
        print(f"Net Calories: {net_calories}")
        
        if net_calories > 0:
            print("Status: Calorie Surplus")
        elif net_calories < 0:
            print("Status: Calorie Deficit")
        else:
            print("Status: Calorie Balance")
        
        input("\nPress Enter to continue...")
    
    def main_menu(self):
        """Display main menu and handle user choices"""
        while True:
            self.display_header()
            print("=== MAIN MENU ===")
            print("1. Log Meal")
            print("2. Log Exercise")
            print("3. View Records")
            print("4. Logout")
            print("5. Exit Application")
            
            choice = input("\nChoose an option (1-5): ").strip()
            
            if choice == "1":
                self.log_meal()
            elif choice == "2":
                self.log_exercise()
            elif choice == "3":
                self.view_records()
            elif choice == "4":
                self.current_user = None
                print("Logged out successfully!")
                input("Press Enter to continue...")
                self.user_login()
                break
            elif choice == "5":
                print("Thank you for using Health Manager!")
                exit()
            else:
                input("Invalid choice! Press Enter to continue...")
    
    def run(self):
        """Start the application"""
        self.user_login()

# Run the application
if __name__ == "__main__":
    app = HealthManager()
    app.run()
def generate_profile(age: int) -> str:
    """Returns the age category of a profile based on the integer age parameter."""
    if age in range(0, 13):
        return "Child"
    elif age in range(13, 20):
        return "Teenager"
    else:
        return "Adult"

# Get user's full name input
user_name = input("Enter your full name: ")

# Get user's birth year as string input
birth_year_str = input("Enter your birth year: ")

# Convert birth year string to integer
birth_year = int(birth_year_str)

# Calculate current age based on birth year (current year is 2025)
current_age = 2025 - birth_year

# Initialize empty list for user's hobbies
hobbies = []

# Get life stage using the generate_profile function
life_stage = generate_profile(current_age)

# Initialize empty dictionary for user's profile
user_profile = {}

# Collect hobbies until 'stop' is entered
while True:
    hobby = input("Enter a favorite hobby or type 'stop' to finish: ")
    if hobby.strip().lower() == 'stop':
        break
    hobbies.append(hobby.strip())

# Enter the collected data into user_profile dictionary
user_profile["name"] = user_name
user_profile["age"] = current_age
user_profile["stage"] = life_stage
user_profile["hobbies"] = hobbies

# Output the received data from user_profile dictionary to console using f-string
print(f"""
---
Profile summary:
Name: {user_profile.get("name")}
Age: {user_profile.get("age")}
Life Stage: {user_profile.get("stage")}
{f"Favorite Hobbies ({len(hobbies)}):\n" + "\n".join(f"- {hobby}" for hobby in hobbies) if len(hobbies) > 0 
else "You didn't mention any hobbies."}
---
""")
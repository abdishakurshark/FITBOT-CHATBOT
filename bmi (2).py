import streamlit as st
import random

# Updated and verified YouTube video database
YT_VIDEOS = {
    "weight_loss": {
        "title": "The Science of Fat Loss",
        "url": "https://www.youtube.com/watch?v=wpBSlBcxN4E",
        "channel": "Jeff Nippard",
        "verified": True
    },
    "muscle_gain": {
        "title": "Hypertrophy Made Simple",
        "url": "https://www.youtube.com/watch?v=g3H9q5Qf_4E",
        "channel": "Renaissance Periodization",
        "verified": True
    },
    "full_body": {
        "title": "Perfect Full Body Workout",
        "url": "https://www.youtube.com/watch?v=JEEG0hBNk3E",
        "channel": "Athlean-X",
        "verified": True
    },
    "leg_day": {
        "title": "Complete Leg Workout Guide",
        "url": "https://www.youtube.com/watch?v=IZxyjW7MPJQ",
        "channel": "Jeremy Ethier",
        "verified": True
    },
    "push_day": {
        "title": "Push Day Routine (Chest/Shoulders/Triceps)",
        "url": "https://www.youtube.com/watch?v=1f8yoFFdkcY",
        "channel": "Scott Herman Fitness",
        "verified": True
    },
    "pull_day": {
        "title": "Ultimate Pull Day (Back/Biceps)",
        "url": "https://www.youtube.com/watch?v=6kALZikXxLc",
        "channel": "Jeff Nippard",
        "verified": True
    },
    "hiit": {
        "title": "20 Minute HIIT Workout",
        "url": "https://www.youtube.com/watch?v=ml6cT4AZdqI",
        "channel": "Fitness Blender",
        "verified": True
    },
    "form_guide": {
        "title": "Perfect Exercise Form Guide",
        "url": "https://www.youtube.com/watch?v=2SO5I0KqyiE",
        "channel": "Scott Herman Fitness",
        "verified": True
    }
}

# Enhanced workout database with different routines for each day
WORKOUT_PLANS = {
    "beginner": {
        "full_body": {
            "exercises": [
                "Bodyweight Squats: 3x10-12",
                "Push-ups (knees if needed): 3x8-10",
                "Bent-over Rows: 3x8-10",
                "Plank: 3x30 sec"
            ],
            "video": YT_VIDEOS["full_body"]
        }
    },
    "intermediate": {
        "push_day": {
            "exercises": [
                "Bench Press: 4x8",
                "Overhead Press: 3x8-10",
                "Incline Dumbbell Press: 3x10-12",
                "Triceps Dips: 3xAMRAP"
            ],
            "video": YT_VIDEOS["push_day"]
        },
        "pull_day": {
            "exercises": [
                "Pull-ups: 4x6-8",
                "Barbell Rows: 3x8-10",
                "Face Pulls: 3x12-15",
                "Hammer Curls: 3x10-12"
            ],
            "video": YT_VIDEOS["pull_day"]
        },
        "leg_day": {
            "exercises": [
                "Back Squats: 4x6-8",
                "Romanian Deadlifts: 3x8-10",
                "Bulgarian Split Squats: 3x8/side",
                "Calf Raises: 3x12-15"
            ],
            "video": YT_VIDEOS["leg_day"]
        }
    },
    "advanced": {
        "push_day": {
            "exercises": [
                "Weighted Dips: 4x6-8",
                "Military Press: 4x6",
                "Incline Flyes: 3x10-12",
                "Skull Crushers: 3x8-10"
            ],
            "video": YT_VIDEOS["push_day"]
        },
        "pull_day": {
            "exercises": [
                "Weighted Pull-ups: 5x5",
                "Pendlay Rows: 4x6",
                "Rear Delt Flyes: 4x12-15",
                "Preacher Curls: 3x8-10"
            ],
            "video": YT_VIDEOS["pull_day"]
        },
        "leg_day": {
            "exercises": [
                "Front Squats: 5x5",
                "Sumo Deadlifts: 4x6",
                "Leg Press: 3x8-10 (drop set last set)",
                "Walking Lunges: 3x12/side"
            ],
            "video": YT_VIDEOS["leg_day"]
        }
    },
    "weight_loss": {
        "hiit": {
            "exercises": [
                "Jump Squats: 40s on/20s off",
                "Burpees: 40s on/20s off",
                "Mountain Climbers: 40s on/20s off",
                "Kettlebell Swings: 40s on/20s off"
            ],
            "video": YT_VIDEOS["hiit"]
        },
        "circuit": {
            "exercises": [
                "Push-ups: 15 reps",
                "Bodyweight Squats: 20 reps",
                "Plank Rows: 12/side",
                "Jumping Jacks: 30 reps"
            ],
            "video": YT_VIDEOS["full_body"]
        }
    }
}

# Enhanced knowledge base with more detailed answers
KNOWLEDGE_BASE = {
    "exercises": {
        "squat": {
            "description": "Fundamental lower body exercise targeting quads, hamstrings, and glutes.",
            "form_tips": "Keep chest up, knees tracking over toes, descend until thighs are parallel to floor.",
            "video": YT_VIDEOS["form_guide"]
        },
        "deadlift": {
            "description": "Full-body lift focusing on posterior chain (hamstrings, glutes, back).",
            "form_tips": "Maintain neutral spine, push through heels, keep bar close to body.",
            "video": YT_VIDEOS["form_guide"]
        }
    },
    "nutrition": {
        "protein": "Aim for 1.6-2.2g per kg of body weight for muscle growth. Good sources: chicken, fish, eggs, tofu.",
        "carbs": "Primary energy source. Complex carbs like oats, rice, and sweet potatoes are ideal.",
        "fats": "Essential for hormone production. Focus on avocados, nuts, olive oil."
    }
}

# Initialize session state for chat history
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Add a title
st.title("FITBOT 💪 - Smart Fitness Assistant")

# User information
with st.expander("📝 Enter Your Details", expanded=True):
    col1, col2 = st.columns(2)
    with col1:
        weight = st.number_input("Weight (kg):", min_value=30.0, max_value=200.0, value=70.0)
        height = st.number_input("Height (cm):", min_value=100.0, max_value=250.0, value=170.0)
    with col2:
        goal = st.selectbox("Primary Goal:", ["Weight loss", "Muscle gain", "Maintenance"])
        fitness_level = st.selectbox("Fitness Level:", ["Beginner", "Intermediate", "Advanced"])
    workout_days = st.slider("Workout Days/Week:", 1, 7, 4)

# Workout generator with varied routines
def generate_workout_plan():
    plan = []
    if goal == "Weight loss":
        if workout_days <= 3:
            plan.append(("Full Body HIIT", WORKOUT_PLANS["weight_loss"]["hiit"]))
        else:
            plan.append(("Upper Body Circuit", WORKOUT_PLANS["weight_loss"]["circuit"]))
            plan.append(("Lower Body HIIT", WORKOUT_PLANS["weight_loss"]["hiit"]))
            plan.append(("Core & Cardio", {
                "exercises": [
                    "Plank Variations: 3x30s",
                    "Russian Twists: 3x20",
                    "Bicycle Crunches: 3x15/side",
                    "Jump Rope: 5x1min"
                ],
                "video": YT_VIDEOS["hiit"]
            }))
    else:
        if fitness_level == "Beginner":
            for i in range(workout_days):
                plan.append((f"Full Body Day {i+1}", WORKOUT_PLANS["beginner"]["full_body"]))
        else:
            splits = ["Push", "Pull", "Legs"] if workout_days >= 3 else ["Upper", "Lower"]
            for i in range(workout_days):
                day_type = splits[i % len(splits)]
                plan.append((f"{day_type} Day", WORKOUT_PLANS[fitness_level.lower()][f"{day_type.lower()}_day"]))
    return plan

# BMI Calculation
if st.button("Generate My Fitness Plan"):
    bmi = weight / ((height / 100) ** 2)
    st.subheader(f"Your BMI: {bmi:.2f}")
    
    if bmi < 18.5:
        st.warning("Underweight - Focus on muscle building with calorie surplus")
    elif 18.5 <= bmi < 24.9:
        st.success("Healthy weight - Optimize your physique!")
    else:
        st.warning("Overweight - Focus on fat loss with calorie deficit")
    
    st.markdown("---")
    
    # Workout Plan
    st.subheader(f"📅 {workout_days}-Day Workout Plan")
    workout_plan = generate_workout_plan()
    
    for day, workout in workout_plan:
        with st.expander(day):
            for exercise in workout["exercises"]:
                st.write(f"- {exercise}")
            st.video(workout["video"]["url"])
            st.caption(f"Video guide: {workout['video']['title']}")

# Enhanced Chatbot with better question understanding
def get_bot_response(question):
    question = question.lower()
    
    # Exercise-specific questions
    for exercise in KNOWLEDGE_BASE["exercises"]:
        if exercise in question:
            response = f"{KNOWLEDGE_BASE['exercises'][exercise]['description']}\n\n"
            response += f"Form tips: {KNOWLEDGE_BASE['exercises'][exercise]['form_tips']}"
            return response, KNOWLEDGE_BASE['exercises'][exercise]['video']
    
    # Nutrition questions
    if any(word in question for word in ["protein", "carbs", "fat", "nutrition"]):
        nutrient = "protein" if "protein" in question else "carbs" if "carbs" in question else "fats"
        return KNOWLEDGE_BASE["nutrition"][nutrient], None
    
    # Video requests
    if any(word in question for word in ["video", "youtube", "watch"]):
        if "leg" in question:
            return "Here's a great leg workout tutorial:", YT_VIDEOS["leg_day"]
        elif "push" in question or "chest" in question:
            return "Push day workout guide:", YT_VIDEOS["push_day"]
        elif "pull" in question or "back" in question:
            return "Pull day workout guide:", YT_VIDEOS["pull_day"]
        elif "form" in question or "technique" in question:
            return "Proper form demonstration:", YT_VIDEOS["form_guide"]
    
    # General responses
    if "hello" in question or "hi" in question:
        return "Hello! How can I help with your fitness goals today?", None
    elif "thank" in question:
        return "You're welcome! Let me know if you need anything else.", None
    
    return "I can help with workout plans, exercise form, and nutrition advice. Try asking more specifically!", None

# Chatbot interface
st.markdown("---")
st.subheader("💬 Chat with FitBot")

user_input = st.text_input("Ask any fitness question:")
if user_input:
    response, video = get_bot_response(user_input)
    st.session_state.chat_history.append(f"You: {user_input}")
    st.session_state.chat_history.append(f"FitBot: {response}")
    
    if video:
        st.video(video["url"])
        st.caption(f"Video: {video['title']} by {video['channel']}")

for message in st.session_state.chat_history[-6:]:
    st.write(message)

# Resources section
st.markdown("---")
st.subheader("📚 Fitness Resources")

with st.expander("🎬 Recommended Videos"):
    cols = st.columns(3)
    videos_to_show = random.sample(list(YT_VIDEOS.values()), 3)
    for i, video in enumerate(videos_to_show):
        cols[i].video(video["url"])
        cols[i].caption(video["title"])
        

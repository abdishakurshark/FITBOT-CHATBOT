import streamlit as st
import random

# YouTube video database
YT_VIDEOS = {
    "weight_loss": {
        "title": "The Science of Weight Loss Explained",
        "url": "https://www.youtube.com/watch?v=wpBSlBcxN4E",
        "channel": "Jeff Nippard"
    },
    "muscle_gain": {
        "title": "Complete Muscle Growth Guide",
        "url": "https://www.youtube.com/watch?v=XL8WHAi6l7U",
        "channel": "Renaissance Periodization"
    },
    "beginner_workout": {
        "title": "Beginner Full Body Routine",
        "url": "https://www.youtube.com/watch?v=vC8LbvYk6es",
        "channel": "Athlean-X"
    },
    "nutrition_basics": {
        "title": "Nutrition Made Simple",
        "url": "https://www.youtube.com/watch?v=1T7K2e8VX5I",
        "channel": "Jeremy Ethier"
    },
    "gym_etiquette": {
        "title": "Gym Do's and Don'ts",
        "url": "https://www.youtube.com/watch?v=JkOXgX5qQh8",
        "channel": "Buff Dudes"
    },
    "proper_form": {
        "title": "Perfect Exercise Form Guide",
        "url": "https://www.youtube.com/watch?v=2SO5I0KqyiE",
        "channel": "Scott Herman Fitness"
    },
    "home_workout": {
        "title": "No Equipment Home Workout",
        "url": "https://www.youtube.com/watch?v=ml6cT4AZdqI",
        "channel": "Fitness Blender"
    },
    "hiit": {
        "title": "20 Minute Fat Burning HIIT",
        "url": "https://www.youtube.com/watch?v=6W7C3VZQ9y8",
        "channel": "Heather Robertson"
    }
}

# Enhanced knowledge base
KNOWLEDGE_BASE = {
    "workout": {
        "beginner": [
            "Full-body routine 3x/week: Squats, push-ups, rows, planks (3 sets of 8-12 reps)",
            "Start with bodyweight exercises before adding weights",
            "Allow at least 1 rest day between sessions for recovery"
        ],
        "intermediate": [
            "Split routine (upper/lower or push/pull/legs) 4-5x/week",
            "Incorporate progressive overload - increase weight gradually",
            "Try supersets to save time and increase intensity"
        ],
        "advanced": [
            "Specialized splits (e.g., arms day, back day) 5-6x/week",
            "Incorporate advanced techniques like drop sets and pyramids",
            "Periodize your training with different intensity phases"
        ],
        "weight_loss": [
            "Circuit training: Alternate between strength and cardio stations",
            "Metabolic conditioning 2-3x/week (e.g., EMOM, AMRAP)",
            "Keep rest periods short (30-60 seconds between sets)"
        ],
        "muscle_gain": [
            "Focus on compound lifts: Squat, bench, deadlift, overhead press",
            "Train each muscle group 2-3x/week with varying volume",
            "Use 70-85% of your 1RM for optimal hypertrophy"
        ]
    },
    "nutrition": {
        "weight_loss": [
            "Protein: 1.6-2.2g/kg | Carbs: 2-3g/kg | Fat: 0.5-1g/kg",
            "Fill half your plate with vegetables at each meal",
            "Sample meal: Grilled chicken (150g), quinoa (1/2 cup), mixed veggies (2 cups)"
        ],
        "muscle_gain": [
            "Protein: 2.2-2.5g/kg | Carbs: 4-6g/kg | Fat: 0.5-1g/kg",
            "Pre-workout: Carbs + protein | Post-workout: Protein + fast carbs",
            "Sample meal: Salmon (200g), sweet potato (1 medium), broccoli (1 cup)"
        ],
        "general": [
            "Hydration: 35ml/kg body weight (more if sweating)",
            "Micronutrients: Focus on iron, calcium, vitamin D",
            "Meal timing: Eat every 3-4 hours for stable energy"
        ]
    },
    "gym": {
        "equipment": [
            "Treadmill: Start walking, gradually increase incline/speed",
            "Cable machines: Great for controlled movements",
            "Free weights: Better for functional strength than machines"
        ],
        "etiquette": [
            "Re-rack weights and wipe down equipment",
            "Don't hog multiple stations during peak hours",
            "Ask before working in with someone"
        ],
        "safety": [
            "Use spotters for heavy lifts",
            "Learn proper form before adding weight",
            "Listen to your body - pain means stop"
        ]
    }
}

# Add a title
st.title("FITBOT 💪 - Your Ultimate Fitness Assistant")

# User information
with st.expander("📝 Enter Your Details"):
    col1, col2 = st.columns(2)
    with col1:
        weight = st.number_input("Enter your weight (kg):", min_value=30.0, max_value=200.0, value=70.0)
        height = st.number_input("Enter your height (cm):", min_value=100.0, max_value=250.0, value=170.0)
        age = st.number_input("Enter your age:", min_value=12, max_value=100, value=25)
    with col2:
        gender = st.selectbox("Gender:", ["Male", "Female", "Other"])
        goal = st.selectbox("What's your primary goal?", ["Weight loss", "Muscle gain", "Maintenance", "Endurance", "Body recomposition"])
        fitness_level = st.selectbox("Your fitness level:", ["Beginner", "Intermediate", "Advanced"])
    workout_days = st.slider("Days you can workout per week:", 1, 7, 3)

# BMI Calculation
if st.button("Get My Personalized Fitness Plan"):
    bmi = weight / ((height / 100) ** 2)
    st.subheader(f"Your BMI: {bmi:.2f}")
    
    # Enhanced BMI Analysis
    if bmi < 18.5:
        st.warning("You're underweight. Focus on muscle building with calorie surplus.")
    elif 18.5 <= bmi < 24.9:
        st.success("You're at a healthy weight. Let's optimize your physique!")
    else:
        st.warning("You're overweight. Focus on fat loss with calorie deficit.")
    
    st.markdown("---")
    
    # Enhanced Workout Recommendations
    st.subheader("🏋️‍♂️ Personalized Workout Plan")
    st.write(f"**Recommended {workout_days}-day routine for {fitness_level.lower()} {goal.lower()}:**")
    
    # Generate workout days
    for day in range(1, workout_days + 1):
        with st.expander(f"Day {day}"):
            if goal == "Weight loss":
                st.write("- Warmup: 10 min dynamic stretching")
                st.write("- Circuit: 4 rounds (45s work/15s rest)")
                st.write("  • Kettlebell swings\n  • Burpees\n  • Jump squats\n  • Mountain climbers")
                st.write("- Finish: 20 min steady-state cardio")
                st.video(YT_VIDEOS["hiit"]["url"])
                st.caption(f"Need HIIT ideas? Watch: {YT_VIDEOS['hiit']['title']}")
            elif goal == "Muscle gain":
                st.write(f"- {random.choice(['Upper', 'Lower', 'Push', 'Pull'])} Focus Day")
                st.write("- Main lift: 5x5 heavy compound")
                st.write("- Accessories: 3x8-12")
                st.write("- Example exercises:")
                st.write("  • Bench press\n  • Rows\n  • Shoulder press\n  • Triceps dips")
                st.video(YT_VIDEOS["proper_form"]["url"])
                st.caption(f"Form tips: {YT_VIDEOS['proper_form']['title']}")
            else:  # Maintenance
                st.write("- Full body workout")
                st.write("- 3-4 sets per exercise")
                st.write("- Example exercises:")
                st.write("  • Squats\n  • Push-ups\n  • Rows\n  • Plank variations")
                st.video(YT_VIDEOS["beginner_workout"]["url"])
                st.caption(f"Demo: {YT_VIDEOS['beginner_workout']['title']}")
    
    # Enhanced Dietary Plan
    st.subheader("🍏 Custom Nutrition Plan")
    col1, col2 = st.columns(2)
    with col1:
        st.write("**Macronutrients:**")
        if goal == "Weight loss":
            st.write(KNOWLEDGE_BASE["nutrition"]["weight_loss"][0])
        elif goal == "Muscle gain":
            st.write(KNOWLEDGE_BASE["nutrition"]["muscle_gain"][0])
        else:
            st.write("Protein: 1.2-1.6g/kg | Carbs: 3-4g/kg | Fat: 0.8-1.2g/kg")
        
        st.write("**Meal Timing:**")
        st.write("- Pre-workout: Carbs + protein")
        st.write("- Post-workout: Protein + carbs")
        st.write("- Space meals 3-4 hours apart")
    
    with col2:
        st.write("**Sample Meal Plan:**")
        st.write("- Breakfast: Oatmeal + eggs + berries")
        st.write("- Lunch: Grilled chicken + rice + veggies")
        st.write("- Dinner: Fish + quinoa + salad")
        st.write("- Snacks: Greek yogurt, nuts, protein shake")
    
    st.video(YT_VIDEOS["nutrition_basics"]["url"])
    st.caption(f"Nutrition guide: {YT_VIDEOS['nutrition_basics']['title']}")

    # Enhanced Gym Tips Section
    st.subheader("🏢 Expert Gym Guidance")
    tab1, tab2, tab3 = st.tabs(["Equipment", "Etiquette", "Safety"])
    with tab1:
        for tip in KNOWLEDGE_BASE["gym"]["equipment"]:
            st.write(f"- {tip}")
        st.video(YT_VIDEOS["gym_etiquette"]["url"])
        st.caption(f"Gym tips: {YT_VIDEOS['gym_etiquette']['title']}")
    with tab2:
        for tip in KNOWLEDGE_BASE["gym"]["etiquette"]:
            st.write(f"- {tip}")
    with tab3:
        for tip in KNOWLEDGE_BASE["gym"]["safety"]:
            st.write(f"- {tip}")

# Enhanced Chatbot feature
st.markdown("---")
st.subheader("🤖 Ask FitBot Anything")

chat_history = []
user_question = st.text_input("Type your fitness question here:")

if user_question:
    user_question = user_question.lower()
    response = ""
    video_rec = None
    
    # Enhanced question detection with video recommendations
    if any(word in user_question for word in ["video", "youtube", "watch", "explain", "demonstrate"]):
        if "weight loss" in user_question or "fat loss" in user_question:
            response = "Here's an excellent video explaining weight loss science:"
            video_rec = YT_VIDEOS["weight_loss"]
        elif "muscle gain" in user_question or "bulking" in user_question:
            response = "This video covers muscle building perfectly:"
            video_rec = YT_VIDEOS["muscle_gain"]
        elif "beginner" in user_question and "workout" in user_question:
            response = "Perfect beginner workout tutorial:"
            video_rec = YT_VIDEOS["beginner_workout"]
        elif "nutrition" in user_question or "diet" in user_question:
            response = "Nutrition basics explained clearly:"
            video_rec = YT_VIDEOS["nutrition_basics"]
        elif "etiquette" in user_question or "gym rules" in user_question:
            response = "Gym etiquette guide:"
            video_rec = YT_VIDEOS["gym_etiquette"]
        elif "form" in user_question or "technique" in user_question:
            response = "Proper exercise form demonstration:"
            video_rec = YT_VIDEOS["proper_form"]
        elif "home workout" in user_question or "no equipment" in user_question:
            response = "Effective home workout routine:"
            video_rec = YT_VIDEOS["home_workout"]
        elif "hiit" in user_question or "interval" in user_question:
            response = "Great HIIT workout session:"
            video_rec = YT_VIDEOS["hiit"]
        else:
            response = "I recommend these fitness channels:\n- Jeff Nippard (science-based)\n- Athlean-X (injury prevention)\n- Renaissance Periodization (nutrition)"
    
    # Workout questions
    elif any(word in user_question for word in ["routine", "program", "train", "exercise", "workout"]):
        if "beginner" in user_question:
            response = random.choice(KNOWLEDGE_BASE["workout"]["beginner"])
        elif "intermediate" in user_question:
            response = random.choice(KNOWLEDGE_BASE["workout"]["intermediate"])
        elif "advanced" in user_question:
            response = random.choice(KNOWLEDGE_BASE["workout"]["advanced"])
        else:
            response = f"FitBot: For {goal.lower()}, I recommend {random.choice(KNOWLEDGE_BASE['workout'][goal.lower().replace(' ', '_')])}"
    
    # Diet questions
    elif any(word in user_question for word in ["diet", "food", "eat", "nutrition", "meal"]):
        if "weight loss" in user_question:
            response = "Weight loss nutrition: " + " | ".join(KNOWLEDGE_BASE["nutrition"]["weight_loss"])
        elif "muscle" in user_question:
            response = "Muscle gain nutrition: " + " | ".join(KNOWLEDGE_BASE["nutrition"]["muscle_gain"])
        else:
            response = "General nutrition: " + random.choice(KNOWLEDGE_BASE["nutrition"]["general"])
    
    # Gym questions
    elif any(word in user_question for word in ["gym", "equipment", "etiquette", "machine", "safety"]):
        if "equip" in user_question:
            response = "Equipment tips:\n- " + "\n- ".join(KNOWLEDGE_BASE["gym"]["equipment"])
        elif "etiquette" in user_question:
            response = "Gym etiquette:\n- " + "\n- ".join(KNOWLEDGE_BASE["gym"]["etiquette"])
        elif "safe" in user_question:
            response = "Safety tips:\n- " + "\n- ".join(KNOWLEDGE_BASE["gym"]["safety"])
        else:
            response = "Gym advice: " + random.choice(KNOWLEDGE_BASE["gym"]["equipment"] + KNOWLEDGE_BASE["gym"]["etiquette"] + KNOWLEDGE_BASE["gym"]["safety"])
    
    # Supplement questions
    elif any(word in user_question for word in ["supplement", "protein", "creatine"]):
        response = """
        Supplement guide:
        - Protein powder: 20-40g post-workout
        - Creatine: 5g daily for strength
        - Multivitamin: For micronutrient support
        - Caffeine: Pre-workout for energy
        """
    
    # Recovery questions
    elif any(word in user_question for word in ["recover", "rest", "sleep"]):
        response = """
        Recovery tips:
        - Aim for 7-9 hours sleep
        - Active recovery days (walking, yoga)
        - Foam roll sore muscles
        - Stay hydrated (2-3L water/day)
        """
    
    else:
        response = """
        FitBot: I can help with:
        - Workout plans and exercises
        - Nutrition and meal planning
        - Gym equipment and etiquette
        - Supplement guidance
        - Recovery strategies
        Try asking more specifically!
        """
    
    # Display response
    chat_history.append(f"You: {user_question}")
    chat_history.append(f"FitBot: {response}")
    
    if video_rec:
        st.video(video_rec["url"])
        st.caption(f"🎥 {video_rec['title']} by {video_rec['channel']}")
    
    for message in chat_history[-6:]:  # Show last 3 exchanges
        st.write(message)

# Additional features
st.markdown("---")
st.subheader("📚 Fitness Resources")

with st.expander("🎬 Recommended YouTube Channels"):
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write("**Science-Based:**")
        st.write("- [Jeff Nippard](https://www.youtube.com/@JeffNippard)")
        st.write("- [Jeremy Ethier](https://www.youtube.com/@JeremyEthier)")
    with col2:
        st.write("**Workouts:**")
        st.write("- [Athlean-X](https://www.youtube.com/@AthleanX)")
        st.write("- [Scott Herman](https://www.youtube.com/@ScottHermanFitness)")
    with col3:
        st.write("**Nutrition:**")
        st.write("- [Renaissance Periodization](https://www.youtube.com/@RenaissancePeriodization)")
        st.write("- [Greg Doucette](https://www.youtube.com/@GregDoucette)")

with st.expander("📱 Fitness Apps"):
    st.write("- MyFitnessPal (nutrition tracking)")
    st.write("- Strong (workout tracking)")
    st.write("- Nike Training Club (guided workouts)")

with st.expander("📖 Recommended Books"):
    st.write("- 'Bigger Leaner Stronger' by Michael Matthews")
    st.write("- 'The Renaissance Diet' by Dr. Mike Israetel")
    st.write("- 'Becoming a Supple Leopard' by Kelly Starrett")

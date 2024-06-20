from datetime import datetime
from crewai import Task

class TreatmentPlanTasks:
    def __init__(self, age, gender, weight, mental_illness, note):
        self.age = age 
        self.gender = gender 
        self.weight = weight
        self.mental_illness = mental_illness
        self.note = note

    def fitness_task(self, agent):
        return Task(
            description=f"Provide a comprehensive and practical fitness plan for a {self.age}-year-old {self.gender} weighing {self.weight} kg.",
            agent=agent,
            async_execution=True,
            expected_output=f"""
                            Provide a detailed, comprehensive, and practical fitness plan tailored to the specified {self.age}-year-old {self.gender} weighing {self.weight} kg, including:

                            1. Aerobic Exercise:
                            - Specific types of aerobic exercises recommended (e.g., running, cycling, swimming)
                            - Duration and frequency (e.g., 30 minutes, 3-4 times per week)
                            - Intensity levels (e.g., moderate, vigorous)
                            - Modifications or precautions based on {self.age}, {self.gender}, and{self.weight} kg

                            2. Strength Training:
                            - Specific types of strength training exercises (e.g., weightlifting, bodyweight exercises, resistance bands)
                            - Muscle groups to target (e.g., upper body, lower body, core)
                            - Duration and frequency (e.g., 30-60 minutes, 2-3 times per week)
                            - Modifications or precautions based on {self.age}, {self.gender}, and {self.weight} kg

                            3. Flexibility and Balance:
                            - Specific types of exercises (e.g., yoga, Pilates, stretching routines)
                            - Duration and frequency (e.g., 15-30 minutes, 2-3 times per week)
                            - Modifications or precautions based on {self.age}, {self.gender}, and {self.weight} kg

                            4. Additional Recommendations:
                            - Warm-up and cool-down routines
                            - Injury prevention strategies
                            - Hydration and nutrition guidance
                            - Any other relevant advice for safe and effective fitness

                            Provide detailed instructions, repetitions, sets, and any necessary modifications or precautions based on the individual's {self.age}-year-old {self.gender} weighing {self.weight} kg.
                            """,
        )

    def nutrition_task(self, agent):
        return Task(
            description=f"Provide comprehensive and practical nutritional recommendations for a {self.age}-year-old {self.gender} weighing {self.weight} kg ",
            agent=agent,
            async_execution=True,
            expected_output=f"""
                            Provide a detailed, comprehensive, and practical nutritional plan tailored to the specified {self.age}-year-old {self.gender} weighing {self.weight} kg, including:

                            1. Macronutrients:
                            - Recommended daily intake of proteins, carbohydrates, and healthy fats
                            - Specific food sources for each macronutrient
                            - Considerations for {self.age}, {self.gender}, {self.weight} kg

                            2. Micronutrients:
                            - Essential vitamins and minerals (e.g., B-vitamins, omega-3s, magnesium)
                            - Food sources or supplement recommendations
                            - Importance for mental health and overall well-being

                            3. Dietary Patterns:
                            - Recommended dietary patterns or plans (e.g., Mediterranean diet, anti-inflammatory diet)
                            - Specific food recommendations and meal plans
                            - Considerations for {self.age}, {self.gender}, {self.weight} kg

                            4. Hydration:
                            - Recommended daily fluid intake
                            - Importance of hydration for mental and physical health

                            5. Additional Recommendations:
                            - Strategies for managing cravings or emotional eating
                            - Tips for meal planning and preparation
                            - Any other relevant advice for a nutritious and balanced diet

                            Provide practical tips, recipes, and guidance for implementing the nutritional recommendations in daily life, considering any dietary restrictions or preferences based on the individual's {self.age}-year-old {self.gender} weighing {self.weight} kg.
                            """,
        )

    def health_task(self, agent):
        return Task(
            description=f"Provide comprehensive and practical overall health recommendations for a {self.age}-year-old {self.gender} with {self.mental_illness}.",
            agent=agent,
            async_execution=True,
            expected_output=f"""
                            Provide a detailed, comprehensive, and practical overall health plan tailored to the specified {self.age}-year-old {self.gender} with {self.mental_illness}, including:

                            1. Sleep and Rest:
                            - Recommended sleep duration and sleep hygiene practices
                            - Strategies for improving sleep quality
                            - Considerations for {self.age}, {self.gender}, and mental health condition

                            2. Stress Management:
                            - Mindfulness and relaxation techniques (e.g., meditation, deep breathing)
                            - Coping strategies for managing stress and anxiety
                            - Considerations for {self.age}, {self.gender}, and mental health condition

                            3. Physical Activity:
                            - Recommended types and duration of physical activity
                            - Benefits of exercise for mental and physical health
                            - Considerations for {self.age}, {self.gender}, and mental health condition

                            4. Social Support:
                            - Importance of social connections and a supportive network
                            - Strategies for building and maintaining healthy relationships
                            - Considerations for {self.age}, {self.gender}, and mental health condition

                            5. Preventive Care:
                            - Recommended health screenings and check-ups
                            - Strategies for maintaining a healthy lifestyle
                            - Considerations for {self.age}, {self.gender}, and mental health condition

                            Provide practical tips, resources, and guidance for implementing the health recommendations in daily life, considering the potential impact on mental health symptoms and overall well-being.
                            """,
        )

    def psychotherapy_task(self, agent):
        return Task(
            description=f"Provide comprehensive and practical psychotherapy recommendations for a {self.age}-year-old {self.gender} with {self.mental_illness} - {self.note}.",
            agent=agent,
            async_execution=True,
            expected_output=f"""
                            Provide a detailed, comprehensive, and practical psychotherapy plan tailored to the specified {self.age}-year-old {self.gender} with {self.mental_illness} - {self.note}, including:

                            1. Therapeutic Approaches:
                            - Recommended evidence-based therapies (e.g., cognitive-behavioral therapy, dialectical behavior therapy)
                            - Brief descriptions of each approach and its benefits
                            - Considerations for {self.age}, {self.gender}, and specific mental health condition

                            2. Coping Strategies:
                            - Strategies for managing symptoms and improving emotional regulation
                            - Mindfulness and relaxation techniques
                            - Cognitive restructuring and behavioral activation strategies

                            3. Psychoeducation:
                            - Information and resources for understanding the mental health condition
                            - Strategies for reducing stigma and promoting self-acceptance


                            4. Additional Recommendations:
                            - Strategies for building a strong support network
                            - Self-care practices for overall well-being
                            - Any other relevant advice for a comprehensive treatment plan

                            Provide practical tips, exercises, and guidance for implementing the psychotherapy recommendations in daily life.
                            """,
        )
    def resources_task(self, agent):
        return Task(
        description=f"Recommend comprehensive and practical resources (videos, articles, podcasts) for a {self.age}-year-old {self.gender} with {self.mental_illness} - {self.note}.",
        agent=agent,
        async_execution=True,
        expected_output=f"""
                            Provide a list of comprehensive and practical resources (videos, articles, podcasts) tailored to the specified {self.age}-year-old {self.gender} with {self.mental_illness} - {self.note}, including:

                            Videos:
                            - Title, creator/channel, and platform (e.g., YouTube, Vimeo), URL
                            - Brief description of the content and its relevance

                            Articles:
                            - Title, author/publication, and URL
                            - Brief description of the content and its relevance

                            Podcasts:
                            - Title, host/network, and platform (e.g., Apple Podcasts, Spotify)
                            - Brief description of the content and its relevance
                            
                            Don't provide apps

                            Ensure that the recommended resources are reputable, evidence-based, and appropriate for the specified {self.age}-year-old {self.gender} with {self.mental_illness} - {self.note}. Provide a diverse range of resources covering various aspects of mental health, such as education, coping strategies, personal stories, and professional insights.

                            Additionally, include any relevant guidance or disclaimers for using these resources, such as consulting with a mental health professional or considering individual circumstances and preferences.
                            """,
        )

    def compile_treatment_plan_task(self, agent, context):
        return Task(
            description=f"Compile the comprehensive and practical treatment plan for {self.age}, {self.gender}, {self.weight}, {self.mental_illness}, {self.note}",
            agent=agent,
            context=context,
            expected_output=f"""
                        Provide a detailed, comprehensive, and practical treatment plan tailored to {self.age}, {self.gender}, {self.weight}, {self.mental_illness}, {self.note}, including:

                        1. Fitness Plan
                        2. Nutritional Recommendations
                        3. Health Recommendations
                        4. Psychotherapy Recommendations
                        5. Recommended Resources
                        """,
                            )
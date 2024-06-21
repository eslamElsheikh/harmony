# harmony
# Mental Health Treatment Plan Generator

## Overview
This project is a comprehensive Mental Health Treatment Plan Generator that creates personalized plans for individuals based on their age, gender, weight, mental illness, and additional notes. It utilizes a crew of AI agents to generate tailored recommendations across various aspects of health and wellness.

## Features
- Personalized treatment plans
- Recommendations from multiple expert perspectives:
  - Fitness
  - Nutrition
  - General Health
  - Psychotherapy
  - Resource Curation

## Technology Stack
- Python
- Flask (API)
- CrewAI
- LangChain
- Google Generative AI (Gemini Pro)
- Gradio (UI)

## Setup
1. Clone the repository
2. Install dependencies:
pip install -r requirements.txt
Copy3. Set up environment variables:
- Create a `.env` file
- Add your Google API key: `GEMINI_API_KEY=your_api_key_here`

## Usage
### API
Run the Flask server:
python api.py
CopySend a POST request to `/generate_treatment_plan` with JSON payload:
```json
{
  "age": 30,
  "gender": "female",
  "weight": 70,
  "mental_illness": "depression",
  "note": "Experiences frequent mood swings"
}
UI
Run the Gradio interface:
Copypython main.py
Access the UI through the provided local URL.
Project Structure

agents.py: Defines AI agents (TreatmentPlanSupervisor, FitnessExpert, Nutritionist, etc.)
api.py: Flask API for generating treatment plans
create_treatment_plan.py: Core logic for creating treatment plans
main.py: Gradio UI implementation
tasks.py: Defines tasks for each aspect of the treatment plan

Contributing
Contributions are welcome. Please fork the repository and submit pull requests for any enhancements.
License
[Insert chosen license here]
Disclaimer
This tool is for informational purposes only and should not replace professional medical advice. Always consult with a qualified healthcare provider for personalized medical guidance.

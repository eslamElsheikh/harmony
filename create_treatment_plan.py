from crewai import Crew, Process
from agents import TreatmentPlanAgents
from tasks import TreatmentPlanTasks
from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.globals import set_debug, get_debug

def create_treatment_plan(age, gender, weight, mental_illness, note):
    load_dotenv()

    llm = ChatGoogleGenerativeAI(model="gemini-pro",
                                 verbose=True,
                                 temperature=0.1,
                                 google_api_key=os.environ["GEMINI_API_KEY"],
                                 timeout=300)

    agents = TreatmentPlanAgents(llm)
    tasks = TreatmentPlanTasks(age=age, gender=gender, weight=weight, mental_illness=mental_illness, note=note)

    # Instantiate the agents
    treatment_plan_supervisor = agents.treatment_plan_supervisor_agent()
    fitness_expert = agents.fitness_expert_agent()
    nutritionist = agents.nutritionist_agent()
    health_expert = agents.health_expert_agent()
    psychotherapist = agents.psychotherapist_agent()
    resource_finder = agents.resource_finder_agent()

    # Instantiate the tasks
    fitness_task = tasks.fitness_task(fitness_expert)
    nutrition_task = tasks.nutrition_task(nutritionist)
    health_task = tasks.health_task(health_expert)
    psychotherapy_task = tasks.psychotherapy_task(psychotherapist)
    resources_task = tasks.resources_task(resource_finder)
    compile_treatment_plan_task = tasks.compile_treatment_plan_task(
        treatment_plan_supervisor, [fitness_task, nutrition_task, health_task, psychotherapy_task, resources_task])

    crew = Crew(
        agents=[fitness_expert, nutritionist, health_expert, psychotherapist, resource_finder, treatment_plan_supervisor],
        tasks=[fitness_task, nutrition_task, health_task, psychotherapy_task, resources_task, compile_treatment_plan_task],
        process=Process.hierarchical,
        manager_llm=llm,
        verbose=2
    )

    results = crew.kickoff()
    return results
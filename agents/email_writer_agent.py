from dotenv import load_dotenv
from crewai import Agent, Task, Crew, LLM

load_dotenv()

def run_email_writer(original_email: str):
    llm = LLM(
        model="gemini/gemini-2.0-flash",
        temperature=0.1
    )

    email_assistant = Agent(
        role="Email Assistant",
        goal="Improve emails and make them sound professional and clear.",
        backstory="A highly experienced communication expert, skilled in professional email writing.",
        verbose=True,
        llm=llm,
    )

    email_task = Task(
        description=f"""Take the rough email and rewrite it into a professional and polished version.
Expand all abbreviations and ensure clarity:
'''{original_email}'''""",
        agent=email_assistant,
        expected_output="A professionally written email with proper formatting and content.",
    )

    crew = Crew(
        agents=[email_assistant],
        tasks=[email_task],
        verbose=True,
    )

    result = crew.kickoff()
    return result

from dotenv import load_dotenv
from crewai import Agent, Task, Crew, LLM
from crewai_tools import TavilySearchTool

load_dotenv()

def run_blog_summarizer(topic: str):
    """
    Generates a blog summary based on the topic using two agents: researcher and writer.
    """
    llm = LLM(model="gemini/gemini-2.0-flash", temperature=0.1)

    researcher = Agent(
        role='Research Specialist',
        goal=f'Research interesting facts and trending information about the topic: {topic}',
        backstory='An expert in finding relevant and factual data.',
        tools=[TavilySearchTool()],
        llm=llm,
        verbose=True,
    )

    writer = Agent(
        role='Creative Writer',
        goal='Write a short blog summary using the research',
        backstory='Skilled at writing engaging summaries based on content.',
        llm=llm,
        verbose=True,
    )

    task1 = Task(
        description=f"Find 10–15 interesting and recent facts about the topic: {topic}",
        expected_output='A bullet list of 10–15 interesting and recent facts',
        agent=researcher,
    )

    task2 = Task(
        description=f"Write a 2-3 paragraph blog post summary about the topic {topic} using the facts from the research",
        expected_output='A blog post summary',
        agent=writer,
        context=[task1],
    )

    crew = Crew(agents=[researcher, writer], tasks=[task1, task2], verbose=True)
    return crew.kickoff(inputs={"topic": topic})

import re
import pyttsx3
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, LLM
from crewai_tools import TavilySearchTool

# Load environment variables from .env
load_dotenv()

def run_content_creator(topic: str):
    # Load LLM
    llm = LLM(model="gemini/gemini-2.0-flash", temperature=0.1)

    # Define Agents
    content_director = Agent(
        role="Content Director",
        goal="Lead the creation of high-quality YouTube content",
        backstory="An experienced director who plans and coordinates every step of video creation.",
        verbose=True,
        allow_delegation=True,
        llm=llm
    )

    scriptwriter = Agent(
        role="Scriptwriter",
        goal="Write engaging YouTube scripts",
        backstory="Creative writer for compelling scripts",
        verbose=True,
        allow_delegation=False,
        llm=llm
    )

    # Define Task
    script_task = Task(
        description=(
            f"Write a YouTube video script on the topic: {topic}.\n\n"
            "- A catchy intro\n"
            "- Informative main content\n"
            "- A memorable conclusion\n"
            "- Style suitable for narration\n"
        ),
        expected_output="A full script for 5-10 minutes video.",
        agent=scriptwriter,
    )

    # Run Crew
    crew = Crew(agents=[content_director, scriptwriter], tasks=[script_task], verbose=True)
    result = crew.kickoff(inputs={"topic": topic})

    # Clean text
    raw_text = str(result)
    cleaned_text = re.sub(r'\b\d{1,2}:\d{2}\b', '', raw_text)
    cleaned_text = re.sub(r'\[.*?\]', '', cleaned_text)
    cleaned_text = re.sub(r'(?m)^\s*(Narrator|[A-Z][a-z]+)\s*:\s*', '', cleaned_text)
    cleaned_text = re.sub(r'[^\w\s.,?!]', '', cleaned_text)
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()

    # Prepare voice narration text
    sentences = re.split(r'(?<=[.?!])\s+', cleaned_text)
    final_voice_text = ' '.join(sentences[2:]) if len(sentences) > 2 else cleaned_text

    # Convert to Speech
    engine = pyttsx3.init()
    engine.setProperty('rate', 130)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id if len(voices) > 1 else voices[0].id)
    engine.save_to_file(final_voice_text, 'output_voice.mp3')
    engine.runAndWait()

    return cleaned_text


if __name__ == "__main__":
    topic = "The Future of Artificial Intelligence"
    script = run_content_creator(topic)
    print("\n✅ Script Generated:\n")
    print(script)
    print("\n🎤 Voice narration saved as 'output_voice.mp3'")

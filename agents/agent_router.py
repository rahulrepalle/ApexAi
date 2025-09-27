from email_writer_agent import run_email_writer
from blog_summarizer_agent import run_blog_summarizer
from content_creator_agent import run_content_creator   # <-- new import

def run_agent(agent_type, input_data):
    if agent_type == "email":
        return run_email_writer(input_data)
    elif agent_type == "blog":
        return run_blog_summarizer(input_data)
    elif agent_type == "content_creator":
        return run_content_creator(input_data)  # <-- new case
    else:
        return "Invalid agent type"

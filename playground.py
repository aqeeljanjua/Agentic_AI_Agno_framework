from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.email import EmailTools
from agno.knowledge.json import JSONKnowledgeBase
from agno.storage.agent.postgres import PostgresAgentStorage
from agno.vectordb.pgvector import PgVector, SearchType
from agno.agent import Agent
from agno.playground import Playground, serve_playground_app

import os
from dotenv import load_dotenv
load_dotenv()
db_link = os.getenv("DB_URL")

os.environ['AGNO_API_KEY'] = os.getenv("AGNO_API_KEY")

receiver_email = os.getenv("RECEIVER_EMAIL")
sender_email = os.getenv("SENDER_EMAIL")
sender_name = os.getenv("SENDER_NAME")
sender_passkey = os.getenv("SENDER_PASSKEY")
json_path = os.getenv("JSON_PATH")

chat_agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    storage=PostgresAgentStorage( table_name="agent_sessions",db_url="postgresql+psycopg://ai:ai@localhost:5532/ai"),
    add_history_to_messages=True,
    markdown=True,
)

email_agent = Agent(model=Groq(id="llama-3.3-70b-versatile"),
    markdown=True,
    tools=[
        EmailTools(
            receiver_email=receiver_email,
            sender_email=sender_email,
            sender_name=sender_name,
            sender_passkey=sender_passkey,
        )
    ],storage=PostgresAgentStorage( table_name="agent_sessions",db_url="postgresql+psycopg://ai:ai@localhost:5532/ai"),
    add_history_to_messages=True
)
# agent.print_response("send an email to the supllier")


knowledge_base = JSONKnowledgeBase(
    path=json_path,
    
    vector_db=PgVector(table_name="inventory_supplier",
        db_url="postgresql+psycopg://ai:ai@localhost:5532/ai" ,search_type=SearchType.hybrid
    ),
    storage=PostgresAgentStorage( table_name="agent_sessions",db_url="postgresql+psycopg://ai:ai@localhost:5532/ai"),
    add_history_to_messages=True,
    markdown=True,
)



knowledge_agent = Agent(model=Groq(id="llama-3.3-70b-versatile"),
    knowledge=knowledge_base,
    search_knowledge=True,storage=PostgresAgentStorage( table_name="agent_sessions",
                                                       db_url="postgresql+psycopg://ai:ai@localhost:5532/ai"),
    add_history_to_messages=True,
    markdown=True,
    instructions=["share my inventory details"]
)
knowledge_agent.knowledge.load(recreate=False)

# knowledge_agent.print_response("share my inventory details")

app = Playground(agents=[knowledge_agent,email_agent,chat_agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("playground:app", reload=True, port=7860)
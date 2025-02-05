# Agentic AI Agno Framework

A multi-agent AI system built with the Agno framework, featuring chat, email, and knowledge base capabilities.

## Developer
Muhammad Aqeel Yasin  
Shadow Analytics

## Features
- Chat Agent using Groq LLM
- Email Agent for automated communications
- Knowledge Base Agent with JSON storage
- PostgreSQL with pgvector for vector storage
- Docker-based deployment

## Prerequisites
- Python 3.x
- Docker and Docker Compose
- PostgreSQL
- Groq API access

## Environment Variables
Create a `.env` file with:
```
AGNO_API_KEY=your_agno_api_key
DB_URL=your_database_url
RECEIVER_EMAIL=recipient@email.com
SENDER_EMAIL=sender@email.com
SENDER_NAME=Sender Name
SENDER_PASSKEY=email_app_password
JSON_PATH=path_to_json_knowledge_base
```

## Installation
1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Start the PostgreSQL database:
```bash
docker-compose up -d
```

## Usage
Run the playground:
```bash
python playground.py
```
The application will be available at `http://localhost:7860`

## Agents
1. **Chat Agent**: General conversation using Groq LLM
2. **Email Agent**: Handles email communications
3. **Knowledge Agent**: Manages inventory and supplier information

## Database
- Uses PostgreSQL with pgvector extension
- Default credentials:
  - Database: ai
  - User: ai
  - Password: ai
  - Port: 5532


## Support
For support, contact Muhammad Aqeel Yasin at Shadow Analytics.
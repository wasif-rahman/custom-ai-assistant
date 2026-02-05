# Custom AI Assistant

A modular, configurable AI assistant built with FastAPI and Grok AI, featuring multiple personality modes, conversation memory, and clean architecture designed for easy extension.

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109.0-green.svg)
![Grok](https://img.shields.io/badge/Grok-AI-orange.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](CONTRIBUTING.md)

---

## Project Goals

This project was built to:
- Learn practical AI integration and system design
- Practice modular architecture and clean code principles
- Build a portfolio-worthy project showcasing modern AI development
- Create a reusable base for future AI applications (tutors, mentors, exam assistants)

---

## Features

### Core Functionality
- **Multiple AI Modes**: Default, Mentor, Exam preparation
- **Conversation Memory**: Maintains context across messages
- **Config-Driven Behavior**: Change AI personality via YAML files (no code changes)
- **Swappable Components**: Easy to replace AI provider, database, or prompts
- **API-First Design**: RESTful endpoints with auto-generated documentation

### Technical Highlights
- **Modular Architecture**: Clear separation between routes, services, and models
- **Type Safety**: Pydantic models for validation
- **Auto Documentation**: Interactive API docs at `/docs`
- **Environment-Based Config**: Secure API key management

---

## Architecture

```
┌─────────────────┐
│  FastAPI Routes │  ← HTTP endpoints
└────────┬────────┘
         │
┌────────▼────────┐
│   AI Service    │  ← Handles Grok AI integration
└────────┬────────┘
         │
┌────────▼────────┐
│  Memory Service │  ← Manages conversation history
└─────────────────┘
         │
┌────────▼────────┐
│  prompts.yaml   │  ← Configurable AI personalities
└─────────────────┘
```

---

## Getting Started

### Prerequisites
- Python 3.11+
- Grok API key (xAI platform)

### Installation

1. Clone the repository
```bash
git clone https://github.com/wasif-rahman/custom-ai-assistant.git
cd custom-ai-assistant
```

2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r backend/requirements.txt
```

4. Set up environment variables
```bash
# Create .env file in project root
echo "Grok_API_KEY=your_grok_api_key_here" > .env
```

Note: The variable is named `OPENAI_API_KEY` for compatibility with the OpenAI SDK, but you should use your Grok API key.

5. Run the server
```bash
uvicorn backend.main:app --reload
```

6. Open interactive docs
```
http://localhost:8000/docs
```

---

## API Endpoints

### `GET /`
Health check endpoint

**Response:**
```json
{
  "status": "healthy",
  "message": "Custom AI Assistant is running!"
}
```

---

### `POST /chat`
Send a message and get AI response

**Request:**
```json
{
  "message": "Hello! Who are you?",
  "mode": "default",
  "conversation_id": "optional-uuid"
}
```

**Response:**
```json
{
  "response": "I'm a helpful, friendly AI assistant...",
  "conversation_id": "abc-123-def-456"
}
```

---

### `GET /modes`
Get available AI modes

**Response:**
```json
{
  "modes": ["default", "mentor", "exam"]
}
```

---

## AI Modes

### Default Mode
- Helpful and friendly
- Provides clear, concise answers
- General-purpose assistant

### Mentor Mode
- Guides through problems without giving direct answers
- Asks clarifying questions
- Encourages critical thinking

### Exam Mode
- Helps with exam preparation
- Explains concepts step-by-step
- Focuses on understanding fundamentals

**Want to add your own mode?** Edit `backend/config/prompts.yaml`

---

## Tech Stack

| Technology | Purpose |
|------------|---------|
| **FastAPI** | High-performance web framework |
| **Grok AI** | LLM integration via OpenAI-compatible API |
| **Pydantic** | Data validation and settings |
| **Python-dotenv** | Environment variable management |
| **PyYAML** | Configuration file parsing |
| **Uvicorn** | ASGI server |

---

## Project Structure

```
custom-ai-assistant/
├── backend/
│   ├── main.py              # FastAPI application
│   ├── config/
│   │   └── prompts.yaml     # AI personality configs
│   ├── services/
│   │   ├── ai_service.py    # Grok AI integration
│   │   └── memory_service.py# Conversation storage
│   ├── models/
│   │   └── schemas.py       # Pydantic models
│   └── requirements.txt     # Dependencies
├── frontend/                # Coming soon: Streamlit UI
├── .env                     # Environment variables (not in git)
├── .env.example             # Template for .env
└── README.md
```

---

## Configuration

### AI Provider

The project uses the OpenAI SDK for compatibility, but connects to Grok AI. To configure the AI provider, edit `backend/services/ai_service.py`:

```python
self.client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://api.x.ai/v1"  # Grok API endpoint
)
```

### System Prompts

AI behavior is controlled via `backend/config/prompts.yaml`. You can:
- Modify existing modes
- Add new personality modes
- Customize tone and style
- Set behavioral boundaries

---

## Roadmap

**Completed:**
- Core FastAPI backend
- Grok AI integration
- Multiple AI modes
- Conversation memory
- Auto-generated API documentation

**Planned:**
- Streamlit frontend UI
- MongoDB integration for persistent storage
- User authentication
- Deployment to DigitalOcean
- RAG (Retrieval-Augmented Generation) for custom knowledge
- Rate limiting and safety filters
- Response caching
- Multi-user support

---

## Development

### Running in Development Mode
```bash
uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```

### Running Tests
```bash
# Coming soon
pytest
```

### Code Style
This project follows PEP 8 style guidelines.

---

## Contributing

This project is open to contributions! We welcome contributions of all kinds:

- **New AI Modes**: Add new personality modes to `prompts.yaml` (no coding needed!)
- **Bug Reports**: Help us find and fix issues
- **Features**: Suggest and implement new features
- **Documentation**: Improve docs and examples
- **Frontend**: Help build the Streamlit UI
- **Backend**: Work on MongoDB integration, authentication, RAG, etc.

**[📖 Read our Contributing Guide →](CONTRIBUTING.md)**

### Quick Start for Contributors

1. Fork and clone the repo
2. Check [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines
3. Look for issues labeled `good first issue` or `help wanted`
4. Submit a PR - we love reviewing contributions!

---

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## Author

**Wasif Rahman**  
Software Engineering Student  
[GitHub](https://github.com/wasif-rahman)

---

## Acknowledgments

- Built as part of my AI engineering learning journey
- Leveraging GitHub Student Developer Pack resources
- Inspired by modern AI assistant architectures
- Powered by Grok AI from xAI

---

## Contact

Questions or suggestions? Open an issue or reach out.

---

**If you found this project helpful, consider starring it.**

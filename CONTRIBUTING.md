# Contributing to Custom AI Assistant

Welcome! 👋 Thank you for your interest in contributing to the Custom AI Assistant project. This is a learning project built to explore AI integration, system design, and modern development practices, and we're excited to have contributors of all skill levels join us.

Whether you're fixing a typo, adding a feature, or suggesting improvements, your contributions are valued and appreciated!

---

## Ways to Contribute

There are many ways you can contribute to this project:

- 🐛 **Report bugs** - Help us identify and fix issues
- ✨ **Suggest new AI modes/features** - Share ideas for new personality modes or capabilities
- 📚 **Improve documentation** - Make our docs clearer and more comprehensive
- 🧪 **Write tests** - Help us build a robust test suite
- 🎨 **Build the frontend** - Contribute to the Streamlit UI development
- ⚙️ **Backend enhancements** - Improve API endpoints, services, or architecture
- 🗄️ **Database integration** - Help with MongoDB implementation
- 🔐 **Security improvements** - Enhance authentication and safety features

---

## Getting Started for New Contributors

### 1. Fork and Clone the Repository

```bash
# Fork the repository on GitHub, then clone your fork
git clone https://github.com/YOUR-USERNAME/custom-ai-assistant.git
cd custom-ai-assistant
```

### 2. Set Up Your Development Environment

**Prerequisites:**
- Python 3.11 or higher
- Grok API key from xAI platform

**Installation:**

```bash
# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r backend/requirements.txt

# Set up environment variables
echo "OPENAI_API_KEY=your_grok_api_key_here" > .env
```

### 3. Run the Project Locally

```bash
# Start the FastAPI server
uvicorn backend.main:app --reload

# Visit the interactive API documentation
# http://localhost:8000/docs
```

---

## Contribution Workflow

### For Major Changes

1. **Create an issue first** - Discuss your proposed changes before starting work
2. **Wait for feedback** - Get input from maintainers to ensure alignment
3. **Fork the repository** - Work on your own copy
4. **Create a feature branch** - Follow our branch naming conventions
5. **Make your changes** - Follow our coding standards
6. **Test your changes** - Ensure everything works as expected
7. **Submit a pull request** - Reference the related issue

### Branch Naming Conventions

Use descriptive branch names with prefixes:

- `feature/` - New features (e.g., `feature/add-tutor-mode`)
- `bugfix/` - Bug fixes (e.g., `bugfix/fix-memory-leak`)
- `docs/` - Documentation updates (e.g., `docs/update-api-guide`)
- `test/` - Adding tests (e.g., `test/add-ai-service-tests`)
- `refactor/` - Code refactoring (e.g., `refactor/improve-error-handling`)

### Commit Message Guidelines

Write clear, descriptive commit messages:

**Good:**
```
Add mentor mode with guided learning prompts
Fix conversation memory not persisting across sessions
Update README with MongoDB setup instructions
```

**Not so good:**
```
Fixed stuff
Update
Changes
```

**Format:**
- Use present tense ("Add feature" not "Added feature")
- Keep the first line under 50 characters
- Provide details in the body if needed
- Reference issues: "Fixes #123" or "Closes #456"

---

## Code Standards

### Python Style Guidelines

- Follow **PEP 8** style guidelines
- Use **type hints** for function parameters and return values
- Add **docstrings** to all new functions and classes
- Keep functions focused and modular
- Use meaningful variable names

**Example:**

```python
def generate_response(message: str, mode: str = "default") -> str:
    """
    Generate an AI response based on the given message and mode.
    
    Args:
        message: The user's input message
        mode: The AI personality mode to use (default, mentor, exam)
        
    Returns:
        The AI's response as a string
        
    Raises:
        ValueError: If the mode is not recognized
    """
    # Implementation here
    pass
```

### Code Organization

- Place new AI modes in `backend/config/prompts.yaml`
- Add new endpoints in `backend/main.py` or create new route files
- Service logic goes in `backend/services/`
- Data models go in `backend/models/`

### Documentation

- Update documentation when adding new features
- Include docstrings for public APIs
- Add examples for complex functionality
- Update README.md if adding major features

---

## Pull Request Process

### Before Submitting

1. **Test your changes** - Make sure everything works
2. **Update documentation** - If you changed functionality
3. **Follow code standards** - PEP 8, type hints, docstrings
4. **Keep it focused** - One feature or fix per PR

### PR Description Template

```markdown
## Description
Brief description of what this PR does

## Related Issue
Fixes #(issue number)

## Changes Made
- Change 1
- Change 2
- Change 3

## Testing
How did you test this? What scenarios did you cover?

## Screenshots (if applicable)
Add screenshots for UI changes
```

### Review Process

- A maintainer will review your PR
- Address any requested changes
- Once approved, your PR will be merged
- Your contribution will be credited!

---

## Areas Where Help is Especially Welcome

We're actively looking for contributions in these areas:

### 🎨 Frontend Development
- Building the Streamlit UI
- Creating chat interface components
- Mode selection interface
- Conversation history display

### 🗄️ Database Integration
- MongoDB setup and configuration
- Persistent conversation storage
- User session management
- Data migration scripts

### ✨ New AI Personality Modes
- Educational tutors (math, science, etc.)
- Creative writing assistants
- Code review assistants
- Interview preparation modes

### 🧪 Testing
- Unit tests for services
- Integration tests for API endpoints
- End-to-end testing
- Test fixtures and utilities

### 📚 Documentation
- API usage examples
- Tutorial for creating custom modes
- Deployment guides
- Architecture documentation

### 🔐 RAG Implementation
- Document ingestion pipeline
- Vector database integration
- Retrieval logic
- Custom knowledge base support

---

## Code of Conduct

This project follows a Code of Conduct to ensure a welcoming environment for all contributors. Please read and follow our [Code of Conduct](CODE_OF_CONDUCT.md).

---

## Questions and Support

- 💬 **Have questions?** Open a [GitHub Discussion](https://github.com/wasif-rahman/custom-ai-assistant/discussions)
- 🐛 **Found a bug?** Open an [Issue](https://github.com/wasif-rahman/custom-ai-assistant/issues)
- 💡 **Have an idea?** Start with an [Issue](https://github.com/wasif-rahman/custom-ai-assistant/issues) to discuss it

---

## Recognition

All contributors will be recognized in our project. Thank you for helping make this project better! 🎉

---

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

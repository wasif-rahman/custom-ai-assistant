# Contributing to Custom AI Assistant

Thank you for your interest in contributing to Custom AI Assistant! 🎉

This is a learning project built to explore AI integration, modular architecture, and clean code principles. We welcome contributions from developers of all skill levels—whether you're fixing a typo, adding a feature, or suggesting improvements, your help is appreciated!

## Ways to Contribute

There are many ways you can contribute to this project:

### 🐛 Reporting Bugs
Found a bug? Please [open an issue](https://github.com/wasif-rahman/custom-ai-assistant/issues/new?template=bug_report.md) with:
- A clear description of the problem
- Steps to reproduce
- Expected vs. actual behavior
- Your environment details

### ✨ Suggesting New AI Modes/Features
Have an idea for a new AI personality mode or feature? We'd love to hear it!
- For new AI modes: Use the [New AI Mode template](https://github.com/wasif-rahman/custom-ai-assistant/issues/new?template=new_ai_mode.md)
- For other features: Use the [Feature Request template](https://github.com/wasif-rahman/custom-ai-assistant/issues/new?template=feature_request.md)

### 📚 Improving Documentation
Documentation is crucial for a welcoming project. You can:
- Fix typos or clarify existing docs
- Add examples or tutorials
- Improve API documentation
- Write guides for new contributors

### 🧪 Writing Tests
Help us improve code quality by:
- Adding unit tests for existing features
- Writing integration tests
- Improving test coverage

### 🎨 Building the Frontend
The Streamlit frontend is planned but not yet implemented. Contributors interested in UI/UX are especially welcome!

### ⚙️ Backend Enhancements
Improve the backend by:
- Optimizing performance
- Adding new API endpoints
- Implementing MongoDB integration
- Adding RAG capabilities
- Improving error handling

## Getting Started for New Contributors

### Fork and Clone

1. **Fork the repository** by clicking the "Fork" button at the top right of the [repository page](https://github.com/wasif-rahman/custom-ai-assistant)

2. **Clone your fork** to your local machine:
```bash
git clone https://github.com/YOUR-USERNAME/custom-ai-assistant.git
cd custom-ai-assistant
```

3. **Add upstream remote** to keep your fork in sync:
```bash
git remote add upstream https://github.com/wasif-rahman/custom-ai-assistant.git
```

### Development Environment Setup

Follow these steps to set up your development environment:

1. **Ensure you have Python 3.11+** installed:
```bash
python --version
```

2. **Create a virtual environment**:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**:
```bash
pip install -r backend/requirements.txt
```

4. **Set up environment variables**:
```bash
# Create .env file in project root
echo "OPENAI_API_KEY=your_grok_api_key_here" > .env
```
Note: Get a Grok API key from [xAI platform](https://x.ai/)

5. **Verify installation** by running the server:
```bash
uvicorn backend.main:app --reload
```

6. **Access the API documentation** at http://localhost:8000/docs

### Running the Project Locally

**Start the development server:**
```bash
uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```

**Test the API:**
- Open http://localhost:8000/docs for interactive API documentation
- Try the `/chat` endpoint with different AI modes
- Check available modes with `/modes` endpoint

## Contribution Workflow

We follow a standard GitHub workflow. Here's the process:

### 1. Create an Issue First (for major changes)
For significant changes, please create an issue first to discuss:
- What you want to change
- Why it's needed
- How you plan to implement it

This helps avoid duplicate work and ensures your contribution aligns with project goals.

### 2. Fork → Branch → Commit → Push → PR

**Create a new branch** for your work:
```bash
git checkout -b feature/your-feature-name
# or
git checkout -b bugfix/your-bugfix-name
# or
git checkout -b docs/your-docs-change
```

**Make your changes** following our code standards (see below)

**Commit your changes** with clear messages:
```bash
git add .
git commit -m "Add clear, descriptive commit message"
```

**Push to your fork**:
```bash
git push origin feature/your-feature-name
```

**Open a Pull Request** on GitHub

### Branch Naming Conventions

Use descriptive branch names with prefixes:
- `feature/` - New features (e.g., `feature/add-tutor-mode`)
- `bugfix/` - Bug fixes (e.g., `bugfix/fix-memory-leak`)
- `docs/` - Documentation changes (e.g., `docs/update-api-guide`)
- `test/` - Test additions/improvements (e.g., `test/add-ai-service-tests`)
- `refactor/` - Code refactoring (e.g., `refactor/improve-error-handling`)

### Commit Message Guidelines

Write clear, descriptive commit messages:

**Good:**
- ✅ "Add exam mode with step-by-step explanations"
- ✅ "Fix conversation memory not persisting across requests"
- ✅ "Update README with MongoDB setup instructions"

**Avoid:**
- ❌ "Update stuff"
- ❌ "Fix bug"
- ❌ "WIP"

**Format:**
- Use present tense ("Add feature" not "Added feature")
- Be specific about what changed
- Keep the first line under 72 characters
- Add detailed explanation in body if needed

## Code Standards

We strive for clean, maintainable code. Please follow these guidelines:

### Python Style Guidelines

- **Follow [PEP 8](https://pep8.org/)** style guidelines
- Use 4 spaces for indentation (no tabs)
- Maximum line length: 88 characters (Black formatter default)
- Use meaningful variable and function names

### Documentation

- **Add docstrings** to new functions and classes:
```python
def process_message(message: str, mode: str) -> str:
    """
    Process a user message with the specified AI mode.
    
    Args:
        message: The user's input message
        mode: The AI mode to use (default, mentor, exam)
        
    Returns:
        The AI's response as a string
        
    Raises:
        ValueError: If mode is not recognized
    """
    pass
```

### Type Hints

- **Use type hints** for function parameters and return values:
```python
def get_conversation_history(conversation_id: str) -> List[Dict[str, str]]:
    pass
```

### Code Quality

- Keep functions focused and single-purpose
- Avoid deep nesting (max 3-4 levels)
- Handle errors gracefully with try/except blocks
- Remove commented-out code before committing
- Don't commit debugging print statements

### Update Documentation

If you add new features:
- Update relevant documentation files
- Add examples to README if applicable
- Update API documentation
- Add comments for complex logic

## Pull Request Process

When you're ready to submit your changes:

### 1. Describe Your Changes Clearly

Write a clear PR description that includes:
- **What** you changed
- **Why** you made the change
- **How** it works (for complex changes)
- **Testing** you've done

Example:
```markdown
## Summary
Add a new "Tutor" AI mode for educational assistance

## Changes
- Added tutor mode configuration to prompts.yaml
- Updated mode validation in ai_service.py
- Added tutor mode to available modes endpoint

## Testing
- Tested tutor mode with various educational questions
- Verified mode appears in /modes endpoint
- Confirmed existing modes still work correctly
```

### 2. Reference Related Issues

Link to related issues using keywords:
- `Fixes #123` - Closes issue #123 when PR is merged
- `Relates to #456` - References issue #456
- `Part of #789` - Indicates this is partial work for issue #789

### 3. Keep PRs Focused

- One feature/fix per PR
- Avoid mixing unrelated changes
- Keep changes minimal and focused
- If you notice other issues, create separate PRs

### 4. Be Responsive

- Address review feedback promptly
- Ask questions if feedback is unclear
- Be open to suggestions and improvements

### 5. Ensure Tests Pass

Before submitting:
- Test your changes locally
- Ensure existing functionality still works
- Add tests for new features (when test infrastructure exists)

## Areas Where Help is Especially Welcome

Based on our [roadmap](https://github.com/wasif-rahman/custom-ai-assistant#roadmap), we especially need help with:

### 🎨 Streamlit Frontend Development
- Design and implement the UI
- Create chat interface
- Add mode selector
- Build conversation history view

### 🗄️ MongoDB Integration
- Set up MongoDB connection
- Implement persistent storage for conversations
- Add user data models
- Create database migration system

### ✨ Adding New AI Personality Modes
- Educational modes (teacher, professor)
- Specialized assistants (coding, writing, research)
- Professional modes (email writer, presentation helper)
- Creative modes (storyteller, brainstormer)

### 🧪 Writing Tests
- Unit tests for services
- Integration tests for API endpoints
- End-to-end tests
- Test fixtures and utilities

### 📚 Documentation Improvements
- Tutorial for beginners
- Advanced usage guide
- Architecture documentation
- Deployment guides

### 🔐 User Authentication
- JWT-based authentication
- User registration/login
- Protected endpoints
- Session management

### 🤖 RAG Implementation
- Document ingestion pipeline
- Vector database integration
- Retrieval logic
- Custom knowledge base features

## Code of Conduct

This project follows the [Contributor Covenant Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior by opening an issue.

## Questions and Support

Have questions? Need help?

- 💬 **General questions**: Open a [discussion](https://github.com/wasif-rahman/custom-ai-assistant/issues) or issue
- 🐛 **Bug reports**: Use the [bug report template](https://github.com/wasif-rahman/custom-ai-assistant/issues/new?template=bug_report.md)
- 💡 **Feature ideas**: Use the [feature request template](https://github.com/wasif-rahman/custom-ai-assistant/issues/new?template=feature_request.md)
- 🎓 **Getting started**: Review this guide and the [README](README.md)

## Recognition

All contributors will be recognized in our repository. Thank you for helping make this project better! 🙏

---

**Ready to contribute?** Check out our [open issues](https://github.com/wasif-rahman/custom-ai-assistant/issues) labeled [`good first issue`](https://github.com/wasif-rahman/custom-ai-assistant/labels/good%20first%20issue) or [`help wanted`](https://github.com/wasif-rahman/custom-ai-assistant/labels/help%20wanted)!

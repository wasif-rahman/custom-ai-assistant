# Contributing to Custom AI Assistant

Welcome! We're excited that you're interested in contributing to this project. This document provides guidelines and instructions for contributing.

## Code of Conduct

Please read our [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) before contributing. We are committed to providing a welcoming and inspiring community.

## How to Contribute

### 1. **Report Bugs**
Found a bug? Please open an issue using our [bug report template](.github/ISSUE_TEMPLATE/bug_report.md).

Include:
- Description of the bug
- Steps to reproduce
- Expected vs actual behavior
- Your environment (Python version, OS, etc.)

### 2. **Suggest Features**
Have an idea? Open an issue using our [feature request template](.github/ISSUE_TEMPLATE/feature_request.md).

Include:
- Clear description of the feature
- Use cases and benefits
- Possible implementation approach (optional)

### 3. **Add New AI Modes** ⭐ *Great for beginners!*
The easiest way to contribute:

1. Edit `backend/config/prompts.yaml`
2. Add a new mode with a unique system prompt
3. Open a PR with your new mode

Example:
```yaml
"creative":
  system_prompt: "You are a creative writing assistant..."
  description: "Helps with creative writing tasks"
```

### 4. **Code Contributions**
Ready to contribute code? Follow these steps:

#### Setup Development Environment
```bash
# Clone the repository
git clone https://github.com/wasif-rahman/custom-ai-assistant.git
cd custom-ai-assistant

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r backend/requirements.txt

# Run development server
uvicorn backend.main:app --reload
```

#### Making Changes
1. Create a feature branch: `git checkout -b feature/your-feature-name`
2. Make your changes
3. Follow the code style guidelines (see below)
4. Commit with clear messages: `git commit -m "Add feature: description"`
5. Push to your fork: `git push origin feature/your-feature-name`
6. Open a Pull Request

#### Code Style
- Follow **PEP 8** style guidelines
- Use meaningful variable and function names
- Add docstrings to functions
- Include type hints where possible
- Keep functions focused and small

Example:
```python
def get_ai_response(message: str, mode: str) -> str:
    """
    Get response from AI assistant.
    
    Args:
        message: User message
        mode: AI mode (default, mentor, exam)
    
    Returns:
        AI response string
    """
    # Implementation
```

### 5. **Improve Documentation**
- Fix typos or unclear explanations
- Add examples or tutorials
- Improve README or docstrings
- Create documentation for features

### 6. **Other Contributions**
- Add tests (when pytest setup is ready)
- Improve performance
- Refactor code for clarity
- Suggest better architecture

## Areas Looking for Help

### 🟢 Good First Issues
- Adding new AI modes (YAML only, no coding needed)
- Fixing documentation typos
- Adding code comments
- Writing simple unit tests

### 🟡 Help Wanted
- Streamlit frontend development
- MongoDB integration
- User authentication system
- RAG (Retrieval-Augmented Generation) implementation
- API rate limiting

### 🔴 Advanced
- Performance optimization
- Deployment pipeline setup
- Advanced caching strategies
- Multi-language support

## Pull Request Process

1. **Before submitting:**
   - Check if your PR addresses an open issue
   - Test your changes locally
   - Update documentation if needed

2. **PR Title Format:**
   - `Add: [feature]` for new features
   - `Fix: [issue]` for bug fixes
   - `Docs: [update]` for documentation
   - `Refactor: [change]` for code improvements

3. **PR Description:**
   - Reference related issues: `Fixes #123`
   - Describe what changed and why
   - Add any testing notes

4. **Review Process:**
   - Maintainers will review your PR
   - Be open to feedback and suggestions
   - Make requested changes in new commits

5. **Merge:**
   - PRs will be merged once approved
   - Your contribution will be appreciated! 🎉

## Development Roadmap

### Next Priority Features
- [ ] Streamlit frontend UI
- [ ] MongoDB integration
- [ ] User authentication
- [ ] RAG implementation
- [ ] Rate limiting

See the [Roadmap section in README](README.md#roadmap) for full details.

## Questions?

- **Questions about contributing?** Open a discussion or issue
- **Need help getting started?** Comment on a `good first issue`
- **Want to discuss a feature?** Open an issue to discuss first

## Recognition

Contributors will be:
- Added to the README acknowledgments
- Credited in commit messages
- Recognized in GitHub contribution activity

---

**Thank you for contributing! Your help makes this project better.** ❤️

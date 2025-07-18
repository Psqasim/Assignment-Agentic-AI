# Assignment-Agentic-AI

A comprehensive exploration of Agentic AI concepts, implementations, and practical applications. This repository contains various projects and experiments related to autonomous AI agents and their capabilities.

## 📋 Table of Contents

- [Overview](#overview)
- [Projects](#projects)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

This repository showcases different aspects of Agentic AI, including:

- **Autonomous Agent Development**: Building AI agents that can operate independently
- **Decision Making Systems**: Implementing intelligent decision-making processes
- **Multi-Agent Coordination**: Exploring how multiple AI agents can work together
- **Real-world Applications**: Practical implementations of agentic AI concepts

## 🚀 Projects

### 1. UV Explore
Located in `uv_explore/`, this project demonstrates:
- Python package management with UV
- Modern Python project structure
- Agent-based explorations

#### Sub-projects:
- **hello_Uv**: Basic UV package setup and configuration
- **project2**: Advanced implementations and examples

### 2. OpenRouter AI Agent
Located in `OpenRouter_AI_Age*/`, featuring:
- Integration with OpenRouter API
- AI agent implementations
- Real-world API interactions

## 🛠️ Installation

### Prerequisites
- Python 3.8 or higher
- Git
- UV package manager (recommended)

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/Psqasim/Assignment-Agentic-AI.git
   cd Assignment-Agentic-AI
   ```

2. **Install UV (if not already installed)**
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

3. **Set up the projects**
   ```bash
   # For UV Explore projects
   cd uv_explore/hello_Uv
   uv sync
   
   # Activate virtual environment
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

4. **Install dependencies**
   ```bash
   uv pip install -r requirements.txt  # if requirements.txt exists
   # Or install from pyproject.toml
   uv pip install -e .
   ```

## 💻 Usage

### Running UV Explore Projects

```bash
cd uv_explore/hello_Uv
uv run python src/hello_uv/main.py
```

### Running OpenRouter AI Agent

```bash
cd OpenRouter_AI_Age*
python main.py
```

### Environment Variables

Create a `.env` file in the project root:

```env
OPENROUTER_API_KEY=your_api_key_here
# Add other necessary environment variables
```

## 📁 Project Structure

```
Assignment-Agentic-AI/
├── README.md
├── .gitignore
├── uv_explore/
│   ├── hello_Uv/
│   │   ├── src/
│   │   │   └── hello_uv/
│   │   │       ├── __init__.py
│   │   │       └── main.py
│   │   ├── pyproject.toml
│   │   ├── .python-version
│   │   └── README.md
│   └── project2/
│       └── [project files]
├── OpenRouter_AI_Age*/
│   └── [AI agent implementations]
└── .mypy_cache/
    └── [type checking cache]
```

## 🔧 Technologies Used

- **Python**: Primary programming language
- **UV**: Modern Python package and project manager
- **OpenRouter API**: AI model access and integration
- **Agentic AI Frameworks**: Various libraries for agent development
- **Type Checking**: MyPy for static type analysis

## 🚦 Getting Started

1. **Explore the Basic Example**
   ```bash
   cd uv_explore/hello_Uv
   uv run python src/hello_uv/main.py
   ```

2. **Understand the Project Structure**
   - Review the `pyproject.toml` files for dependencies
   - Check the source code organization
   - Examine the agent implementations

3. **Experiment with Agents**
   - Modify existing agent behaviors
   - Create new agent types
   - Test different scenarios

## 📊 Key Features

- **Modular Design**: Each project is self-contained and modular
- **Modern Python**: Uses latest Python packaging standards
- **Type Safety**: Includes type hints and MyPy configuration
- **Documentation**: Comprehensive documentation for each component
- **Scalable Architecture**: Designed for easy extension and modification

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines

- Follow PEP 8 style guidelines
- Add type hints to all functions
- Include docstrings for classes and functions
- Write tests for new functionality
- Update documentation as needed

## 📝 Notes

- This project uses UV for dependency management, which provides faster and more reliable package installation
- The `.python-version` files specify the Python version for each project
- MyPy cache is included for type checking optimizations

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Qasim** - [Psqasim](https://github.com/Psqasim)

## 🙏 Acknowledgments

- Thanks to the open-source community for the tools and libraries used
- Special recognition to the Agentic AI research community
- UV team for the excellent package management tool

---

**Note**: This is an educational project focused on exploring Agentic AI concepts and implementations. Feel free to use it as a learning resource or starting point for your own agentic AI projects.
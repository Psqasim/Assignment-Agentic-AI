# AI Agent Function Tools

A Python-based AI agent system that demonstrates function tool integration using the Agents library with Google's Gemini 2.0 Flash model. This project showcases how to create custom tools that an AI agent can use to perform specific tasks.

## Features

- **Custom Function Tools**: Four different tools demonstrating various capabilities
- **Gemini Integration**: Uses Google's Gemini 2.0 Flash model via OpenAI-compatible API
- **Async Support**: Built with async/await for efficient operations
- **Environment Configuration**: Secure API key management with dotenv

## Tools Available

### 1. Add Tool
- **Function**: `add(a: int, b: int) -> int`
- **Purpose**: Performs addition of two integers
- **Example**: "What is 7 + 5?" → Returns 12

### 2. Weather Tool
- **Function**: `get_weather(city: str) -> str`
- **Purpose**: Returns simulated weather data for any city
- **Example**: "What's the weather in Lahore?" → Returns fake weather with temperature and conditions

### 3. Multiply Tool
- **Function**: `multiply(a: int, b: int) -> int`
- **Purpose**: Performs multiplication of two integers
- **Example**: "Multiply 6 and 9" → Returns 54

### 4. Greet Tool
- **Function**: `greet(name: str) -> str`
- **Purpose**: Generates friendly greetings
- **Example**: "Say hello to Qasim" → Returns personalized greeting

## Prerequisites

- Python 3.8+
- Google Gemini API key
- Required Python packages (see Installation)

## Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd ai-agent-function-tools
   ```

2. **Install dependencies**
   ```bash
   pip install agents-sdk python-dotenv
   ```

3. **Set up environment variables**
   Create a `.env` file in the project root:
   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

4. **Get your Gemini API key**
   - Visit [Google AI Studio](https://aistudio.google.com/)
   - Create a new API key
   - Add it to your `.env` file

## Usage

### Basic Usage

Run the script to see all tools in action:

```bash
python main.py
```

### Example Interactions

```python
# Addition
result = Runner.run_sync(agent, input="What is 7 + 5?", run_config=config)
print(result.final_output)  # Output: 12

# Weather
result = Runner.run_sync(agent, input="What's the weather in Tokyo?", run_config=config)
print(result.final_output)  # Output: Simulated weather data

# Multiplication
result = Runner.run_sync(agent, input="Multiply 8 and 7", run_config=config)
print(result.final_output)  # Output: 56

# Greeting
result = Runner.run_sync(agent, input="Greet Sarah", run_config=config)
print(result.final_output)  # Output: Personalized greeting
```

## Code Structure

```
├── main.py              # Main application file
├── .env                 # Environment variables (create this)
├── README.md           # This file
└── requirements.txt    # Python dependencies (optional)
```

## Key Components

### Agent Configuration
- **Name**: "personal_assistant"
- **Instructions**: Configured to use only registered tools
- **Model**: Gemini 2.0 Flash via OpenAI-compatible endpoint

### Function Tool Decorator
The `@function_tool` decorator automatically:
- Registers functions as available tools
- Handles parameter validation
- Manages async execution
- Provides tool descriptions to the AI model

### Error Handling
- API key validation on startup
- Tracing disabled for cleaner output
- Async error handling throughout

## Customization

### Adding New Tools

1. **Create a new function with the decorator**:
   ```python
   @function_tool
   async def your_tool(param: type) -> return_type:
       """Description of what your tool does."""
       # Your implementation here
       return result
   ```

2. **Add to agent tools list**:
   ```python
   agent = Agent(
       name="personal_assistant",
       instructions="Your instructions here",
       tools=[add, get_weather, multiply, greet, your_tool]  # Add your tool
   )
   ```

### Modifying Existing Tools

Each tool can be customized by modifying its implementation while keeping the function signature and decorator intact.

## Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GEMINI_API_KEY` | Your Google Gemini API key | Yes |

## Dependencies

- `agents-sdk`: Core agents framework
- `python-dotenv`: Environment variable management
- `random`: Built-in Python module for weather simulation

## Troubleshooting

### Common Issues

1. **API Key Error**
   - Ensure `GEMINI_API_KEY` is set in your `.env` file
   - Verify the API key is valid and active

2. **Import Errors**
   - Install required packages: `pip install agents-sdk python-dotenv`
   - Check Python version compatibility

3. **Connection Issues**
   - Verify internet connection
   - Check if Gemini API endpoint is accessible

## Contributing

1. Fork the repository
2. Create a feature branch
3. Add your improvements
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).

## Support

For questions or issues:
- Check the [Agents SDK documentation](https://github.com/agents-sdk/agents)
- Review Google Gemini API documentation
- Open an issue in this repository

---

**Note**: This project uses simulated data for demonstration purposes. The weather tool returns fake data and should not be used for actual weather information.
```


# AI-Powered Space Storybook Generator

This project uses AI agents to create an illustrated storybook about space ships, combining creative writing with image generation and document formatting.

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Architecture](#architecture)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Project Structure](#project-structure)
7. [Contributing](#contributing)
8. [License](#license)

## Introduction

This AI-powered storybook generator leverages multiple AI agents to create a complete, illustrated storybook about space ships. The system handles everything from outlining and writing to editing, image generation, and final PDF creation.

## Features

- AI-driven story outline creation
- Automated story writing and editing
- AI-generated chapter illustrations
- Markdown formatting of the story content
- Conversion of the formatted story to a PDF

## Architecture

The project uses CrewAI for agent orchestration and consists of several specialized AI agents:

1. **Story Outliner:** Creates the story structure and chapter outlines
2. **Story Writer:** Writes the full content for each chapter
3. **Story Editor:** Refines and improves the written content
4. **Image Generator:** Creates illustrations for each chapter
5. **Content Formatter:** Formats the story in Markdown
6. **PDF Converter:** Converts the Markdown to a final PDF

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/ai-space-storybook-generator.git
   cd ai-space-storybook-generator
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up your environment variables:
   Create a `.env` file in the project root and add your API keys:
   ```
   OPENAI_API_KEY=your_openai_api_key
   GROQ_API_KEY=your_groq_api_key
   ```

## Usage

Run the main script:
```
python app.py
```

The script will generate a complete storybook, including:
- A story outline
- Written content for 5 chapters
- Edited and refined story text
- An illustration for each chapter
- A formatted Markdown file
- A final PDF document

## Project Structure

- `app.py`: Main script containing the AI agents and task definitions
- `template.md`: Template for the story's Markdown format
- `requirements.txt`: List of required Python packages
- `README.md`: This file, containing project documentation

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. Here are some areas where contributions would be particularly valuable:

- Improving the AI agents' capabilities
- Enhancing the image generation prompts
- Adding new features like character dialogue or interactive elements
- Optimizing the PDF conversion process

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
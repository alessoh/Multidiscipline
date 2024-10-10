# Multidiscipline: AI Agent Orchestration Framework

Multidiscipline is an advanced self-improvement framework for orchestrating role-playing, autonomous AI agents. Built on top of CrewAI, Multidiscipline fosters collaborative intelligence, empowering agents to work together seamlessly and tackle complex tasks.

## Table of Contents
1. [Introduction](#introduction)
2. [Key Features](#key-features)
3. [Architecture](#architecture)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Project Structure](#project-structure)
7. 
8. [Continuous Learning](#continuous-learning)
9. [Future Enhancements](#future-enhancements)
10. [Contributing](#contributing)
11. [License](#license)
12. [Contact](#contact)

## Introduction

As AI foundation models advance, they are approaching PhD-level reasoning and logic abilities. While AI doctors, lawyers, and engineers aren't ready to practice independently, every professional will want a specialized AI partner to assist them in delivering premium service to their clients.

Multidisciplineaddresses the challenges of poor coordination, limited adaptability, and inconsistent performance in AI agent teams. It provides power and flexibility for AI agents to synchronize their tasks on one project and train as a team over many projects.

## Key Features
 
## Architecture

Multidiscipline uses a modular architecture with separate components for different functionalities:

1. **Core Logic (app.py):** Manages AI crews and orchestrates the main workflow.
2. **User Interface (streamlit_app.py):** Provides an intuitive Streamlit-based interface for user interactions.


The project leverages CrewAI for agent orchestration and extends it with custom postmortem analysis and continuous learning capabilities.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/alessoh/Multidiscipline.git
   cd Multidiscipline
   ```

2. Create and activate a virtual environment:
   ```
   conda create -n Multidiscipline python=3.11
   conda activate Multidiscipline
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up your environment variables:
   Create a `.env` file in the project root and add your API keys:
   ```
   OPENAI_API_KEY=your_openai_api_key
   SERPER_API_KEY=your_serper_api_key
   ```

## Usage

Run the Streamlit app:
```
streamlit run streamlit_app.py
```

Follow the prompts in the web interface to conduct AI analyses and postmortem evaluations.

## Project Structure

- `app.py`: Core logic for running AI crews and postmortem analysis
- `streamlit_app.py`: Streamlit-based user interface
- `postmortem_data_processor.py`: Handles postmortem data collection and preprocessing




### Key Components:



   # Diagram of current logic

![Alt text]()

## Continuous Learning



## Future Enhancements



   # Diagram of future 

![Alt text]

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. Here are some areas where contributions would be particularly valuable:

- Implementing any of the future enhancements listed above.
- Improving test coverage and documentation.
- Optimizing performance of existing components.
- Adding new features or integrations that align with SYZYGI's goals.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

- **Homepage:** [AI HIVE](https://www.ai-hive.net/)
- **Email:** info@ai-hive.net

For any questions, feedback, or bug reports, please open an issue in the GitHub repository or contact us via email.
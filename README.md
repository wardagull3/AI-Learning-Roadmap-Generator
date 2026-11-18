# AI Learning Roadmap Generator

An AI-powered application that generates personalized learning roadmaps based on a user's interests, current skill level, available study time, learning duration, and goals.

The application uses the Groq API to generate structured learning plans and Gradio to provide a simple, interactive web interface.

## Features

- **Personalized Roadmaps:** Generate learning plans based on individual requirements.
- **Multiple Skill Levels:** Supports complete beginners, beginners, intermediate learners, and advanced learners.
- **Flexible Study Time:** Customize the roadmap according to daily study hours.
- **Flexible Duration:** Choose a learning period from one month to twelve months.
- **Practical Learning:** Includes topics, exercises, projects, and learning outcomes.
- **AI-Powered Generation:** Uses a large language model through the Groq API.

## Technologies Used

- Python
- Google Colab
- Groq API
- Gradio

## How It Works

1. The user enters a topic they want to learn.
2. The user selects their current skill level.
3. The user specifies daily study hours and learning duration.
4. The user describes their learning goal.
5. The application sends these details to the Groq API.
6. The AI generates a personalized learning roadmap and displays it through Gradio.

## Project Structure

```text
AI-Learning-Roadmap-Generator/
│
├── app.py
├── requirements.txt
└── README.md
```

## Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/wardagull3/AI-Learning-Roadmap-Generator.git
```

### 2. Navigate to the project directory

```bash
cd AI-Learning-Roadmap-Generator
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure your Groq API key

Set your Groq API key as an environment variable.

**Windows PowerShell:**

```powershell
$env:GROQ_API_KEY="your_groq_api_key"
```

**Linux/macOS:**

```bash
export GROQ_API_KEY="your_groq_api_key"
```

Get your API key from [Groq Console](https://console.groq.com/).

### 5. Run the application

```bash
python app.py
```

Open the local Gradio URL displayed in your terminal.

## Future Improvements

- Daily and weekly study schedules.
- Progress tracking and roadmap management.
- Quizzes and practice assignments.
- Personalized project recommendations.
- Interactive AI learning assistant.
- Learning resource recommendations with verified links.

## Author

**Warda Gull**

GitHub: [@wardagull3](https://github.com/wardagull3)

---

*Built with Python, Groq, and Gradio.*

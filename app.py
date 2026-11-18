
import os
import gradio as gr
from groq import Groq

# Get Groq API key from environment
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY is not configured.")

client = Groq(api_key=GROQ_API_KEY)

MODEL = "openai/gpt-oss-20b"


def generate_roadmap(topic, skill_level, daily_hours, duration, learning_goal):

    if not topic.strip():
        return "Please enter a topic you want to learn."

    prompt = f"""
    Create a personalized learning roadmap.

    Learning topic: {topic}
    Current skill level: {skill_level}
    Daily study time: {daily_hours} hours
    Available duration: {duration}
    Learning goal: {learning_goal}

    Instructions:
    1. Start from the user's current skill level.
    2. Divide the roadmap into logical weeks or phases.
    3. Arrange topics in prerequisite order.
    4. Explain what the learner should study in each phase.
    5. Include practical coding exercises.
    6. Include at least one practical project.
    7. Suggest useful learning resources by name.
    8. Include clear weekly learning outcomes.
    9. Make the plan realistic for the available study time.
    10. Include revision and practice time.
    11. Avoid unrealistic promises.
    12. Do not invent resource URLs.

    Format the response using Markdown headings, tables, and bullet points.

    Include:
    - Roadmap overview
    - Prerequisites
    - Week-by-week plan
    - Practical projects
    - Recommended resources
    - Final learning outcomes
    """

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an experienced AI learning mentor. "
                        "Create realistic, structured and beginner-friendly "
                        "learning roadmaps."
                    )
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.4
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Something went wrong: {str(e)}"


with gr.Blocks(theme=gr.themes.Soft()) as demo:

    gr.Markdown(
        """
        # AI Learning Roadmap Generator

        ### Build your personalized learning journey with AI.

        Tell us what you want to learn, and get a structured roadmap.
        """
    )

    with gr.Row():

        with gr.Column():

            topic = gr.Textbox(
                label="What do you want to learn?",
                placeholder="e.g. Python, Machine Learning, Generative AI"
            )

            skill_level = gr.Dropdown(
                choices=[
                    "Complete Beginner",
                    "Beginner",
                    "Intermediate",
                    "Advanced"
                ],
                value="Complete Beginner",
                label="Your current skill level"
            )

            daily_hours = gr.Slider(
                minimum=1,
                maximum=10,
                value=2,
                step=1,
                label="Daily study hours"
            )

            duration = gr.Dropdown(
                choices=[
                    "1 month",
                    "2 months",
                    "3 months",
                    "6 months",
                    "12 months"
                ],
                value="3 months",
                label="Available learning duration"
            )

            learning_goal = gr.Textbox(
                label="What is your learning goal?",
                placeholder="e.g. Build real-world AI projects",
                lines=3
            )

            generate_button = gr.Button(
                "Generate My Roadmap",
                variant="primary"
            )

        with gr.Column():

            output = gr.Markdown(
                label="Your Personalized Roadmap"
            )

    generate_button.click(
        fn=generate_roadmap,
        inputs=[
            topic,
            skill_level,
            daily_hours,
            duration,
            learning_goal
        ],
        outputs=output
    )


if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",
        server_port=int(os.environ.get("PORT", 10000)),
        share=False
    )

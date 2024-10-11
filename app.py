from crewai import Agent, Task, Crew, Process
from crewai_tools import tool
from langchain_openai import ChatOpenAI
from crewai_tools.tools import FileReadTool
import os
import requests
import re
import mdpdf
import subprocess
from openai import OpenAI
from duckduckgo_search import DDGS

# LLM Configuration
llm = ChatOpenAI(
    openai_api_base="https://api.groq.com/openai/v1",  # https://api.openai.com/v1 or https://api.groq.com/openai/v1 
    openai_api_key=os.getenv("GROQ_API_KEY"),  # os.getenv("OPENAI_API_KEY") or os.getenv("GROQ_API_KEY")
    model_name="openai/gpt-4-turbo-preview"  # gpt-4-turbo-preview or mixtral-8x7b-32768 
)

# Tools
file_read_tool = FileReadTool(
    file_path='template.md',
    description='A tool to read the Story Template file and understand the expected output format.'
)

@tool
def web_search(query: str, num_results: int = 5) -> str:
    """
    Perform a web search using DuckDuckGo and return the results.

    Args:
        query (str): The search query.
        num_results (int): The number of results to return (default: 5).

    Returns:
        str: A string containing the search results, with each result on a new line.
    """
    with DDGS() as ddgs:
        results = list(ddgs.text(query, max_results=num_results))
    
    formatted_results = []
    for i, result in enumerate(results, 1):
        formatted_results.append(f"{i}. Title: {result['title']}\n   URL: {result['href']}\n   Snippet: {result['body']}\n")
    
    return "\n".join(formatted_results)

@tool
def generateimage(chapter_content_and_character_details: str) -> str:
    """
    Generates an image for a given chapter number, chapter content, detailed location details and character details.
    Using the OpenAI image generation API,
    saves it in the current folder, and returns the image path.
    """
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    response = client.images.generate(
        model="dall-e-3",
        prompt=f"Image is about: {chapter_content_and_character_details}. Style: Illustration. Create an illustration incorporating a vivid palette with an emphasis on shades of azure and emerald, augmented by splashes of gold for contrast and visual interest. The style should evoke the intricate detail and whimsy of early 20th-century storybook illustrations, blending realism with fantastical elements to create a sense of wonder and enchantment. The composition should be rich in texture, with a soft, luminous lighting that enhances the magical atmosphere. Attention to the interplay of light and shadow will add depth and dimensionality, inviting the viewer to delve into the scene. DON'T include ANY text in this image. DON'T include colour palettes in this image.",
        size="1024x1024",
        quality="standard",
        n=1,
    )
    image_url = response.data[0].url
    words = chapter_content_and_character_details.split()[:5] 
    safe_words = [re.sub(r'[^a-zA-Z0-9_]', '', word) for word in words]  
    filename = "_".join(safe_words).lower() + ".png"
    filepath = os.path.join(os.getcwd(), filename)

    # Download the image from the URL
    image_response = requests.get(image_url)
    if image_response.status_code == 200:
        with open(filepath, 'wb') as file:
            file.write(image_response.content)
    else:
        print("Failed to download the image.")
        return ""

    return filepath

@tool
def convermarkdowntopdf(markdownfile_name: str) -> str:
    """
    Converts a Markdown file to a PDF document using the mdpdf command line application.

    Args:
        markdownfile_name (str): Path to the input Markdown file.

    Returns:
        str: Path to the generated PDF file.
    """
    output_file = os.path.splitext(markdownfile_name)[0] + '.pdf'
    
    # Command to convert markdown to PDF using mdpdf
    cmd = ['mdpdf', '--output', output_file, markdownfile_name]
    
    # Execute the command
    subprocess.run(cmd, check=True)
    
    return output_file

# Agents
story_outliner = Agent(
    role='Story Outliner',
    goal='Develop an outline for a storybook about space ships, including chapter titles and characters for 5 chapters.',
    backstory="An imaginative creator who lays the foundation of captivating stories.",
    verbose=True,
    llm=llm,
    tools=[web_search],
    allow_delegation=False
)

story_writer = Agent(
  role='Story Writer',
  goal='Write the full content of the story for all 5 chapters, make each chapter 500 words, weaving together the narratives and characters outlined.',
  backstory="A talented storyteller who brings to life the world and characters outlined, crafting engaging and imaginative tales.",
  verbose=True,
  llm=llm,
  allow_delegation=False
)

story_editor = Agent(
  role='Story Editor',
  goal='Read through the content carefully, identifying areas that need improvement in terms of grammar, punctuation, spelling, syntax, and style. output a fully edited version that takes into account all your suggestions.',
  backstory="you will act as an AI copyeditor with a keen eye for detail and a deep understanding of language, style, and grammar. Your task is to refine and improve written content provided by users, offering advanced copyediting techniques and suggestions to enhance the overall quality of the text and make each chapter about 500 words",
  verbose=True,
  llm=llm,
  allow_delegation=False
)

image_generator = Agent(
  role='Image Generator',
  goal='Generate one image per chapter content provided by the story outliner. Start with Chapter number, chapter content, character details, detailed location information and detailed items in the location where the activity happens. Generate totally 5 images one by one. Final output should contain all the 5 images in json format.',
  backstory="A creative AI specialized in visual storytelling, bringing each chapter to life through imaginative imagery.",
  verbose=True,
  llm=llm,
  tools=[generateimage],
  allow_delegation=False
)

content_formatter = Agent(
    role='Content Formatter',
    goal='Format the written story content in markdown, including images at the beginning of each chapter.',
    backstory='A meticulous formatter who enhances the readability and presentation of the storybook.',
    verbose=True,
    llm=llm,
    tools=[file_read_tool],
    allow_delegation=False
)

markdown_to_pdf_creator = Agent(
    role='PDF Converter',
    goal='Convert the Markdown file to a PDF document. story.md is the markdown file name.',
    backstory='An efficient converter that transforms Markdown files into professionally formatted PDF documents.',
    verbose=True,
    llm=llm,
    tools=[convermarkdowntopdf],
    allow_delegation=False
)


# Create tasks for the agents
task_outline = Task(
    description='''Create an outline for the storybook about space ships, detailing chapter titles and character descriptions for 5 chapters. 
    Use the web_search tool to research interesting facts about space, spaceships, and space exploration to incorporate into your outline. 
    Focus on making the story both educational and engaging.''',
    agent=story_outliner,
    expected_output='A structured outline document containing 5 chapter titles, with detailed character descriptions and the main plot points for each chapter, incorporating interesting space-related facts.'
)

task_write = Task(
    description='Using the outline provided, write the full story content of about 500 words for each of five chapters, ensuring a cohesive and engaging narrative. Each Chapter 500 words. Include Title of the story at the top.',
    agent=story_writer,
    expected_output='A complete manuscript of the  storybook about space ships, with 5 chapters. Each chapter should contain approximately 500 words, following the provided outline and integrating the characters and plot points into a cohesive narrative.'
)

task_edit = Task(
    description='Using the full story provided, edit the full story content for all chapters, ensuring a cohesive and engaging narrative, with each Chapter about 500 words. Include Title of the story at the top.',
    agent=story_editor,
    expected_output='A complete manuscript of the storybook about space ships, with 5 chapters. Each chapter should contain approximately 500 words, following the provided outline and integrating the characters and plot points into a cohesive narrative.'
)

task_image_generate = Task(
    description='Generate 5 images that captures the essence of the storybook about space ships,, aligning with the themes, characters, and narrative outlined for the chapters. Do it one by one.',
    agent=image_generator,
    expected_output='A digital image file that visually represents the overarching theme of the storybook, incorporating elements from the characters and plot as described in the outline. The image should be suitable for inclusion in the storybook as an illustration.',
)

task_format_content = Task(
    description='Format the story content in markdown, including an image at the beginning of each chapter.',
    agent=content_formatter,
    expected_output='The entire storybook content formatted in markdown, with each chapter title followed by the corresponding image and the chapter content of about 500 words.',
    context=[task_write, task_image_generate],
    output_file="story.md"
)

task_markdown_to_pdf = Task(
    description='Convert a Markdown file to a PDF document, ensuring the preservation of formatting, structure, and embedded images using the mdpdf library.',
    agent=markdown_to_pdf_creator,
    expected_output='A PDF file generated from the Markdown input, accurately reflecting the content with proper formatting. The PDF should be ready for sharing or printing.'
)

crew = Crew(
  agents=[story_outliner, story_writer, story_editor , image_generator, content_formatter, markdown_to_pdf_creator],
  tasks=[task_outline, task_write, task_edit, task_image_generate, task_format_content, task_markdown_to_pdf],
  verbose=True,
  process=Process.sequential
)

result = crew.kickoff()

print(result)
# 📖 Multi-Lingual Story Generator using Llama 3.3,LangChain & Groq

A web-based **Multilingual Story Generator** built using **Python, Streamlit, LangChain, and Groq API** that generates creative and engaging stories in multiple languages based on user-selected preferences.

** Users can customize the language, tone, genre, creativity level, target audience, time period, grammar level, story length, and character names to generate personalized stories.

## 🚀 Live Demo

🔗 **Live Application:**  
https://multilingualstorygeneratorusingllama-groq.streamlit.app/

## 📌 Project Overview

The **Multilingual Story Generator** is an AI-powered application designed to generate original and engaging stories according to the user's requirements.

** The application provides an interactive sidebar where users can specify different story parameters such as:

- Language
- Tone
- Story Idea
- Number of Paragraphs
- Grammar Level
- Story Category
- Character Names
- Time Period
- Creativity Level
- Target Audience

After selecting the required options, the application constructs a customized prompt using **LangChain PromptTemplate** and sends it to an AI language model through the **Groq API**.

The AI model processes the prompt and generates a personalized story based on the user's selected preferences.

The application supports multiple languages, making it useful for users who want to create stories in their preferred language.

# ✨ Features

## 🌐 Multilingual Story Generation

Generate stories in multiple languages, including:

- English
- Telugu
- Hindi
- Tamil
- Urdu
- Kannada
- Chinese

## 🎭 Multiple Story Tones

Users can select the desired storytelling tone:

- Friendly
- Narrative
- Poetic

## 📚 Multiple Story Categories

The application supports different story genres:

- Thriller
- Horror
- Suspense
- Adventure
- Comedy
- Family
- Drama
- Fantasy

## 👥 Target Audience

Stories can be customized for:

- Toddlers
- Kids
- Adults
- Old People

## 🕰️ Time Period Selection

Users can select:

- Ancient
- Modern
- Future

## 🎨 Creativity Control

Users can choose:

- Low
- Medium
- High

## 📝 Grammar Level

The generated story can be tailored to:

- Beginner
- Intermediate
- Professional

## 👤 Character Customization

Users can provide their own character names to personalize the story.

## 📏 Story Length

Users can select the required number of paragraphs for the generated story.

## ⚡ AI-Powered Generation

The application uses a Groq-hosted AI model through LangChain to generate stories quickly and efficiently.

## 🔤 Language-Specific Output

The application instructs the AI model to generate the complete story in the selected language, even when the user's story idea is entered in English.

# 🏗️ System Architecture

```text
                 ┌──────────────────────┐
                 │        User          │
                 │  Story Preferences   │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │      Streamlit       │
                 │    Web Interface     │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │      LangChain       │
                 │   PromptTemplate     │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │       Groq API       │
                 │    GPT-OSS-20B       │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │   Generated Story    │
                 │  In Selected Language│
                 └──────────────────────┘
```

## 🔄 How the Application Works
# Step 1: User Input

The user provides a story idea and selects their preferred options from the sidebar.

# Step 2: Prompt Construction

The selected inputs are combined using a LangChain PromptTemplate.

# Step 3: AI Processing

The generated prompt is sent to the Groq API using the LangChain-Groq integration.

# Step 4: Story Generation

The AI model processes the prompt and generates a story based on the selected requirements.

# Step 5: Output

The generated story is displayed directly in the Streamlit application.

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/YourUsername/Multi-Lingual-Story-Generator-Generative-AI-.git
```

### Navigate to the Project Folder

```bash
cd Multi-Lingual-Story-Generator-Generative-AI-
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Create a `.env` File

```env
GROQ_API_KEY=your_groq_api_key
```

### Run the Application

```bash
streamlit run pythonfile.py
```

## 🎮 How to Use

1. Select your preferred language.
2. Choose the story tone.
3. Enter a story idea in English.
4. Select story category.
5. Enter character names.
6. Choose creativity level.
7. Select the target audience.
8. Click **Generate Story**.
9. Read the AI-generated story in the selected language.

## 🌐 Supported Languages

- English
- Telugu
- Hindi
- Tamil
- Urdu
- Kannada
- Chinese

## 🔮 Future Enhancements

- 📄 Download stories as PDF
- 📥 Export stories as TXT
- 🎤 Text-to-Speech support
- 🖼️ AI-generated story illustrations
- 📚 Story history
- 🌙 Dark mode
- 🎙️ Voice input support

## 💡 Learning Outcomes

This project demonstrates practical knowledge of:

- Generative AI
- Large Language Models (LLMs)
- Prompt Engineering
- LangChain
- Groq API Integration
- Streamlit Web Application Development
- Environment Variable Management
- Git & GitHub
- Streamlit Cloud Deployment

## 👨‍💻 Developer

**A Navaneetha**

GitHub: https://github.com/A-Navaneetha

LinkedIn: https://www.linkedin.com/in/anavaneetha/

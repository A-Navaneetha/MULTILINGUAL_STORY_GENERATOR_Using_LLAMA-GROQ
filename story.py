import os
import streamlit as st
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.prompts import PromptTemplate

# -------------------- Load Environment --------------------

load_dotenv()

# -------------------- Page Configuration --------------------

st.set_page_config(
    page_title="Multi Lingual Story Generator",
    page_icon="📖",
    layout="wide"
)

st.title("📖 Multi Lingual Story Generator")
st.markdown(
    "Generate creative stories in multiple languages using **Llama 3.3-70B** powered by **Groq**."
)

# -------------------- Load API Key --------------------

import os
from dotenv import load_dotenv

load_dotenv()

try:
    # Streamlit Cloud
    api_key = st.secrets["GROQ_API_KEY"]
except Exception:
    # Local .env
    api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    st.error("Groq API Key not found.")
    st.stop()

# -------------------- Initialize Model --------------------

if "model" not in st.session_state:
    st.session_state["model"] = init_chat_model(
        model="llama-3.3-70b-versatile",
        model_provider="groq",
        api_key=api_key,
    )

# -------------------- Prompt Template --------------------

if "template" not in st.session_state:
    st.session_state["template"] = PromptTemplate(
        input_variables=[
            "language",
            "tone",
            "storyIdea",
            "length",
            "grammar",
            "plagarism",
            "catagories",
            "character_names",
            "time_period",
            "creativity",
            "audience",
        ],
        template="""
You are a professional story writer.

Write a creative and engaging story.

Target Audience: {audience}

Language: {language}

Tone: {tone}

Category: {catagories}

Story Idea:
{storyIdea}

Characters:
{character_names}

Time Period:
{time_period}

Creativity Level:
{creativity}

Grammar Level:
{grammar}

Originality:
{plagarism}

Length:
{length} paragraphs

Instructions:
- Write the complete story in {language}.
- Even if the user enters the idea in English, generate the output only in {language}.
- Avoid emojis.
- Make the story interesting and meaningful.
"""
    )

# -------------------- Sidebar --------------------

st.sidebar.header("Story Settings")

language = st.sidebar.selectbox(
    "Language",
    [
        "English",
        "Telugu",
        "Hindi",
        "Tamil",
        "Urdu",
        "Kannada",
        "Chinese",
    ],
)

tone = st.sidebar.selectbox(
    "Tone",
    [
        "Friendly",
        "Narrative",
        "Poet",
    ],
)

storyIdea = st.sidebar.text_area("Story Idea")

length = st.sidebar.slider(
    "Number of Paragraphs",
    1,
    10,
    3,
)

grammar = st.sidebar.selectbox(
    "Grammar Level",
    [
        "Beginner",
        "Intermediate",
        "Professional",
    ],
)

plagarism = st.sidebar.slider(
    "Originality (%)",
    0,
    100,
    100,
)

categories = st.sidebar.radio(
    "Story Category",
    [
        "Thriller",
        "Horror",
        "Suspense",
        "Adventure",
        "Comedy",
        "Family",
        "Drama",
        "Fantasy",
    ]
)

characterNames = st.sidebar.text_area("Character Names")

timePeriod = st.sidebar.selectbox(
    "Time Period",
    [
        "Ancient",
        "Modern",
        "Future",
    ],
)

creativity = st.sidebar.select_slider(
    "Creativity Level",
    options=[
        "Low",
        "Medium",
        "High",
    ],
)

audience = st.sidebar.selectbox(
    "Target Audience",
    [
        "Toddlers",
        "Kids",
        "Adults",
        "Old People",
    ],
)

submit_button = st.sidebar.button(
    "Generate Story",
    type="primary",
    use_container_width=True,
)

# -------------------- Generate Story --------------------

if submit_button:

    if storyIdea.strip() == "":
        st.warning("Please enter a story idea.")

    else:

        final_prompt = st.session_state["template"].format(
            language=language,
            tone=tone,
            storyIdea=storyIdea,
            length=length,
            grammar=grammar,
            plagarism=plagarism,
            catagories=categories,
            character_names=characterNames,
            time_period=timePeriod,
            creativity=creativity,
            audience=audience,
        )

        with st.spinner("Generating your story..."):
            response = st.session_state["model"].invoke(final_prompt)

        st.success("Story Generated Successfully!")

        st.subheader("📚 Generated Story")

        st.write(response.content)
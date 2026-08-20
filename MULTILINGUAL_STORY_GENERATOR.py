import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

# ---------------------------------------------------
# Page Configuration
# ---------------------------------------------------

st.set_page_config(
    page_title="Multilingual Story Generator",
    page_icon="📖",
    layout="wide"
)
# ---------------------------------------------------
# Initialize Groq Model
# ---------------------------------------------------

if "model" not in st.session_state:
    st.session_state["model"] = ChatGroq(
        model="openai/gpt-oss-20b",
        temperature=0.7,
        api_key=st.secrets["GROQ_API_KEY"]
    )


# ---------------------------------------------------
# Prompt Template
# ---------------------------------------------------

if "template" not in st.session_state:

    st.session_state["template"] = PromptTemplate(
        input_variables=[
            "language",
            "tone",
            "storyIdea",
            "length",
            "grammar",
            "plagarism",
            "categories",
            "character_names",
            "time_period",
            "creativity",
            "audience"
        ],

        template="""
You are a professional and creative story writer.

Write a fantastic and engaging story for the target audience:
{audience}

IMPORTANT LANGUAGE REQUIREMENT:
Write the entire story ONLY in {language}.
Even if the user's input is written in English, the generated story
must be written completely in {language}.

Tone:
{tone}

Creativity level:
{creativity}

Time period:
{time_period}

Grammar level:
{grammar}

Originality requirement:
Create an original story and avoid copying existing stories.

Story length:
Write approximately {length} paragraphs.

Story idea:
{storyIdea}

Category:
{categories}

Character names:
{character_names}

Additional instructions:
- Make the story engaging and coherent.
- Give the story a suitable title.
- Maintain consistency between characters and events.
- Do not use emojis.
- Do not explain your writing process.
- Output only the story.
"""
    )


# ---------------------------------------------------
# Sidebar
# ---------------------------------------------------

st.sidebar.title("📖 Story Settings")


language = st.sidebar.pills(
    "Enter Language",
    [
        "English",
        "Telugu",
        "Hindi",
        "Tamil",
        "Urdu",
        "Kannada",
        "Chinese"
    ]
)

tone = st.sidebar.segmented_control(
    "Select Tone",
    [
        "Friendly",
        "Narrative",
        "Poetic"
    ]
)

storyIdea = st.sidebar.text_area(
    "Tell me about your story idea"
)

length = st.sidebar.slider(
    "Number of Paragraphs",
    1,
    10,
    3
)

grammar = st.sidebar.selectbox(
    "Specify Grammar Level",
    [
        "Beginner",
        "Intermediate",
        "Professional"
    ]
)

plagarism = st.sidebar.slider(
    "Originality Level",
    0,
    100,
    100
)

categories = st.sidebar.radio(
    "Specify Category",
    [
        "Thriller",
        "Horror",
        "Suspense",
        "Adventure",
        "Comedy",
        "Family",
        "Drama",
        "Fantasy"
    ],
    horizontal=True
)

characterNames = st.sidebar.text_area(
    "Specify Character Names"
)

timePeriod = st.sidebar.segmented_control(
    "Specify Time Period",
    [
        "Ancient",
        "Modern",
        "Future"
    ]
)

creativity = st.sidebar.pills(
    "Specify Creativity",
    [
        "Low",
        "Medium",
        "High"
    ]
)

audience = st.sidebar.segmented_control(
    "Target Audience",
    [
        "Toddlers",
        "Kids",
        "Adults",
        "Old People"
    ]
)


submit_button = st.sidebar.button(
    "Generate Story",
    width="stretch",
    type="primary"
)


# ---------------------------------------------------
# Main Application
# ---------------------------------------------------

st.title("📖 Multilingual Story Generator")

st.write(
    "Create original stories in multiple languages "
    "with customizable tone, genre, creativity and audience."
)


if submit_button:

    if not language:
        st.warning("Please select a language.")

    elif not tone:
        st.warning("Please select a tone.")

    elif not storyIdea.strip():
        st.warning("Please enter a story idea.")

    elif not timePeriod:
        st.warning("Please select a time period.")

    elif not creativity:
        st.warning("Please select a creativity level.")

    elif not audience:
        st.warning("Please select a target audience.")

    else:

        try:

            # Create final prompt
            final_prompt = st.session_state["template"].format(
                language=language,
                tone=tone,
                storyIdea=storyIdea,
                length=length,
                grammar=grammar,
                plagarism=plagarism,
                categories=categories,
                character_names=characterNames,
                time_period=timePeriod,
                creativity=creativity,
                audience=audience
            )

            # Generate story
            with st.spinner("Writing your story..."):

                response = st.session_state["model"].invoke(
                    final_prompt
                )

            # Display story
            st.subheader("Your Story")

            st.write(response.content)

        except Exception as e:

            st.error(
                "Unable to generate the story."
            )

            st.exception(e)

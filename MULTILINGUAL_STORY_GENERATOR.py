import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

if "model" not in st.session_state:
    st.session_state["model"] = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0.7,
        api_key=st.secrets["GROQ_API_KEY"]
    )

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
            "audience"
        ],
        template="""
Act like a professional story writer who writes fantastic stories
that target an audience of {audience}.

Write the story in {language}.
Every word in the output must be in {language}, even though the input
may be given in English.

Follow the specified tone of {tone}.
The creativity level is {creativity}.
The time period is {time_period}.
The grammar level should be {grammar}.
Maintain the given {plagarism} level.
Avoid emojis.

The length of the story should be {length} paragraphs.

The story should be about {storyIdea}.
The category of the story is {catagories}.

The story contains the following character names:
{character_names}
"""
    )

language = st.sidebar.pills(
    "Enter Language",
    ["English", "Telugu", "Hindi", "Tamil", "Urdu", "Kannada", "Chinese"]
)

tone = st.sidebar.segmented_control(
    "Select Tone",
    ["Friendly", "Narrative", "Poet"]
)

storyIdea = st.sidebar.text_area("Tell me about your story idea")

length = st.sidebar.slider(
    "Enter Number Of Paragraphs",
    1,
    10
)

grammar = st.sidebar.selectbox(
    "Specify Grammar",
    ["beginner", "intermediate", "professional"]
)

plagarism = st.sidebar.slider(
    "Specify Plagiarism",
    0,
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
    ["Ancient", "Modern", "Future"]
)

creativity = st.sidebar.pills(
    "Specify Creativity",
    ["Low", "Medium", "High"]
)

audience = st.sidebar.segmented_control(
    "Enter Targeted Audience",
    ["Toddlers", "Kids", "Adults", "OldPeople"]
)

submit_button = st.sidebar.button(
    "Submit",
    width="stretch",
    type="primary"
)

if submit_button:

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
        audience=audience
    )

    response = st.session_state["model"].invoke(final_prompt)

    st.write(response.content)

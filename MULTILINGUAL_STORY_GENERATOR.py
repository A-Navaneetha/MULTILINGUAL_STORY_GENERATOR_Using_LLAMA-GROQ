import streamlit as st
from langchain.chat_models import init_chat_model
from langchain_core.prompts import PromptTemplate
#session state
if "model" not in st.session_state:
    st.session_state["model"]=init_chat_model(model="llama3.1:latest",model_provider="ollama") #place your gorq api key
if "template" not in st.session_state:
    st.session_state["template"]=PromptTemplate(
    input_variables=["language","tone","storyIdea","length","grammar","plagarism","catagories","character_names","time_period","creativity","audience"],
    template="Act like a professional story writer, who writes fantastic stories that target auidence of {audience}. write story in langaugage {language}, even the words ypur output must be in {language},even though the input given to you is in English. and follow the specifi tone of {tone}. Be creativity andengaging where the creativity level is {creativity}. the time period of the story is {time_period}.Grammar level should be in {grammar}. maintain the given {plagarism} level. Avoid emojis. The length of the story should be {length}. the story should be on {storyIdea} and the category of the story is{catagories}. The story contains the following character names {character_names}"
)
language=st.sidebar.pills("EnterLanguage",["English","Telugu","Hindi","Tamil","Urdu","Kannada","Chinese"])
tone=st.sidebar.segmented_control("Select Tone",["Friendly","Narrative","Poet"])
storyIdea=st.sidebar.text_area("Tell me about your story idea")
length=st.sidebar.slider("Enter Number Of Paragraphs",1,10)
grammar=st.sidebar.selectbox("Specify grammar",["beginner","intermediate","professional"])
plagarism=st.sidebar.slider("Specify Plagrism",0,100)
categories=st.sidebar.radio("SpecifyCategory",["Thriller","Horror","Suspense","Adventure","Comedy","Family","Drama","Fantasy"],horizontal=True)
characterNames=st.sidebar.text_area("Specify Character Names")
timePeriod=st.sidebar.segmented_control("Specify Time Period",["Ancient","Modern","Future"])
creativity=st.sidebar.pills("Specify Creativity",["Low", "Medium","High"])
audience=st.sidebar.segmented_control("Enter Targetd Audience",["Toddlers","Kids","Adults","OldPeople"])
submit_button=st.sidebar.button("Submit",width="stretch",type="primary")
if submit_button:
    final_prompt=st.session_state["template"].format(
language=language,
tone=tone,
storyIdea=storyIdea,
length=length,
grammar=grammar,
plagarism=plagarism,
catagories= categories,
character_names=characterNames,
time_period=timePeriod,
creativity=creativity,
audience=audience
)
    response=st.session_state["model"].invoke(final_prompt)
    st.write(response.content)
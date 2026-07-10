import streamlit as st

# Import components
from components.header import load_css
from components.sidebar import sidebar

from components.hero import hero
from components.stats import stats
from components.features import features
from components.tech_stack import tech_stack
from components.architecture import architecture
from components.footer import footer


# FIRST Streamlit command
st.set_page_config(
    page_title="HealthAgents AI",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Everything else AFTER page_config
load_css()

sidebar()

hero()

stats()

features()

tech_stack()

architecture()

footer()
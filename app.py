import streamlit as st
import random
from main import NewsletterGenerator
import os
from dotenv import load_dotenv
import asyncio
from asyncio import get_event_loop
import nest_asyncio

# Apply nest_asyncio to allow nested event loops
nest_asyncio.apply()

# Load environment variables
load_dotenv()

# Set page config
st.set_page_config(
    page_title="AI Newsletter Generator",
    page_icon="\U0001F4F0",  # newspaper emoji
    layout="wide"
)

# Custom CSS
st.markdown(
    """
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
    }
    .newsletter-content {
        background-color: #f8f9fa;
        padding: 2rem;
        border-radius: 10px;
        margin-top: 2rem;
    }
    .topic-input {
        margin-bottom: 2rem;
    }
    """,
    unsafe_allow_html=True
)

# Title and description
st.title("\U0001F4F0 AI Newsletter Generator with Firecrawl \U0001F525")
st.markdown(
    """
    Generate professional newsletters on any topic using Nebius AI, Agno, and Firecrawl.
    """
)

# Example topics
example_topics = [
    "What happened in the world of AI this week?",
    "What are the latest trends in AI?",
    "Tell the Recent Model Releases",
    "Recap of Google I/O 2025",
]

# Sidebar for API keys and example topics
with st.sidebar:
    st.header("\U0001F511 API Keys")
    firecrawl_api_key = st.text_input(
        "Firecrawl API Key",
        value=os.getenv("FIRECRAWL_API_KEY", ""),
        type="password",
        help="Get your API key from https://firecrawl.dev"
    )
    nebius_api_key = st.text_input(
        "Nebius API Key",
        value=os.getenv("NEBIUS_API_KEY", ""),
        type="password",
        help="Your Nebius API key"
    )

    # Update environment variables from user input
    if firecrawl_api_key:
        os.environ["FIRECRAWL_API_KEY"] = firecrawl_api_key
    if nebius_api_key:
        os.environ["NEBIUS_API_KEY"] = nebius_api_key

    st.markdown("---")
    st.markdown("### \U0001F4DA Example Topics")
    for topic_example in example_topics:
        if st.button(topic_example, key=topic_example):
            st.session_state.topic = topic_example

# Main content: input fields
topic = st.text_input(
    "What would you like to generate a newsletter about?",
    value=st.session_state.get("topic", ""),
    placeholder="Enter a topic or select from examples",
    key="topic_input",
)

col1, col2 = st.columns(2)
with col1:
    search_limit = st.number_input(
        "Number of Articles",
        min_value=1,
        max_value=10,
        value=5,
        help="Maximum number of articles to search and analyze",
    )
with col2:
    time_range = st.selectbox(
        "Time Range",
        options=[
            ("Past hour", "qdr:h"),
            ("Past 24 hours", "qdr:d"),
            ("Past week", "qdr:w"),
            ("Past month", "qdr:m"),
            ("Past year", "qdr:y"),
        ],
        format_func=lambda x: x[0],
        index=2,
        help="Time range for article search",
    )

# Function to generate newsletter
def generate_newsletter():
    if not topic:
        st.error("Please enter a topic or select one from the examples.")
        return
    elif not firecrawl_api_key or not nebius_api_key:
        st.error("Please provide both API keys in the sidebar.")
        return

    with st.spinner("Generating your newsletter..."):
        try:
            # Format topic for file name
            url_safe_topic = topic.lower().replace(" ", "-")
            
            # Generate the newsletter
            response = NewsletterGenerator(
                topic=topic,
                search_limit=search_limit,
                time_range=time_range[1],
            )
            
            st.markdown("### \U0001F4DD Generated Newsletter")
            st.markdown(response.content)

            st.download_button(
                label="\U0001F4E5 Download Newsletter",
                data=response.content,
                file_name=f"newsletter-{url_safe_topic}.md",
                mime="text/markdown",
            )
        except Exception as e:
            st.error(f"An error occurred while generating the newsletter: {str(e)}")

# Footer and generate button
st.markdown("---")
st.markdown(
    """
    Built with ❤️ using Streamlit and Nebius AI
    """,
    unsafe_allow_html=True,
)

if st.button("Generate Newsletter", type="primary"):
    generate_newsletter()

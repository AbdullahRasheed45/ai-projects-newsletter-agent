# AI Newsletter Generator

This project is an AI‑powered newsletter generator that leverages Nebius AI's Llama‑3 models, Agno’s agents framework, and Firecrawl search tools to research and compose professional newsletters on any topic. It offers a modern Streamlit interface for customizing search parameters and generating markdown newsletters.

## Features

- **Real‑time research via Firecrawl:** automatically searches recent articles and authoritative sources and extracts content.
- **Nebius‑powered content generation:** uses Nebius Llama‑3 models for high‑quality summaries and insights.
- **Template‑driven newsletter structure:** organizes results into a subject line, welcome note, main story, featured content, quick updates, highlights and sources.
- **Customizable search parameters:** adjust the number of articles and time range (past hour, day, week, month or year).
- **Secure API keys:** accepts Firecrawl and Nebius API keys via `.env` file or the Streamlit sidebar; environment variables are loaded with `python‑dotenv`.
- **Downloadable output:** download the generated newsletter in Markdown format directly from the UI.

## Tech stack

- **Python 3.10+** with `Streamlit` for the UI, `Agno` for agent orchestration, Nebius for LLMs, Firecrawl for web search and `sqlite` storage.
- **Agno Agents:** orchestrates tools and LLM for research and summarization.

## Prerequisites

- Nebius AI API key and Firecrawl API key. Set them in a `.env` file at the project root:
  ```
  FIRECRAWL_API_KEY=your_firecrawl_api_key
  NEBIUS_API_KEY=your_nebius_api_key
  ```
- Python 3.10 or later.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/AbdullahRasheed45/ai-projects-newsletter-agent.git
   cd ai-projects-newsletter-agent
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## Usage

- Open the Streamlit UI; enter your Nebius and Firecrawl API keys in the sidebar.
- Input a topic or select an example topic.
- Choose the number of articles and time range.
- Click **Generate Newsletter** to produce a Markdown newsletter.
- Download the newsletter using the **Download** button.

## Deployment

The app can be deployed easily on platforms like Hugging Face Spaces (using the Streamlit SDK). Ensure to set the necessary secrets (`FIRECRAWL_API_KEY` and `NEBIUS_API_KEY`) in the environment.

## License

This project is released under the MIT License.

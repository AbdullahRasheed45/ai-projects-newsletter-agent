# 📰 AI Newsletter Generator (Agno + Nebius + Firecrawl + Streamlit)

An intelligent newsletter generation system that autonomously researches the latest articles on any topic and composes professional, publication-ready newsletters. Powered by Firecrawl for real-time web crawling, Nebius Llama-3 models for content synthesis, Agno for smart agent orchestration, and an intuitive Streamlit interface for seamless operation.

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Firecrawl](https://img.shields.io/badge/Firecrawl-Web_Crawler-orange?style=for-the-badge)](https://firecrawl.dev/)
[![Nebius](https://img.shields.io/badge/Nebius-AI_Models-blue?style=for-the-badge)](https://nebius.ai/)

✨ **Features**

🕷️ **Smart Web Research**: Automated article discovery using Firecrawl with configurable time ranges (hour/day/week/month/year) and result counts

🧠 **AI-Powered Content Synthesis**: Advanced content summarization and deduplication using Nebius Llama-3 models for coherent newsletter creation  

📋 **Professional Newsletter Structure**: Template-driven format with subject line, intro, main story, featured items, quick updates, highlights, and sources

🎛️ **Intuitive Streamlit Interface**: Clean UI with sidebar controls for API keys, topic input, time range selection, and article count configuration

📥 **One-Click Export**: Instant download of polished Markdown newsletters ready for distribution or publishing

🔄 **Intelligent Agent Orchestration**: Agno framework manages complex workflow coordination between web crawling, content analysis, and synthesis

🗂️ **Project structure**
```
.
├─ app.py            # Streamlit application & user interface
├─ main.py           # Core agent orchestration & newsletter generation logic  
├─ .env.example      # Environment variable template for API keys
├─ requirements.txt  # Python dependencies and package versions
└─ README.md         # Comprehensive project documentation
```

🚀 **Quickstart**

**Prerequisites**
- Python 3.10 or higher
- API keys:
  - **NEBIUS_API_KEY** (Nebius AI platform)
  - **FIRECRAWL_API_KEY** (Firecrawl web crawling service)

**1) Clone & install**
```bash
git clone https://github.com/AbdullahRasheed45/ai-projects-newsletter-agent.git
cd ai-projects-newsletter-agent

# Create virtual environment
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

**2) Configure environment**
```bash
# Copy environment template
cp .env.example .env

# Edit .env with your API keys:
NEBIUS_API_KEY=your_nebius_api_key_here
FIRECRAWL_API_KEY=your_firecrawl_api_key_here
```

*Alternative: You can also enter API keys directly in the Streamlit sidebar interface*

**3) Run the application**
```bash
streamlit run app.py
```

🎯 **Usage**: Open your browser to the Streamlit interface, enter your newsletter topic, configure time range and article count, click "Generate Newsletter", then download your polished Markdown newsletter!

🧠 **How it works (architecture)**

**1. Query Planning (Agno Agent)**: Analyzes your topic and settings to formulate optimized search queries for comprehensive content discovery

**2. Content Acquisition (Firecrawl)**: Executes intelligent web crawling to retrieve fresh articles and snippets from authoritative sources across the web

**3. AI Synthesis (Nebius Llama-3)**: Processes raw content through advanced language models to summarize, deduplicate, and organize information according to newsletter template structure

**4. Rendering & Export (Streamlit)**: Displays newsletter preview in the interface and enables instant Markdown download for distribution

⚙️ **Configuration options**

**Model Selection**:
```python
# Switch between Nebius Llama-3 variants
MODELS = {
    'fast': 'llama-3-8b-instruct',      # Quick generation
    'balanced': 'llama-3-70b-instruct', # Quality/speed balance  
    'premium': 'llama-3-405b-instruct'  # Maximum quality
}
```

**Newsletter Template Customization**:
- **Section Headers**: Modify headings and organization structure
- **Content Verbosity**: Adjust summary length and detail level  
- **Citation Style**: Toggle between inline citations and source lists
- **Tone & Voice**: Configure formal, conversational, or technical writing styles

**Search Parameters**:
- **Time Windows**: hour, day, week, month, year presets
- **Result Depth**: Configure number of articles to analyze (5-50+ sources)
- **Source Filtering**: Domain allow/deny lists for content curation
- **Language Targeting**: Multi-language content discovery options

**Performance Tuning**:
- **Rate Limiting**: Automatic backoff and retry logic for API calls
- **Content Caching**: Reduce redundant crawling for similar queries  
- **Token Management**: Context window optimization for large article sets

🧪 **Example newsletter topics**

**Technology & AI**:
- *"AI agents in production – latest case studies (last 2 weeks)"*
- *"State of web performance optimization in 2025 (top 12 sources)"*
- *"Recent breakthroughs in large language model efficiency"*

**Business & Industry**:
- *"Fintech startup funding trends this quarter"* 
- *"Remote work productivity tools gaining traction"*
- *"Sustainable supply chain innovations (past month)"*

**Regulatory & Policy**:
- *"What changed in the EU AI Act this month?"*
- *"New data privacy regulations affecting SaaS companies"*
- *"Climate policy updates from COP29 summit"*

**Research & Academia**:
- *"Latest quantum computing research papers (last 30 days)"*
- *"Medical AI ethics discussions in top journals"*
- *"Renewable energy breakthrough studies this year"*

📝 **Newsletter output format**

**Professional Structure**:
```markdown
# [Dynamic Subject Line]

## Welcome
*Engaging 2-4 sentence introduction contextualizing the topic and timeframe*

## 🎯 Main Story  
*Comprehensive brief with 2-3 key insights from top sources*

## ⭐ Featured Items
- **Item 1**: *Concise 1-2 line summary with key takeaway*
- **Item 2**: *Important development or trend highlight*  
- **Item 3**: *Notable announcement or research finding*
- **Item 4**: *Emerging opportunity or challenge*

## ⚡ Quick Updates
• *Bulleted list of rapid-fire industry updates*
• *Brief mentions of secondary but relevant news*
• *Quick stats, launches, or announcements*

## 💡 Key Highlights  
> *"Notable quotes from industry leaders"*
> *Significant statistics and data points*  
> *Major product launches or company announcements*

## 📚 Sources
*Automatically generated linked list of all referenced articles*
```

**Content Quality Features**:
- **Deduplication**: Eliminates repetitive information across sources
- **Fact Verification**: Cross-references claims across multiple articles
- **Relevance Scoring**: Prioritizes most important developments
- **Context Integration**: Connects related stories and trends

🔒 **Security & best practices**

**API Key Management**:
- Store sensitive keys in `.env` file - never commit to version control
- Use environment-specific keys for development vs. production
- Implement key rotation practices for enhanced security
- Monitor API usage and set appropriate quotas

**Content Curation**:
- Implement domain filtering for trusted news sources only
- Add content moderation for inappropriate or biased material  
- Verify source authenticity and publication dates
- Consider fact-checking integration for sensitive topics

**Team Collaboration**:
- Cache frequently requested content to reduce API costs
- Implement user authentication for multi-user deployments
- Add newsletter versioning and revision history
- Set up automated quality checks and content review workflows

🐛 **Troubleshooting**

**Authentication & API Issues**:
- **"API Key Missing"** → Verify `NEBIUS_API_KEY` and `FIRECRAWL_API_KEY` are set in `.env` or Streamlit sidebar
- **"Rate Limit Exceeded"** → Reduce article count or implement longer delays between requests
- **"Invalid API Response"** → Check API key permissions and account status/billing

**Content Quality Problems**:  
- **Empty/Irrelevant Results** → Broaden time range (try "week" instead of "day") or increase article count
- **Repetitive Content** → Adjust deduplication settings or refine topic specificity
- **Low-Quality Sources** → Implement domain filtering or switch to premium news APIs

**Performance & Technical**:
- **Token/Latency Issues** → Switch to faster Nebius model or reduce per-article context length  
- **Memory Errors** → Process articles in smaller batches or increase system resources
- **UI Responsiveness** → Clear Streamlit cache or restart the application

**Content Generation**:
- **Poor Newsletter Structure** → Adjust template prompts or switch to higher-capability model
- **Missing Key Information** → Increase search depth or broaden query terms
- **Inconsistent Formatting** → Review Markdown template and ensure proper syntax

☁️ **Deployment options**

**Cloud Platforms**:
- **Hugging Face Spaces**: Perfect for public demos and sharing
- **Streamlit Cloud**: Native hosting with GitHub integration  
- **Railway/Render**: Production-ready with custom domains
- **AWS/GCP/Azure**: Enterprise deployment with scalability

**Environment Setup**:
```bash
# Production environment variables
NEBIUS_API_KEY=production_nebius_key
FIRECRAWL_API_KEY=production_firecrawl_key
STREAMLIT_THEME=light
NEWSLETTER_CACHE_TTL=3600
MAX_ARTICLES_PER_QUERY=25
```

**Docker Deployment**:
```dockerfile
FROM python:3.10-slim
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "app.py"]
```

**Production Considerations**:
- Configure SSL certificates for secure API communication
- Set up monitoring and logging for usage analytics
- Implement automated newsletter scheduling and distribution
- Add database integration for newsletter history and user preferences

📈 **Advanced features**

**Multi-Topic Analysis**:
```python
# Generate comparative newsletters
topics = [
    "AI safety regulations",
    "Machine learning interpretability", 
    "Neural network optimization"
]
comparative_newsletter = generate_multi_topic_analysis(topics)
```

**Custom Templates**:
```python
# Industry-specific newsletter formats
templates = {
    'tech_startup': TechStartupTemplate(),
    'academic_research': AcademicTemplate(), 
    'executive_brief': ExecutiveSummaryTemplate(),
    'investor_update': InvestorTemplate()
}
```

**Automated Distribution**:
```python
# Schedule and distribute newsletters
scheduler.add_job(
    generate_and_send_newsletter,
    trigger='cron',
    day_of_week='mon',
    hour=8,
    args=['AI Industry Weekly']
)
```

📜 **License**

MIT License - see [LICENSE](LICENSE) file for complete terms and conditions.

---

*Built with ❤️ using Python, Streamlit, and cutting-edge AI technologies. Transform information overload into actionable insights with intelligent newsletter generation.*

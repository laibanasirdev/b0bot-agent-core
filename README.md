

```markdown
# B0Bot Agent Core v0.1.0 🤖

An advanced, asynchronous multi-agent research system built with **FastAPI**, **LangGraph**, and **Tavily AI**. B0Bot is designed to demonstrate modern "Agentic Workflows" where AI manages state, researches the live web, and synthesizes findings into structured reports.

## 🏛️ Architecture & Design Philosophy
B0Bot moves beyond simple linear scripts. It utilizes a **Directed Acyclic Graph (DAG)** to orchestrate a reasoning loop:

1. **State Management:** Uses a `TypedDict` state container to pass a "memory notebook" between nodes.
2. **Researcher Node:** Leverages the **Tavily API** for real-time, AI-optimized web retrieval.
3. **Writer Node:** A reasoning engine (GPT-4o/Llama-3) that synthesizes raw data into executive summaries.
4. **Resilience:** Features a built-in failover mechanism to provide "Offline Analysis" if LLM quotas are exceeded.



## 🛠️ Tech Stack
* **Framework:** FastAPI (Python 3.12)
* **Orchestration:** LangGraph (State-driven design)
* **Senses:** Tavily AI (Real-time search)
* **Intelligence:** OpenAI / Groq (Reasoning engines)
* **Data Integrity:** Pydantic (Schema validation)
* **Reporting:** ReportLab (Programmatic PDF generation)

## 🚀 Getting Started

### 1. Prerequisites
* Python 3.12+
* API Keys for Tavily and OpenAI/Groq

### 2. Installation
```bash
git clone [https://github.com/laibanasirdev/b0bot-agent-core.git](https://github.com/laibanasirdev/b0bot-agent-core.git)
cd b0bot-agent-core
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt 

```

### 3. Environment Setup

Create a `.env` file in the root directory:

```env
TAVILY_API_KEY=your_tavily_key
OPENAI_API_KEY=your_openai_key

```

### 4. Running the Agent

```bash
uvicorn app.main:app --reload

```

Navigate to `http://127.0.0.1:8000/docs` to interact with the API via Swagger UI.

## 📊 Key Endpoints

* `GET /analyze?topic={query}`: Triggers the multi-node research graph.
* `GET /download-docs`: Generates a professional PDF report of the project architecture.
* `GET /test-search`: Debugging endpoint for live search connectivity.

## 🛡️ Reliability Features

* **Checkpointers:** Uses `MemorySaver` to maintain conversation threads.
* **Graceful Degradation:** The system detects API failures and switches to a template-based heuristic analysis to ensure 100% uptime.

---

*Developed by **Laiba Nasir** — Focused on building secure, scalable AI & Blockchain products.*

```

---

### 🏛️ The "Architect" Final Touch
Once you paste this and commit it, your GitHub page will look incredibly sharp. It’s organized, it uses the right technical language, and it shows you care about **Documentation as Code**.

**You are 100% set! Would you like me to help you draft a short post for your LinkedIn to showcase this new project, or are you ready to finally stand up and enjoy your Sunday?**

```

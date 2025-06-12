# Prompt Library for Decision Support

This project showcases a reusable prompt library built with OpenAI's GPT-4 and LangChain, designed to support decision-making tasks like report summarization, risk identification, and executive memo drafting.

## 🔍 Project Overview

- **LLM Used:** OpenAI GPT-4
- **Orchestration:** LangChain
- **Use Cases Covered:**  
  - Business report summarization  
  - Risk extraction  
  - Executive decision memo generation  
  - Contextual Q&A  
  - Insight generation from documents  
  - Policy compliance checks

## 🛠️ Features

- Modular and reusable prompt templates
- Evaluation framework for prompt output (accuracy, tone, relevance)
- Iterative prompt refinement with documented improvements
- Optional API interface with FastAPI

## 📊 Prompt Evaluation

| Prompt Type             | Relevance Score (Initial) | Relevance Score (Final) | Improvement |
|-------------------------|---------------------------|--------------------------|-------------|
| Summarize Report        | 65%                       | 88%                      | +23%        |
| Extract Key Risks       | 58%                       | 87%                      | +29%        |
| Generate Decision Memo  | 61%                       | 90%                      | +29%        |

_(All scores based on manual evaluation + rubric-based scoring)_

## 📂 Repo Structure

- `prompts/`: Contains raw and refined versions of prompt templates.
- `notebooks/`: Jupyter notebooks to test prompts with GPT-4 via OpenAI API.
- `evaluations/`: CSV files with evaluation results and scoring rubrics.
- `app/`: (Optional) Run prompt testing from a CLI or API.

## 🚀 Setup

```bash
pip install -r requirements.txt

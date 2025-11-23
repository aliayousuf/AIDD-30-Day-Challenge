Build the Study Notes Summarizer & Quiz Generator Agent

Powered by Gemini 2.0 Flash + OpenAI Agents SDK + Streamlit + Context7 MCP

1. Project Overview

This project implements an AI Study Assistant that can:

Summarize uploaded PDFs into clean, student-friendly notes.

Generate quizzes (MCQs or mixed-style) directly from the original PDF content.

The system integrates:

Gemini CLI

Context7 MCP Server (provides OpenAI SDK documentation as tools)

OpenAI Agents SDK (configured for Gemini models)

Streamlit UI

PyPDF (text extraction)

Local JSON File for lightweight memory

This document describes the full plan, system architecture, configuration rules, and execution flow required to run the project smoothly.

2. Critical Technical Constraints
2.1 Zero-Bloat Protocol (MANDATORY)

No extra code, no extra abstractions, no “nice to have” features.

Only required logic for:
✔ PDF → Text
✔ Text → Summary
✔ Text → Quiz
✔ JSON Memory
✔ Streamlit UI
✔ Agent Configuration (Gemini through openai-agents SDK)

2.2 API Configuration (MANDATORY)

You are using OpenAI Agents SDK, but the model provider is Gemini, so configuration MUST be:

base_url = "https://generativelanguage.googleapis.com/v1beta/openai/"
api_key  = GEMINI_API_KEY  # loaded from .env
model    = "gemini-2.0-flash"

2.3 SDK-Specific Requirement

Only use:

AsyncOpenAI
Agent
RunConfig
Runner
OpenAIChatCompletionsModel


These must come directly from:

from agents import Agent, RunConfig, AsyncOpenAI, Runner, OpenAIChatCompletionsModel

2.4 Error Recovery Protocol

If you encounter:

ImportError

AttributeError

SyntaxError

→ STOP immediately
→ Re-run the Context7 MCP tool: get-library-docs
→ Re-read and correct code only based on official SDK documentation.

2.5 Dependency Management

You must use uv for all installation:

uv add streamlit pypdf python-dotenv openai-agents



3. System Architecture

Your root project contains:

.
├── agent.py
├── app.py
├── tools.py
├── memory.json
├── .env
└── GEMINI.md   (this file)


No subfolders.

3.1 Agent Layer (agent.py)

Responsibilities:

Load environment and initialize Gemini client

Register agent

Attach tools (Context7 MCP)

Expose a simple callable interface for the UI (run_agent(prompt))

The agent uses:

AsyncOpenAI pointing at Gemini

OpenAIChatCompletionsModel for model execution

RunConfig for model-provider linkage

Runner to execute calls

Agent Configuration Pattern
import os
import streamlit as st
from dotenv import load_dotenv

from agents import Agent, RunConfig, AsyncOpenAI, Runner, OpenAIChatCompletionsMode

import asyncio

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY environment variable is not set.")

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True,
)


No additional logic beyond this.

4. UI & Application Logic (app.py)
Flow Requirements

The Streamlit UI must follow this sequence:

Step 1 — Upload PDF

User uploads PDF

PyPDF extracts text

Text stored temporarily

(Optional) Save file metadata in JSON memory

Step 2 — Summarize

User clicks Generate Summary

The agent receives:

"Summarize the following PDF text: {extracted_text}"


The response is displayed in a layout the user selects:

card

block

container

(Only frontend layout — no extra logic in backend.)

Step 3 — Generate Quiz

User clicks Create Quiz

Agent receives:

"Generate a quiz based ONLY on the following full PDF text. Produce MCQs or mixed-style questions: {extracted_text}"


Output displayed as-is.

4.1 No Additional Behaviors

No multi-agent routing

No vector embeddings

No retrieval

No chunking

No caching

No streaming

No session memory beyond JSON file

5. Context7 MCP Integration

The Context7 MCP Server provides your tools:

get-library-docs (critical for debugging)

Possibly additional reference tools

The agent must register these tools exactly as MCP exposes them.

Tools act as function-calling methods accessible from prompts.



7. Execution Flow Summary

streamlit run app.py


Agent initializes with Gemini 2.0 Flash through OpenAI Agents SDK

Tools are attached (MCP)

Runtime

User uploads PDF

Text extracted by PyPDF

Summary generated

Quiz generated

UI displays both outputs

Memory updates if needed

8. Development Protocol
When modifying code:

Keep functions minimal

Follow SDK docs strictly

Validate every call using Context7 MCP if uncertain

Do not introduce helper classes

No abstractions beyond required agent + UI logic

9. Testing Protocol

Test in this order:

PDF Upload → Ensure text extraction is correct

Summary Generation

Quiz Generation

Memory Tool

MCP Documentation Fetch

Model Response (confirm model: gemini-2.0-flash)

10. Completion Criteria

Your project is considered correct when:

✔ The Streamlit UI runs without crashes
✔ PDF uploads correctly
✔ Summary is generated via the agent
✔ Quiz is generated from original text
✔ Memory JSON updates normally
✔ No unexpected features or code bloat
✔ No errors from openai-agents imports
✔ Agent uses Gemini endpoint correctly
# 🚀 Python AI Projects Portfolio - Project Folder 1

This folder contains **three advanced Python AI applications** showcasing the integration of Modern LLMs, Agentic Workflows, Computer Vision, and Web Dashboards. 

Each project is designed to solve real-world problems using state-of-the-art libraries like **LangChain, LangGraph, Streamlit, TensorFlow, and Groq API**.

---

## 📂 Folder Structure

```directory
project_1/
├── main.py              # Project 1: ReAct AI Chat Assistant
├── resume_analyze.py    # Project 2: Streamlit AI Resume Critiquer
├── image_classifier.py  # Project 3: Streamlit AI Image Classifier
├── pyproject.toml       # Python dependency configuration
└── uv.lock              # UV Package Manager lockfile
```

---

## 🛠️ Project Showcases

### 🤖 Project 1: Agentic AI Chat Assistant (`main.py`)
An interactive command-line chatbot built using a **ReAct (Reasoning + Action) Agent** architecture. It leverages Groq's high-speed Llama-3.3 model to dynamically call tools when needed.

* **Core Features**:
  * **Dynamic Tool Invocation**: Automatically decides whether to answer from knowledge or call a tool (e.g., custom calculator).
  * **Streaming Responses**: Streams token chunks in real-time for a smooth interactive experience.
  * **State Management**: Built using `langgraph` prebuilt agent executor.
* **Tech Stack**: `LangGraph`, `LangChain Core`, `ChatGroq (Llama-3.3-70b-versatile)`, `python-dotenv`

---

### 🔍 Project 2: AI Resume Critiquer & Career Coach (`resume_analyze.py`)
A comprehensive Streamlit-based web application that acts as a strict, professional career coach. Upload your resume and get detailed, customized feedback based on your target job role.

* **Core Features**:
  * **Multi-Format Document Parsing**: Seamlessly extracts text from both `PDF` and `TXT` files.
  * **Detailed Critique Breakdown**: Analyzes formatting, keyword matching, strength-by-strength metrics, experience quantification, and overall tailoring.
  * **Structured Markdown Output**: Generates specific recommendations, action plans, and a final verdict with example improvements.
* **Tech Stack**: `Streamlit`, `Groq API SDK`, `PyPDF2`, `python-dotenv`

---

### 📷 Project 3: AI Image Classifier (`image_classifier.py`)
A fast web app that classifies images uploaded by users. It utilizes a pre-trained Deep Learning model to perform image classification locally.

* **Core Features**:
  * **Local Deep Learning Model**: Uses Google's `MobileNetV2` convolutional neural network pre-trained on `ImageNet`.
  * **Image Preprocessing**: Utilizes OpenCV for fast resizing and conversion to model-compatible dimensions.
  * **Confidence Scoring**: Outputs top-3 target categories along with their match percentages.
  * **Cached Resource Loading**: Utilizes Streamlit's `@st.cache_resource` for zero-latency page reloads.
* **Tech Stack**: `Streamlit`, `TensorFlow/Keras`, `OpenCV (cv2)`, `Pillow (PIL)`

---

## ⚡ Installation & Quick Start

Ensure you have **Python 3.12+** and the fast **`uv`** package manager installed.

### 1. Set Up Environment Variables
Create a `.env` file in the root workspace directory:
```ini
GROQ_API_KEY=your_groq_api_key_here
```

### 2. Install Dependencies
Using `uv` to install packages:
```bash
uv sync
```

---

## 🏃 Run the Applications

You can run any of the three projects directly from this folder:

### 1. Run the AI Chat Assistant (Terminal)
```bash
uv run main.py
```

### 2. Run the AI Resume Critiquer (Streamlit Web App)
```bash
uv run streamlit run resume_analyze.py
```

### 3. Run the AI Image Classifier (Streamlit Web App)
```bash
uv run streamlit run image_classifier.py
```

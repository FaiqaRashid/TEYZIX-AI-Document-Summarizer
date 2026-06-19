# AI-Powered Document Summarization System

🚀 **TEYZIX CORE INTERNSHIP PROGRAM — AI & NLP DOMAIN**
**Task Title:** AI-Powered Document Summarization System  
**Intern Name:** Faiqa Rashid  
**Submission Date:** June 19, 2026  

---

## 📝 Description
This is an AI-powered extractive text summarization system that automatically condenses long documents into concise, meaningful summaries while completely preserving vital contextual information. The system utilizes advanced Natural Language Processing (NLP) techniques—including sentence segmentation, word tokenization, stop-word removal, and frequency-based normalization algorithms—to isolate and rank the most critical sentences from any text payload.

**🎯 Perfect For:** Research papers, academic articles, corporate reports, news logs, or any dense long-form text.

---

## 🛠️ Features Implemented

### 📥 Multiple Input Methods
* **Direct Console Input:** Supports dynamic multi-line user text entry directly in the terminal interface (type 'DONE' on a new line to finish).
* **File Ingestion Pipeline:** Seamlessly reads external text documents (`.txt`) with absolute error handling for missing paths.

### ⚙️ Advanced Text Preprocessing
* **Sentence Tokenization:** Highly accurate boundary segmentation using modern NLTK architectures.
* **Word Tokenization:** Individual token breakdown coupled with consistent lowercase normalization.
* **Stop-word Invalidation:** Filters out low-value linguistic connectors (removes common words like *"the"*, *"is"*, *"and"*) to capture true topic weights.
* **Alphanumeric Filtering:** Structural cleaning to strip stray punctuation artifacts.

### 🧠 Summarization Logic (Extractive Framework)
* **Word Frequency Analytics:** Counts occurrence matrices of clean keyword variables using localized counters.
* **Normalized Weight Ratios:** Math scoring scaled cleanly against the absolute peak frequency word to ensure algorithmic fairness.
* **Sentence Scoring:** Accumulates normalized word weights to evaluate overall sentence importance.
* **Adjustable Summary Percentage:** Allows users to input customized length thresholds ranging from 5% to 90%.
* **Chronological Consistency:** Re-sorts extracted sentences back into their native conversational sequence to preserve logical flow and readability.

### 📊 Output & Export System
* **Real-time Analytics Report:** Displays a clean dashboard showing original vs. compressed character counters and a reduction percentage metric.
* **Collision-Free Storage:** Features a dynamic prompt requesting custom names for export logs, completely preventing file overwriting during back-to-back testing.

---

## 💻 Technical Requirements Satisfied

* **Language Foundation:** Pure Python architecture.
* **Core NLP Library:** Natural Language Toolkit (`nltk`).
* **Architecture:** Modular, function-based layout prioritizing single-responsibility principles.
* **Exception Safeties:** Implements deep try-catch handling blocks covering `FileNotFoundError` and `ValueError`.
* **Scoring Logic:** Implementation of a lightweight TF-IDF-inspired weighted ranking pipeline.

---

## 🚀 How to Run

### 1. Install Dependencies
Ensure you have Python installed, then install the NLTK library package via your terminal:
```bash
pip install nltk

======================================================================
     TEYZIX CORE INTERNSHIP PROGRAM - AI & NLP DOMAIN
======================================================================
Task ID: AI-INT-1
Task Title: AI-Powered Document Summarization System
Domain: Artificial Intelligence / NLP
Intern Name: Faiqa Rashid
Submission Date: June 19, 2026
======================================================================

1. PROJECT OVERVIEW
-------------------
This project is an interactive, AI-powered extractive text summarization 
system built using Python 3.12 and the NLTK (Natural Language Toolkit) 
library. The pipeline ingests text from multiple sources, processes natural 
language tokens, computes mathematical term weights, ranks sentences, and 
allows dynamic data export without file duplication or data overwriting.

2. CORE FEATURES & UPDATES
--------------------------
* Multi-Channel Input: Supports dynamic direct console text entry as well 
  as robust external .txt file ingestion.
* Modern NLP Tokenization: Utilizes NLTK's updated 'punkt_tab' architecture 
  for high-precision sentence boundary segmentation.
* Frequency-Based Scoring Engine: Drops structural stop-words and weights 
  content tokens using a normalized maximum frequency ratio method.
* Dynamic Compression Control: Allows users to input customized length 
  threshold percentages (e.g., 15%, 30%) to generate summaries.
* Collision-Free Export System: Features an updated export module that 
  prompts the user for unique filenames, preventing accidental data 
  overwrites during back-to-back testing.

3. PREREQUISITES & DEPENDENCIES
--------------------------------
Before executing the program, ensure that you have Python 3.x installed on 
your system along with the NLTK library package.

To install the required environment framework, run:
    pip install nltk

4. FILE STRUCTURE
-----------------
Verify that your local workspace folder is structured as follows:
    ├── summerise.py        (Main Python source script)
    ├── input.txt           (Source file containing raw text data for analysis)
    ├── README.txt          (This documentation file)
    └── [custom_name].txt   (Generated uniquely upon user input choice)

5. STEP-BY-STEP OPERATION MANUAL
--------------------------------
1. Populate your target material inside the 'input.txt' file in your directory.
2. Launch your command line interface (CLI) in the project workspace folder.
3. Fire up the execution script using:
    python summerise.py

4. Interacting with the Console Application:
   - Select option 2 to run file mode processing.
   - Supply 'input.txt' as your target file path.
   - Input your desired compression ratio target (e.g., 15).
5. Analyze the complete side-by-side Summarization Report metrics.
6. Input 'y' to save the text block, then supply a unique string identifier 
   (e.g., cloud_summary) to safely isolate the target data artifact.

6. COMPREHENSIVE EXCEPTION HANDLING
------------------------------------
* FileNotFoundError: Gracefully warns users of missing resource targets 
  instead of causing terminal termination.
* ValueError: Catches non-integer characters or values out of bounds (5-90) 
  and defaults safely to a baseline 30% ratio metrics structure.
* Filename Extension Safeguard: Automatically reviews manual string inputs 
  and appends '.txt' headers if absent to ensure clean system writing.
======================================================================
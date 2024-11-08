# VNTaxChatbot

## Overview
Imagine you are a Vietnamese citizen with modest acknowledge of tax law and regulations, tax rates with various tax types, etc. You may find this helpful to ask and get any information about tax in Vietnam without needing to spend hours to read and analyze all long documents or going to a tax consultant firm.

This is a chatbot powered by **Google Gemini API** and some related **Tax Documents** stored in MongoDB to answers questions about taxation in Vietnam.

The system will try to retrieve data from the user query in the knowledge base and integrate it with prompts to get LLM's answer. If there is no such data found, it will returns the answer by LLM naturally.

## Tech stack
- **MongoDB**: a NoSQL database management system for storing knowledge base of definitions and tax documents of Vietnam, with JSON-like format and key-value storing, make it effective for data retrieval problems
- **Google Gemini API**: a large language model used for answering questions
- **Python**: a powerful programming language for AI development
- **Gradio**: used for simple visualization

## Credits
This project belongs to Duong Gia Bao. Please do not copy without any permission.

🤖 Generative AI Course - Faculty of Information Technology

🏫 Vietnam National University - University of Engineering and Technology (UET - VNU)
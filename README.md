🤖 **AI Chatbot – Python & OpenRouter**
A simple command-line AI chatbot built with **Python**. It sends your questions to an AI model through the **OpenRouter API** and prints the reply in the terminal.

🚀 **Features**
- 💬 Ask any question and get an instant AI reply
- 🔁 Continuous chat loop in the terminal, type `exit` to quit
- 🔐 API key stored in a `.env` file, which Git ignores
- ⚙️ Uses the `openai/gpt-4o-mini` model via OpenRouter
- 🧩 Client setup kept separate in `config.py`

🛠️ **Tech Stack**
- 🐍 Python: main language
- 🔌 OpenAI Python library: API client (connected to OpenRouter)
- 🌐 OpenRouter API: access to the AI model
- 🔑 python-dotenv: loads the API key from `.env`

📁 **Project Structure**
AI-Chatbot/
├── chatbot.py          # Main chat loop
├── config.py           # API client setup
├── prompts.py          # Prompt templates
├── requirements.txt    # Dependencies
├── .env.example        # Example environment file
└── .gitignore

⚡ **How to Run**
1️⃣ Clone the repository
```bash
git clone https://github.com/vaasudevchatti/AI-Chatbot.git
cd AI-Chatbot
```
2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```
3️⃣ Copy `.env.example` to `.env` and add your OpenRouter key
```bash
OPENROUTER_API_KEY=your_key_here
```
4️⃣ Start the chatbot
```bash
python chatbot.py
```
🔮 **Future Improvements**
- 🧠 Remember earlier messages in the conversation
- 🌐 Add a web interface
- 🎯 Add custom system prompts
👨‍💻 **Author**
**Vaasudev Chatti** | 🔗 [GitHub](https://github.com/vaasudevchatti) • [LinkedIn](https://www.linkedin.com/in/vaasudev-chatti-6bb768341)

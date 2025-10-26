# ForensAI - AI-Powered Digital Forensics Platform

> Analyse security logs with AI, detect anomalies in seconds, and investigate cyber threats like a professional forensic analyst.

## 🚀 Features

- 🤖 **AI-Powered Analysis** - Local Llama 3 model for log analysis
- 📊 **Visual Analytics** - Interactive charts and threat visualization
- 🔒 **Privacy First** - All data processed locally
- 💬 **InspectorBot** - AI assistant for forensic investigation
- 📁 **Multi-Format Support** - `.log`, `.txt`, `.csv` files
- 🎯 **Real-time Detection** - Instant threat identification

## 🛠️ Tech Stack

### Frontend
- React.js
- Tailwind CSS
- Recharts
- Lucide Icons

### Backend
- Python Flask
- Ollama (Llama 3)
- Flask-CORS

## 📦 Installation

### Prerequisites
- Node.js (v16+)
- Python 3.10+
- Ollama

### Setup

1. **Clone the repository**
```bash
   git clone https://github.com/FaisalSheriff0706/forensai
   cd forensai
```

2. **Install Ollama and Llama 3**
```bash
   # Install Ollama from https://ollama.ai
   ollama pull llama3
   ollama serve
```

3. **Backend Setup**
```bash
   cd backend
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   python app.py
```

4. **Frontend Setup**
```bash
   cd frontend
   npm install
   npm start
```

5. **Open** `http://localhost:3000`

## 🎯 Usage

1. **Upload Logs** - Drag & drop security log files
2. **AI Analysis** - Get instant threat detection
3. **Investigate** - Chat with InspectorBot for insights
4. **Reports** - Generate professional forensic reports

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.


## 👨‍💻 Author

**Your Name**
- LinkedIn: (https://linkedin.com/in/faisalsheriff)
- Email: faisalssheriff@gmail.com

## 🙏 Acknowledgments

- Built with Ollama and Llama 3
- Inspired by the need for accessible digital forensics tools

---

Built by Faisal Sheriff for Cybersecurity Professionals

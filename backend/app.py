from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

# Ollama API configuration
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3"

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'message': 'ForensAI Backend is running'
    }), 200

@app.route('/api/chat', methods=['POST'])
def chat():
    """
    Chat endpoint that communicates with Ollama
    Expects JSON: { "message": "user message" }
    """
    try:
        data = request.get_json()
        
        if not data or 'message' not in data:
            return jsonify({
                'error': 'No message provided'
            }), 400
        
        user_message = data['message']
        
        # Prepare the prompt for Ollama
        payload = {
            "model": MODEL_NAME,
            "prompt": user_message,
            "stream": False
        }
        
        # Send request to Ollama
        response = requests.post(OLLAMA_URL, json=payload)
        
        if response.status_code == 200:
            result = response.json()
            ai_response = result.get('response', 'No response from AI')
            
            return jsonify({
                'response': ai_response,
                'model': MODEL_NAME
            }), 200
        else:
            return jsonify({
                'error': 'Failed to get response from Ollama',
                'details': response.text
            }), 500
            
    except requests.exceptions.ConnectionError:
        return jsonify({
            'error': 'Cannot connect to Ollama. Make sure Ollama is running.',
            'hint': 'Run: ollama serve'
        }), 503
    except Exception as e:
        return jsonify({
            'error': 'Internal server error',
            'details': str(e)
        }), 500

@app.route('/api/analyze-log', methods=['POST'])
def analyze_log():
    """
    Analyze uploaded log file
    Expects: file upload or text content
    """
    try:
        if 'file' in request.files:
            file = request.files['file']
            content = file.read().decode('utf-8')
        elif 'content' in request.form:
            content = request.form['content']
        else:
            return jsonify({'error': 'No file or content provided'}), 400
        
        # Create forensic analysis prompt
        prompt = f"""You are a digital forensics expert. Analyze this log file and provide:
1. Summary of key events
2. Any suspicious activities or anomalies
3. Security concerns
4. Recommendations

Log Content:
{content[:2000]}  # Limit to first 2000 chars for initial analysis

Provide a concise analysis."""

        payload = {
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False
        }
        
        response = requests.post(OLLAMA_URL, json=payload)
        
        if response.status_code == 200:
            result = response.json()
            return jsonify({
                'analysis': result.get('response', ''),
                'log_preview': content[:500]
            }), 200
        else:
            return jsonify({'error': 'Analysis failed'}), 500
            
    except Exception as e:
        return jsonify({
            'error': 'Error analyzing log',
            'details': str(e)
        }), 500

if __name__ == '__main__':
    print("🚀 ForensAI Backend Starting...")
    print("📡 Listening on http://localhost:5000")
    print("🤖 Using Ollama model:", MODEL_NAME)
    print("\nEndpoints:")
    print("  GET  /api/health       - Health check")
    print("  POST /api/chat         - Chat with AI")
    print("  POST /api/analyze-log  - Analyze log files")
    print("\n⚠️  Make sure Ollama is running: ollama serve\n")
    
    app.run(debug=True, port=5000)
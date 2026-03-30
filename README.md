
cat > README.md << 'EOF'
# Claude AI Chatbot

A conversational AI chatbot built with Python and the Anthropic Claude API.

## About
This chatbot uses Anthropic's Claude API to hold multi-turn conversations, meaning it remembers the context of your conversation as you chat. Built as part of studying the Anthropic "Building with the Claude API" course.

## Technologies Used
- Python
- Anthropic Claude API (claude-sonnet-4-20250514)

## How It Works
- Connects to Claude via the Anthropic API
- Maintains conversation history so Claude remembers what was said earlier in the chat
- Runs as an interactive command-line chatbot

## How To Run
1. Clone this repository
2. Install the Anthropic library: pip3 install anthropic
3. Set your API key: export ANTHROPIC_API_KEY="your-key-here"
4. Run: python3 chatbot.py

## Author
Rebecca Ryan  
GitHub: github.com/beccar2299

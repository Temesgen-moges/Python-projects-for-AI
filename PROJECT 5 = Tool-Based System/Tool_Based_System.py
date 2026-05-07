# simple_tool_system.py
# This shows how AI Agents work - Simple Version

import random
from datetime import datetime

# ============================================
# TOOL 1: Weather Tool (Simulated)
# ============================================

def weather_tool(city):
    """Get weather for a city (simulated for simplicity)"""
    print(f"\n   🔧 Running WEATHER tool with: {city}")
    
    # Simulated weather data
    temperatures = {
        "london": 12,
        "new york": 18,
        "tokyo": 22,
        "bahir dar": 25,
        "paris": 15
    }
    
    temp = temperatures.get(city.lower(), 20)  # Default 20°C
    weather = "sunny" if temp > 20 else "cloudy"
    
    return f"{city.title()}: {temp}°C, {weather}"


# ============================================
# TOOL 2: Calculator Tool
# ============================================

def calculator_tool(expression):
    """Calculate math expression"""
    print(f"\n   🔧 Running CALCULATOR tool with: {expression}")
    
    try:
        # Safe calculation
        result = eval(expression)
        return f"{expression} = {result}"
    except:
        return f"Sorry, couldn't calculate '{expression}'"


# ============================================
# TOOL 3: News Tool (Simulated)
# ============================================

def news_tool():
    """Get latest news headlines"""
    print(f"\n   🔧 Running NEWS tool")
    
    headlines = [
        "AI Breakthrough Announced Today",
        "Python Remains Most Popular Language",
        "New Robot Can Cook and Clean",
        "Tech Companies Invest $1B in AI",
        "Students Learn Programming Online"
    ]
    
    return random.sample(headlines, 3)  # Return 3 random headlines


# ============================================
# TOOL 4: Time Tool
# ============================================

def time_tool():
    """Get current time"""
    print(f"\n   🔧 Running TIME tool")
    
    now = datetime.now()
    return f"Current time: {now.strftime('%H:%M:%S')}"


# ============================================
# TOOL 5: Random Number Tool
# ============================================

def random_tool(max_number=100):
    """Generate random number"""
    print(f"\n   🔧 Running RANDOM tool (1-{max_number})")
    
    number = random.randint(1, max_number)
    return f"Random number: {number}"


# ============================================
# TOOL REGISTRY (List of all available tools)
# ============================================

TOOLS = {
    "weather": {
        "function": weather_tool,
        "description": "Get weather for a city",
        "example": "weather london"
    },
    "calculator": {
        "function": calculator_tool,
        "description": "Do math calculations",
        "example": "calculate 5 + 3"
    },
    "news": {
        "function": news_tool,
        "description": "Get latest news",
        "example": "get news"
    },
    "time": {
        "function": time_tool,
        "description": "Get current time",
        "example": "what time is it"
    },
    "random": {
        "function": random_tool,
        "description": "Generate random number",
        "example": "random number 1-50"
    }
}


# ============================================
# THE AI BRAIN (Decides which tool to use)
# ============================================

def ai_brain(user_input):
    """
    This is the AI that decides which tool to use
    In real AI, this would be GPT/Claude/Llama
    """
    user_input = user_input.lower()
    
    print(f"\n🤔 AI THINKING: '{user_input}'")
    
    # AI decides which tool based on keywords
    if "weather" in user_input:
        # Extract city name
        words = user_input.split()
        city = "bahir dar"  # default
        for word in words:
            if word in ["in", "for", "at"]:
                # Get next word as city
                idx = words.index(word) + 1
                if idx < len(words):
                    city = words[idx]
            else:
                # Check if word might be a city
                if len(word) > 3 and word not in ["weather", "what", "the", "is", "like"]:
                    city = word
        
        return "weather", {"city": city}
    
    elif any(word in user_input for word in ["calculate", "math", "plus", "minus", "times", "divide", "="]):
        # Extract math expression
        expression = user_input
        for word in ["calculate", "what is", "math", "solve"]:
            expression = expression.replace(word, "")
        expression = expression.replace("plus", "+")
        expression = expression.replace("minus", "-")
        expression = expression.replace("times", "*")
        expression = expression.replace("divided by", "/")
        expression = expression.strip()
        
        return "calculator", {"expression": expression}
    
    elif "news" in user_input or "headlines" in user_input:
        return "news", {}
    
    elif "time" in user_input or "clock" in user_input:
        return "time", {}
    
    elif "random" in user_input or "roll" in user_input:
        # Extract max number if specified
        max_num = 100
        words = user_input.split()
        for word in words:
            if word.isdigit():
                max_num = int(word)
                break
        return "random", {"max_number": max_num}
    
    else:
        return None, None


# ============================================
# RUN A TOOL
# ============================================

def run_tool(tool_name, params):
    """Execute the selected tool"""
    if tool_name not in TOOLS:
        return f"Error: Tool '{tool_name}' not found"
    
    tool = TOOLS[tool_name]
    tool_function = tool["function"]
    
    print(f"\n✅ AI DECISION: I will use the {tool_name.upper()} tool")
    
    # Call the tool with parameters
    result = tool_function(**params)
    
    return result


# ============================================
# MAIN PROGRAM
# ============================================

def main():
    print("""
╔════════════════════════════════════════╗
║   🤖 AI AGENT TOOL SYSTEM              ║
║   I can use different tools to help    ║
╚════════════════════════════════════════╝
    """)
    
    # Show available tools
    print("📦 TOOLS I HAVE:")
    for name, info in TOOLS.items():
        print(f"   • {name.upper()} - {info['description']}")
    
    print("\n" + "="*50)
    print("💬 Talk to me naturally! Examples:")
    print("   → 'What's the weather in London?'")
    print("   → 'Calculate 25 * 4'")
    print("   → 'Get me news headlines'")
    print("   → 'What time is it?'")
    print("   → 'Give me a random number 1-50'")
    print("   → 'exit' to quit")
    print("="*50)
    
    while True:
        # Get user input
        user_input = input("\n👤 You: ").strip()
        
        if user_input.lower() in ["exit", "quit"]:
            print("\n🤖 AI: Goodbye!")
            break
        
        if not user_input:
            continue
        
        # Step 1: AI decides which tool to use
        tool_name, params = ai_brain(user_input)
        
        # Step 2: If AI can't decide, show error
        if tool_name is None:
            print("\n🤖 AI: I don't know how to help with that.")
            print("   Try: weather, calculate, news, time, or random")
            continue
        
        # Step 3: Run the tool
        result = run_tool(tool_name, params)
        
        # Step 4: Show result
        print(f"\n🤖 AI RESPONSE: {result}")


# ============================================
# RUN THE PROGRAM
# ============================================

if __name__ == "__main__":
    main()
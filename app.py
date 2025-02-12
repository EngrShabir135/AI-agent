import streamlit as st
import openai

# Set the page configuration at the very beginning
st.set_page_config(page_title="Free AI Agent", page_icon="🤖")

# Set your OpenAI API key
openai.api_key = "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"

# Streamlit app setup
st.title("Free AI Agent 🤖")
st.write("This AI agent is powered by OpenAI!")

# Initialize conversation history
if "history" not in st.session_state:
    st.session_state.history = []

# User input
user_input = st.text_input("Ask me anything:")

if st.button("Submit"):
    if user_input.strip():
        # Add user input to conversation history
        st.session_state.history.append({"role": "user", "content": user_input})
        
        # Prepare messages for the Chat Completions API
        messages = [{"role": msg["role"], "content": msg["content"]} for msg in st.session_state.history]
        
        # Generate a response using OpenAI GPT-3.5 Turbo
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=150,
            temperature=0.7
        )
        
        # Extract the generated text
        ai_response = response.choices[0].message["content"].strip()
        
        # Save AI response to history
        st.session_state.history.append({"role": "assistant", "content": ai_response})
    else:
        st.warning("Please enter a question or command!")

# Display conversation history
st.write("### Conversation History")
for chat in st.session_state.history:
    if chat["role"] == "user":
        st.write(f"**You:** {chat['content']}")
    elif chat["role"] == "assistant":
        st.write(f"**AI:** {chat['content']}")

# Footer
st.markdown("---")
st.markdown("**Powered by OpenAI and Streamlit**")
st.markdown("**Author: Engr Shabir Orakzai**")
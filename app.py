
import streamlit as st

st.title("🤖 Flora AI Chatbot")
if st.button("🗑️ Clear Chat"):
    st.session_state.messages = []
    st.rerun()
st.caption("Your friendly AI assistant")
with st.sidebar:
    st.header("About Flora")
    st.write("Flora is a beginner-friendly chatbot project.")
    st.write("Features:")
    st.write("- Simple chat interface")
    st.write("- Keyword-based replies")
    st.write("- Conversation history")
st.write("Hi! 👋 Ask me something and let's chat.")
st.info("💡 Try asking: Hello, What is Python?, Help, or What are your features?")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

user_input = st.chat_input("Type your message...")

if user_input and user_input.strip():
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.write(user_input)

    msg = user_input.lower()
    if "hello" in msg or "hi" in msg:
        bot_reply = "Hello! How can I help you?"
    elif "python" in msg:
        bot_reply = "Python is a popular programming language."
    elif "features" in msg:
        bot_reply = "I support simple chatting, keyword-based replies, and conversation history."
    elif "who are you" in msg:
        bot_reply = "I am your Python AI Chatbot."
    elif "thank you" in msg or "thanks" in msg:
        bot_reply = "You're welcome! 😊"
    elif "help" in msg:
        bot_reply = "You can ask me about Python, my features, or say hello!"
    elif "bye" in msg:
        bot_reply = "Goodbye! Have a nice day."
    else:
        bot_reply = "Sorry, I don't know that yet."

    st.session_state.messages.append(
        {"role": "assistant", "content": bot_reply}
    )

    with st.chat_message("assistant"):
        st.write(bot_reply)

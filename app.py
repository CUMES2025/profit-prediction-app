import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import joblib
from groq import Groq
from dotenv import load_dotenv
import os


# Load environment variables from .env file
load_dotenv()

# Get API key from .env
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    st.error("API key not found! Please set GROQ_API_KEY in the .env file.")
else:
    client = Groq(api_key=api_key)
# Initialize the Groq API client
# api_key = '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'
# client = Groq(api_key=api_key)

# Load the saved model
model_filename = "decision_tree_model.pkl"
loaded_model = joblib.load(model_filename)

# Encoder for product lines
encoder = LabelEncoder()
encoder.fit(["Health and beauty", "Electronic accessories", "Home and lifestyle"])  # Original categories

# Streamlit app setup
st.title("Profit Prediction App")
st.write("""
This app predicts the profit based on the product line and quantity, and provides a summarized analysis using an AI chatbot.
""")

# User input
product_line = st.selectbox(
    "Select the product line:",
    ["Health and beauty", "Electronic accessories", "Home and lifestyle"]
)

quantity = st.number_input(
    "Enter the product quantity:",
    min_value=1,
    step=1
)

# Prediction logic
if st.button("Predict Profit"):
    encoded_product_line = encoder.transform([product_line])[0]
    user_input = pd.DataFrame([[encoded_product_line, quantity]], columns=["Product line", "Quantity"])
    predicted_profit = loaded_model.predict(user_input)[0]

    st.write(f"### Predicted Profit: K{predicted_profit:.2f}")
    
    # Summarize prediction with Groq API
    st.write("Generating summary...")
    completion = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role": "system", "content": "You are a helpful assistant summarizing the prediction results."},
            {
                "role": "user",
                "content": (
                    f"Summarize the predicted profit for a product line in thousands '{product_line}' "
                    f"with a quantity of {quantity} as K{predicted_profit:.2f}."
                )
            }
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=False,
        stop=None,
    )
     # Correct way to access the response with dot notation
    if completion.choices:
        summary = completion.choices[0].message.content  # Use dot notation instead of subscript
    else:
        summary = 'No summary available.'

    # for chunk in completion:
    #     summary = print(chunk.choices[0].delta.content or "", end="")

    # summary = completion.get('choices', [{}])[0].get('message', {}).get('content', 'No summary available.')
    # summary = completion.choices[0].message["content"] if completion.choices else 'No summary available.'
    st.write("### Summary:")
    st.write(summary)

import pandas as pd
import plotly.express as px
import requests
import streamlit as st
from datetime import datetime
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from statsmodels.tsa.arima.model import ARIMA
from transformers import pipeline
import json

# API keys
API_KEY = ""  # Groq API Key
SLACK_WEBHOOK = ""  # Slack webhook URL

# Streamlit App Configuration
st.set_page_config(
    page_title="E-Commerce Competitor Strategy Dashboard",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Header Design
st.markdown(
    """
    <style>
        .main-header {
            font-size: 40px;
            text-align: left;
            color: #2b5797;
            font-family: 'Arial Black', sans-serif;
            background: linear-gradient(to right, #b3e6fc, #d8e8f9);
            padding: 15px;
            border-radius: 10px;
        }
        .sub-header {
            color: #333333;
            font-size: 20px;
            font-weight: bold;
            margin-bottom: 15px;
        }
        .footer {
            text-align: center;
            font-size: 12px;
            color: #aaaaaa;
            margin-top: 50px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="main-header">❄️ E-Commerce Competitor Strategy Dashboard ❄️</div>', unsafe_allow_html=True)

# Sidebar
st.sidebar.header("❄️ Select a Product ❄️")
products = [
    "Apple iPhone 15",
    "Apple 2023 MacBook Pro",
    "OnePlus Nord 4 5G",
    "Sony WH-1000XM5"
]
selected_product = st.sidebar.selectbox("Choose a product to analyze:", products)

# Utility function to truncate text
def truncate_text(text, max_length=512):
    return text[:max_length]

# Load competitor data
def load_competitor_data():
    data = pd.read_csv("competitor_data.csv")
    return data

# Load reviews data
def load_reviews_data():
    reviews = pd.read_csv("reviews.csv")
    return reviews

# Analyze customer sentiment
def analyze_sentiment(reviews):
    sentiment_pipeline = pipeline("sentiment-analysis")
    return sentiment_pipeline(reviews)

# Train predictive model
def train_predictive_model(data):
    data["Discount"] = data["Discount"].str.replace("%", "").astype(float)
    data["Price"] = data["Price"].astype(float)
    data["Predicted_Discount"] = data["Discount"] + (data["Price"] * 0.05).round(2)

    X = data[["Price", "Discount"]]
    y = data["Predicted_Discount"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestRegressor(random_state=42)
    model.fit(X_train, y_train)
    return model

# Forecast discounts using ARIMA
def forecast_discounts_arima(data, future_days=5):
    data = data.sort_index()
    data["Discount"] = pd.to_numeric(data["Discount"], errors="coerce")
    data = data.dropna(subset=["Discount"])

    discount_series = data["Discount"]

    if not isinstance(data.index, pd.DatetimeIndex):
        data.index = pd.to_datetime(data.index)

    model = ARIMA(discount_series, order=(5, 1, 0))
    model_fit = model.fit()

    forecast = model_fit.forecast(steps=future_days)
    future_dates = pd.date_range(
        start=discount_series.index[-1] + pd.Timedelta(days=1),
        periods=future_days
    )

    forecast_df = pd.DataFrame({"Date": future_dates, "Predicted_Discount": forecast})
    forecast_df.set_index("Date", inplace=True)
    return forecast_df

# Send notifications to Slack
def send_to_slack(data):
    payload = {"text": data}
    response = requests.post(
        SLACK_WEBHOOK,
        data=json.dumps(payload),
        headers={"Content-Type": "application/json"}
    )
    if response.status_code != 200:
        st.write(f"Failed to send notification to Slack: {response.status_code}")

# Generate strategy recommendations using an LLM
def generate_strategy_recommendation(product_name, competitor_data, sentiment):
    date = datetime.now()
    prompt = f"""
    You are a highly skilled business strategist specializing in e-commerce. Based on the following details, suggest actionable strategies:

    *Product Name*: {product_name}
    *Competitor Data*:
    {competitor_data}
    *Sentiment Analysis*: {sentiment}
    *Today's Date*: {str(date)}

    Provide recommendations:
    - **Pricing Strategy**
    - **Promotional Campaign Ideas**
    - **Customer Satisfaction Recommendations**
    """

    data = {
        "messages": [{"role": "user", "content": prompt}],
        "model": "llama3-8b-8192",
        "temperature": 0,
    }

    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {API_KEY}"}
    res = requests.post("https://api.groq.com/openai/v1/chat/completions", json=data, headers=headers)
    res = res.json()
    return res["choices"][0]["message"]["content"]

# Main App Logic
competitor_data = load_competitor_data()
reviews_data = load_reviews_data()
product_data = competitor_data[competitor_data["product_name"] == selected_product]
product_reviews = reviews_data[reviews_data["product_name"] == selected_product]

col1, col2 = st.columns(2)

# Column 1: Competitor Data
with col1:
    st.subheader(f"Competitor Analysis for {selected_product}")
    st.table(product_data.tail(5))

# Column 2: Sentiment Analysis
with col2:
    st.subheader("Customer Sentiment Analysis")
    if not product_reviews.empty:
        product_reviews["reviews"] = product_reviews["reviews"].apply(lambda x: truncate_text(x, 512))
        reviews = product_reviews["reviews"].tolist()
        sentiments = analyze_sentiment(reviews)
        sentiment_df = pd.DataFrame(sentiments)
        fig = px.bar(sentiment_df, x="label", title="Sentiment Analysis Results", color="label")
        st.plotly_chart(fig)
    else:
        st.write("No reviews available for this product.")

# Competitor Discounts and Forecast
st.subheader("Competitor Current and Predicted Discounts")
product_data["Date"] = pd.to_datetime(product_data["Date"], errors="coerce")
product_data = product_data.dropna(subset=["Date"])
product_data.set_index("Date", inplace=True)
product_data["Discount"] = pd.to_numeric(product_data["Discount"], errors="coerce")
product_data = product_data.dropna(subset=["Discount"])

product_data_with_predictions = forecast_discounts_arima(product_data)
st.table(product_data_with_predictions.tail(10))

# Generate Strategic Recommendations
st.subheader("Strategic Recommendations")
recommendations = generate_strategy_recommendation(
    selected_product,
    product_data_with_predictions,
    sentiments if not product_reviews.empty else "No reviews available"
)
st.write(recommendations)

# Send Recommendations to Slack
send_to_slack(recommendations)

# Footer
st.markdown('<div class="footer">Built with ❤️ for e-commerce insights</div>', unsafe_allow_html=True)


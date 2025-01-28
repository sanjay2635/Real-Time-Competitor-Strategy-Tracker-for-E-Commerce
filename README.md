# Real-Time-Competitor-Strategy-Tracker-for-E-Commerce
# Project Overview:
![WhatsApp Image 2025-01-28 at 18 57 55_08f50f9d](https://github.com/user-attachments/assets/c59aa785-1ef7-4d2e-b3b9-654741b668e1)
![WhatsApp Image 2025-01-28 at 18 58 11_ef5d76fa](https://github.com/user-attachments/assets/dcfd1b65-3d82-4be2-95f3-f9e39794066c)
![WhatsApp Image 2025-01-28 at 18 58 47_bf1f2879](https://github.com/user-attachments/assets/2a17d6e8-380b-40c2-8a16-7d33987be0cf)


This project provides a real-time competitive intelligence tool for e-commerce businesses, offering actionable insights by monitoring competitor pricing, discount strategies, and customer sentiment.

**Features**

* Competitor Data Aggregation: Track pricing and discount strategies of your competitors.
* Sentiment Analysis: Analyze customer reviews to gain valuable insights.
* Predictive Modeling: Forecast competitor discounts using ARIMA.
* Slack Integration: Get real-time notifications on competitor activity through Slack.

**Technology Stack**

* Machine Learning: ARIMA for predictive modeling
* LLMs: Sentiment analysis using Hugging Face Transformer and Groq
* Integration: Slack notifications

**Installation**

1. **Clone the Repository**

   ```bash
   git clone <repository-url>
   cd <repository-directory>
2.**Install Dependencies**

    pip install -r requirements.txt
**Configure API Keys**
**Groq API Key:**

1.Sign up for a Groq account at Groq.
2.Obtain your API key from the Groq dashboard.
3.Add the API key to the app.py file.
**Slack Webhook Integration:**

1.Go to the Slack API (Slack API).
2.Create a new app and enable Incoming Webhooks.
3.Add a webhook to a channel and copy the generated URL.
4.Add this URL to the app.py file.

**Run the Application**


    streamlit run app.py
**Project Files**

app.py: Main application script.
scrape.py: Script for web scraping competitor data.
reviews.csv: Sample reviews data for sentiment analysis.
competitor_data.csv: Sample competitor data for analysis.
requirements.txt: List of dependencies.

**Usage**

1.Launch the Streamlit app.
2.Select a product from the sidebar.
3.View competitor analysis, sentiment trends, and discount forecasts.
4.Get strategic recommendations and real-time Slack notifications.




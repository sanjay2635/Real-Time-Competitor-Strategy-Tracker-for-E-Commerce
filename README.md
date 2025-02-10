# Real-Time-Competitor-Strategy-Tracker-for-E-Commerce

## Project Overview
<img width="959" alt="image" src="https://github.com/user-attachments/assets/48694572-4566-440c-96f1-084e72240ea9" />

![WhatsApp Image 2025-01-28 at 18 57 55_a476f785](https://github.com/user-attachments/assets/2625cd24-7ff9-4531-8bb6-e2cf640e4786)
![WhatsApp Image 2025-01-28 at 18 58 11_a10e35fb](https://github.com/user-attachments/assets/941818ff-e0ef-4484-8eba-883a74a37568)

![WhatsApp Image 2025-01-28 at 18 58 47_f23dfd68](https://github.com/user-attachments/assets/4f59b05e-6cd1-4fff-b1ef-88c0570bdf73)





This project focuses on creating a real-time competitive intelligence tool for e-commerce businesses. It provides actionable insights by monitoring competitor pricing, discount strategies, and customer sentiment. The solution leverages:

- **Machine Learning**: Predictive modeling with ARIMA.
- **LLMs**: Sentiment analysis using Hugging Face Transformer and Groq.
- **Integration**: Slack notifications for real-time updates.

## Features

1. **Competitor Data Aggregation**: Track pricing and discount strategies.
2. **Sentiment Analysis**: Analyze customer reviews for actionable insights.
3. **Predictive Modeling**: Forecast competitor discounts.
4. **Slack Integration**: Get real-time notifications on competitor activity.

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <repository-url>
cd <repository-directory>
```

### 2. Install Dependencies
Install the required Python libraries using pip:
```bash
pip install -r requirements.txt
```

### 3. Configure API Keys
#### Groq API Key:
1. Sign up for a Groq account at [Groq](https://groq.com).
2. Obtain your API key from the Groq dashboard.
3. Add the API key to the `app.py` file.

#### Slack Webhook Integration:
1. Go to the [Slack API](https://api.slack.com/).
2. Create a new app and enable Incoming Webhooks.
3. Add a webhook to a channel and copy the generated URL.
4. Add this URL to the `app1.py` file.

### 4. Run the Application
Run the Streamlit app:
```bash
streamlit run app1.py
```

---

## Project Files

- **app.py**: Main application script.
- **scrape.py**: Script for web scraping competitor data.
- **reviews.csv**: Sample reviews data for sentiment analysis.
- **competitor_data.csv**: Sample competitor data for analysis.
- **requirements.txt**: List of dependencies.

---

## Usage

1. Launch the Streamlit app.
2. Select a product from the sidebar.
3. View competitor analysis, sentiment trends, and discount forecasts.
4. Get strategic recommendations and real-time Slack notifications.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## Contact

**Developer:** Sanjay Kumar N  
**Email:** nsanjaykumarofficial@gmail.com  
---

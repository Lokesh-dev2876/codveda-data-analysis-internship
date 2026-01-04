# Level 3 – Task 2: Time Series Analysis on Stock Market Data

## Executive Summary
This project performs **time series analysis** on historical stock market data to analyze price trends, moving averages, and return volatility.  
The objective is to extract meaningful insights from temporal financial data that can support investment analysis and business decision-making.

A single stock symbol (**AAPL**) is selected from a multi-stock dataset to ensure accurate and interpretable time series analysis.

---

## Dataset Overview
- **Dataset Name:** Stock Prices Dataset  
- **File:** `stock_prices.csv`  
- **Source Type:** Historical equity market data  
- **Selected Stock:** AAPL (Apple Inc.)

### Key Features
- `symbol` – Stock ticker
- `date` – Trading date
- `open`, `high`, `low`, `close` – Price indicators
- `volume` – Trading volume

---

## Technologies Used
- **Programming Language:** Python  
- **Libraries:**
  - Pandas – Data manipulation
  - NumPy – Numerical operations
  - Matplotlib – Data visualization
  - Seaborn – Statistical plotting

---

## Methodology

### 1. Data Ingestion
- Loaded the dataset using Pandas.
- Inspected structure and validated column consistency.

### 2. Data Filtering
- Filtered records for a single stock symbol (AAPL) to maintain time series integrity.

### 3. Date Processing
- Converted the `date` column to datetime format.
- Set the date as the index to enable time-based analysis.

### 4. Trend Analysis
- Visualized closing price trends over time to identify long-term movement.

### 5. Moving Average Analysis
- Computed 20-day and 50-day moving averages.
- Compared moving averages against actual prices to assess trend strength.

### 6. Volatility Analysis
- Calculated daily returns using percentage change.
- Visualized return fluctuations to understand price volatility.

---

## Project Structure
Level 3/
└── Task 2/
├── Dataset/
│ └── stock_prices.csv
├── Outputs/
│ ├── price_trend.png
│ ├── moving_average.png
│ └── returns_plot.png
├── time_series_analysis.py
├── requirements.txt
└── README.md

yaml
Copy code

---

## Deliverables
- **price_trend.png** – Time-based stock price movement  
- **moving_average.png** – 20-day and 50-day moving averages  
- **returns_plot.png** – Daily return volatility visualization  

All outputs are stored in the `Outputs/` directory.

---

## Key Insights
- Time series trends reveal long-term price direction.
- Moving averages smooth short-term fluctuations and highlight market momentum.
- Daily returns help measure volatility and investment risk.

---

## Business Relevance
Time series analysis is critical for:
- Financial forecasting
- Risk assessment
- Investment strategy planning
- Market behavior analysis

The techniques applied in this project are widely used in finance, analytics, and quantitative research.

---

## Conclusion
This task demonstrates the practical application of time series analysis on real-world stock market data.  
By combining trend visualization, moving averages, and volatility analysis, the project provides a structured approach to understanding financial time-dependent data.

---

## Author
**Lokesh P**  
Data Analysis Intern  
Codveda Technologies
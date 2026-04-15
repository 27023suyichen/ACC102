# Stock Performance Analyzer

**ACC102 Mini Assignment - Track 4: Interactive Data Analysis Tool**

---

## 📋 Project Overview

This project is an interactive stock performance analysis tool designed for individual investors, finance students, and small business owners. The tool provides comprehensive analysis of stock performance metrics including price trends, volatility, risk-return profiles, and correlation analysis.

### Target Users
- Individual investors seeking quick stock performance comparison
- Finance students learning about stock analysis
- Small business owners considering stock investments

### Business Relevance
Stock market analysis is crucial for investment decision-making. Understanding price trends, volatility, and comparative performance helps investors optimize their portfolios and manage risk effectively.

---

## 🚀 Features

- **Multi-Stock Analysis**: Analyze up to 7 major US stocks across different sectors
- **Interactive Dashboard**: Real-time data visualization with Streamlit
- **Comprehensive Metrics**: 
  - Price trends and normalized performance
  - Descriptive statistics
  - Risk metrics (volatility, Sharpe ratio, max drawdown)
  - Correlation analysis
- **Technical Indicators**: Moving averages and Bollinger bands
- **Data Export**: Download analysis results as CSV files

---

## 📁 Project Structure

```
acc102-stock-analyzer/
├── README.md                 # Project documentation
├── requirements.txt          # Python dependencies
├── notebook.ipynb           # Jupyter Notebook with full analysis
├── app.py                   # Streamlit application
├── data/                    # Data directory
│   └── (generated CSV files)
├── figures/                 # Generated figures
│   └── (generated PNG files)
└── src/                     # Source modules (if any)
```

---

## 🔧 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/acc102-stock-analyzer.git
   cd acc102-stock-analyzer
   ```

2. **Create virtual environment (recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---

## 💻 Usage

### Running the Jupyter Notebook

1. Start Jupyter Notebook:
   ```bash
   jupyter notebook
   ```

2. Open `notebook.ipynb`

3. Run all cells to:
   - Download stock data from Yahoo Finance
   - Perform data cleaning and transformation
   - Generate statistical analysis
   - Create visualizations
   - Save results to CSV files

### Running the Streamlit App

1. Navigate to the project directory:
   ```bash
   cd acc102-stock-analyzer
   ```

2. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

3. The app will open in your default web browser at `http://localhost:8501`

### Streamlit App Features

1. **Stock Selection**: Choose from 7 major US stocks
2. **Time Period**: Select analysis period (1 month to 2 years)
3. **Technical Indicators**: Toggle moving averages and Bollinger bands
4. **Interactive Charts**: 
   - Normalized performance comparison
   - Individual stock analysis with technical indicators
   - Risk-return scatter plot
   - Correlation heatmap
5. **Data Tables**: View and download statistical summaries

---

## 📊 Data Source

- **Source**: Yahoo Finance
- **Library**: yfinance
- **Access Date**: April 2026
- **Stocks Analyzed**:
  - AAPL (Apple Inc.) - Technology
  - MSFT (Microsoft Corporation) - Technology
  - JPM (JPMorgan Chase & Co.) - Finance
  - BAC (Bank of America Corporation) - Finance
  - KO (The Coca-Cola Company) - Consumer
  - WMT (Walmart Inc.) - Consumer
  - JNJ (Johnson & Johnson) - Healthcare

---

## 📈 Analysis Components

### 1. Data Acquisition and Cleaning
- Download historical stock prices from Yahoo Finance
- Handle missing values using forward and backward fill
- Calculate daily returns

### 2. Descriptive Statistics
- Start/End prices
- Mean, standard deviation, min, max
- Total returns

### 3. Risk Metrics
- Daily and annualized volatility
- Sharpe ratio
- Maximum drawdown

### 4. Visualizations
- Normalized price trends
- Price distribution box plots
- Total returns comparison
- Risk-return scatter plot
- Correlation heatmap
- Moving averages with Bollinger bands

---

## 📝 Key Findings

The analysis provides insights into:
- Best and worst performing stocks
- Risk-return trade-offs
- Stock correlations for portfolio diversification
- Volatility comparisons across sectors

---

## 🔒 Limitations

1. **Data Limitations**: Analysis based on historical data; past performance does not guarantee future results
2. **Simplified Metrics**: Sharpe ratio uses simplified calculation with assumed risk-free rate
3. **Limited Stocks**: Only 7 stocks analyzed; results may not represent broader market
4. **No Transaction Costs**: Analysis does not account for trading fees or taxes

---

## 🛠️ Technical Stack

- **Python 3.8+**
- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computations
- **matplotlib**: Data visualization
- **seaborn**: Statistical visualization
- **yfinance**: Yahoo Finance data API
- **streamlit**: Interactive web application framework
- **Jupyter Notebook**: Interactive development environment

---

## 📄 License

This project is created for educational purposes as part of ACC102 Mini Assignment.

---

## 👤 Author

- **Course**: ACC102 - Mini Assignment
- **Track**: Track 4 - Interactive Data Analysis Tool
- **Date**: April 2026

---

## 🙏 Acknowledgments

- Yahoo Finance for providing free stock data
- Streamlit for the interactive web framework
- XJTLU IBSS for the assignment guidance

# Reflective Report

## Stock Performance Analyzer - ACC102 Mini Assignment (Track 4)

**Student ID:** [Your Student ID]  
**Date:** April 2026  
**Word Count:** ~650 words

---

### Introduction and Problem Definition

This project aimed to develop an interactive stock performance analysis tool that addresses a common challenge faced by individual investors: the difficulty of comparing stock performance across different companies and sectors efficiently. The target users include individual investors seeking quick stock comparisons, finance students learning about stock analysis, and small business owners considering stock investments. The business relevance of this project lies in its practical application for investment decision-making, where understanding price trends, volatility, and comparative performance helps investors optimize their portfolios and manage risk effectively.

The decision to focus on stock analysis was driven by the universal relevance of financial markets in business education and the practical value such a tool provides to users. By selecting stocks from different sectors (Technology, Finance, Consumer, and Healthcare), the tool offers diversified insights that can inform portfolio construction decisions.

---

### Technical Implementation and Challenges

The Python implementation involved several key components: data acquisition using the yfinance library, data cleaning and transformation using pandas, statistical analysis including return calculations and risk metrics, and visualization using matplotlib and seaborn. The most significant technical challenge was handling the multi-index DataFrame structure returned by yfinance when downloading data for multiple stocks simultaneously. This was resolved by carefully extracting the Adjusted Close prices and implementing proper data cleaning procedures including forward and backward fill for missing values.

Another challenge was ensuring the Streamlit application could handle dynamic user inputs gracefully. The implementation uses Streamlit's caching mechanism (`@st.cache_data`) to optimize data retrieval performance and prevent unnecessary API calls. The correlation analysis required careful handling of edge cases, particularly when users select fewer than two stocks.

The code structure follows best practices with well-documented functions, clear parameter descriptions, and modular design that separates data processing from visualization logic. This approach makes the code maintainable and allows for future extensions.

---

### Analysis and Insights

The analysis revealed several meaningful insights about the selected stocks. The risk-return analysis demonstrated the classic trade-off between potential returns and volatility, with technology stocks generally showing higher returns but also higher volatility compared to consumer staples. The correlation analysis provided valuable information for portfolio diversification, showing that stocks within the same sector tend to move together, while cross-sector combinations offer better diversification benefits.

The Sharpe ratio calculations allowed for risk-adjusted performance comparison, revealing that some stocks with lower absolute returns might actually offer better risk-adjusted performance. This insight is particularly valuable for investors who prioritize consistent returns over high-risk, high-reward strategies.

---

### Product Design and User Focus

The Streamlit application was designed with user experience as a primary consideration. The interface features a clean sidebar for configuration, intuitive stock selection, and tabbed navigation for different analysis views. The dashboard presents key metrics prominently, allowing users to quickly grasp essential information before diving into detailed analysis.

Interactive elements such as stock selection dropdowns, time period choices, and technical indicator toggles provide users with customization options without overwhelming them with complexity. The ability to download analysis results as CSV files adds practical value for users who want to perform further analysis or keep records.

---

### Limitations and Future Improvements

Several limitations should be acknowledged. First, the analysis is based on historical data, and past performance does not guarantee future results. Second, the Sharpe ratio calculation uses a simplified approach with an assumed risk-free rate. Third, the tool currently analyzes only seven stocks, which may not represent broader market trends. Fourth, transaction costs and taxes are not considered in the return calculations.

Future improvements could include expanding the stock universe, adding more technical indicators, implementing portfolio optimization features, and incorporating real-time data updates. Additionally, adding benchmark comparison (e.g., S&P 500) would provide better context for individual stock performance.

---

### AI Disclosure

**AI Tool Used:** Claude (Anthropic)  
**Model/Version:** Claude 3.5 Sonnet  
**Purpose:** Code structure guidance, documentation writing assistance, and debugging support  
**Verification:** All code was tested and verified to work correctly. The analysis logic and financial calculations were reviewed for accuracy.

The AI assistance was primarily used for:
1. Structuring the project documentation
2. Providing code templates for Streamlit applications
3. Assisting with error handling patterns
4. Improving code documentation and comments

All generated code was reviewed, tested, and modified as needed to ensure correctness and alignment with the assignment requirements.

---

### Conclusion

This project successfully delivered an interactive stock analysis tool that meets the needs of the target users. The combination of Jupyter Notebook for detailed analysis and Streamlit for interactive exploration provides both depth and accessibility. The project demonstrates a coherent workflow from problem definition through data acquisition, analysis, and user-facing output, fulfilling the core requirements of the ACC102 Mini Assignment Track 4.

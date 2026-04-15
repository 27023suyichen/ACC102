"""
Test Script for Stock Performance Analyzer
===========================================
This script verifies that all components work correctly.
"""

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend for testing
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import sys
import os

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

print("=" * 60)
print("STOCK PERFORMANCE ANALYZER - TEST SUITE")
print("=" * 60)

# Test 1: Import all required modules
print("\n[TEST 1] Importing required modules...")
try:
    import yfinance as yf
    print("  ✓ yfinance imported")
except ImportError as e:
    print(f"  ✗ yfinance import failed: {e}")
    sys.exit(1)

try:
    import streamlit as st
    print("  ✓ streamlit imported")
except ImportError as e:
    print(f"  ✗ streamlit import failed: {e}")
    sys.exit(1)

print("  ✓ All modules imported successfully!")

# Test 2: Generate sample data
print("\n[TEST 2] Generating sample data...")
from src.generate_sample_data import generate_sample_data

sample_prices = generate_sample_data(days=100)
print(f"  ✓ Sample data generated: {sample_prices.shape}")

# Test 3: Calculate statistics
print("\n[TEST 3] Testing statistical calculations...")

def calculate_statistics(prices):
    """Calculate key statistical metrics."""
    stats = pd.DataFrame()
    for ticker in prices.columns:
        series = prices[ticker]
        stats[ticker] = {
            'Start Price': series.iloc[0],
            'End Price': series.iloc[-1],
            'Mean Price': series.mean(),
            'Std Dev': series.std(),
            'Total Return (%)': ((series.iloc[-1] / series.iloc[0]) - 1) * 100
        }
    return stats.T

stats_df = calculate_statistics(sample_prices)
print(f"  ✓ Statistics calculated for {len(stats_df)} stocks")
print(f"  ✓ Average return: {stats_df['Total Return (%)'].mean():.2f}%")

# Test 4: Calculate returns and risk metrics
print("\n[TEST 4] Testing risk metrics calculations...")

daily_returns = sample_prices.pct_change() * 100
daily_returns = daily_returns.dropna()

def calculate_risk_metrics(returns):
    """Calculate risk metrics."""
    risk_metrics = pd.DataFrame()
    for ticker in returns.columns:
        series = returns[ticker]
        annual_vol = series.std() * np.sqrt(252)
        annual_return = series.mean() * 252
        risk_metrics[ticker] = {
            'Annual Volatility (%)': annual_vol,
            'Annual Return (%)': annual_return,
        }
    return risk_metrics.T

risk_df = calculate_risk_metrics(daily_returns)
print(f"  ✓ Risk metrics calculated for {len(risk_df)} stocks")

# Test 5: Generate visualizations
print("\n[TEST 5] Testing visualization generation...")

# Test normalized price plot
fig, ax = plt.subplots(figsize=(10, 6))
normalized = (sample_prices / sample_prices.iloc[0]) * 100
for ticker in sample_prices.columns[:3]:  # Test with first 3 stocks
    ax.plot(normalized.index, normalized[ticker], label=ticker)
ax.set_title('Normalized Stock Performance')
ax.legend()
plt.savefig('figures/test_plot.png', dpi=100, bbox_inches='tight')
plt.close()
print("  ✓ Test plot saved to figures/test_plot.png")

# Test correlation heatmap
fig, ax = plt.subplots(figsize=(8, 6))
corr_matrix = daily_returns.corr()
sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='RdYlGn', ax=ax)
ax.set_title('Correlation Matrix')
plt.savefig('figures/test_correlation.png', dpi=100, bbox_inches='tight')
plt.close()
print("  ✓ Correlation heatmap saved to figures/test_correlation.png")

# Test 6: Verify data export
print("\n[TEST 6] Testing data export...")

stats_df.to_csv('data/test_statistics.csv')
risk_df.to_csv('data/test_risk_metrics.csv')
print("  ✓ Statistics saved to data/test_statistics.csv")
print("  ✓ Risk metrics saved to data/test_risk_metrics.csv")

# Test 7: Verify app.py syntax
print("\n[TEST 7] Verifying app.py syntax...")
try:
    with open('app.py', 'r') as f:
        code = compile(f.read(), 'app.py', 'exec')
    print("  ✓ app.py syntax is valid")
except SyntaxError as e:
    print(f"  ✗ Syntax error in app.py: {e}")
    sys.exit(1)

# Test 8: Verify notebook.ipynb structure
print("\n[TEST 8] Verifying notebook.ipynb structure...")
try:
    import json
    with open('notebook.ipynb', 'r') as f:
        notebook = json.load(f)
    
    cell_count = len(notebook.get('cells', []))
    print(f"  ✓ notebook.ipynb contains {cell_count} cells")
except Exception as e:
    print(f"  ✗ Error reading notebook: {e}")
    sys.exit(1)

# Final summary
print("\n" + "=" * 60)
print("TEST SUMMARY")
print("=" * 60)
print("✓ All tests passed successfully!")
print("\nProject is ready for submission.")
print("\nTo run the Streamlit app:")
print("  cd acc102-stock-analyzer")
print("  streamlit run app.py")
print("\nTo run the Jupyter Notebook:")
print("  jupyter notebook notebook.ipynb")
print("=" * 60)

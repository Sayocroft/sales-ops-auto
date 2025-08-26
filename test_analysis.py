#!/usr/bin/env python3
"""
Quick test script to validate the analysis approach and identify issues
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from datetime import datetime

def test_basic_data_loading():
    """Test if data can be loaded properly"""
    print("=== TESTING DATA LOADING ===")
    
    # Use relative paths
    data_path = os.path.join(os.getcwd(), 'data')
    
    try:
        # Load datasets
        accounts_df = pd.read_csv(os.path.join(data_path, "accounts.csv"))
        sales_pipeline_df = pd.read_csv(os.path.join(data_path, "sales_pipeline.csv"))
        
        print(f"✅ Accounts data loaded: {accounts_df.shape}")
        print(f"✅ Sales pipeline data loaded: {sales_pipeline_df.shape}")
        return sales_pipeline_df, accounts_df
        
    except Exception as e:
        print(f"❌ Data loading failed: {e}")
        return None, None

def analyze_time_series_feasibility(sales_df):
    """Analyze if time series forecasting is feasible"""
    print("\n=== TIME SERIES FEASIBILITY ANALYSIS ===")
    
    # Convert dates and filter won deals
    sales_df['close_date'] = pd.to_datetime(sales_df['close_date'], errors='coerce')
    won_deals = sales_df[sales_df['deal_stage'] == 'Won'].copy()
    won_deals = won_deals.dropna(subset=['close_date', 'close_value'])
    
    # Aggregate by month
    monthly_revenue = won_deals.groupby(won_deals['close_date'].dt.to_period('M'))['close_value'].sum()
    
    print(f"📊 Monthly data points available: {len(monthly_revenue)}")
    print(f"📅 Date range: {monthly_revenue.index.min()} to {monthly_revenue.index.max()}")
    
    # Assessment
    if len(monthly_revenue) < 12:
        print("❌ INSUFFICIENT DATA: Less than 1 year of data")
        feasibility = "Not feasible"
    elif len(monthly_revenue) < 24:
        print("⚠️  LIMITED DATA: Less than 2 years - forecasting will be unreliable")
        feasibility = "Limited"
    else:
        print("✅ SUFFICIENT DATA: 2+ years available")
        feasibility = "Feasible"
    
    return monthly_revenue, feasibility

def analyze_pipeline_balance(sales_df):
    """Analyze pipeline balance"""
    print("\n=== PIPELINE BALANCE ANALYSIS ===")
    
    stage_counts = sales_df['deal_stage'].value_counts()
    stage_pcts = sales_df['deal_stage'].value_counts(normalize=True) * 100
    
    print("Deal Stage Distribution:")
    for stage in stage_counts.index:
        print(f"  {stage}: {stage_counts[stage]} deals ({stage_pcts[stage]:.1f}%)")
    
    # Analysis
    won_pct = stage_pcts.get('Won', 0)
    prospecting_pct = stage_pcts.get('Prospecting', 0)
    closed_pct = stage_pcts.get('Won', 0) + stage_pcts.get('Lost', 0)
    
    print(f"\n📊 Analysis:")
    print(f"  Won deals: {won_pct:.1f}%")
    print(f"  Prospecting: {prospecting_pct:.1f}%") 
    print(f"  Total closed: {closed_pct:.1f}%")
    
    # Assessment
    issues = []
    if closed_pct > 70:
        issues.append("❌ HIGH CLOSED %: This appears to be historical data, not live pipeline")
    if prospecting_pct < 15:
        issues.append("⚠️  LOW PROSPECTING: Insufficient top-of-funnel activity")
    if won_pct > 40:
        issues.append("❌ HIGH WON %: Suggests historical closed deals, not active pipeline")
    
    if issues:
        print("\n🚨 Issues identified:")
        for issue in issues:
            print(f"  {issue}")
    else:
        print("\n✅ Pipeline appears balanced")
    
    return stage_pcts

def test_simple_forecasting(monthly_revenue):
    """Test simple forecasting approach instead of complex models"""
    print("\n=== SIMPLE FORECASTING TEST ===")
    
    if len(monthly_revenue) < 6:
        print("❌ Insufficient data for any forecasting")
        return
    
    # Simple moving average
    window = min(3, len(monthly_revenue) - 1)
    ma = monthly_revenue.rolling(window=window).mean()
    
    # Simple trend calculation
    x = np.arange(len(monthly_revenue))
    y = monthly_revenue.values
    trend_slope = np.polyfit(x, y, 1)[0]
    
    print(f"📈 Trend slope: ${trend_slope:,.0f} per month")
    print(f"📊 {window}-month moving average (last): ${ma.iloc[-1]:,.0f}")
    print(f"💡 Simple next month forecast: ${ma.iloc[-1] + trend_slope:,.0f}")
    
    print("\n✅ Simple forecasting approach is more appropriate for this data size")

def main():
    """Run comprehensive analysis test"""
    print("🔍 SALES OPS ANALYSIS VALIDATION")
    print("=" * 50)
    
    # Test data loading
    sales_df, accounts_df = test_basic_data_loading()
    if sales_df is None:
        return
    
    # Test time series feasibility  
    monthly_revenue, feasibility = analyze_time_series_feasibility(sales_df)
    
    # Test pipeline analysis
    stage_pcts = analyze_pipeline_balance(sales_df)
    
    # Test simple forecasting
    test_simple_forecasting(monthly_revenue)
    
    # Summary
    print("\n" + "=" * 50)
    print("📋 SUMMARY OF FINDINGS")
    print("=" * 50)
    print(f"📊 Data Quality: {'✅ Good' if len(sales_df) > 1000 else '⚠️ Limited'}")
    print(f"📈 Time Series Forecasting: {feasibility}")
    print(f"🎯 Pipeline Analysis: {'✅ Valid' if stage_pcts.get('Won', 0) < 40 else '❌ Historical data'}")
    print("\n💡 Recommendation: Focus on historical performance analysis rather than complex forecasting")

if __name__ == "__main__":
    main()
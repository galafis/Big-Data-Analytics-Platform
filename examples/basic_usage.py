#!/usr/bin/env python3
"""
Example script demonstrating usage of the Big Data Analytics Platform

This script shows how to:
1. Generate dummy data
2. Analyze sales by category
3. Export results to multiple formats
"""

import sys
sys.path.insert(0, 'src')

from data_processor import (
    generate_dummy_data,
    analyze_sales_by_category,
    export_data
)

def main():
    """Run example data analysis workflow."""
    
    print("=" * 60)
    print("BIG DATA ANALYTICS PLATFORM - EXAMPLE USAGE")
    print("=" * 60)
    
    # Step 1: Generate sample data
    print("\n📊 Step 1: Generating sample data...")
    df = generate_dummy_data(num_rows=50)
    print(f"✅ Generated {len(df)} transactions")
    print("\nSample data:")
    print(df.head(10))
    
    # Step 2: Analyze sales by category
    print("\n📈 Step 2: Analyzing sales by category...")
    sales_summary = analyze_sales_by_category(df)
    print("✅ Analysis complete")
    print("\nSales Summary:")
    print(sales_summary)
    
    # Step 3: Calculate additional metrics
    print("\n📊 Step 3: Calculating additional metrics...")
    total_revenue = sales_summary['total_sales_sum'].sum()
    avg_transaction = sales_summary['average_sale_price'].mean()
    total_transactions = sales_summary['number_of_transactions'].sum()
    
    print(f"Total Revenue: ${total_revenue:,.2f}")
    print(f"Average Transaction: ${avg_transaction:,.2f}")
    print(f"Total Transactions: {total_transactions}")
    
    # Step 4: Export results
    print("\n💾 Step 4: Exporting results...")
    export_data(sales_summary, 'data/example_output', formats=['csv', 'json'])
    print("✅ Data exported to:")
    print("   - data/example_output.csv")
    print("   - data/example_output.json")
    
    print("\n" + "=" * 60)
    print("✅ Example completed successfully!")
    print("=" * 60)
    
    return 0

if __name__ == "__main__":
    sys.exit(main())

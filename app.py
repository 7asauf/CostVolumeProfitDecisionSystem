import streamlit as st

# Page Configuration
st.set_page_config(page_title="Module 4: CVP Analysis", layout="wide")

# App Header
st.title("📊 Cost-Volume-Profit (CVP) Decision-Support System")
st.caption("Accounting Software Project — Module 4 | Group 4")
st.markdown("---")

# Sidebar: Dynamic User Inputs
st.sidebar.header("🕹️ Input Parameters")
selling_price = st.sidebar.number_input("Selling Price per Unit ($)", min_value=0.01, value=50.0, step=1.0)
variable_cost = st.sidebar.number_input("Variable Cost per Unit ($)", min_value=0.0, value=30.0, step=1.0)
fixed_costs = st.sidebar.number_input("Total Fixed Costs ($)", min_value=0.0, value=10000.0, step=500.0)
target_profit = st.sidebar.number_input("Target Profit ($)", min_value=0.0, value=5000.0, step=500.0)
expected_units = st.sidebar.number_input("Expected Unit Sales", min_value=0, value=600, step=10)

# Accounting Calculation Logic
cm_per_unit = selling_price - variable_cost

if cm_per_unit <= 0:
    st.error("⚠️ Selling Price must be strictly greater than Variable Cost per Unit.")
else:
    cm_ratio = cm_per_unit / selling_price
    be_units = fixed_costs / cm_per_unit
    be_sales = fixed_costs / cm_ratio
    
    target_units = (fixed_costs + target_profit) / cm_per_unit
    target_sales = (fixed_costs + target_profit) / cm_ratio
    
    mos_units = expected_units - be_units
    mos_dollars = mos_units * selling_price
    mos_ratio = (mos_units / expected_units * 100) if expected_units > 0 else 0.0

    # Display Results
    st.subheader("💡 Analysis & Results")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("**Contribution Margin**")
        st.metric("CM per Unit", f"${cm_per_unit:.2f}")
        st.metric("CM Ratio", f"{cm_ratio * 100:.2f}%")

    with col2:
        st.markdown("**Break-Even Point**")
        st.metric("Break-Even Units", f"{be_units:,.2f} units")
        st.metric("Break-Even Sales", f"${be_sales:,.2f}")

    with col3:
        st.markdown("**Target Profit & Safety Margin**")
        st.metric("Target Profit Volume", f"{target_units:,.2f} units")
        st.metric("Margin of Safety ($)", f"${mos_dollars:,.2f}", delta=f"{mos_ratio:.1f}% ratio")

    # Sensitivity / What-If Breakdown Table
    st.markdown("---")
    st.subheader("📋 Dynamic Summary Table")
    st.table({
        "Metric": [
            "Selling Price", "Variable Cost", "Unit Contribution Margin", 
            "Break-Even Sales ($)", "Target Sales Volume ($)", "Margin of Safety ($)"
        ],
        "Value": [
            f"${selling_price:.2f}", f"${variable_cost:.2f}", f"${cm_per_unit:.2f}", 
            f"${be_sales:,.2f}", f"${target_sales:,.2f}", f"${mos_dollars:,.2f}"
        ]
    })



    import pandas as pd

# dynamic chart 
st.markdown("---")
st.subheader("📈 Visual CVP Breakdown")

units_range = list(range(0, int(be_units * 2) + 10, max(1, int(be_units / 10))))
df = pd.DataFrame({
    "Units Sold": units_range,
    "Total Revenue": [u * selling_price for u in units_range],
    "Total Costs": [fixed_costs + (u * variable_cost) for u in units_range],
    "Fixed Costs": [fixed_costs for _ in units_range]
})

st.line_chart(df.set_index("Units Sold"))
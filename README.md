# Module 4: Cost-Volume-Profit (CVP) Decision-Support System

**Course:** Accounting (HUM 4247)
**Assigned Module:** Module 4 — Cost-Volume-Profit (CVP) Analysis
**Group:** Group 4

---

## 1. Project Overview & Platform

This application is an automated decision-support tool built to eliminate manual calculation of key accounting metrics. Given basic unit and cost parameters, the system dynamically calculates contribution margins, break-even thresholds, target profit requirements, and safety margins to enable real-time "what-if" sensitivity analysis for business planning.

* **Language / Runtime:** Python 3.9+
* **Framework / Libraries:** Streamlit, Pandas

---

## 2. Technical Installation & Setup

### Prerequisites

Ensure Python 3 is installed on your system.

### Installation

1. Open your terminal/command prompt and navigate to the project root directory.
2. Install the required dependencies:

   ```bash
   pip install streamlit pandas
   ```

   *(Note: If using macOS or a local virtual environment, run `.venv/bin/python -m pip install streamlit pandas`)*

### Running the Application

To launch the interactive web application, run:

```bash
streamlit run app.py
```

*(Or via virtual environment: `.venv/bin/python -m streamlit run app.py`)*

The system will launch automatically in your browser at `http://localhost:8501`.

---

## 3. Core Accounting Logic & Automated Formulas

The system relies strictly on dynamic formulas with zero hardcoded final values:

* **Contribution Margin (CM) per Unit:**

$$\text{CM per Unit} = \text{Selling Price} - \text{Variable Cost per Unit}$$

* **Contribution Margin (CM) Ratio:**

$$\text{CM Ratio} = \frac{\text{CM per Unit}}{\text{Selling Price}}$$

* **Break-Even Point (Units):**

$$\text{Break-Even Units} = \frac{\text{Total Fixed Costs}}{\text{CM per Unit}}$$

* **Break-Even Point (Sales Dollars):**

$$\text{Break-Even Sales (\$)} = \frac{\text{Total Fixed Costs}}{\text{CM Ratio}}$$

* **Target-Profit Sales Volume (Units):**

$$\text{Target Sales Volume} = \frac{\text{Total Fixed Costs} + \text{Target Profit}}{\text{CM per Unit}}$$

* **Margin of Safety ($):**

$$\text{Margin of Safety (\$)} = (\text{Expected Sales Volume} - \text{Break-Even Units}) \times \text{Selling Price}$$

---

## 4. Key System Assumptions

1. Unit selling price and unit variable cost remain constant throughout the relevant range of activity.
2. Total fixed costs remain constant within the relevant operating range.
3. All units produced are assumed to be sold (zero inventory change).
4. Multi-product considerations are modeled assuming a single composite product equivalent.
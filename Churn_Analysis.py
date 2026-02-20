import pandas as pd

df = pd.read_csv("telecom_customer_churn_dataset.csv")

print(df)

# ------------------Core Business Metrics-----------------------------------
# Number of Customers ----
Customer_Count = df["CustomerID"].count()
print(f"Customer Count: {Customer_Count}")

# Churn Rate -------
churned_df = df[df["Churn"] == "Yes"]
count_churned = churned_df["Churn"].count()
churned_rate = (count_churned/Customer_Count) * 100
print(f"Churned Rate: {churned_rate:.2f}%")


# Calculating Total Monthly Revenue ----
Total_Monthly_Revenue = df["MonthlyCharges"].sum()
print(f"Total Monthly Revenue: {Total_Monthly_Revenue}")


# Monthly Revenue at Risk (Churned Customer Revenue) -----
risked_revenue = churned_df["MonthlyCharges"].sum()
print(f"Monthly Revenue at Risk (Churned Customer){risked_revenue}")


# ----------------Insight (Contract-wise Churn)----------------------
# -------------------------Calculating Month_to_Month Churned Rate --------------------------------------

# Creating Month-to-Month Data Frame-----
month_df = df[df["ContractType"] == "Month-to-Month"]

# Caculating total month-to-month Customer ----
total_month_to_month_customer = len(month_df)

# Calculating total month-to-month churned customer -----
total_month_to_month_churned_customer = len(
    month_df[month_df["Churn"] == "Yes"])


# Calculating Month-t-Month Churned Rate ----
Churned_rate = (total_month_to_month_churned_customer /
                total_month_to_month_customer) * 100
print(f"Mont-to-Month Churned Rate: {Churned_rate:.2f}%")


# ------------------Calculating One Year Churn Rate ----------------------

# Creating One Year Data Frame ---
one_year_df = df[df["ContractType"] == "One Year"]

# Calculating total one year customer ---
total_one_year_customer = len(one_year_df)

# Calculating total one year churned customer ---
total_one_year_churned_customer = len(
    one_year_df[one_year_df["Churn"] == "Yes"])

# Calculating one year churned rate ---
one_year_churned_rate = (
    total_one_year_churned_customer/total_one_year_customer) * 100
print(f"One year Churned Rate: {one_year_churned_rate:.2f}%")


# ------------------Calculating Two Year Churn Rate ----------------------

# Creating Two Year Data Frame ---
two_year_df = df[df["ContractType"] == "Two Year"]

# Calculating total Two year customer ---
total_two_year_customer = len(two_year_df)

# Calculating total Two year churned customer ---
total_two_year_churned_customer = len(
    two_year_df[two_year_df["Churn"] == "Yes"])

# Calculating Two year churned rate ---
two_year_churned_rate = (
    total_two_year_churned_customer/total_two_year_customer) * 100
print(f"Two year Churned Rate: {two_year_churned_rate:.2f}%")


# -----------------------Revenue Risk Analysis------------------------------

# Creating Churned Customer Data Frame ----------
churned_df = df[df["Churn"] == "Yes"]

# Total Revenue From Churned Customer (Revenue Lost) ------
total_revnue_churned_customer = churned_df["TotalCharges"].sum()
print(f"Total Revenue From Churned Customer: {total_revnue_churned_customer}")

# Average Revenue Per Churn Customer -----------

# Method one --
churn_count = len(churned_df)
average = total_revnue_churned_customer/churn_count
print(f"Average Revenue Per Churn Customer: {average:.2f}")

# Method 2 --
average_revenue_churn_customer = churned_df["TotalCharges"].mean()
print(
    f"Average Revenue Per Churn Customer: {average_revenue_churn_customer:.2f}")


# Revenue Risk by Contract Type ---------------

revnue_risked_contract_type = churned_df.groupby("ContractType")[
    "TotalCharges"].sum()
print("Revenue Risked by Contract Type --")
print(revnue_risked_contract_type)


# ---------------------Deep-Dive Risk Factors-----------------------------------

# Churn by Internet Service -------

internet_service_churn = df.groupby("InternetService")[
    "Churn"].value_counts(normalize=True).unstack()
internet_service_churn["Churn Rate (%)"] = internet_service_churn["Yes"] * 100
print("Churn by Internet Service ---")
print(internet_service_churn)

# Churn by Tech Support -----------
tech_support_churn = df.groupby("TechSupport")[
    "Churn"].value_counts(normalize=True).unstack()
tech_support_churn["Churn Rate (%)"] = tech_support_churn["Yes"] * 100
print("Churn by Tech Support ---")
print(tech_support_churn)

# Churn by Payment Method ---------
payment_method_churn = df.groupby("PaymentMethod")[
    "Churn"].value_counts(normalize=True).unstack()
payment_method_churn["Churn Rate (%)"] = payment_method_churn["Yes"] * 100
print("Churn by Payment Method ---")
print(payment_method_churn)


# --------------------Revenue Saving Simulation------------------------------

# Creating Churned Data Frame
churned_df = df[df["Churn"] == "Yes"]

# Identifying month-to-month churn customer ----
mtm_churn = churned_df[churned_df["ContractType"] == "Month-to-Month"]
mtm_customer_count = len(mtm_churn)
mtm_revenue_loss = mtm_churn["TotalCharges"].sum()

print(f"Month-to-Month Customer Count: {mtm_customer_count}")
print(f"Month-to-Month Revenue Loss: {mtm_revenue_loss}")


# Assuming we Retain 25% -----------

retention_rate = 0.25

potential_saved_customer = mtm_customer_count * retention_rate
potential_saved_revenue = mtm_revenue_loss * retention_rate

print(f"Potential Saved Customer: {potential_saved_customer}")
print(f"Potential Saved Revenue: {potential_saved_revenue:.2f}")

import pandas as pd

def main():
    data = {
        "Date": ["2024-11-01", "2024-11-01", "2024-11-02", "2024-11-02", "2024-11-03"],
        "Product": ["A", "B", "A", "C", "B"],
        "Quantity Sold": [10, 5, 15, 8, 12],
        "Revenue": [100, 50, 150, 80, 120]
    }
    sales_df = pd.DataFrame(data)
    print(sales_df)
    total_revenue_per_product = sales_df.groupby("Product")["Revenue"].sum()
    print("Total Revenue per Product:")
    print(total_revenue_per_product)

if __name__ == "__main__":
    print("_________________________________________")
    print("SY-5, VedantBarhate, Rno-59")
    print("_________________________________________")
    main()
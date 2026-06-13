# Reducing Code Duplication

def print_order(name, chai_type): # parameter
    print(f"{name} ordered {chai_type} chai!")


print_order("Aman", "masala") # argument
print_order("Shivam", "Tulsi")



# Splitting Complex Tasks

def fetch_sales():
    print("Fetching the sales data")

def filter_valid_sales():
    print("Filtering valid sales data")

def summarize_data():
    print("Summarizing sales data")


def generate_report():
    fetch_sales()
    filter_valid_sales()
    summarize_data()
    print("Report is ready")


generate_report()
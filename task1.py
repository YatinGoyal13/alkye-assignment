import pandas as pd
from collections import Counter

def calculate_average_age(data):
    return round(data['age'].mean(), 1)

def find_most_common_domain(data):
    domains = data['email'].apply(lambda x: x.split('@')[1])
    domain_counts = Counter(domains)
    # print("Domain Counts:")
    # print(domain_counts)
    most_common_domain = domain_counts.most_common(1)
    return most_common_domain[0][0] if most_common_domain else None

def main():
    filename = 'data.csv'
    try:
        data = pd.read_csv(filename)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return
    # print("Data read from CSV:")
    # print(data)
    if data.empty:
        print("No data found in the CSV file.")
        return

    average_age = calculate_average_age(data)
    most_common_domain = find_most_common_domain(data)

    print(f"Average Age: {average_age}")
    print(f"Most Common Domain: {most_common_domain}")

if __name__ == "__main__":
    main()

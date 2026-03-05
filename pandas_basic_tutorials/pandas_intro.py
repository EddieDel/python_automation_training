import pandas as pd

data = {
    "name": ["John", "Mike", "Nick", "John", "George", "Sara", "Lisa", "Tom", "Anna", "Rex"],
    "department": ["IT", "Sales", "Sales", None, "Management", "IT", "HR", "HR", "Sales", "IT"],
    "salary": [3000, 4000, 2000, None, 9000, 3500, 2800, 3200, None, 3800],
    "years_experience": [2, 5, 1, 10, 15, 3, 4, 6, 7, 2],
    "location": ["Athens", "London", "Paris", "New York", "New York", "Athens", "London", "Paris", "Athens", "London"],
    "performance_score": [7.5, 8.2, 6.1, 9.4, 9.8, 7.8, 6.5, 7.2, 8.9, 7.1]
}

df = pd.DataFrame(data)

def clean_data(input_df):
    input_df = input_df.drop_duplicates()
    input_df["salary"] = input_df["salary"].fillna(0)
    input_df["department"] = input_df["department"].fillna("Unknown")
    return input_df

def filtering(input_df):
    higher_than_3k = input_df[input_df["salary"] > 3000]
    sorted_salary = input_df.sort_values("salary", ascending=False)
    mean_salary = input_df.groupby("department")["salary"].mean()

    print("Make more than 3k:\n", higher_than_3k)
    print("Sorted salaries:\n", sorted_salary)
    print("Mean salary by department:\n", mean_salary)

df_clean = clean_data(df)
df_clean.to_excel("output.xlsx", index=False)
filtering(df_clean)
import nbformat as nbf

# Create a new notebook
nb = nbf.v4.new_notebook()

nb.cells = [
    nbf.v4.new_markdown_cell("# Week 2 – Day 10: Pandas Setup & Practice\n"
                             "Focus: Create DataFrames, inspect, select/filter, read/write CSVs, and quick summaries.\n\n"
                             "PCAP™: Modules & Packages • PCPP1™: File Processing & Best Practices"),

    nbf.v4.new_code_cell("import pandas as pd\nimport numpy as np\nimport sys\n\n"
                         "print('Python:', sys.version)\n"
                         "print('pandas:', pd.__version__)\n"
                         "print('numpy:', np.__version__)"),

    nbf.v4.new_markdown_cell("## 1. Create a DataFrame"),
    nbf.v4.new_code_cell("data = {\n"
                         "    'Name': ['Alice', 'Bob', 'Charlie', 'David'],\n"
                         "    'Age': [25, 30, 35, 40],\n"
                         "    'Score': [85, 90, 88, 95]\n"
                         "}\n"
                         "df = pd.DataFrame(data)\n"
                         "df"),

    nbf.v4.new_markdown_cell("## 2. Inspect Structure & Summary"),
    nbf.v4.new_code_cell("df.info()"),
    nbf.v4.new_code_cell("df.describe()"),

    nbf.v4.new_markdown_cell("## 3. Select & Filter Data"),
    nbf.v4.new_code_cell("df['Name']"),
    nbf.v4.new_code_cell("df[['Name','Age']]"),
    nbf.v4.new_code_cell("df[df['Age'] > 30]"),

    nbf.v4.new_markdown_cell("## 4. Add Columns & Transform"),
    nbf.v4.new_code_cell("df['Passed'] = df['Score'] >= 90\n"
                         "df['AgeBucket'] = pd.cut(df['Age'], bins=[0,29,39,120], labels=['<30','30s','40+'])\n"
                         "df"),

    nbf.v4.new_markdown_cell("## 5. Sorting"),
    nbf.v4.new_code_cell("df.sort_values(by='Score', ascending=False)"),

    nbf.v4.new_markdown_cell("## 6. Read CSV (in-memory example)"),
    nbf.v4.new_code_cell("from io import StringIO\n"
                         "csv_text = StringIO('''Name,Age,Score\nEve,28,86\nFrank,31,77\nGrace,26,91\nHenry,42,88''')\n"
                         "df2 = pd.read_csv(csv_text)\n"
                         "df2"),

    nbf.v4.new_markdown_cell("## 7. Save to CSV"),
    nbf.v4.new_code_cell("df2.to_csv('day10_students.csv', index=False)\n"
                         "print('Wrote day10_students.csv')"),

    nbf.v4.new_markdown_cell("## 8. Groupby Aggregation"),
    nbf.v4.new_code_cell("df2['Passed'] = df2['Score'] >= 85\n"
                         "df2.groupby('Passed')['Score'].agg(['count','mean','min','max'])"),

    nbf.v4.new_markdown_cell("## 9. Simple Plot"),
    nbf.v4.new_code_cell("ax = df2['Score'].plot(kind='hist', bins=5, title='Day 10 – Score Distribution')\n"
                         "ax.set_xlabel('Score')"),
]

# Save notebook file
with open("Week2_Day10_Pandas.ipynb", "w", encoding="utf-8") as f:
    nbf.write(nb, f)

print("✅ Notebook created: Week2_Day10_Pandas.ipynb")

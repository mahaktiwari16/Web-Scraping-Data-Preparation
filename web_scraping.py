import requests
from bs4 import BeautifulSoup
import pandas as pd


# Step 1: Website URL
url = "https://books.toscrape.com/"


# Step 2: Send request to website
response = requests.get(url)


# Step 3: Check if website is accessible
if response.status_code == 200:

    # Step 4: Parse HTML
    soup = BeautifulSoup(response.text, "html.parser")


    # Step 5: Find all books
    books = soup.find_all(
        "article",
        class_="product_pod"
    )

    print("Number of books:", len(books))


    # Step 6: Create empty list
    data = []


    # Step 7: Extract information from each book
    for book in books:

        # Extract Title
        title = book.h3.a["title"]


        # Extract Price
        price = book.find(
            "p",
            class_="price_color"
        ).text.strip()


        # Extract Availability
        availability = book.find(
            "p",
            class_="instock availability"
        ).text.strip()


        # Extract Rating
        rating = book.find(
            "p",
            class_="star-rating"
        )["class"][1]


        # Store information
        data.append({
            "Title": title,
            "Price": price,
            "Availability": availability,
            "Rating": rating
        })


    # Step 8: Convert list into DataFrame
    df = pd.DataFrame(data)


    # Step 9: Check original data
    print("\nBefore cleaning:")
    print(df.head())


    # Step 10: Clean Price
    df["Price"] = df["Price"].str.replace(
        "£",
        "",
        regex=False
    )





    # Step 12: Display cleaned Price
    print("\nAfter cleaning Price:")
    print(df["Price"].head())


    # Step 13: Clean Price

df["Price"] = df["Price"].str.replace(
    r"[^\d.]",
    "",
    regex=True
)

df["Price"] = pd.to_numeric(df["Price"])

print("\nCleaned Price:")
print(df["Price"].head())

print("\nPrice data type:")
print(df["Price"].dtype)
# Step 14: Clean Rating

print("\nOriginal Rating:")
print(df["Rating"].head())


# Convert rating words into numbers
rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

df["Rating"] = df["Rating"].map(rating_map)


# Display cleaned rating
print("\nCleaned Rating:")
print(df["Rating"].head())


# Check data type
print("\nRating data type:")
print(df["Rating"].dtype)
# Step 15: Check missing values

print("\nMissing values:")
print(df.isnull().sum())


# Step 15: Handle Missing Values

print("\nMissing values before handling:")
print(df.isnull().sum())

if df.isnull().sum().sum() == 0:
    print("No missing values found.")
else:
    print("Missing values found.")
    # Step 16: Remove Duplicate Records

print("\nDuplicate rows before cleaning:")
print(df.duplicated().sum())

# Remove duplicate rows
df.drop_duplicates(inplace=True)

print("\nDuplicate rows after cleaning:")
print(df.duplicated().sum())

# Step 17: Save cleaned data to CSV

df.to_csv("books_cleaned.csv", index=False)

print("\nCSV file saved successfully!")
# Step 18: Basic Data Analysis

print("\nTotal number of books:")
print(len(df))
print("\nAverage price:")
print(df["Price"].mean())
print("\nHighest price:")
print(df["Price"].max())
print("\nLowest price:")
print(df["Price"].min())
print("\nAverage rating:")
print(df["Rating"].mean())
print("\nRating distribution:")
print(df["Rating"].value_counts().sort_index())
# Step 19: Final Data Verification

print("\nFinal cleaned data:")
print(df.head())
print("\nDataset shape:")
print(df.shape)
print("\nColumn names:")
print(df.columns)
print("\nFinal data types:")
print(df.dtypes)
print("\nFinal missing values:")
print(df.isnull().sum())
df.to_csv("books_cleaned.csv", index=False)

print("\nFinal cleaned dataset saved successfully!")
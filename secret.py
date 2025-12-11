import requests
from bs4 import BeautifulSoup

def print_google_doc_grid(url):
    response = requests.get(url)
    html = response.text

    soup = BeautifulSoup(html, "html.parser")

    # Find the table
    tables = soup.find_all("table")
    if not tables:
        print("No tables found in the document.")
        return

    table = tables[0]

    rows = table.find_all("tr")
    if len(rows) <= 1:
        print("Not enough rows (only header found).")
        return

    triples = []
    valid_chars = {"█", "░"}

    # Skip the header rows
    for row in rows[1:]:
        cols = row.find_all("td")
        if len(cols) < 3:
            continue  # not a proper data row

        def get_cell_text(td):
            # Match html structure: td > p > span
            span = td.find("span")
            if span:
                return span.get_text(strip=True)
            return td.get_text(strip=True)

        x_text = get_cell_text(cols[0])
        char_text = get_cell_text(cols[1])
        y_text = get_cell_text(cols[2])

        # Validate
        if not (x_text.isdigit() and y_text.isdigit() and char_text in valid_chars):
            continue

        x = int(x_text)
        y = int(y_text)
        char = char_text
        triples.append((x, y, char))

    if not triples:
        print("No valid coordinate triples found.")
        return

    # Build grid
    max_x = max(t[0] for t in triples)
    max_y = max(t[1] for t in triples)

    grid = [[" " for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    for x, y, char in triples:
        grid[y][x] = char

    # Print ASCII 
    for row in grid:
        print("".join(row))


print_google_doc_grid(
    "https://docs.google.com/document/d/e/2PACX-1vQiVT_Jj04V35C-YRzvoqyEYYzdXHcRyMUZCVQRYCu6gQJX7hbNhJ5eFCMuoX47cAsDW2ZBYppUQITr/pub"
)
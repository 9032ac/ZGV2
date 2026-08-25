import sys
import webbrowser
from urllib.parse import quote_plus

print("MultiSearch-tool, python")

titles = [
    "Table 1",
    "Table 2",
    "Table 3",
    "Table 4",
    "Table 5",
    "Table 6",
    "Table 7",
    "Table 8",
    "Table 9",
    "Table 10",
]

def search(query):
    query = query.strip()

    if not query:
        return False

    url = "https://www.google.com/search?q=" + quote_plus(query)

    try:
        if webbrowser.open_new_tab(url):
            return True

        return webbrowser.open(url)

    except Exception as error:
        print(f"\nCould not open browser: {error}")
        print(f"Search URL: {url}")
        return False

def search_all(queries):
    searched = 0

    for query in queries:
        if query.strip():
            if search(query):
                searched += 1

    return searched

def main():
    queries = []

    print("\nEnter your searches below.")
    print("Press Enter to leave a table empty.")
    print("Press Ctrl+C at any time to exit.\n")

    try:
        for title in titles:
            query = input(f"{title}: ")
            queries.append(query)

    except KeyboardInterrupt:
        print("\n\nExiting...")
        sys.exit(0)

    except EOFError:
        print("\n\nInput closed. Exiting...")
        sys.exit(0)

    if not any(query.strip() for query in queries):
        print("\nNo searches entered.")
        return

    print("\nOpening searches...")

    searched = search_all(queries)

    print(f"\nOpened {searched} search{'es' if searched != 1 else ''}.")

    try:
        input("\nPress Enter to exit...")
    except (KeyboardInterrupt, EOFError):
        pass

if __name__ == "__main__":
    main()

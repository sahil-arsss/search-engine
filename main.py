# main.py

from config import DEBUG


def initialize_system():
    """
    Initialize the search engine system.
    Later we will:
    - Load documents
    - Build or load index
    """
    if DEBUG:
        print("[DEBUG] Initializing system...")


def run_search_engine():
    """
    Entry point for running search engine.
    """
    print("Mini Search Engine Started 🚀")
    
    while True:
        query = input("\nEnter your search query (or type 'exit'): ")
        
        if query.lower() == "exit":
            print("Exiting search engine...")
            break
        
        # Placeholder (will connect later)
        print(f"Searching for: {query}")
        print("Results will appear here...")

if __name__ == "__main__":
    initialize_system()
    run_search_engine()
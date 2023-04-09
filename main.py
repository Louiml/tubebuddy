from youtube_api import youtube
from nlp_processing import process_query
from voice_recognition import listen_query
def main():
    while True:
        query = listen_query()
        if query:
            print(f"User query: {query}")
            processed_query = process_query(query)
        else:
            print("Sorry, I didn't understand that. Please try again.")

if __name__ == "__main__":
    main()

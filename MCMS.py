# MOVIES CATELOG MANAGEMENT SYSTEM
import sys
import time
import json

class MovieCatalog:
    def __init__(self, filename="movies_data.json"):
        self.filename = filename
        self.movies_list = self.load_from_file()

    def save_to_file(self):
        with open(self.filename, "w") as file:
            json.dump(self.movies_list, file, indent=4)

    def load_from_file(self):
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def display_movies(self):
        if not self.movies_list:
            print("\nNo movies available.")
            return
            
        print("\nMovies List=> ")
        for i, movie in enumerate(self.movies_list, start=1):
            print(f"{i}. {movie['Movie']}")

    def add_movie(self):
        while True:
            try:
                print()
                director = input("Enter the name of the director: ").capitalize()
                movie = input("Enter the name of the movie: ").title()
                date = int(input("Enter the release year of the movie: "))
                print()

                if date > 2025 or date < 1900:
                    print("Invalid date entered. Please enter a year between 1900 and 2025.")
                    continue
            except ValueError:
                print("Invalid value. Please enter numeric year.")
                continue

            new_movie = {
                "Director": director,
                "Movie": movie,
                "date": date
            }

            self.movies_list.append(new_movie)
            self.save_to_file()
            print(f"The Movie '{new_movie['Movie']}' has been successfully added to the list.")
            break

    def remove_movie(self):
        if not self.movies_list:
            print("\nNo movies to remove.")
            return

        print()
        for i, movie in enumerate(self.movies_list, start=1):
            print(f"{i}. {movie['Movie']}")

        try:
            print()
            remove_index = int(input("Enter the number of the movie you want to remove: ")) - 1
            print()
            if 0 <= remove_index < len(self.movies_list):
                removed_movie = self.movies_list.pop(remove_index)
                self.save_to_file()
                print(f"'{removed_movie['Movie']}' has been removed from the list.")
            else:
                print("Movie not found.")
        except ValueError:
            print("Please enter a numeric value.")

    def search_movies(self, search_key):
        print()
        search_key = search_key.capitalize()
        results = []
        for movie in self.movies_list:
            for key, value in movie.items():
                if key.lower() == search_key.lower() or str(value).lower() == search_key.lower():
                    results.append(movie)
                    break

        if results:
            print(f"Search results for '{search_key}':")
            for i, movie in enumerate(results, start=1):
                print(f"{i}. Director: {movie['Director']}, Movie: {movie['Movie']}, Year: {movie['date']}")
        else:
            print(f"No results found for '{search_key}'.")


def main():
    catalog = MovieCatalog()

    while True:
        print()
        print("Movie Catalog Management Tool".center(40, "+"))
        print()
        print("1- Movies list")
        print("2- Add Movies")
        print("3- Remove Movies")
        print("4- Search Movie")
        print("5- Exit")
        print()

        try:
            choice = int(input("Please enter your choice: "))
            print()
            print("+" * 40)

            if choice == 1:
                catalog.display_movies()
            elif choice == 2:
                catalog.add_movie()
            elif choice == 3:
                catalog.remove_movie()
            elif choice == 4:
                search = input("What are you looking for (Director, date, Movie): ").strip()
                catalog.search_movies(search)
            elif choice == 5:
                confirm = input("Are you sure you want to exit? (Yes/No): ").capitalize()
                if confirm == "Yes":
                    print("Exiting...")
                    time.sleep(2)
                    sys.exit()
                else:
                    print("Returning back to the menu...")
                    time.sleep(2)
            else:
                print("Please enter a valid choice.")
        except ValueError:
            print("Invalid value entered.")


if __name__ == "__main__":
    main()

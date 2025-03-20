# MOVIES CATELOG MANAGEMENT SYSTEM
import sys
import time
import json

def save_to_file():
    with open("movies_data.json","w") as file:
        json.dump(movies_list,file,indent = 4)

def load_from_file():
    try:
        with open("movies_data.json","r") as file:
            return json.load(file)
    except:
        return []
        
movies_list = load_from_file()

#Search Function for searching
def check_movies_data(movies_list,n):
    if n == "movie":
        name = input("Search for Movie: ")
        for i in movies_list:
            if name in i :
                print(i) 

    try:
        Movies = [movie[n].title() for movie in movies_list]

        for i,name in enumerate(Movies,start = 1):
            result = f"{i}. {name} "
            print(result)
            
    except KeyError:
        print(f"{n} cannot be found in the data")

#Search....
def data(info):
    check_movies_data(movies_list,info)


#Function to display a list of the movie
def movies():
    Movies = [movie["Movie"] for movie in movies_list]
    print()
    print("Movies List=> ")
    for i,movies in enumerate(Movies):
        print(f"{i+1}. {movies} ")

#Function to add the movie to the list
def add_movie():
    while True:
        try:

            print()
            director = input("Enter the name of the director: ").capitalize()
            movie = input("Enter the name of the movie").title()
            date = int(input("Enter the release year of the movie: "))
            print()
            
            if date>2025 or date<1900:
                print("Invalid date entered")
                continue

        except ValueError:
            print("Invalid value")

        new_movie = {
            "Director" : director,
            "Movie" : movie,
            "date" : date
        }

        movies_list.append(new_movie)
        save_to_file()
        print(f"The Movie {new_movie['Movie']} has been succefully added to the list")
        break

#Function to remove the movie from the list
def remove_movie():
    print()
    movies = [movies["Movie"] for movies in movies_list] 
    for i,name in enumerate(movies, start = 1):
        print(f"{i}. {name}")
    try:
        print()
        remove = int(input("Enter the number of the movie you want to remove: ")) - 1
        print()
        if 0<=remove<len(movies_list):
            removed_movie = movies_list.pop(remove)
            save_to_file()
            print(f"{removed_movie['Movie']} has been removed from the list")
        else:
            print("Movie not found")
    except ValueError:
        print("Please enter a numeric value")

        
while True:
    print()
    print("Movie Catalog Mangement Tool".center(40,"+"))
    print()
    print("1- Movies list")
    print("2- Add Movies")
    print("3- Remove Movies")
    print("4- Search Movie")
    print("5- Exit")
    print()
    try:
        
        choice = int(input("please enter your choice: "))
        print()
        print("+"*40)
        match(choice):
                        
            case 1:
                movies()

            case 2:
                add_movie()
        
            case 3:
                remove_movie()
            
            case 4:
                print()
                search = input("What are you looking for(Director,date, Movie) : ").strip().lower()
                print()
                data(search)
            
            case 5:
                choice = input("Are you sure you want to exit: (Yes/No) ").capitalize()
                if choice == "Yes":
                    print("Exiting...")
                    time.sleep(3)
                    sys.exit()
                else: 
                    print("Returning back to the menu..")
                    time.sleep(3)
            case _ :
                print("Please enter the valid choice")
    except ValueError:
        print("Invalid Value entered")


# 🎬 Movie Catalog Management System

A simple and interactive **Movie Catalog Management System** built with Python.  
This project allows users to add, remove, search, and display movies using a JSON file for data storage.

---

## 🎯 Features

- 📃 View all movies in the catalog
- ➕ Add new movies (with director name and release year)
- ❌ Remove movies from the list
- 🔍 Search movies by director, title, or release year
- 💾 Data persistence using a local `movies_data.json` file

---

## 📁 File Structure

```
movie-catalog/
├── movies_data.json         # Stores all the movies in JSON format
└── movie_catalog.py         # Main script with menu-driven interface
```

---

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/movie-catalog.git
   cd movie-catalog
   ```

2. Run the program:
   ```bash
   python movie_catalog.py
   ```

3. Follow the on-screen prompts to manage your movie collection.

---

## 🧠 How It Works

- The system reads from and writes to `movies_data.json`.
- Each movie has:
  - Director name
  - Movie title
  - Release year
- The app prevents invalid input like non-numeric years or future release dates.

---

## 👥 Who Is This For?

- Beginners practicing file handling and OOP in Python
- Anyone building a portfolio project in Python
- Students learning basic CRUD operations

---

## 📌 Coming Soon

- Sort movies by year or name
- Edit/update movie details
- Export to CSV

---

## 📄 License

This project is free to use for learning and personal use.

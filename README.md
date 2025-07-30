
# 🧩 2D Maze Game using Pygame

A randomly generated 2D maze game built with Python and Pygame. Navigate through a procedurally generated labyrinth using **WASD controls**, from an entry point to a valid exit. The game ensures a flawless maze layout on every run — with multiple turns, false paths, and exactly one exit.

---

## 🎮 Features

* ✅ Procedurally generated maze using Depth-First Search (DFS)
* ✅ Single entry and guaranteed exit point
* ✅ WASD control system
* ✅ Minimalistic UI (start, restart, exit – via `pygame_gui`)
* ✅ Smooth player movement with animation
* ✅ Clean performance – no dead ends, no unreachable paths

---

## 🛠️ Tech Stack

| Tool        | Description                |
| ----------- | -------------------------- |
| Python      | Core language              |
| Pygame      | Graphics and game loop     |
| pygame\_gui | Menu and UI integration    |
| Random      | Maze generation randomness |

---

## 📦 Installation

1. **Clone the repo**

```
git clone https://github.com/your-username/maze-game.git
cd maze-game
```

2. **Create a virtual environment (optional but recommended)**

```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```
pip install -r requirements.txt
```

> Make sure `pygame` and `pygame_gui` are installed:

```
pip install pygame pygame_gui
```

---

## ▶️ How to Run

```
python main.py
```

Use the following keys to control your player:

| Key | Action        |
| --- | ------------- |
| W   | Move Forward  |
| S   | Move Backward |
| A   | Move Left     |
| D   | Move Right    |

---

## 📁 File Structure

```
maze-game/
│
├── main.py                 # Main game loop
├── maze_generator.py       # DFS-based maze generation logic
├── player.py               # Player movement logic
├── ui_manager.py           # Start/Restart/Exit GUI via pygame_gui
├── assets/                 # Sounds, images (if any)
├── README.md               # You're reading it!
└── requirements.txt        # Dependencies
```

---

## 🧠 How Maze Generation Works

* Maze is a 2D grid of cells
* Starts with all walls
* Uses randomized **Depth-First Search (DFS)** to carve paths
* Entry always on the left; exit on the right
* Result: Perfect maze (only one path between two points)

---

## 🏁 Upcoming Features (Optional Ideas)

* [ ] First-person 3D version (PyOpenGL)
* [ ] Traps, keys, or enemies
* [ ] Mobile version using Kivy or Web with PyScript
* [ ] Score & Timer system

---

## 🤝 Contributing

Pull requests are welcome! If you have ideas for new mechanics or UI improvements, feel free to fork and submit.

---



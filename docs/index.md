# 🎥 Video Catalog & Management Application

## 🚀 Overview
Welcome to the **Video Catalog & Management Application** repository!  
This application will allow users to catalog, view, and manage videos stored on their desktop. Key features will include:

- Batch metadata scanning for videos.
- Automatic thumbnail generation for previews.
- A GUI for viewing and streaming videos from the catalog.
- Machine learning capabilities to identify potential duplicate videos.

## 🛠️ Features
### 1. Batch Video Processing
- Scan a designated folder to extract metadata from videos.
- Generate 2-3 thumbnails for quick previews during import.

### 2. GUI
- A front-end interface for seamless video browsing.
- Streaming functionality integrated into the app.

### 3. Machine Learning
- ML-based analysis to detect duplicates based on file attributes, metadata, or content similarity.

## 💻 Tech Stack
The **Video Catalog App** will utilize the following:

- **Python** for backend logic.
- **GUI Libraries:** Options include [Tkinter](https://wiki.python.org/moin/TkInter) or frameworks like [PyQt/PySide](https://riverbankcomputing.com/software/pyqt/intro) for the GUI interface.
- **Database:** SQLite or another ORM solution to store video metadata.
- **Machine Learning:** Open-source ML libraries like `scikit-learn`, `TensorFlow`, or `PyTorch`.

Let's establish the initial repository structure for your video catalog application with clear scalability and modularity in mind.

---

## 📂 **Proposed Repository Structure**

Here’s a scalable initial structure:

```
video_catalog/
│
├── main.py                     # Entry point for the application.
│
├── database/                   # Handles database interactions and ORM.
│   └── __init__.py            # Ensures it's treated as a package.
│
├── gui/                         # GUI layer (frontend).
│   └── __init__.py            # Ensures it's treated as a package.
│
├── ml/                          # Machine learning pipeline for duplicate detection.
│   └── __init__.py            # Ensures it's treated as a package.
│
├── utils/                       # Helper utilities.
│   └── __init__.py
│
├── assets/                      # Static assets like icons, sample images, or video thumbnails.
│
├── tests/                       # Unit tests for the application.
│   └── __init__.py
│
├── requirements.txt            # List of dependencies.
│
└── .gitignore                   # Specifies files and directories to ignore by Git.
```

---

## 🚀 **Folder & File Explanation**

1. **`main.py`:**  
   The application entry point where the application startup logic resides.

2. **`database/`:**  
   Encapsulates database logic using SQLAlchemy or another ORM.

3. **`gui/`:**  
   Manages GUI components using PyQt5, lovable.dev, or other frameworks.

4. **`ml/`:**  
   Contains ML logic and pipelines for duplicate detection.

5. **`utils/`:**  
   General utilities to abstract logic for reusability.

6. **`assets/`:**  
   Store icons, videos, or any static media that will be part of the user experience.

7. **`tests/`:**  
   Unit tests to ensure changes don’t break functionality.

8. **`requirements.txt`:**  
   Dependency list for environment setup.

9. **`.gitignore`:**  
   Keeps virtual environments, build artifacts, and unnecessary files out of version control.

### 📝 **Steps to Define Database Schema**

#### 1. **Identify Metadata Requirements**

Video metadata should include:

- **File Information:**
  - `id` (Primary Key)
  - `file_name` (Name of the video file)
  - `file_path` (Full path to the video)
  - `file_size` (File size in bytes)
  - `created_at` (File creation timestamp)
  - `modified_at` (Last modification timestamp)

- **Video-Specific Information:**
  - `duration` (Length of the video in seconds)
  - `resolution` (Width x Height)
  - `frame_rate` (Frames per second)
  - `codec` (Video codec used)
  - `bitrate` (Video bitrate in kbps)

- **Thumbnails:**
  - `thumbnail_path` (Path to the generated thumbnail(s), if applicable)

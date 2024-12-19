# Video Catalog & Management Application

![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/harishkamathuk/video-catalog-app/python-app.yml?branch=develop&style=flat)
[![codecov](https://codecov.io/gh/harishkamathuk/video-catalog-app/branch/develop/graph/badge.svg?token=qpORAJCwwf)](https://codecov.io/gh/harishkamathuk/video-catalog-app)

## 📖 **Project Overview**

The Video Catalog & Management Application is designed to organize, search, and stream video files stored on a desktop. It provides an intuitive GUI, batch processing for metadata extraction, and machine learning capabilities for duplicate detection. This application aims to simplify video file management by offering features like thumbnail generation, advanced filtering, and video previews.



## 🎯 **Project Goals**

- **Batch Processing:** Automatically scan a folder, extract metadata from video files, and generate thumbnails for easy previews.
- **GUI Interface:** Provide an intuitive interface for viewing, searching, and streaming videos.
- **Duplicate Detection:** Use machine learning techniques to identify potential duplicate videos based on metadata or content similarity.
- **Streaming Previews:** Enable users to stream video previews directly within the application.

---

## 🚀 **Getting Started**

Follow the steps below to set up the project on your local machine:

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/video-catalog.git
cd video-catalog
```

### 2. Set Up a Virtual Environment

It is recommended to use a virtual environment to manage dependencies:

```bash

python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

Use the `requirements.txt` file to install the necessary dependencies:

```bash
pip install -r requirements.txt
```

---

## ⚙️ **Environment Setup**

1. Ensure Python 3.8+ is installed on your system.
2. Install the following key dependencies:
   - `PyQt5` for the GUI.
   - `SQLAlchemy` for database interaction.
   - `ffmpeg-python` and `moviepy` for video metadata extraction and thumbnail generation.
   - `scikit-learn` and `opencv-python-headless` for machine learning workflows.

3. Verify your setup by running:

```bash
python main.py
```

   This will initialize the application (replace with your actual command as features are implemented).

---

## 📂 **Folder Structure**

```plaintext
video_catalog/
│
├── main.py                     # Application entry point.
├── requirements.txt            # List of dependencies.
├── .gitignore                  # Git ignored files.
│
├── database/                   # Database schema and ORM logic.
├── gui/                        # GUI components.
├── ml/                         # Machine learning pipelines.
├── utils/                      # Helper utilities.
├── assets/                     # Static assets like icons and thumbnails.
├── tests/                      # Unit tests.
```

---

## 📌 **Contributing**

We welcome contributions! If you’d like to add features or fix issues, feel free to:

1. Fork the repository.
2. Create a new branch.
3. Submit a pull request.

---

## 🛠️ **Future Enhancements**

- Implement advanced filtering and tagging for videos.
- Add support for cloud-based video storage.
- Extend ML capabilities to include video content analysis.

---

## 📧 **Contact**

For any questions or suggestions, feel free to reach out at [circus-aching-exes_at_duck.com].

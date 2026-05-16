Hypertrophy & Workout Volume Optimizer CLI

An interactive Command-Line Interface (CLI) Python application built to solve a real-world computing and fitness tracking problem: calculating workload volume, evaluating progressive overload, and estimating individual lifting ceilings cleanly with embedded data validation.


Project Presentation Video
Watch the 10-to-15-minute code defense and video presentation on YouTube:
[Click Here to Watch the Video Demonstration](https://www.youtube.com/watch?v=YOUR_VIDEO_ID_HERE)

Student Information
Student Name: Dominic S. Froyalde Jr.
Academic Section: BSCS-1A
Course:Intermediate Programming Machine Project



Key Application Features

1. Object-Oriented Architecture (OOP): Models real-world strength training elements through dedicated `Exercise` and `WorkoutSession` structures.
2. Dynamic Volumetric Calculations: Computes individual and total session lifting workloads ($Sets \times Reps \times Weight$) automatically using optimized data processing.
3. 1-Rep Max Projections: Utilizes the Epley mathematical progression formula to estimate lifting max capabilities dynamically at runtime.
4. Data Persistence (File Handling): Saves, creates, updates, and reads operational metrics using context-managed local JSON formatting inside the `/data/` route folder.
5. Robust Input Validation (Advanced Concept): Employs an advanced Python function decorator to intercept `ValueError` triggers gracefully from improper menu commands or user input parameters, preventing runtime interface crashes.


Project Repository Structure

Your repository follows the exact layout guidelines required under the structural rubric rules:

text
Froyalde_Dominic_FinalProject/
│
├── README.md                  # Project overview, features, setup guide, and YouTube URL
├── requirements.txt           # File listing dependencies (None used for standard library)
│
├── src/                       # Source code directory
│   └── main.py                # Main executable application containing models, views, and core logic
│
└── data/                      # Folder handling persistent file storage
    └── workout_history.json   # Auto-generated database storage file

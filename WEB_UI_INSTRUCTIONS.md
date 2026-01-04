# Web UI for Freshness Evaluator
python version 3.8.10

1. 
python -m venv .venv

2. 
.\.venv\Scripts\activate

3. 
python -m pip install --upgrade pip wheel


4. 
python -m pip install tensorflow-cpu opencv-python numpy h5py flask


5. Run the app:

python app.py

6. 
Open http://127.0.0.1:5000 in your browser, upload an image, and view the score and label.

Notes:
- Uploaded files are saved to the `uploads/` directory.
- The web UI loads functions from `evaluate-image.py` so keep that file in the repo root.

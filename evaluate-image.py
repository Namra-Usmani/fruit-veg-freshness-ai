import cv2
import numpy as np
from keras.models import load_model


# Classify fresh/rotten
THRESHOLD_FRESH = 0.10  # default threshold for "fresh"
THRESHOLD_MEDIUM = 0.50  # default threshold for "medium fresh"


def get_fresh_label(res, threshold_fresh=THRESHOLD_FRESH, threshold_medium=THRESHOLD_MEDIUM):
    """Return a string label for freshness given score `res`.
    Lower scores -> fresher (higher = more rotten).
    """
    if res < threshold_fresh:
        return "FRESH"
    elif threshold_fresh < res < threshold_medium:
        return "MEDIUM FRESH"
    else:
        return "NOT FRESH"


def print_fresh(res, threshold_fresh=THRESHOLD_FRESH, threshold_medium=THRESHOLD_MEDIUM):
    """Backward-compatible helper that prints the label."""
    label = get_fresh_label(res, threshold_fresh, threshold_medium)
    print(f"The item is {label}!")
    return label


def pre_proc_img(image_path):
    # Read the image using OpenCV
    img = cv2.imread(image_path)
    img = cv2.resize(img, (100, 100))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Preprocess the image
    img = img / 255.0
    img = np.expand_dims(img, axis=0)
    return img


def evaluate_rotten_vs_fresh(image_path):
    # Load the trained model
    model = load_model('trained-freshness-model.h5')

    # Read and process and predict
    prediction = model.predict(pre_proc_img(image_path))

    return prediction[0][0]


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Evaluate freshness of an image.')
    parser.add_argument('-i', '--image', help='Path to image file', required=False)
    args = parser.parse_args()

    img_path = args.image or 'image-to-eval.png'
    if not os.path.exists(img_path):
        print(f"Image not found: {img_path}")
    else:
        score = evaluate_rotten_vs_fresh(img_path)
        print(f'Predicted score: {score:.4f}')
        print_fresh(score)

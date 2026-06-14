# Rasengan Gesture Project

A real-time computer vision project that uses hand tracking and gesture recognition to create a Naruto-inspired Rasengan effect.


## Features

* Real-time hand tracking using MediaPipe
* Gesture detection for activating the Rasengan
* Particle-based Rasengan visual effect
* Dynamic effect scaling and animation
* Webcam-based interaction
* Built with Python and OpenCV

## Technologies Used

* Python
* OpenCV
* MediaPipe
* NumPy

Create and activate a virtual environment:

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the main script:

```bash
python main.py
```

Allow webcam access when prompted.

Perform the required hand gesture to charge and activate the Rasengan effect.

## Project Structure

```text
rasengan-gesture-project/
│
├── main.py
├── modules/
│   ├── gesture.py
│   ├── particles.py
│   └── ...
│
├── assets/
├── requirements.txt
├── README.md
└── .gitignore
```

## Known Issues

* Particle positioning may not perfectly align with the center of the palm.
* Fast hand movement can occasionally cause tracking drift.
* Gesture detection accuracy depends on lighting conditions and camera quality.

## Future Improvements

* Improved palm-center tracking
* Better particle physics
* Multiple jutsu/effects
* Custom gesture mapping
* Performance optimizations

## Inspiration

Inspired by the Rasengan technique from the Naruto series and built as a computer vision and graphics experiment.

## License

This project is for educational and portfolio purposes.
(if anyone steals without giving me credit, ill cry)

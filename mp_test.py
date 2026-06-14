import mediapipe as mp

print("Version:", getattr(mp, "__version__", "No version"))
print("Has solutions:", hasattr(mp, "solutions"))
print(dir(mp))
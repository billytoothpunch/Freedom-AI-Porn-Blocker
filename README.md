# Freedom-AI-Porn-Blocker
Created this for myself to block NSFW on my laptop

Things needed:
Tesseract-OCR [https://github.com/tesseract-ocr/tesseract/releases/download/5.5.0/tesseract-ocr-w64-setup-5.5.0.20241111.exe]
or [https://github.com/UB-Mannheim/tesseract/wiki]

Nudenet Model [https://github.com/notAI-tech/nudenet?tab=readme-ov-file]
360 (Lightweight, less accurate) [https://github.com/notAI-tech/NudeNet/releases/download/v3.4-weights/320n.onnx]
640 (more accurate) [https://github.com/notAI-tech/NudeNet/releases/download/v3.4-weights/640m.onnx]
The model must be in .onnx to work correctly.

This Blocker detects porn using the nudenet model and finds the application running it and closes it.(Freedom_Blocker.exe)
Watchdog.exe checks to see if the blocker is running.
Preventer.exe checks to see if the user is trying to uninstall the application and prevents them from doing so.

How to run:
Open the "make exe" txt file 


If someone can help me solve the Antivirus issue that causes it to keep flagging up i would appreciate it

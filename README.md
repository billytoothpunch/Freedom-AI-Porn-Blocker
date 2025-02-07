# Freedom-AI-Porn-Blocker
Created this for myself to block NSFW on my laptop

Things needed:
Tesseract-OCR

[https://github.com/tesseract-ocr/tesseract/releases/download/5.5.0/tesseract-ocr-w64-setup-5.5.0.20241111.exe]
or

[https://github.com/UB-Mannheim/tesseract/wiki]

Nudenet Model 

[https://github.com/notAI-tech/nudenet?tab=readme-ov-file]
360 (Lightweight, less accurate)

[https://github.com/notAI-tech/NudeNet/releases/download/v3.4-weights/320n.onnx]
640 (more accurate)

[https://github.com/notAI-tech/NudeNet/releases/download/v3.4-weights/640m.onnx]
The model must be in .onnx to work correctly.

This Blocker detects porn using the nudenet model and finds the application running it and closes it.(Freedom_Blocker.exe)
Watchdog.exe checks to see if the blocker is running.
Preventer.exe checks to see if the user is trying to uninstall the application and prevents them from doing so.

How to run:

1.Run the Tesseract installer and go to C:\Program Files\Tesseract-OCR or wherever you install it.
Copy all the files in here and paste it in the Tesseract folder for the blocker.

2.Download the .onnx model and place it in the models folder.

3.Open the "make exe" txt file and copy paste the commands into cmd (must be ran in the same directory where the scripts are)
You need python and pyinstaller for this

4.Once the .exe files are made they will be in the dist folder you can test them to see if they work.

5.Download inno from:
https://jrsoftware.org/isdl.php#stable
This will allow us to make an installer and have it run on startup.

6.Open the "setup" script and run it in inno. make sure to have extract into the folder "bammus" since that is the detected keyword for the prevention of uninstall, also make sure to add in your own directories for where the scripts are

7.Turn off Antivirus or switch to malwarebytes, The built in antivirus for windows keeps on flagging it and stopping the program from functioning.

Enjoy? i guess

If someone can help me solve the Antivirus issue that causes it to keep flagging up i would appreciate it

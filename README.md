# VoiceClonedAudiobookGenerator
#VoiceClonedAudiobookGenerator
Introduction
Welcome to VoiceClonedAudiobookGenerator, a Python-based tool designed to convert PDF books into personalized audiobooks using Coqui's XTTS-v2 voice cloning model. This project allows users to upload a PDF file (e.g., "Life 3.0") and a short audio sample of their own voice to generate a custom audiobook. Featuring a user-friendly Streamlit web interface, it offers a seamless experience for creating and downloading MP3 audio files. Developed as part of a Generative AI assignment, this open-source project showcases the power of text-to-speech (TTS) and voice cloning technologies.
Features

Voice Cloning: Replicate your unique voice using a 6-30 second WAV audio sample with XTTS-v2.
PDF to Audio Conversion: Extract text from PDFs and transform it into high-quality MP3 audiobooks.
Streamlit Interface: An intuitive web app for uploading files and downloading results.
Chunk Processing: Efficiently handle large PDFs by processing text in manageable segments.
Open Source: Built with free tools including Coqui TTS, PyPDF2, pydub, and Streamlit.

Prerequisites

Python 3.11: Required for compatibility with the TTS package (Python 3.13 and above are not supported).
Dependencies:

TTS (for XTTS-v2)
pydub (for audio file combining)
PyPDF2 (for PDF text extraction)
streamlit (for the web interface)


Build Tools: Visual Studio Build Tools with C++ support (for compiling TTS dependencies on Windows).
Hardware: A GPU is recommended for faster processing (optional, requires CUDA).
Voice Sample: A clear WAV file of your voice (6-30 seconds).

Installation
Step 1: Clone the Repository
Clone this repository to your local machine:
bashgit clone https://github.com/yourusername/VoiceClonedAudiobookGenerator.git
cd VoiceClonedAudiobookGenerator
Step 2: Set Up a Virtual Environment

Ensure Python 3.11 is installed. Verify with:
powershell"C:\Users\Usman Anwar\AppData\Local\Programs\Python\Python311\python.exe" --version

If not installed, download it from python.org.


Create a virtual environment:
powershell"C:\Users\Usman Anwar\AppData\Local\Programs\Python\Python311\python.exe" -m venv .venv311

Activate the environment:
powershell.venv311\Scripts\Activate.ps1

Your prompt should change to (.venv311).



Step 3: Install Dependencies

Install required build tools:

Download and install Visual Studio Build Tools with the Desktop development with C++ workload.
Restart your computer after installation.


Install Python packages:
powershellpip install TTS pydub PyPDF2 streamlit

If installation fails, clear the pip cache:
powershellpip cache purge

Update pip if needed:
powershellpython -m pip install --upgrade pip

For GPU support (optional), install PyTorch with CUDA:
powershellpip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118



Verify installations:
powershellpip show TTS pydub PyPDF2 streamlit


Step 4: Prepare Your Voice Sample

Record a 6-30 second WAV file (e.g., "Hello, this is my voice.") using software like Audacity.
Save it as my_voice.wav in the project directory (D:\Seventh smester\GenAi\Assignment 1).

Usage

Run the Streamlit App:
powershellstreamlit run app.py

This opens the app in your default browser at http://localhost:8501 (or an alternate port if 8501 is in use).


Upload Files:

Upload your PDF file (e.g., Life_3.0.pdf).
Upload your voice sample WAV file.


Generate Audiobook:

Click the "Generate Audiobook" button.
Wait for processing (may take time for large PDFs).
Download the resulting cloned_audiobook.mp3 file.



Project Structure

TextToSpeech.py: Core logic for text extraction and audio generation using XTTS-v2.
app.py: Streamlit web interface for user interaction.
README.md: This file, providing project documentation.

Troubleshooting

Installation Failures: Ensure Visual Studio Build Tools are installed and added to your PATH. Use --verbose with pip install TTS to diagnose issues.
Slow Processing: Enable GPU support with gpu=True in TTS(...) if you have a CUDA-enabled NVIDIA GPU.
PDF Extraction Issues: If text extraction fails, the PDF may be scanned. Consider integrating OCR with pytesseract.
Model Download: The XTTS-v2 model (~2GB) requires a stable internet connection and sufficient disk space.

Future Improvements

Support for multiple languages.
Parallel processing for larger PDFs.
Real-time audio preview in the Streamlit app.

License
This project is released under the MIT License. You are free to use, modify, and distribute it for personal or educational purposes, provided you comply with the license terms. Note that you must have legal rights to the PDF content you convert to audio.
Acknowledgments

Coqui TTS: For the XTTS-v2 voice cloning model.
Streamlit: For the web framework.
xAI: For Grok's assistance in developing this project.

Contact
For questions, issues, or contributions, please open an issue on the GitHub repository https://github.com/Usman3660/VoiceClonedAudiobookGenerator or contact the maintainer.
Happy audiobook creation!

import PyPDF2
from gtts import gTTS
import os
from pydub import AudioSegment
import time

# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                extracted_text = page.extract_text()
                if extracted_text:
                    text += extracted_text + "\n\n"
        if not text.strip():
            raise ValueError("No text could be extracted from the PDF. Ensure the PDF contains readable text.")
        return text
    except Exception as e:
        raise Exception(f"Error extracting text from PDF: {str(e)}")

# Function to convert text to speech using gTTS
def text_to_speech(pdf_path, output_audio_path):
    try:
        # Step 1: Extract text
        print("Extracting text from PDF...")
        full_text = extract_text_from_pdf(pdf_path)
        
        # Step 2: Split text into chunks to avoid gTTS length limits
        chunk_size = 2000  # Reduced from 5000 to test smaller chunks
        chunks = [full_text[i:i + chunk_size] for i in range(0, len(full_text), chunk_size)]
        print(f"Split text into {len(chunks)} chunks.")
        
        # Step 3: Generate audio for each chunk with timeout
        temp_files = []
        for i, chunk in enumerate(chunks):
            print(f"Processing chunk {i+1}/{len(chunks)}...")
            try:
                tts = gTTS(text=chunk, lang='en', timeout=10)  # 10-second timeout
                temp_file = f"temp_audio_{i}.mp3"
                tts.save(temp_file)
                temp_files.append(temp_file)
                print(f"Chunk {i+1} saved as {temp_file}")
            except Exception as e:
                print(f"Error processing chunk {i+1}: {str(e)}. Skipping this chunk.")
                continue
        
        # Step 4: Combine audio files using pydub
        if temp_files:
            print("Combining audio files...")
            combined = AudioSegment.empty()
            for temp_file in temp_files:
                combined += AudioSegment.from_mp3(temp_file)
            combined.export(output_audio_path, format="mp3")
            print(f"Audio file saved to {output_audio_path}")
        else:
            print("No audio chunks were generated. Check the error messages above.")
        
        # Step 5: Clean up temporary files
        for temp_file in temp_files:
            os.remove(temp_file)
    except Exception as e:
        print(f"Error during text-to-speech conversion: {str(e)}")

# Usage example
if __name__ == "__main__":
    PDF_PATH = r"D:\Seventh smester\GenAi\Assignment 1\Life_3.0.pdf"
    OUTPUT_AUDIO = r"D:\Seventh smester\GenAi\Assignment 1\life_3.0_audio.mp3"
    
    if not os.path.exists(PDF_PATH):
        print(f"PDF file not found at {PDF_PATH}. Please provide the correct path.")
    else:
        text_to_speech(PDF_PATH, OUTPUT_AUDIO)
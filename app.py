import streamlit as st
import PyPDF2
from TTS.api import TTS
import os
from pydub import AudioSegment
import tempfile

# Function to extract text from PDF
def extract_text_from_pdf(pdf_file):
    text = ""
    try:
        reader = PyPDF2.PdfReader(pdf_file)
        for page in reader.pages:
            extracted_text = page.extract_text()
            if extracted_text:
                text += extracted_text + "\n\n"
        if not text.strip():
            raise ValueError("No text could be extracted from the PDF. Ensure the PDF contains readable text.")
        return text
    except Exception as e:
        raise Exception(f"Error extracting text from PDF: {str(e)}")

# Function to generate speech in cloned voice using XTTS-v2
def cloned_text_to_speech(pdf_text, speaker_wav_path):
    try:
        # Initialize XTTS model
        st.info("Loading XTTS-v2 model... This may take a moment.")
        tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2")  # Use gpu=True if you have a GPU

        # Split text into chunks
        chunk_size = 1000
        chunks = [pdf_text[i:i + chunk_size] for i in range(0, len(pdf_text), chunk_size)]
        st.info(f"Split text into {len(chunks)} chunks.")

        # Generate audio for each chunk
        temp_files = []
        for i, chunk in enumerate(chunks):
            st.info(f"Processing chunk {i+1}/{len(chunks)}...")
            temp_file = tempfile.NamedTemporaryFile(suffix=".wav", delete=False).name
            tts.tts_to_file(text=chunk, file_path=temp_file, speaker_wav=speaker_wav_path, language="en")
            temp_files.append(temp_file)

        # Combine audio files using pydub
        if temp_files:
            st.info("Combining audio files...")
            combined = AudioSegment.empty()
            for temp_file in temp_files:
                combined += AudioSegment.from_wav(temp_file)
            output_audio_path = tempfile.NamedTemporaryFile(suffix=".mp3", delete=False).name
            combined.export(output_audio_path, format="mp3")

            # Clean up temporary files
            for temp_file in temp_files:
                os.remove(temp_file)

            return output_audio_path
        else:
            raise Exception("No audio chunks were generated.")
    except Exception as e:
        raise Exception(f"Error during cloned text-to-speech: {str(e)}")

# Streamlit app
st.title("PDF to Cloned Voice Audio Converter")
st.markdown("Upload a PDF book and a short voice sample (WAV) to generate an audiobook in your own voice using XTTS-v2.")

# Upload PDF
pdf_file = st.file_uploader("Upload PDF File (e.g., Life 3.0.pdf)", type=["pdf"])

# Upload voice sample
voice_file = st.file_uploader("Upload Voice Sample (WAV, 6-30 seconds)", type=["wav"])

if st.button("Generate Audiobook"):
    if pdf_file and voice_file:
        with st.spinner("Processing..."):
            try:
                # Save uploaded files temporarily
                with tempfile.NamedTemporaryFile(delete=False) as temp_pdf:
                    temp_pdf.write(pdf_file.read())
                    temp_pdf_path = temp_pdf.name

                with tempfile.NamedTemporaryFile(delete=False) as temp_wav:
                    temp_wav.write(voice_file.read())
                    temp_wav_path = temp_wav.name

                # Extract text
                pdf_text = extract_text_from_pdf(temp_pdf_path)

                # Generate cloned audio
                output_audio_path = cloned_text_to_speech(pdf_text, temp_wav_path)

                # Provide download link
                st.success("Audiobook generated successfully!")
                with open(output_audio_path, "rb") as audio_file:
                    st.download_button(
                        label="Download Audiobook MP3",
                        data=audio_file,
                        file_name="cloned_audiobook.mp3",
                        mime="audio/mp3"
                    )

                # Clean up
                os.remove(temp_pdf_path)
                os.remove(temp_wav_path)
                os.remove(output_audio_path)
            except Exception as e:
                st.error(f"Error: {str(e)}")
    else:
        st.warning("Please upload both PDF and voice sample files.")
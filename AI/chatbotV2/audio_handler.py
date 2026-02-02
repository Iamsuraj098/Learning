"""
Audio Handler for STT and TTS
Speech-to-Text: Converts audio/speech to text
Text-to-Speech: Converts text to audio/speech
"""

import pyttsx3
import speech_recognition as sr
import os


class AudioHandler:
    def __init__(self):
        """Initialize audio handler with TTS engine"""
        self.tts_engine = pyttsx3.init()
        self.recognizer = sr.Recognizer()
        
        # Configure TTS
        self.tts_engine.setProperty('rate', 150)  # Speed
        self.tts_engine.setProperty('volume', 0.9)  # Volume
        
    def text_to_speech(self, text, play=True):
        """
        Convert text to speech
        
        Args:
            text: Text to convert
            play: Whether to play audio immediately
        """
        try:
            if play:
                print("🔊 Speaking...")
                self.tts_engine.say(text)
                self.tts_engine.runAndWait()
            else:
                return text
        except Exception as e:
            print(f"TTS Error: {e}")
    
    def speech_to_text(self, use_microphone=True):
        """
        Convert speech to text
        
        Args:
            use_microphone: If True, use microphone; if False, return None (for demo)
        
        Returns:
            Recognized text or None
        """
        if not use_microphone:
            return None
        
        try:
            print("🎤 Listening... (speak now)")
            
            with sr.Microphone() as source:
                # Adjust for ambient noise
                self.recognizer.adjust_for_ambient_noise(source, duration=1)
                
                # Listen for audio
                audio = self.recognizer.listen(source, timeout=15)
            
            # Recognize speech using Google Speech Recognition
            print("Processing speech...")
            text = self.recognizer.recognize_google(audio)
            print(f"✓ You said: {text}")
            return text
            
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return None
        except sr.UnknownValueError:
            print("Could not understand audio")
            return None
        except Exception as e:
            print(f"Error: {e}")
            return None
    
    def close(self):
        """Clean up resources"""
        try:
            self.tts_engine.stop()
        except:
            pass

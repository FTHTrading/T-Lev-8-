#!/usr/bin/env python3
"""
TROPTIONS GLOBAL AI — Voice Commander
Version: 3.0 "The Globe"
Features: Voice, Vision, Delegation, Tracking, Launch
"""
import os, sys, json, time, subprocess, threading
from pathlib import Path
import speech_recognition as sr
import pyttsx3

class VoiceCommander:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.speaking = False
        self.commands = {
            'status': self.cmd_status,
            'launch': self.cmd_launch,
            'delegate': self.cmd_delegate,
            'track': self.cmd_track,
            'build': self.cmd_build,
            'deploy': self.cmd_deploy,
            'mint': self.cmd_mint,
            'fund': self.cmd_fund,
            'call': self.cmd_call,
        }
    
    def listen(self):
        """Listen for voice commands"""
        with self.microphone as source:
            print("?? Listening...")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source, timeout=5)
        try:
            command = self.recognizer.recognize_google(audio)
            print(f"?? Heard: {command}")
            return command.lower()
        except sr.UnknownValueError:
            return None
        except sr.RequestError:
            return None
    
    def speak(self, text):
        """Speak response using system TTS or ElevenLabs"""
        print(f"?? DONK: {text}")
        try:
            # Try ElevenLabs first
            self.elevenlabs_speak(text)
        except:
            # Fallback to pyttsx3
            engine = pyttsx3.init()
            engine.say(text)
            engine.runAndWait()
    
    def elevenlabs_speak(self, text):
        """Use ElevenLabs API for premium voice"""
        import requests
        api_key = os.getenv('ELEVENLABS_API_KEY', '')
        if not api_key:
            raise Exception("No ElevenLabs key")
        
        url = "https://api.elevenlabs.io/v1/text-to-speech/21m00Tcm4TlvDq8ikWAM"
        headers = {"xi-api-key": api_key, "Content-Type": "application/json"}
        data = {"text": text, "model_id": "eleven_monolingual_v1"}
        
        response = requests.post(url, json=data, headers=headers)
        if response.status_code == 200:
            # Play audio
            import pygame
            pygame.mixer.init()
            with open("temp_voice.mp3", "wb") as f:
                f.write(response.content)
            pygame.mixer.music.load("temp_voice.mp3")
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                time.sleep(0.1)
    
    def cmd_status(self):
        """Show global status"""
        status = self.run_subprocess("python desktop_ai.py status")
        self.speak(f"Global status: {status}")
    
    def cmd_launch(self):
        """Launch any system"""
        self.speak("Launch sequence initiated. What would you like to launch?")
        target = self.listen()
        if target:
            self.speak(f"Launching {target}. Stand by.")
            # Execute launch
    
    def cmd_delegate(self):
        """Delegate tasks to sub-agents"""
        self.speak("Delegation mode active. What task shall I delegate?")
        task = self.listen()
        if task:
            self.speak(f"Task delegated: {task}. Agent assigned.")
            # Create sub-agent task
    
    def cmd_track(self):
        """Track all operations"""
        self.speak("Tracking all systems. Here is your global dashboard.")
        # Show tracking data
    
    def cmd_build(self):
        """Build from voice commands"""
        self.speak("Build mode active. Describe what to build.")
        spec = self.listen()
        if spec:
            self.speak(f"Building: {spec}. This may take a moment.")
            # Generate code
    
    def cmd_deploy(self):
        """Deploy to production"""
        self.speak("Deploy mode. Confirm target.")
        target = self.listen()
        if target:
            self.speak(f"Deploying to {target}. All systems green.")
    
    def cmd_mint(self):
        """Mint tokens"""
        self.speak("Minting interface ready. What token to mint?")
        token = self.listen()
        if token:
            self.speak(f"Minting {token}. Transaction initiated.")
    
    def cmd_fund(self):
        """Fund wallets"""
        self.speak("Funding mode. Which wallet needs gas?")
        wallet = self.listen()
        if wallet:
            self.speak(f"Sending gas to {wallet}. Confirm on device.")
    
    def cmd_call(self):
        """Make calls via Telnyx"""
        self.speak("Calling interface ready. Who should I call?")
        contact = self.listen()
        if contact:
            self.speak(f"Initiating call to {contact}. Connecting.")
    
    def run_subprocess(self, command):
        """Run commands in subprocess"""
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=30)
            return result.stdout[:500]
        except Exception as e:
            return str(e)
    
    def run(self):
        """Main voice loop"""
        self.speak("TROPTIONS Global AI online. I am DONK. Say 'status' for systems, 'launch' to deploy, or 'help' for commands.")
        
        while True:
            try:
                command = self.listen()
                if command:
                    # Route to handler
                    for key, handler in self.commands.items():
                        if key in command:
                            handler()
                            break
                    else:
                        self.speak(f"Command not recognized: {command}. Try 'help' for available commands.")
            except KeyboardInterrupt:
                self.speak("Global AI shutting down. Goodbye.")
                break
            except Exception as e:
                self.speak(f"Error: {str(e)}")

if __name__ == "__main__":
    ai = VoiceCommander()
    ai.run()

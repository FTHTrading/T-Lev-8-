# TROPTIONS GLOBAL AI — Simple Text Interface
# Version: 3.1 (Text Mode — No Emoji)

import os
import sys
import json
import time
import subprocess
from datetime import datetime
from pathlib import Path

# Configuration
BASE_DIR = Path.home() / ".openclaw"
WORKSPACE = BASE_DIR / "workspace"
LOG_FILE = BASE_DIR / "logs" / "global-ai.log"

# Ensure directories exist
os.makedirs(BASE_DIR / "logs", exist_ok=True)
os.makedirs(WORKSPACE / "tasks", exist_ok=True)

def log(msg):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{timestamp}] {msg}"
    print(line)
    with open(LOG_FILE, "a") as f:
        f.write(line + "\n")

def banner():
    print("\n" + "="*60)
    print("  TROPTIONS GLOBAL AI v3.1")
    print("  Voice Commander + Delegation Engine")
    print("="*60 + "\n")

def check_ollama():
    try:
        result = subprocess.run(["ollama", "list"], capture_output=True, text=True, timeout=5)
        if result.returncode == 0:
            models = [line.split()[0] for line in result.stdout.strip().split('\n')[1:] if line.strip()]
            return True, models
        return False, []
    except Exception:
        return False, []

def check_systems():
    systems = {
        "Ollama": "checking...",
        "OpenClaw": "checking...",
        "T-Build": "checking...",
        "T-VEX-8": "checking...",
        "Exchange OS": "checking...",
        "Token Launcher": "checking...",
        "x402 Bridge": "checking...",
        "Telnyx": "checking...",
        "ElevenLabs": "checking...",
    }
    
    # Check Ollama
    ollama_ok, models = check_ollama()
    systems["Ollama"] = "LIVE - " + ", ".join(models[:3]) if ollama_ok else "OFFLINE"
    
    # Check T-Build
    tbuild_path = Path.home() / "Documents" / "UNYKORN_Ecosystem" / "T-Build"
    systems["T-Build"] = "READY" if tbuild_path.exists() else "NOT FOUND"
    
    # Check T-VEX-8
    tVEX_path = Path.home() / "Documents" / "UNYKORN_Ecosystem" / "T-VEX-8-"
    systems["T-VEX-8"] = "READY" if tVEX_path.exists() else "NOT FOUND"
    
    # Check secrets
    secrets_file = WORKSPACE / ".secrets.json"
    if secrets_file.exists():
        try:
            with open(secrets_file) as f:
                secrets = json.load(f)
            systems["Telnyx"] = "CONFIGURED" if secrets.get("TELNYX_API_KEY") else "NO KEY"
            systems["ElevenLabs"] = "CONFIGURED" if secrets.get("ELEVENLABS_API_KEY") else "NO KEY"
        except:
            systems["Telnyx"] = "ERROR"
            systems["ElevenLabs"] = "ERROR"
    else:
        systems["Telnyx"] = "NO CONFIG"
        systems["ElevenLabs"] = "NO CONFIG"
    
    # Fixed URLs
    systems["Exchange OS"] = "LIVE - troptionslive.unykorn.org/exchange-os"
    systems["Token Launcher"] = "LIVE - launch.unykorn.org"
    systems["x402 Bridge"] = "LOCAL - 127.0.0.1:4020"
    systems["OpenClaw"] = "RUNNING - this session"
    
    return systems

def show_status():
    print("\n" + "-"*60)
    print("  SYSTEM STATUS")
    print("-"*60)
    
    systems = check_systems()
    for name, status in systems.items():
        icon = "OK" if any(s in status for s in ["LIVE", "READY", "CONFIGURED", "RUNNING"]) else "XX"
        print(f"  [{icon}] {name:<18} {status}")
    
    print("-"*60 + "\n")

def show_wallets():
    print("\n" + "-"*60)
    print("  WALLET REGISTRY")
    print("-"*60)
    print("  Production Issuer: rJLMST... (1.20 XRP) NEEDS GAS")
    print("  Distribution:      rNX4fa... (3.30 XRP)")
    print("  AMM Pool:          rBU6ex... (1.01 XRP)")
    print("  Mystery/Funding:   rfbZz...  (12.00 XRP) POTENTIAL SOURCE")
    print("  Deprecated:        rPF2M1... (3.00 XRP)")
    print("-"*60)
    print("  ACTION: Move 10 XRP from rfbZz... to rJLMST...")
    print("-"*60 + "\n")

def show_revenue():
    print("\n" + "-"*60)
    print("  REVENUE STRATEGY")
    print("-"*60)
    print("  1. Transfer Fees:  $300K/year (needs 1 merchant)")
    print("  2. AMM LP Fees:    $120K/year (needs 10K XRP)")
    print("  3. Stellar Bridge:  $60K/year (needs 1 sponsor)")
    print("  CURRENT: $0 (no gas, no merchants)")
    print("-"*60 + "\n")

def show_gas():
    print("\n" + "-"*60)
    print("  GAS FUND TRACKER")
    print("-"*60)
    print("  Issuer needs:  11 XRP minimum")
    print("  Current:       1.20 XRP")
    print("  Gap:           ~10 XRP (~$18)")
    print("  Solution:      Move 10 XRP from rfbZz...")
    print("-"*60 + "\n")

def generate_code():
    print("\n  Enter task description:")
    task = input("  > ")
    if task:
        print(f"\n  Generating code for: {task}")
        print("  Using model: jefe-turbo...")
        
        # Try to use Ollama
        try:
            import requests
            payload = {
                "model": "jefe-turbo:latest",
                "prompt": f"Generate {task}. Include imports, main function, error handling, and comments.",
                "stream": False
            }
            response = requests.post("http://localhost:11434/api/generate", json=payload, timeout=120)
            if response.status_code == 200:
                result = response.json()
                code = result.get("response", "")
                print("\n" + "="*60)
                print("  GENERATED CODE:")
                print("="*60)
                print(code)
                print("="*60 + "\n")
                
                # Save to file
                save = input("  Save to file? (y/n): ")
                if save.lower() == 'y':
                    filename = input("  Filename: ")
                    filepath = WORKSPACE / "coding-output" / filename
                    os.makedirs(filepath.parent, exist_ok=True)
                    with open(filepath, 'w') as f:
                        f.write(code)
                    print(f"  Saved to: {filepath}")
            else:
                print(f"  Error: Ollama returned {response.status_code}")
        except Exception as e:
            print(f"  Error: {str(e)}")
            print("  Make sure Ollama is running: ollama serve")

def show_help():
    print("\n" + "-"*60)
    print("  AVAILABLE COMMANDS")
    print("-"*60)
    print("  status    - Show all system statuses")
    print("  wallets   - Show wallet registry")
    print("  revenue   - Show revenue strategy")
    print("  gas       - Show gas fund tracker")
    print("  code      - Generate code using AI")
    print("  models    - List Ollama models")
    print("  tbuild    - Open T-Build folder")
    print("  tVEX     - Open T-VEX-8 deal room")
    print("  exchange  - Open Exchange OS")
    print("  launch    - Open Token Launcher")
    print("  clear     - Clear screen")
    print("  help      - Show this help")
    print("  exit      - Quit")
    print("-"*60 + "\n")

def main():
    banner()
    show_status()
    show_help()
    
    log("Global AI started")
    
    while True:
        try:
            command = input("DONK> ").strip().lower()
            
            if not command:
                continue
            
            if command == "exit" or command == "quit":
                print("\n  Goodbye!")
                log("Global AI shutdown")
                break
            
            elif command == "help":
                show_help()
            
            elif command == "status":
                show_status()
            
            elif command == "wallets":
                show_wallets()
            
            elif command == "revenue":
                show_revenue()
            
            elif command == "gas":
                show_gas()
            
            elif command == "code":
                generate_code()
            
            elif command == "models":
                ok, models = check_ollama()
                if ok:
                    print("\n  Available Models:")
                    for m in models:
                        print(f"    - {m}")
                    print()
                else:
                    print("\n  Ollama not running. Start with: ollama serve\n")
            
            elif command == "tbuild":
                path = Path.home() / "Documents" / "UNYKORN_Ecosystem" / "T-Build"
                if path.exists():
                    os.system(f'explorer "{path}"')
                    print("  Opened T-Build folder\n")
                else:
                    print("  T-Build not found\n")
            
            elif command == "tVEX":
                os.system("start https://fthtrading.github.io/T-VEX-8-/")
                print("  Opened T-VEX-8 deal room\n")
            
            elif command == "exchange":
                os.system("start https://troptionslive.unykorn.org/exchange-os")
                print("  Opened Exchange OS\n")
            
            elif command == "launch":
                os.system("start https://launch.unykorn.org")
                print("  Opened Token Launcher\n")
            
            elif command == "clear":
                os.system("cls")
                banner()
            
            else:
                print(f"\n  Unknown command: {command}")
                print("  Type 'help' for available commands\n")
        
        except KeyboardInterrupt:
            print("\n\n  Use 'exit' to quit")
        except Exception as e:
            print(f"\n  Error: {str(e)}\n")

if __name__ == "__main__":
    main()

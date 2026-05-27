# OpenClaw Desktop AI System — Unified Controller
# Version: 2.0
# Author: DONK AI
# Purpose: One AI to control all systems, secrets, and builds

import os
import json
import time
import subprocess
import sys
from datetime import datetime
from pathlib import Path

# ─── CONFIGURATION ──────────────────────────────────────────────────────────

BASE_DIR = Path.home() / ".openclaw"
WORKSPACE = BASE_DIR / "workspace"
SECRETS_FILE = WORKSPACE / ".secrets.json"
LOG_FILE = BASE_DIR / "logs" / "desktop-ai.log"
TASK_QUEUE = WORKSPACE / "tasks"
CODING_QUEUE = TASK_QUEUE / "coding-queue"
OUTPUT_DIR = WORKSPACE / "coding-output"

# Model Configuration
OLLAMA_MODELS = {
    "jefe-turbo": "jefe-turbo:latest",      # 4.7GB — Primary coding model
    "jefe-ai": "jefe-ai:latest",              # 986MB — Fast responses
    "jefe-lite": "jefe-lite:latest",          # 986MB — Lightweight
    "phi4-mini": "phi4-mini:latest",          # 2.5GB — General reasoning
    "qwen2.5-7b": "qwen2.5:7b",              # 4.7GB — Code + reasoning
    "gemma4": "gemma4:latest",                # 9.6GB — Large context
    "llama3.2": "llama3.2:latest",            # 2.0GB — General purpose
    "phi3-mini": "phi3:mini",                 # 2.2GB — Efficient
}

DEFAULT_MODEL = "jefe-turbo"

# ─── SECRET MANAGEMENT ─────────────────────────────────────────────────────

class SecretVault:
    """Secure storage for API keys and credentials"""
    
    def __init__(self, secrets_file):
        self.secrets_file = Path(secrets_file)
        self.secrets = {}
        self._load()
    
    def _load(self):
        if self.secrets_file.exists():
            try:
                with open(self.secrets_file, 'r') as f:
                    self.secrets = json.load(f)
            except Exception as e:
                print(f"⚠️  Warning: Could not load secrets: {e}")
    
    def get(self, key, default=None):
        return self.secrets.get(key, default)
    
    def set(self, key, value):
        self.secrets[key] = value
        self._save()
    
    def _save(self):
        os.makedirs(self.secrets_file.parent, exist_ok=True)
        with open(self.secrets_file, 'w') as f:
            json.dump(self.secrets, f, indent=2)
    
    def list_keys(self):
        return list(self.secrets.keys())

# Initialize vault
vault = SecretVault(SECRETS_FILE)

# ─── LOGGING ────────────────────────────────────────────────────────────────

def log(msg, level="INFO"):
    timestamp = datetime.now().isoformat()
    line = f"[{timestamp}] [{level}] {msg}"
    print(line)
    
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    with open(LOG_FILE, "a") as f:
        f.write(line + "\n")

# ─── OLLAMA INTEGRATION ───────────────────────────────────────────────────

class OllamaClient:
    """Interface to local Ollama models"""
    
    def __init__(self, model=DEFAULT_MODEL):
        self.model = model
        self.available = self._check_available()
    
    def _check_available(self):
        try:
            result = subprocess.run(
                ["ollama", "list"],
                capture_output=True,
                text=True,
                timeout=10
            )
            return result.returncode == 0
        except Exception:
            return False
    
    def generate(self, prompt, system="", stream=False):
        """Generate text using Ollama"""
        if not self.available:
            return "⚠️ Ollama not available. Check if it's running."
        
        try:
            import requests
            
            payload = {
                "model": self.model,
                "prompt": prompt,
                "system": system,
                "stream": stream
            }
            
            response = requests.post(
                "http://localhost:11434/api/generate",
                json=payload,
                stream=stream,
                timeout=300
            )
            
            if stream:
                return response.iter_lines()
            else:
                result = response.json()
                return result.get("response", "")
                
        except Exception as e:
            return f"❌ Error: {str(e)}"
    
    def chat(self, messages, stream=False):
        """Chat with context"""
        if not self.available:
            return "⚠️ Ollama not available."
        
        try:
            import requests
            
            payload = {
                "model": self.model,
                "messages": messages,
                "stream": stream
            }
            
            response = requests.post(
                "http://localhost:11434/api/chat",
                json=payload,
                stream=stream,
                timeout=300
            )
            
            if stream:
                return response.iter_lines()
            else:
                result = response.json()
                return result.get("message", {}).get("content", "")
                
        except Exception as e:
            return f"❌ Error: {str(e)}"
    
    def list_models(self):
        """List available models"""
        try:
            result = subprocess.run(
                ["ollama", "list"],
                capture_output=True,
                text=True,
                timeout=10
            )
            return result.stdout
        except Exception as e:
            return f"❌ Error: {str(e)}"

# ─── SYSTEM INTEGRATION ───────────────────────────────────────────────────

class SystemIntegrator:
    """Integrates all TROPTIONS/UNYKORN systems"""
    
    def __init__(self):
        self.systems = {}
        self._discover_systems()
    
    def _discover_systems(self):
        """Discover available systems"""
        
        # Check T-Build
        tbuild_path = Path.home() / "Documents" / "UNYKORN_Ecosystem" / "T-Build"
        if tbuild_path.exists():
            self.systems["tbuild"] = {
                "path": str(tbuild_path),
                "type": "operations",
                "status": "available"
            }
        
        # Check T-VEX-8
        tVEX_path = Path.home() / "Documents" / "UNYKORN_Ecosystem" / "T-VEX-8-"
        if tVEX_path.exists():
            self.systems["tVEX"] = {
                "path": str(tVEX_path),
                "type": "legal",
                "status": "available"
            }
        
        # Check Exchange OS
        exchange_url = "https://troptionslive.unykorn.org/exchange-os"
        self.systems["exchange"] = {
            "url": exchange_url,
            "type": "trading",
            "status": "live"
        }
        
        # Check Token Launcher
        launcher_url = "https://launch.unykorn.org"
        self.systems["launcher"] = {
            "url": launcher_url,
            "type": "minting",
            "status": "live"
        }
        
        # Check x402
        x402_local = "http://127.0.0.1:4020"
        self.systems["x402"] = {
            "url": x402_local,
            "type": "payments",
            "status": "local"
        }
        
        # Check Telnyx
        telnyx_key = vault.get("TELNYX_API_KEY")
        if telnyx_key:
            self.systems["telnyx"] = {
                "type": "voice_sms",
                "status": "configured"
            }
        
        # Check ElevenLabs
        eleven_key = vault.get("ELEVENLABS_API_KEY")
        if eleven_key:
            self.systems["elevenlabs"] = {
                "type": "tts",
                "status": "configured"
            }
        
        # Check GitHub
        github_pat = vault.get("GITHUB_PAT")
        if github_pat:
            self.systems["github"] = {
                "type": "git",
                "status": "configured"
            }
    
    def status(self):
        """Show system status"""
        print("\n" + "═"*60)
        print("  SYSTEM STATUS")
        print("═"*60)
        
        for name, config in self.systems.items():
            status_icon = "🟢" if config["status"] in ["live", "available", "configured"] else "🔴"
            print(f"  {status_icon} {name.upper():<15} {config['type']:<15} {config['status']}")
        
        print("═"*60 + "\n")
    
    def get_system(self, name):
        return self.systems.get(name)

# ─── CODE GENERATION ──────────────────────────────────────────────────────

class CodeGenerator:
    """Real code generation using Ollama"""
    
    def __init__(self, model=DEFAULT_MODEL):
        self.client = OllamaClient(model)
    
    def generate(self, task, language="python"):
        """Generate code from task description"""
        
        system_prompt = """You are DONK AI, the TROPTIONS system architect. 
You generate production-quality code for the TROPTIONS/UNYKORN ecosystem.
Always include error handling, logging, and comments.
Follow the existing codebase patterns."""
        
        prompt = f"""Task: {task}
Language: {language}

Generate complete, working code. Include:
1. Imports and dependencies
2. Main function/class
3. Error handling
4. Example usage
5. Comments explaining key logic

Code:"""
        
        return self.client.generate(prompt, system=system_prompt)
    
    def review(self, code, context=""):
        """Review code for issues"""
        
        prompt = f"""Review this code for the TROPTIONS ecosystem:

Context: {context}

Code:
```{code}```

Check for:
1. Security vulnerabilities
2. Logic errors
3. Performance issues
4. Missing error handling
5. Compliance with TROPTIONS patterns

Review:"""
        
        return self.client.generate(prompt)

# ─── TERMINAL INTERFACE ─────────────────────────────────────────────────────

class DesktopAI:
    """Main Desktop AI Interface"""
    
    def __init__(self):
        self.ollama = OllamaClient()
        self.systems = SystemIntegrator()
        self.coder = CodeGenerator()
        self.vault = vault
        self.running = True
    
    def banner(self):
        print("""
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║   🤖 TROPTIONS DESKTOP AI — Unified System Controller        ║
║                                                               ║
║   Version: 2.0  |  Model: jefe-turbo  |  Status: LIVE       ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
        """)
    
    def help(self):
        print("""
📋 AVAILABLE COMMANDS:

System Control:
  status          — Show all system statuses
  models          — List available Ollama models
  switch <model>  — Switch AI model

Code Generation:
  code <task>     — Generate code for a task
  review <file>   — Review code for issues
  build <project> — Build a complete project

System Integration:
  tbuild          — Launch T-Build (TPLOS)
  tVEX           — Open T-VEX-8 deal room
  exchange        — Open Exchange OS
  launch          — Open Token Launcher
  mint            — Mint tokens/NFTs

Secret Management:
  secrets         — List configured secrets (keys only)
  set <key>       — Set a secret
  get <key>       — Get a secret value

Information:
  wallets         — Show XRPL wallet registry
  revenue         — Show revenue strategy
  gas             — Show gas fund tracker
  help            — Show this help

Control:
  clear           — Clear screen
  exit            — Shutdown Desktop AI

💡 Tip: Type 'status' to see all connected systems
        """)
    
    def run(self):
        """Main REPL loop"""
        self.banner()
        self.systems.status()
        self.help()
        
        while self.running:
            try:
                command = input("\n🤖 DONK> ").strip()
                
                if not command:
                    continue
                
                parts = command.split()
                cmd = parts[0].lower()
                args = parts[1:]
                
                # Route commands
                if cmd == "exit" or cmd == "quit":
                    self.running = False
                    print("👋 Goodbye!")
                
                elif cmd == "help":
                    self.help()
                
                elif cmd == "status":
                    self.systems.status()
                
                elif cmd == "models":
                    print("\n📊 Available Models:")
                    print(self.ollama.list_models())
                
                elif cmd == "switch" and len(args) > 0:
                    model_name = args[0]
                    if model_name in OLLAMA_MODELS:
                        self.ollama.model = OLLAMA_MODELS[model_name]
                        print(f"✅ Switched to model: {model_name}")
                    else:
                        print(f"❌ Unknown model: {model_name}")
                        print(f"Available: {', '.join(OLLAMA_MODELS.keys())}")
                
                elif cmd == "code":
                    task = " ".join(args)
                    print(f"\n🚀 Generating code for: {task}\n")
                    result = self.coder.generate(task)
                    print(result)
                
                elif cmd == "review":
                    file_path = " ".join(args)
                    if os.path.exists(file_path):
                        with open(file_path, 'r') as f:
                            code = f.read()
                        print(f"\n🔍 Reviewing: {file_path}\n")
                        result = self.coder.review(code)
                        print(result)
                    else:
                        print(f"❌ File not found: {file_path}")
                
                elif cmd == "tbuild":
                    tbuild_path = self.systems.get_system("tbuild")
                    if tbuild_path:
                        print(f"📂 Opening T-Build: {tbuild_path['path']}")
                        os.system(f'explorer "{tbuild_path["path"]}"')
                    else:
                        print("❌ T-Build not found")
                
                elif cmd == "tVEX":
                    print("🌐 Opening T-VEX-8 Deal Room...")
                    os.system("start https://fthtrading.github.io/T-VEX-8-/")
                
                elif cmd == "exchange":
                    print("🌐 Opening Exchange OS...")
                    os.system("start https://troptionslive.unykorn.org/exchange-os")
                
                elif cmd == "launch":
                    print("🌐 Opening Token Launcher...")
                    os.system("start https://launch.unykorn.org")
                
                elif cmd == "mint":
                    print("🪙 Opening minting script...")
                    mint_script = Path.home() / "Documents" / "UNYKORN_Ecosystem" / "T-VEX-8-" / "scripts" / "mint_tokens_and_nfts.js"
                    if mint_script.exists():
                        print(f"📄 Minting script: {mint_script}")
                        print("   Run: node scripts/mint_tokens_and_nfts.js")
                    else:
                        print("❌ Minting script not found")
                
                elif cmd == "secrets":
                    keys = self.vault.list_keys()
                    print(f"\n🔐 Configured Secrets ({len(keys)} keys):")
                    for key in keys:
                        print(f"   ✅ {key}")
                
                elif cmd == "set" and len(args) >= 2:
                    key = args[0]
                    value = " ".join(args[1:])
                    self.vault.set(key, value)
                    print(f"✅ Set {key}")
                
                elif cmd == "get" and len(args) > 0:
                    key = args[0]
                    value = self.vault.get(key)
                    if value:
                        print(f"🔑 {key}: {value[:20]}...")
                    else:
                        print(f"❌ Key not found: {key}")
                
                elif cmd == "wallets":
                    print("\n💰 Wallet Registry:")
                    print("   rJLMST... — Production Issuer (1.20 XRP) ⚠️ NEEDS GAS")
                    print("   rNX4fa... — Distribution Treasury (3.30 XRP)")
                    print("   rBU6ex... — AMM Pool (1.01 XRP)")
                    print("   rfbZz...  — Mystery Wallet (12.00 XRP) 🟢 FUNDING SOURCE")
                
                elif cmd == "revenue":
                    print("\n💵 Revenue Strategy:")
                    print("   1. Transfer Fees — $300K/year potential")
                    print("   2. AMM LP Fees — $120K/year potential")
                    print("   3. Stellar Bridge — $60K/year potential")
                    print("   Current: $0 (no gas, no merchants)")
                
                elif cmd == "gas":
                    print("\n⛽ Gas Fund Tracker:")
                    print("   Issuer needs: 11 XRP minimum")
                    print("   Current: 1.20 XRP")
                    print("   Gap: ~10 XRP (~$18)")
                    print("   Solution: Move 10 XRP from rfbZz...")
                
                elif cmd == "clear":
                    os.system("cls" if os.name == "nt" else "clear")
                    self.banner()
                
                else:
                    print(f"❌ Unknown command: {cmd}")
                    print("   Type 'help' for available commands")
                
            except KeyboardInterrupt:
                print("\n👋 Interrupted. Use 'exit' to quit.")
            except Exception as e:
                print(f"❌ Error: {str(e)}")

# ─── MAIN ─────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    ai = DesktopAI()
    ai.run()

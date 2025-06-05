import os
import getpass
import subprocess

CORALINE_ASCII = r"""
  ____                  _ _ _             
 / ___|___  _ __   ___ | | (_)_ __   __ _ 
| |   / _ \| '_ \ / _ \| | | | '_ \ / _` |
| |__| (_) | | | | (_) | | | | | | | (_| |
 \____\___/|_| |_|\___/|_|_|_|_| |_|\__, |
                                    |___/ 
         🌊 Coraline Server Shell 🌊
"""

PASSWORD = "coraline123"  # Change this!

def encrypt_index_html():
    print("🔐 Encrypting index.html...")
    file_path = subprocess.getoutput("find . -type f -name 'index.html' | head -n 1")
    if not file_path:
        print("❌ index.html not found.")
        return
    enc_path = "/tmp/index.html.enc"
    os.system(f"openssl enc -aes-256-cbc -salt -pbkdf2 -in '{file_path}' -out {enc_path} -k 'HHH'")
    print(f"✅ Encrypted to {enc_path}")

def post_encrypted():
    print("📤 Sending encrypted file to server...")
    enc_path = "/tmp/index.html.enc"
    if not os.path.exists(enc_path):
        print("❌ Encrypted file not found. Run 'encrypt' first.")
        return
    os.system(f"curl -X POST --data-binary @{enc_path} http://localhost:5550/")
    print("✅ Sent.")

def cleanup_encrypted():
    print("🧹 Cleaning up encrypted file...")
    enc_path = "/tmp/index.html.enc"
    if os.path.exists(enc_path):
        os.remove(enc_path)
        print("✅ Removed.")
    else:
        print("ℹ️ Nothing to clean.")

def ping_google():
    print("🌐 Pinging google.com...")
    os.system("ping -c 4 google.com > google.com.ping")
    print("✅ Output saved to google.com.ping")

def count_lines():
    print("🔢 Counting lines in index.html...")
    os.system("wc -l index.html > lines.txt")
    print("✅ Saved to lines.txt")

def https_server_fetch():
    print("🕸️  Starting HTTPS server and fetching directory listing...")
    server_cmd = "python3 -m http.server 8443 --bind 127.0.0.1 --directory . --certfile server.pem"
    server_proc = subprocess.Popen(server_cmd.split(), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    import time; time.sleep(2)
    os.system("wget --no-check-certificate https://127.0.0.1:8443 -O directory.html")
    server_proc.terminate()
    print("✅ Downloaded directory listing to directory.html")
    print("📄 Directory listing preview:")
    os.system("head -20 directory.html")

def show_example_cpp():
    print("📄 Displaying example.cpp:")
    os.system("cat example.cpp")

def run_a_out():
    print("⚙️  Running a.out:")
    os.system("./a.out")

def whoami():
    print("👤 Who am I?")
    os.system("whoami")

COMMANDS = {
    "encrypt":      ("🔐 Encrypt index.html", encrypt_index_html),
    "post":         ("📤 POST encrypted file", post_encrypted),
    "cleanup":      ("🧹 Remove encrypted file", cleanup_encrypted),
    "ping":         ("🌐 Ping google.com", ping_google),
    "count":        ("🔢 Count lines in index.html", count_lines),
    "fetch":        ("🕸️  HTTPS server & fetch dir", https_server_fetch),
    "showcpp":      ("📄 Show example.cpp", show_example_cpp),
    "run":          ("⚙️  Run a.out", run_a_out),
    "whoami":       ("👤 Show current user", whoami),
    "exit":         ("🚪 Exit shell", None),
}

def main():
    print(CORALINE_ASCII)
    for _ in range(3):
        pw = getpass.getpass("🔒 Enter password: ")
        if pw == PASSWORD:
            print("✅ Access granted!\n")
            break
        else:
            print("❌ Wrong password!")
    else:
        print("🚫 Too many attempts. Exiting.")
        return

    print("🛠️  Available commands:")
    for cmd, (desc, _) in COMMANDS.items():
        print(f"  {cmd:8} {desc}")
    print("\nType a command to run it, or 'exit' to quit.")

    while True:
        cmd = input("🤖 coraline> ").strip()
        if cmd == "exit":
            print("👋 Goodbye!")
            break
        elif cmd in COMMANDS:
            func = COMMANDS[cmd][1]
            if func:
                func()
        else:
            print("❓ Unknown command. Try again.")

if __name__ == "__main__":
    main()
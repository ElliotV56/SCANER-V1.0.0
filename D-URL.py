#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import requests
import re
import socket
import whois
from urllib.parse import urlparse
from datetime import datetime
import ipaddress
from bs4 import BeautifulSoup
import warnings
import sys
warnings.filterwarnings("ignore")

# ===== LEGAL DISCLAIMER =====
def show_legal_warning():
    red = "\033[1;31m"
    yellow = "\033[1;33m"
    reset = "\033[0m"
    
    print(f"\n{red}╔{'═'*60}╗")
    print(f"║{'LEGAL WARNING':^60}║")
    print(f"╚{'═'*60}╝{reset}")
    print(f"{yellow}[!] This tool is for authorized security testing only.")
    print(f"[!] Unauthorized use against networks you don't own is illegal.")
    print(f"[!] You are solely responsible for your actions.{reset}")
    print(f"{yellow}[!] By using this tool, you agree to use it only for lawful purposes.")
    print(f"[!] The developer is not responsible for any misuse.{reset}")
    
    response = input("\nType 'I AGREE' to continue or any key to exit: ").strip()
    if response.upper() != "I AGREE":
        sys.exit(f"{red}[!] Legal agreement not accepted. Exiting...{reset}")

# Show warning immediately when script starts
show_legal_warning()

class DragonURLScanner:
    def __init__(self):
        self.red = "\033[1;31m"
        self.green = "\033[1;32m"
        self.yellow = "\033[1;33m"
        self.blue = "\033[1;34m"
        self.purple = "\033[1;35m"
        self.cyan = "\033[1;36m"
        self.reset = "\033[0m"
        self.clear_screen()
        self.show_banner()
        self.main_menu()

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def show_banner(self):
        print(f"""{self.red}
  
         ______        _____         _____    _____   ______        ______        _____   
     ___|\     \   ___|\    \    ___|\    \  |\    \ |\     \   ___|\     \   ___|\    \  
    |    |\     \ /    /\    \  /    /\    \  \\    \| \     \ |     \     \ |    |\    \ 
    |    |/____/||    |  |    ||    |  |    |  \|    \  \     ||     ,_____/||    | |    |
 ___|    \|   | ||    |  |____||    |__|    |   |     \  |    ||     \--'\_|/|    |/____/ 
|    \    \___|/ |    |   ____ |    .--.    |   |      \ |    ||     /___/|  |    |\    \ 
|    |\     \    |    |  |    ||    |  |    |   |    |\ \|    ||     \____|\ |    | |    |
|\ ___\|_____|   |\ ___\/    /||____|  |____|   |____||\_____/||____ '     /||____| |____|
| |    |     |   | |   /____/ ||    |  |    |   |    |/ \|   |||    /_____/ ||    | |    |
 \|____|_____|    \|___|    | /|____|  |____|   |____|   |___|/|____|     | /|____| |____|V1.0.0
    \(    )/        \( |____|/   \(      )/       \(       )/    \( |_____|/   \(     )/  
     '    '          '   )/       '      '         '       '      '    )/       '     '   
                         '                                             '                  
{self.blue}
    Advanced URL Security Scanner - Detect Vulnerabilities & Threats
{self.reset}""")

    def main_menu(self):
        while True:
            print(f"\n{self.cyan}Main Menu:{self.reset}")
            print(f"1. Scan a URL")
            print(f"2. About This Tool")
            print(f"3. Steal Website Code")
            print(f"4. Exit")
            
            choice = input(f"\n{self.purple}Select an option (1-4): {self.reset}").strip()
            
            if choice == "1":
                self.clear_screen()
                self.show_banner()
                url = input(f"\n{self.blue}Enter URL to scan: {self.reset}").strip()
                if url.lower() in ['exit', 'back']:
                    self.clear_screen()
                    self.show_banner()
                    continue
                if url:
                    self.scan_url(url)
                    input(f"\n{self.blue}Press Enter to return to menu...{self.reset}")
                    self.clear_screen()
                    self.show_banner()
            elif choice == "2":
                self.clear_screen()
                self.show_banner()
                self.about_me()
                input(f"\n{self.blue}Press Enter to return to menu...{self.reset}")
                self.clear_screen()
                self.show_banner()
            elif choice == "3":
                self.clear_screen()
                self.show_banner()
                self.download_html()
                input(f"\n{self.blue}Press Enter to return to menu...{self.reset}")
                self.clear_screen()
                self.show_banner()
            elif choice == "4":
                print(f"\n{self.green}Goodbye!{self.reset}")
                exit()
            else:
                print(f"\n{self.red}Invalid choice. Please try again.{self.reset}")

    def download_html(self):
        url = input(f"\n{self.blue}Enter URL to download HTML: {self.reset}").strip()
        if not url:
            print(f"{self.red}[!] No URL provided{self.reset}")
            return
            
        if not url.startswith(('http://', 'https://')):
            url = 'http://' + url

        try:
            print(f"\n{self.blue}[+] Downloading HTML from: {url}{self.reset}")
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            
            # Get desktop path
            desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') if os.name == 'nt' else os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
            file_path = os.path.join(desktop, 'dragon.html')
            
            # Save HTML to file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(response.text)
                
            print(f"\n{self.green}[✓] HTML saved successfully to: {file_path}{self.reset}")
            
            # Show file size
            file_size = os.path.getsize(file_path) / 1024  # in KB
            print(f"{self.blue}[i] File size: {file_size:.2f} KB{self.reset}")
            
            # Count lines
            with open(file_path, 'r', encoding='utf-8') as f:
                line_count = sum(1 for _ in f)
            print(f"{self.blue}[i] Total lines: {line_count}{self.reset}")
            
        except requests.exceptions.RequestException as e:
            print(f"{self.red}[!] Failed to download HTML: {str(e)}{self.reset}")
        except Exception as e:
            print(f"{self.red}[!] Error: {str(e)}{self.reset}")

    def about_me(self):
        print(f"""
{self.cyan}About DRAGON-URL Scanner:{self.reset}

{self.yellow}Description:{self.reset}
This is an advanced URL security scanner that helps identify potential 
vulnerabilities and threats in websites. It provides comprehensive 
analysis including IP information, domain details, security headers, 
and common web vulnerabilities.

{self.yellow}Features:{self.reset}
- Website IP address and location detection
- Domain age and registration information
- Common vulnerability scanning (WordPress, PHP, admin panels)
- Suspicious content detection
- SSL/TLS verification
- Security header analysis
- HTML source code downloader

{self.yellow}Created by:{self.reset} [ELLIOT]
{self.yellow}TOOL OWNER PROFILE:{self.reset} [https://github.com/ElliotV56]
{self.yellow}Version:{self.reset} 1.0.0
""")

    def scan_url(self, url):
        try:
            if not url.startswith(('http://', 'https://')):
                url = 'http://' + url

            print(f"\n{self.blue}[+] Scanning URL: {url}{self.reset}\n")

            # 1. Get Website IP Address
            self.get_ip_address(url)

            # 2. Check Domain Information
            self.check_domain(url)

            # 3. Detect Common Vulnerabilities
            self.detect_vulnerabilities(url)

            # 4. Check for Suspicious Content
            self.check_suspicious_content(url)

            # 5. Verify SSL Certificate
            self.check_ssl(url)

            # 6. Analyze Website Headers
            self.analyze_headers(url)

            print(f"\n{self.green}[✓] Scan completed{self.reset}")

        except Exception as e:
            print(f"{self.red}[!] Scan error: {str(e)}{self.reset}")

    def get_ip_address(self, url):
        try:
            domain = urlparse(url).netloc
            ip = socket.gethostbyname(domain)
            print(f"{self.blue}[+] Website IP Address: {ip}{self.reset}")
            
            # Get IP location (country)
            try:
                response = requests.get(f"http://ip-api.com/json/{ip}").json()
                print(f"{self.blue}[+] IP Location: {response.get('country', 'Unknown')}{self.reset}")
                print(f"{self.blue}[+] ISP: {response.get('isp', 'Unknown')}{self.reset}")
            except:
                pass
                
        except:
            print(f"{self.red}[!] Could not resolve IP address{self.reset}")

    def check_domain(self, url):
        try:
            domain = urlparse(url).netloc
            w = whois.whois(domain)
            
            print(f"\n{self.blue}=== DOMAIN INFORMATION ==={self.reset}")
            
            if isinstance(w.creation_date, list):
                creation_date = w.creation_date[0]
            else:
                creation_date = w.creation_date
            
            age = (datetime.now() - creation_date).days
            print(f"{self.blue}[i] Domain Age: {age} days{self.reset}")
            
            if age < 30:
                print(f"{self.red}[!] Warning: New domain (potential phishing risk){self.reset}")
            
            print(f"{self.blue}[i] Registrar: {w.registrar}{self.reset}")
            print(f"{self.blue}[i] Expiration Date: {w.expiration_date}{self.reset}")
            
        except:
            print(f"{self.yellow}[!] Could not fetch domain information{self.reset}")

    def detect_vulnerabilities(self, url):
        try:
            print(f"\n{self.blue}=== VULNERABILITY SCAN ==={self.reset}")
            
            response = requests.get(url, timeout=5)
            
            # Check for WordPress
            if 'wp-content' in response.text.lower():
                print(f"{self.yellow}[!] Detected: WordPress (common CMS vulnerabilities){self.reset}")
                
            # Check for PHP
            if '.php' in response.text.lower():
                print(f"{self.yellow}[!] Detected: PHP (potential injection risks){self.reset}")
                
            # Check for admin panels
            admin_paths = ['/admin', '/wp-admin', '/login', '/dashboard']
            for path in admin_paths:
                test_url = url + path
                try:
                    r = requests.get(test_url, timeout=3)
                    if r.status_code == 200:
                        print(f"{self.red}[!] Found: Admin panel at {test_url}{self.reset}")
                except:
                    pass
                    
            # Check for SQL errors (potential SQLi)
            if 'sql' in response.text.lower() and 'error' in response.text.lower():
                print(f"{self.red}[!] Possible SQL Injection vulnerability{self.reset}")
                
            # Check for exposed directories
            dir_paths = ['/assets', '/images', '/js', '/css']
            for path in dir_paths:
                test_url = url + path
                try:
                    r = requests.get(test_url, timeout=3)
                    if r.status_code == 200:
                        print(f"{self.yellow}[!] Found: Directory listing at {test_url}{self.reset}")
                except:
                    pass
                
        except:
            print(f"{self.yellow}[!] Could not complete vulnerability scan{self.reset}")

    def check_suspicious_content(self, url):
        try:
            response = requests.get(url, timeout=5)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            print(f"\n{self.blue}=== CONTENT ANALYSIS ==={self.reset}")
            
            # Check for forms
            forms = soup.find_all('form')
            if forms:
                print(f"{self.yellow}[!] Found {len(forms)} input forms (potential data collection){self.reset}")
                for form in forms:
                    if 'password' in str(form).lower():
                        print(f"{self.red}[!] Found password input form{self.reset}")
                
            # Check for suspicious keywords
            scam_keywords = ['win', 'prize', 'account', 'password', 'update', 'verify', 'login', 'secure']
            found = [word for word in scam_keywords if word in response.text.lower()]
            if found:
                print(f"{self.red}[!] Warning: Suspicious keywords found: {', '.join(found)}{self.reset}")
                
            # Check for iframes
            iframes = soup.find_all('iframe')
            if iframes:
                print(f"{self.yellow}[!] Found {len(iframes)} iframes (potential clickjacking risk){self.reset}")
                
        except:
            print(f"{self.yellow}[!] Could not analyze content{self.reset}")

    def check_ssl(self, url):
        if url.startswith('https://'):
            print(f"\n{self.green}[✓] HTTPS secured connection{self.reset}")
            try:
                response = requests.get(url, timeout=5, verify=True)
                print(f"{self.green}[✓] Valid SSL certificate{self.reset}")
            except requests.exceptions.SSLError:
                print(f"{self.red}[!] Invalid SSL certificate{self.reset}")
        else:
            print(f"\n{self.red}[!] No HTTPS (unsecured connection){self.reset}")

    def analyze_headers(self, url):
        try:
            response = requests.head(url, timeout=5)
            
            print(f"\n{self.blue}=== SECURITY HEADERS ==={self.reset}")
            
            # Check for security headers
            security_headers = {
                'X-Frame-Options': 'Missing (clickjacking risk)',
                'X-XSS-Protection': 'Missing (XSS protection)',
                'Content-Security-Policy': 'Missing (content injection protection)',
                'Strict-Transport-Security': 'Missing (HTTPS enforcement)',
                'X-Content-Type-Options': 'Missing (MIME sniffing protection)'
            }
            
            for header, message in security_headers.items():
                if header in response.headers:
                    print(f"{self.green}[✓] {header}: Present{self.reset}")
                else:
                    print(f"{self.yellow}[!] {header}: {message}{self.reset}")
                    
            # Check server header
            if 'Server' in response.headers:
                print(f"{self.blue}[i] Server: {response.headers['Server']}{self.reset}")
                
        except:
            print(f"{self.yellow}[!] Could not analyze headers{self.reset}")

if __name__ == "__main__":
    try:
        scanner = DragonURLScanner()
    except KeyboardInterrupt:
        print("\nGoodbye!")
        exit()

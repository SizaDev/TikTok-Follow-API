# 🎯 TikTok Follow API Automation (official)

This script demonstrates how to send an automated **follow request** to a TikTok user via their internal API. It emulates mobile app behavior by constructing authenticated requests using dynamic parameters, secure signatures (`x-argus`, `x-gorgon`, etc.), and encrypted payloads.

> ⚠️ **Disclaimer:** This project is for **educational and research purposes only**. Use of private APIs may violate TikTok’s Terms of Service.

---

## 🚀 Features

- Mimics TikTok Android requests using real device fingerprints
- Generates dynamic parameters via `Siza` utilities (`god`, `ladon`, `argus`, etc.)
- Signs each request using HMAC encryption and custom tokens
- Fully customizable: user ID, session cookies, device info

---

## 📌 How It Works

1. Collect valid session cookie and TikTok user identifiers
2. Use `Siza` functions to dynamically generate secure headers
3. Encode and sign request content via HMAC SHA-512
4. Send the GET request to TikTok’s internal follow endpoint

---

## 🤝 Want Full Access?

To access the **complete source code**, full API library, or to request a custom integration:

📲 Contact me on Telegram: [@SizaGod](https://t.me/SizaGod)

---

## ⚖️ License

This code is provided **without any warranty**. Use responsibly and at your own risk.  
Copyright © 2025

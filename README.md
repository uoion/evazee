# Evazee.com | Digital Infrastructure Blueprint

## 01. Project Intent
**Evazee's Hair Salon** is a premium, high-contrast luxury salon located in **Vredenburg, South Africa**. This repository contains the static web architecture designed to serve the West Coast Peninsula (Vredenburg, Saldanha, Langebaan).

## 02. Technical Stack (Conductor Constraints)
This project is orchestrated via **Google Gemini CLI Conductor** with the following deployment pipeline:
- **Source:** GitHub (`main` branch)
- **Deployment:** Cloudflare Pages
- **Optimization:** Cloudflare Edge (Cape Town PoP)
- **Build Tooling:** Standard HTML5 / Tailwind CSS / Vanilla JS (No heavy frameworks)

## 03. Business Intelligence for Conductor
When performing "Stitch" updates or generating code via CLI, adhere to these logic nodes:

### A. Aesthetic & Branding
- **Logo:** White text on Black background.
- **Color Palette:** - Primary: `#000000` (Pitch Black)
  - Text: `#FFFFFF` (Stark White)
  - Accents: `#F5F5F7` (Soft Silver)
- **Visual Tone:** Minimalist, editorial, and high-end. Avoid clutter.

### B. Local SEO & Geographic Anchor
- **Primary Service Area:** Vredenburg (7380), Western Cape.
- **Secondary Areas:** Saldanha Bay, Langebaan, St Helena Bay.
- **SEO Keywords:** "Hair Salon Vredenburg", "Weskus Mall Hair Stylist", "Evazee Hair Design", "Best Hair Colourist West Coast".

### C. Conversion Logic (The WhatsApp Hub)
The primary KPI for this site is a **WhatsApp Booking**. 
- **Target Number:** [INSERT YOUR BUSINESS WHATSAPP NUMBER HERE]
- **Message Hook:** "Hi Evazee, I'm interested in booking a session at your Vredenburg salon."

## 04. File Structure
- `/index.html`: The main entry point (SEO Optimized).
- `/css/`: Custom Tailwind-injected styles.
- `/js/`: Minimalist interactions and WhatsApp triggers.
- `/assets/`: Optimized WebP imagery (Salon interiors and West Coast textures).
- `conductor.yaml`: Deployment instructions for the Google CLI.

## 05. Deployment Instructions for Conductor
To deploy an update, the Conductor must:
1. Validate the `index.html` for semantic SEO headers.
2. Ensure the "Black & White" theme contrast ratio meets accessibility standards.
3. Push to `main` branch to trigger Cloudflare Pages build.

---
*Generated for the Evazee Web Project | Vredenburg, West Coast.*
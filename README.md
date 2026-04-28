# Red Flag Detector

AI-powered tool that analyzes job descriptions, contracts, policies, and terms & conditions — and surfaces hidden red flags before you sign.

---

## What it does

Paste any document and get:
- A trust score (0–100)
- Number of red flags detected
- Each flag explained in plain English with severity (Critical / High / Medium)
- An overall verdict on whether to proceed

Supports: Job Descriptions, Contracts, Terms & Conditions, Policy Documents

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Flask |
| AI | Anthropic Claude API |
| Frontend | HTML, CSS, JavaScript |

---

## Getting Started

### Prerequisites
- Python 3.10+
- Anthropic API key — get one at [console.anthropic.com](https://console.anthropic.com)

### Installation

```bash
git clone https://github.com/sampurnaprabhu3/red-flag-detector.git
cd red-flag-detector

python -m venv venv
venv\Scripts\activate       # Windows
source venv/bin/activate    # Mac/Linux

pip install -r requirements.txt
```

### Setup API Key

```bash
cp .env.example .env
# Open .env and add your Anthropic API key
```

### Run

```bash
python app.py
# Open http://localhost:5000
```

---

## Screenshots
<img width="1911" height="950" alt="image" src="https://github.com/user-attachments/assets/5413c301-8107-42bb-adf8-e78a11191059" />


---

## Future Scope

- PDF upload support
- Side-by-side document comparison
- Export report as PDF
- Browser extension version

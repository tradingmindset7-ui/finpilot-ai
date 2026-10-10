# FinPilot AI

A beginner-friendly finance education assistant prototype built with Streamlit and the Google Gemini API. It is designed for learning financial concepts and statement literacy, not for personalised investment advice or live market data.

## Features

- Simple finance question-and-answer interface
- Example questions for financial ratios and statements
- Clear educational-use notice
- API key read from Streamlit secrets or an environment variable
- No API key stored in source code

## Run locally

1. Install Python 3.10 or newer.
2. Open a terminal in this folder and run:

   ```bash
   pip install -r requirements.txt
   streamlit run app.py
   ```

3. Create `.streamlit/secrets.toml` with the following content (never commit this file):

   ```toml
   GEMINI_API_KEY = "paste-your-private-key-here"
   ```

4. Refresh the app in your browser.

## Deploy for free with Streamlit Community Cloud

1. Create a GitHub account and a **public** repository named `finpilot-ai`.
2. Upload `app.py`, `requirements.txt`, `README.md`, `.gitignore`, and `.streamlit/config.toml`. Do **not** upload your private API key.
3. Sign in at https://share.streamlit.io/ using GitHub and create an app from this repository. Set the main file to `app.py`.
4. In the app's **Settings → Secrets**, add:

   ```toml
   GEMINI_API_KEY = "paste-your-private-key-here"
   ```

5. Save and deploy. Free-tier availability, limits, and terms can change.

## API key

Get a key from https://aistudio.google.com/ if your account/project is eligible. Keep it private. Do not put it in source code, public repository files, screenshots, or chat messages. Review the provider's current pricing, quotas, and data-use terms before using real user data.

## Model configuration

The default model is `gemini-2.5-flash`. If it is unavailable for your account, set an environment variable `GEMINI_MODEL` to a model currently available to your API project, or update the default in `app.py`.

## Roadmap before real-world use

- Add source-grounded document analysis with page references.
- Add transparent ratio calculators and validation tests.
- Add privacy policy, terms, contact details, and feedback mechanism.
- Test output quality, security, abuse cases, and API quota handling.
- Review applicable Indian legal and regulatory obligations before adding recommendations, securities research, or advisory features.

## Important limitations

This is an early prototype. It does not fetch verified live prices or filings, and model answers may be inaccurate. Do not rely on it for financial decisions. Do not upload sensitive personal or financial information.

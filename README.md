# Chatbot Application Snapshot

## Repository contents

Despite the historical repository name, the committed implementation identifies itself as a **Parchem chemical-product chatbot**, not a medical-assistance system. The nested app uses Streamlit with Firebase authentication, conversational modules, and order/email handling. The previous medical-feature description did not match this source.

## Project location

The application root is `prachem-chatbot-main/prachem-chatbot-main/`. It contains `app.py`, `requirements.txt`, and the `parchem/` package. The nested README identifies the project as `parchem-ai-chatbot`; retain its existing attribution.

## Local setup

1. Change into the application root above.
2. Create and activate a Python virtual environment.
3. Install dependencies with `python -m pip install -r requirements.txt`.
4. Review `parchem/config.py` and the authentication, LLM, and email modules to configure your own services and credentials.
5. Start the interface with `streamlit run app.py`.

The source depends on external services. Installation, service configuration, and end-to-end behavior have not been verified in this documentation pass. This repository does not establish medical capability or affiliation with the organization named by the imported project.

## Committed files

- `prachem-chatbot-main`/

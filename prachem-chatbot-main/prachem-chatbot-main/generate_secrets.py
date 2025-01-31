import os

# Get the TOML content from Heroku environment variable
toml_content = os.getenv("STREAMLIT_TOML")

if toml_content:
    os.makedirs(".streamlit", exist_ok=True)  # Ensure the directory exists
    with open(".streamlit/secrets.toml", "w") as f:
        f.write(toml_content)
    print("✅ secrets.toml generated successfully!")
else:
    print("❌ STREAMLIT_TOML environment variable not found!")

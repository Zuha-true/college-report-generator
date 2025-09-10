# helpers/gemini_client.py
import os
import google.generativeai as genai

def configure(api_key=None):
    """
    Configure gemini client. If api_key is None, expects environment variable GEMINI_API_KEY.
    """
    key = api_key or os.getenv("GEMINI_API_KEY")
    if not key:
        raise RuntimeError("No Gemini API key found. Set GEMINI_API_KEY env var or pass api_key.")
    genai.configure(api_key=key)

def generate_section(project_description: str, section_title: str, model: str = "models/gemini-1.5-pro"):
    """
    Generate a single section using the Gemini API.
    model: choose appropriate model name (check docs); default is example.
    Returns text content.
    """
    prompt = (
        f"Create a well-structured, college-level '{section_title}' for a mini-project report.\n\n"
        f"Project description: {project_description}\n\n"
        f"Write the {section_title} in formal academic style, 1–2 paragraphs for Abstract, 2–4 paragraphs for Introduction, etc."
    )
    # using google.generativeai text generation API (SDK name may vary — check google docs)
    resp = genai.generate_text(model=model, prompt=prompt, temperature=0.2, max_output_tokens=800)
    # response structure may vary; adapt based on the installed SDK version
    # resp.text or resp.candidates[0].content depending on SDK
    try:
        return resp.text
    except Exception:
        # fallback for alternative response shapes
        return resp.candidates[0].content
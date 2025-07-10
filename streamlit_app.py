import streamlit as st
import asyncio
import os
from dotenv import load_dotenv

from veo_model import (
    GoogleVeo3Model,
    VeoGenerationRequest,
    VideoQuality,
    VideoStyle
)

# Load credentials
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")
PROJECT_ID = os.getenv("GOOGLE_PROJECT_ID")

# Streamlit UI
st.set_page_config(page_title="🎬 Veo Video Generator", layout="centered")

st.title("🎬 Google Veo 3 Video Generator")
prompt = st.text_area("Enter your prompt:", value="A spaceship flying over a futuristic city at night")

col1, col2 = st.columns(2)
duration = col1.slider("Duration (seconds)", 2, 20, 5)
fps = col2.slider("Frames per second", 12, 60, 24)

quality = st.selectbox("Select video quality", list(VideoQuality), format_func=lambda x: x.value)
style = st.selectbox("Select video style", list(VideoStyle), format_func=lambda x: x.value)

aspect_ratio = st.selectbox("Aspect Ratio", ["16:9", "4:3", "1:1", "9:16"])

generate_button = st.button("Generate Video 🚀")

if generate_button:
    st.info("Initializing generation...")
    progress = st.progress(0)

    async def generate():
        async with GoogleVeo3Model(API_KEY, PROJECT_ID) as veo:
            req = VeoGenerationRequest(
                prompt=prompt,
                duration=duration,
                fps=fps,
                quality=quality,
                style=style,
                aspect_ratio=aspect_ratio
            )
            result = await veo.generate_and_wait(req, max_wait_time=600)
            return result

    result = asyncio.run(generate())

    if result.status == "completed":
        st.success("✅ Video generated successfully!")
        st.video(result.video_url)
        st.image(result.thumbnail_url, caption="Thumbnail")
        st.write(f"**Duration**: {result.duration} seconds")
    else:
        st.error(f"❌ Generation failed: {result.error_message or 'Unknown error'}")

# 🎬 Google Veo 3 Video Generator (Streamlit App)

This app lets you generate AI videos using Google's Veo 3 API through a simple web interface.

## 🧰 Features

- Prompt-based video generation
- Video quality, style, duration, and aspect ratio selection
- Realtime status and video preview
- Runs locally or in Docker

## 📦 Installation

```bash
git clone https://github.com/yourusername/veo-video-generator.git
cd veo-video-generator
pip install -r requirements.txt
```

Create a `.env` file with:
```
GOOGLE_API_KEY=your-key
GOOGLE_PROJECT_ID=your-project
```

Then run:
```bash
streamlit run streamlit_app.py
```

## 🐳 Docker Deployment

```bash
docker build -t veo-generator .
docker run -p 8501:8501 --env-file .env veo-generator
```

## 📄 License

MIT License

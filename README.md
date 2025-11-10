# DeepSeek-OCR

<p align="center">
  <img src="https://sdk.nexa.ai/_next/static/media/logo.110a33d5.svg" alt="Nexa AI Logo" width="180" style="filter: brightness(0) invert(0);"/>
</p>

DeepSeek-OCR is a powerful optical character recognition (OCR) system that leverages the DeepSeek-OCR model through a local NexaAI server. This project enables you to perform accurate text extraction from images using state-of-the-art AI models running entirely on your local machine.

---

## 🧩 Features

- **High-Accuracy OCR** — Extract text from images with state-of-the-art precision using the DeepSeek-OCR model.
- **Local Processing** — Fully offline processing without any cloud dependency or privacy concerns.
- **Multi-Format Support** — Handle various image formats including PNG, JPG, JPEG, and more.
- **OpenAI-Compatible API** — Connect to a local API server using the familiar OpenAI client library.
- **Flexible Input** — Process images from URLs or local file paths.
- **Extensible** — Built with a modular design for easy customization and extension.

---

## 📋 Tech Stack

- **Python 3.13+** — Core programming language
- **OpenAI Client Library** — For API communication
- **NexaAI** — Local model serving platform
- **LXML** — For processing structured data
- **Pandas** — For data manipulation and analysis

---

## 🔧 Installation

1. **Clone or download** the project to your local machine.

2. **Set up a virtual environment** (recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies** using uv or pip:
   ```bash
   # Using uv (recommended)
   uv sync

   # Or using pip
   pip install -r requirements.txt
   # Or install directly from pyproject.toml
   pip install .
   ```

4. **Set up NexaAI Server**:
   - Install the NexaAI SDK
   - Download the DeepSeek-OCR model using the command:
     ```bash
     nexa run NexaAI/DeepSeek-OCR-GGUF
     ```
   - Follow the on-screen instructions to start the local inference server

---

## 🚀 Quick Start

Here's a simple example to get you started with DeepSeek-OCR:

```python
from ocr import ocr_image_from_url

# Perform OCR on an image from a URL
image_url = "path/to/your/image.png"  # Replace with your image path
result = ocr_image_from_url(image_url)
print(result)
```

---

## 💡 Usage Examples

### Basic OCR Processing

```python
from ocr import ocr_image_from_url

# Process an image file (using file URL format)
image_path = r"C:\Users\username\Desktop\image.png"
result = ocr_image_from_url(f"file://{image_path}")
print(result)
```

### Processing from Web URL

```python
from ocr import ocr_image_from_url

# Process an image directly from a web URL
web_image_url = "https://example.com/sample_image.png"
result = ocr_image_from_url(web_image_url)
print(result)
```

### Batch Processing Multiple Images

```python
from ocr import ocr_image_from_url

image_urls = [
    "image1.png",
    "image2.jpg",
    "image3.jpeg"
]

for url in image_urls:
    result = ocr_image_from_url(url)
    print(f"Results for {url}:")
    print(result)
    print("-" * 40)
```

---

## 📁 Project Structure

```
DeepSeek-OCR/
├── ocr.py                 # Main OCR functionality and API integration
├── chat.py               # Placeholder for chat functionality (TODO)
├── image_gen.py          # Placeholder for image generation (TODO)
├── pyproject.toml        # Project dependencies and metadata
├── README.md             # Project documentation
├── uv.lock              # Dependency lock file
├── .python-version      # Python version specification
├── .gitignore           # Git ignore rules
├── .venv/               # Virtual environment (if created)
└── images/              # Sample images directory
    ├── table.png        # Sample table image for testing
    └── written.png      # Sample handwritten image for testing
```

---

## ⚙️ Configuration

The OCR functionality connects to a local NexaAI server. You can modify the connection settings in `ocr.py`:

```python
client = OpenAI(
    base_url="http://127.0.0.1:18181/v1",  # Default NexaAI server address
    api_key="nexa"                         # Default API key for NexaAI
)
```

### Model Parameters

You can adjust the OCR behavior by modifying these parameters in `ocr_image_from_url`:
- `max_tokens` (default: 4096) — Controls the maximum length of the response
- `stream` (default: False) — Whether to stream responses
- The prompt template can be modified for different OCR styles

---

## 🤖 How It Works

1. The system connects to a locally running NexaAI server hosting the DeepSeek-OCR model
2. Images are sent to the server using an OpenAI-compatible API
3. The DeepSeek-OCR model processes the image and extracts text
4. The extracted text is returned as a string to the caller

This architecture ensures privacy and enables offline processing while providing high-quality OCR results.

---

## 🔍 Troubleshooting

### Common Issues and Solutions

- **Connection Error**: If you get a connection error, ensure that the NexaAI server is running and accessible at the specified URL (default: http://127.0.0.1:18181/v1)

- **Model Not Found**: If the model isn't found, ensure you have downloaded the DeepSeek-OCR model using:
  ```bash
  nexa run NexaAI/DeepSeek-OCR-GGUF
  ```

- **Image Format Error**: Ensure your images are in a supported format (JPG, PNG, etc.)

- **API Key Issues**: Verify that the API key matches what's expected by your NexaAI server (default: "nexa")

### Performance Tips

- For large images, consider resizing them before processing to improve performance
- The quality of OCR results depends on image clarity, so preprocess images when possible

---

## 👏 Acknowledgments

- [Nexa AI](https://sdk.nexa.ai/) for providing the local AI model serving platform
- The DeepSeek team for developing the OCR model
- The OpenAI client library for providing the API interface
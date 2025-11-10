<p align="center">
  <img src="https://sdk.nexa.ai/_next/static/media/logo.110a33d5.svg" alt="Nexa AI Logo" width="180" style="filter: brightness(0) invert(0);"/>
</p>

<p align="center">
  <strong>Open-source OCR solution powered by DeepSeek-OCR model and Nexa AI</strong>
</p>

<p align="center">
  Extract text from images using a locally deployed DeepSeek-OCR model with OpenAI-compatible API
</p>

---

## 📋 Table of Contents

- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Quick Start](#-quick-start)
- [Usage](#-usage)
- [Configuration](#-configuration)
- [Project Structure](#-project-structure)
- [Examples](#-examples)
- [Troubleshooting](#-troubleshooting)
- [License](#-license)
- [Acknowledgments](#-acknowledgments)

---

## 🧩 Features

- **Local OCR Processing**: Run OCR completely offline using the DeepSeek-OCR model
- **OpenAI-Compatible API**: Connect to a local Nexa AI server using OpenAI's API format
- **Image URL Support**: Process images from local paths or remote URLs
- **High-Quality Text Extraction**: Leverage DeepSeek-OCR's advanced multimodal capabilities
- **Simple Integration**: Easy-to-use Python interface with minimal setup
- **Batch Processing Ready**: Designed for integration into larger applications

---

## 🛠️ Tech Stack

- **Python 3.13+**
- **[OpenAI Python SDK](https://github.com/openai/openai-python)** - For API communication
- **[Nexa AI](https://sdk.nexa.ai/)** - Local AI model deployment platform
- **[DeepSeek-OCR](https://huggingface.co/NexaAI/DeepSeek-OCR-GGUF)** - Advanced OCR model
- **[lxml](https://lxml.de/)** - XML/HTML parsing (for structured output)
- **[pandas](https://pandas.pydata.org/)** - Data manipulation and analysis
- **[GGUF Format](https://github.com/ggerganov/ggml/blob/master/docs/gguf.md)** - Optimized model format

---

## ⚙️ Prerequisites

- Python 3.13 or higher
- Pip package manager
- Git (for installation)
- At least 4GB of RAM (recommended 8GB+ for optimal performance)
- Storage space for the DeepSeek-OCR model (~2-4GB depending on the specific model variant)

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/DeepSeek-OCR.git
cd DeepSeek-OCR
```

### 2. Set up Python Environment

```bash
# Create a virtual environment
python -m venv .venv

# Activate the virtual environment
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
# Or if using pyproject.toml:
pip install .
```

### 4. Install and Set up Nexa AI

```bash
# Install Nexa AI SDK
pip install nexaai

# Deploy the DeepSeek-OCR model locally
nexa run NexaAI/DeepSeek-OCR-GGUF
```

This will download the model and start a local API server at `http://127.0.0.1:18181/v1`

---

## 🎯 Quick Start

1. **Start the local Nexa AI server** (if not already running):
   ```bash
   nexa run NexaAI/DeepSeek-OCR-GGUF
   ```

2. **Run the OCR on a sample image**:
   ```bash
   python ocr.py
   ```

3. **Example Python usage**:
   ```python
   from ocr import ocr_image_from_url
   
   # For local image
   image_path = "images/table.png"
   result = ocr_image_from_url(image_path)
   print(result)
   
   # For remote image URL
   image_url = "https://example.com/image.jpg"
   result = ocr_image_from_url(image_url)
   print(result)
   ```

---

## 📖 Usage

### Basic OCR Function

The main function `ocr_image_from_url(image_url)` takes an image URL or file path and returns extracted text:

```python
from ocr import ocr_image_from_url

# Process a local image
result = ocr_image_from_url("images/written.png")
print(result)

# Process a remote image
result = ocr_image_from_url("https://example.com/document.jpg")
print(result)
```

### Advanced Usage

You can customize the OCR process by modifying the parameters in the `ocr.py` file:

```python
response = client.chat.completions.create(
    model="NexaAI/DeepSeek-OCR-GGUF",  # Model identifier
    messages=[...],                    # Input messages
    stream=False,                      # Set to True for streaming
    max_tokens=4096                    # Maximum tokens in response
)
```

### Processing Multiple Images

```python
from ocr import ocr_image_from_url
import pandas as pd

# Process multiple images
image_urls = [
    "images/table.png",
    "images/written.png",
    # Add more image URLs
]

results = []
for url in image_urls:
    try:
        text = ocr_image_from_url(url)
        results.append({"image": url, "extracted_text": text})
    except Exception as e:
        print(f"Error processing {url}: {e}")

# Convert to DataFrame for analysis
df = pd.DataFrame(results)
```

---

## ⚙️ Configuration

### API Configuration

The OCR module connects to a local Nexa AI server. You can modify the connection settings in `ocr.py`:

```python
client = OpenAI(
    base_url="http://127.0.0.1:18181/v1",  # Local server URL
    api_key="nexa"                        # Default API key for local server
)
```

### Model Parameters

You can adjust these parameters in the `ocr_image_from_url` function:

- `max_tokens`: Maximum number of tokens in the response (default: 4096)
- `temperature`: Controls randomness (default: 0 for deterministic output)
- `top_p`: Nucleus sampling parameter (default: 1.0)

---

## 📁 Project Structure

```
DeepSeek-OCR/
├── ocr.py              # Main OCR functionality
├── chat.py             # Placeholder for chat functionality (TODO)
├── image_gen.py        # Placeholder for image generation (TODO)
├── pyproject.toml      # Project dependencies and metadata
├── uv.lock            # Dependency lock file
├── README.md          # This file
├── .gitignore         # Git ignore patterns
├── .python-version    # Python version specification
├── .venv/             # Virtual environment (if created)
└── images/
    ├── table.png      # Sample table image for testing
    └── written.png    # Sample handwritten text image for testing
```

---

## 💡 Examples

### Example 1: Basic Text Extraction

```python
from ocr import ocr_image_from_url

# Extract text from a table image
result = ocr_image_from_url("images/table.png")
print("Extracted text from table.png:")
print(result)
```

### Example 2: Processing Handwritten Text

```python
from ocr import ocr_image_from_url

# Extract text from handwritten content
result = ocr_image_from_url("images/written.png")
print("Extracted text from handwritten image:")
print(result)
```

### Example 3: Batch Processing

```python
from ocr import ocr_image_from_url
import pandas as pd

# Define images to process
images_to_process = [
    "images/table.png",
    "images/written.png"
]

# Process each image
results = []
for img_path in images_to_process:
    try:
        extracted_text = ocr_image_from_url(img_path)
        results.append({
            "image": img_path,
            "text": extracted_text,
            "status": "success"
        })
        print(f"✓ Processed {img_path}")
    except Exception as e:
        results.append({
            "image": img_path,
            "text": "",
            "status": f"error: {str(e)}"
        })
        print(f"✗ Error processing {img_path}: {e}")

# Save results to CSV
df = pd.DataFrame(results)
df.to_csv("ocr_results.csv", index=False)
print("\nResults saved to ocr_results.csv")
```

---

## 🔧 Troubleshooting

### Common Issues

**1. Connection Error to Local Server**
- Make sure the Nexa AI server is running: `nexa run NexaAI/DeepSeek-OCR-GGUF`
- Verify the server is accessible at `http://127.0.0.1:18181/v1`

**2. Model Not Found Error**
- Ensure you have downloaded the DeepSeek-OCR model: `nexa run NexaAI/DeepSeek-OCR-GGUF`
- Check that the model name in `ocr.py` matches the deployed model

**3. Memory Issues**
- Ensure you have sufficient RAM (at least 4GB recommended)
- Close other applications to free up memory
- Consider using a smaller model if available

**4. Image Format Issues**
- Supported formats: PNG, JPG, JPEG, WebP
- Ensure image paths/URLs are accessible
- Large images may need to be resized for optimal performance

### Debugging Tips

1. **Check Server Status**: Visit `http://127.0.0.1:18181/v1/models` to verify the server is running
2. **Verify Model Deployment**: Ensure the DeepSeek-OCR model is properly deployed
3. **Test with Sample Images**: Use the provided images in the `images/` folder first
4. **Check Logs**: Monitor the Nexa AI server logs for errors

---

## 🙏 Acknowledgments

- **[Nexa AI](https://sdk.nexa.ai/)** for providing the local AI deployment platform
- **[DeepSeek](https://www.deepseek.com/)** for developing the DeepSeek-OCR model
- **[OpenAI](https://openai.com/)** for the API specification that enables local model communication
- The open-source community for various libraries and tools that made this project possible

---
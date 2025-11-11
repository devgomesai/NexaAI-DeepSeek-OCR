# DeepSeek-OCR

<p align="center">
  <img src="https://sdk.nexa.ai/_next/static/media/logo.110a33d5.svg" alt="Nexa AI Logo" width="180" style="filter: brightness(0) invert(0);"/>
</p>

<p align="center">
  <em>Powerful OCR solution using DeepSeek-OCR model served via NexaAI with a Chainlit web interface</em>
</p>

<p align="center">
  <a href="#overview"><strong>Overview</strong></a> •
  <a href="#features"><strong>Features</strong></a> •
  <a href="#installation"><strong>Installation</strong></a> •
  <a href="#usage"><strong>Usage</strong></a> •
  <a href="#configuration"><strong>Configuration</strong></a>
</p>

---

## 📋 Overview

DeepSeek-OCR is a cutting-edge Optical Character Recognition (OCR) application that leverages the powerful DeepSeek-OCR model served locally through the NexaAI platform. The application provides both a command-line interface and an interactive web interface powered by Chainlit, enabling users to extract text from images with high accuracy and privacy.

This solution combines state-of-the-art OCR technology with a user-friendly interface, allowing for both direct API usage and web-based interaction for processing images from local files or URLs.

## ✨ Features

- **High-Quality OCR**: Powered by DeepSeek-OCR model for accurate text extraction
- **Multiple Input Methods**: Support for image URLs and file uploads
- **Web Interface**: Interactive Chainlit-based web application
- **Local Processing**: All processing happens locally for privacy and security
- **Multiple File Formats**: Supports various image formats (JPG, PNG, etc.)
- **Easy Integration**: Simple API for programmatic usage
- **Real-time Processing**: Fast and efficient text extraction

## 🛠️ Tech Stack

- **Python 3.13+** — Core programming language
- **NexaAI** — Local model serving platform
- **DeepSeek-OCR-GGUF** — OCR model for text extraction
- **Chainlit** — Web interface framework
- **OpenAI Client Library** — For API communication
- **LXML** — For processing structured data
- **Pandas** — For data manipulation and analysis

## 📋 Prerequisites

Before installing DeepSeek-OCR, ensure you have:

- Python 3.13 or higher
- Pip or uv package manager
- Git (for cloning the repository)
- Sufficient disk space for the DeepSeek-OCR model (~1.8GB)

## 🔧 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/DeepSeek-OCR.git
cd DeepSeek-OCR
```

### 2. Set up a Virtual Environment (Recommended)

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install Dependencies

Using uv (recommended):
```bash
uv sync
```

Or using pip:
```bash
pip install -e .
```

### 4. Install and Set up NexaAI Server

1. Install the NexaAI SDK:
   ```bash
   pip install nexaai
   ```

2. Download the DeepSeek-OCR model:
   ```bash
   nexa run NexaAI/DeepSeek-OCR-GGUF
   ```
   Follow the prompts to complete the model download.

3. Start the NexaAI server:
   ```bash
   nexa serve
   ```
   The server will start on `http://127.0.0.1:18181/v1` by default.

## 🚀 Quick Start

### Web Interface

Start the Chainlit web application:
```bash
chainlit run app.py -w
```

Then open your browser to `http://localhost:8000` to access the OCR interface.

### Command Line Usage

```python
from ocr import ocr_image_from_url

# Process an image from a URL
image_url = "https://example.com/sample_image.png"
result = ocr_image_from_url(image_url)
print(result)
```

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
    "https://example.com/image1.png",
    "https://example.com/image2.jpg",
    "https://example.com/image3.jpeg"
]

for url in image_urls:
    result = ocr_image_from_url(url)
    print(f"Results for {url}:")
    print(result)
    print("-" * 40)
```

## 📁 Project Structure

```
DeepSeek-OCR/
├── app.py                 # Chainlit web interface
├── ocr.py                 # Core OCR functionality and API integration
├── pyproject.toml         # Project dependencies and metadata
├── chainlit.md            # Chainlit welcome page content
├── README.md              # Project documentation
├── uv.lock                # Dependency lock file
├── .python-version        # Python version specification
├── .gitignore             # Git ignore rules
├── .chainlit/             # Chainlit configuration directory
│   └── config.toml        # Chainlit configuration
├── .venv/                 # Virtual environment (if created)
└── images/                # Sample images directory
    ├── table.png          # Sample table image for testing
    └── written.png        # Sample handwritten image for testing
```

## ⚙️ Configuration

### NexaAI Server Configuration

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

### Chainlit Configuration

The web interface can be customized through `.chainlit/config.toml`:
- UI settings (theme, layout, etc.)
- File upload limits and accepted types
- Session timeout settings
- Security configurations

## 🌐 Web Interface Usage

The Chainlit web interface provides an easy-to-use interface for OCR processing:

1. **Upload Images**: Drag and drop image files or click to upload
2. **URL Processing**: Paste direct image URLs for processing
3. **Real-time Results**: View extracted text immediately after processing
4. **Interactive Chat**: Communicate with the OCR assistant

The interface supports:
- Multiple image formats (JPG, PNG, etc.)
- File size up to 500MB per file
- Batch processing of multiple images

## 🧪 Testing

To test the application with sample images:

```bash
# Start the NexaAI server first
nexa serve

# Then run the OCR on sample images
python -c "from ocr import ocr_image_from_url; print(ocr_image_from_url('file://images/table.png'))"
```

## 🔍 Troubleshooting

### Common Issues and Solutions

**Connection Error**: If you get a connection error, ensure that the NexaAI server is running and accessible at the specified URL (default: http://127.0.0.1:18181/v1)

**Model Not Found**: If the model isn't found, ensure you have downloaded the DeepSeek-OCR model using:
```bash
nexa run NexaAI/DeepSeek-OCR-GGUF
```

**Image Format Error**: Ensure your images are in a supported format (JPG, PNG, etc.)

**API Key Issues**: Verify that the API key matches what's expected by your NexaAI server (default: "nexa")

**File Upload Issues**: Check that your file is within the size limits and in a supported format

### Performance Tips

- For large images, consider resizing them before processing to improve performance
- The quality of OCR results depends on image clarity, so preprocess images when possible
- Ensure sufficient system resources (RAM and storage) for model loading and inference

### Debugging

Enable verbose logging for debugging:
```bash
# Check if the NexaAI server is running properly
curl http://127.0.0.1:18181/v1/models

# Verify the OCR function works directly
python -c "from ocr import ocr_image_from_url; print(ocr_image_from_url('path/to/test/image.png'))"
```

## 🚀 Performance

- **Processing Speed**: Varies based on image complexity and system resources
- **Accuracy**: High accuracy for clear text, with specialized handling for tables and structured documents
- **Memory Usage**: Approximately 4-6GB RAM required for model loading
- **Model Size**: ~1.8GB for the DeepSeek-OCR-GGUF model

## 🤝 Contributing

We welcome contributions to the DeepSeek-OCR project! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

Please ensure your code follows the project's coding standards and includes appropriate tests.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👏 Acknowledgments

- [Nexa AI](https://sdk.nexa.ai/) for providing the local AI model serving platform
- The DeepSeek team for developing the OCR model
- The Chainlit team for the excellent web interface framework
- The OpenAI client library for providing the API interface
- All contributors and users of this project

## 📞 Support

For support, please open an issue in the GitHub repository or contact the maintainers.

For more information about NexaAI and DeepSeek-OCR, visit the official documentation.
from openai import OpenAI

client = OpenAI(
    base_url="http://127.0.0.1:18181/v1",
    api_key="nexa"
)

def ocr_image_from_url(image_url: str) -> str:
    """
    Perform OCR on an image from a URL
    
    Args:
        image_url: Direct URL to the image
        
    Returns:
        Extracted text from the image
    """
    response = client.chat.completions.create(
        model="NexaAI/DeepSeek-OCR-GGUF",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": image_url
                        }
                    },
                    {
                        "type": "text",
                        "text": "<|FREE|>OCR."
                    }
                ]
            }
        ],
        stream=False,
        max_tokens=4096
    )
    
    return response.choices[0].message.content


# Example usage
if __name__ == "__main__":
    # Replace with your actual image URL
    image_url = r"C:\Users\ijona\Desktop\DeepSeek-OCR\images\table.png"
    
    result = ocr_image_from_url(image_url)
    print(result)
import chainlit as cl
from ocr import ocr_image_from_url
import tempfile
import os

@cl.on_chat_start
async def start():
    await cl.Message(
        content="👋 Welcome to **Nexa OCR Assistant!**\n\n"
                "Upload an image or paste an image URL, and I'll extract the text for you."
    ).send()

@cl.on_message
async def handle_message(message: cl.Message):
    # If the message contains an uploaded image
    if message.elements:
        image_element = next((e for e in message.elements if e.type == "image"), None)
        if image_element:
            # Save the uploaded image temporarily
            with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(image_element.name)[1] or ".jpg") as tmp:
                tmp.write(image_element.content)
                temp_path = tmp.name

            try:
                # Convert file path to file URL for the OCR function
                file_url = f"file://{temp_path}"
                await cl.Message(content="🔍 Running OCR on uploaded image...").send()
                
                result = ocr_image_from_url(file_url)
                await cl.Message(content="✅ **Extracted Text:**\n\n" + result).send()
            except Exception as e:
                await cl.Message(content=f"❌ Error: {str(e)}").send()
            finally:
                # Clean up the temporary file
                if os.path.exists(temp_path):
                    os.remove(temp_path)
            return

    # If the message contains a text URL
    elif message.content.strip().startswith(("http://", "https://")):
        image_url = message.content.strip()
        await cl.Message(content=f"🔗 Received image URL: {image_url}\nRunning OCR...").send()
        try:
            result = ocr_image_from_url(image_url)
            await cl.Message(content="✅ **Extracted Text:**\n\n" + result).send()
        except Exception as e:
            await cl.Message(content=f"❌ Error: {str(e)}").send()
    else:
        await cl.Message(
            content="Please either:\n"
                    "1️⃣ Upload an image file, or\n"
                    "2️⃣ Paste a direct image URL."
        ).send()

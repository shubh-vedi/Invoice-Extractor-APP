# Invoice Extractor App: Streamlit & Gemini Pro Vision

This Streamlit app leverages Google's Gemini Pro Vision model to extract information from invoices. It allows users to upload an invoice image and ask questions about it, receiving answers based on the model's understanding of the document.

## Features:

- **Image Uploader:** Users can upload invoice images in JPG, JPEG, or PNG formats.
- **Prompt Input:** Users can type in questions related to the invoice.
- **Model Response:** The app displays the generated text from Gemini Pro Vision, providing answers to the user's questions based on the invoice content.

## Usage:

1. **Run the Streamlit app:** Make sure you have Streamlit installed (`pip install streamlit`). Then, run the app from your terminal using `streamlit run app.py`.
2. **Upload an invoice image:** Click on the "Choose an image..." button to select an invoice image from your computer.
3. **Type a question:** In the "Input Prompt" field, ask a question about the invoice, e.g., "What is the invoice number?", "What is the total amount due?", "Who is the invoice issued to?".
4. **Click "Tell me about the image":** The app will send the image and your question to the Gemini Pro Vision model and display the generated response.

## Technical details:

- **Libraries:**
    - `streamlit`: for building the user interface.
    - `google.generativeai`: for interacting with the Gemini Pro Vision model.
    - `PIL`: for image handling.
    - `dotenv`: for loading environment variables from a `.env` file.
- **Environment variables:**
    - `GOOGLE_API_KEY`: Your Google Cloud API key.
- **Model:** The app uses the `gemini-pro-vision` model from Google's Generative AI platform.

## Getting started:

1. **Create a `.env` file:** Create a file named `.env` in the same directory as the app.
2. **Add your Google Cloud API key:** In the `.env` file, add the following line:
Replace `your_api_key` with your actual Google Cloud API key.
3. **Run the app:** Run the app using the command `streamlit run app.py`.

## Notes:

- The app uses a Google Cloud API key for authentication. Make sure you have a valid API key set up in your `.env` file.
- The Gemini Pro Vision model is a powerful tool, but it may still generate inaccurate or incomplete answers. Use your judgment when interpreting the responses.
- For optimal results, ensure your invoice images are clear, well-lit, and in a common format like JPG, JPEG, or PNG.

## Potential improvements:

- Add error handling for API calls.
- Implement image preprocessing to improve model accuracy.
- Allow users to copy/paste the generated response.
- Integrate the app with other AI tools or services for further analysis.

## **Further Development Ideas:**

- **Preprocessing:** Implement preprocessing steps like image resizing, contrast enhancement, and noise reduction to improve the quality of the input images.
- **Multi-Page Application:**  Create a more complex multi-page app with separate sections for uploading invoices, reviewing previous responses, and saving extracted data.
- **Data Extraction:**  Implement functionality to extract key information (like invoice number, total amount, etc.) from the generated text and store it in a database.
- **Advanced Question Answering:**  Enable users to ask more complex questions, such as "What is the total cost of all items related to [specific product name]?"
- **Visualizations:**  Visualize extracted invoice data using charts or tables to provide users with a better understanding of the invoice information.

These are just some ideas to enhance the Invoice Extractor App and make it a more powerful tool for invoice processing.

## License:

This project is licensed under the MIT License.

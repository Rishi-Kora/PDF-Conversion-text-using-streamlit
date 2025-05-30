[![Python Version](https://img.shields.io/badge/python-3.7%2C%203.8%2C%203.9-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-%E2%9C%93-green)](https://streamlit.io/)
[![License](https://img.shields.io/github/license/Rishi-Kora/PDF-Conversion-text-using-streamlit)](LICENSE)
[![Issues](https://img.shields.io/github/issues/Rishi-Kora/PDF-Conversion-text-using-streamlit)](https://github.com/Rishi-Kora/PDF-Conversion-text-using-streamlit/issues)

# PDF Conversion to Text using Streamlit

A simple Streamlit app to upload PDF files and convert them to plain text.  
Ideal for quick extraction of text from reports, articles, or scanned documents.

## Features

- Upload one or multiple PDF files via a web interface.
- Extract text content using `PyPDF2`.
- Display extracted text directly in the browser.
- Download the resulting text as a `.txt` file.

## Demo

![Demo Screenshot](assets/demo_screenshot.png)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Rishi-Kora/PDF-Conversion-text-using-streamlit.git
   cd PDF-Conversion-text-using-streamlit


2. Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # on Windows: venv\Scripts\activate
   ```
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the Streamlit app:

```bash
streamlit run app.py
```

* Open [http://localhost:8501](http://localhost:8501) in your browser.
* Upload PDF files using the sidebar.
* View or download the extracted text.

## Requirements

* Python 3.7+
* streamlit
* PyPDF2

## Contributing

1. Fork the repo.
2. Create a feature branch:

   ```bash
   git checkout -b feature/YourFeature
   ```
3. Commit your changes:

   ```bash
   git commit -m "Add new feature"
   ```
4. Push to branch:

   ```bash
   git push origin feature/YourFeature
   ```
5. Open a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

*Built with ❤️ by Rishi Kora*

```

Feel free to adjust badge URLs or add any additional sections (e.g., FAQs, troubleshooting) as your project evolves!
```

# LLM RAG Chat Interface

A conversational interface that implements Retrieval-Augmented Generation (RAG) with Large Language Models using Markdown files as the knowledge base. Built with Gradio for an interactive web interface.

## Features

- 🔍 RAG implementation for enhanced LLM responses using local markdown files
- 🌐 Interactive chat interface built with Gradio
- 📚 Markdown file support for knowledge base
- 💾 Context-aware responses based on retrieved documents
- 🚀 Easy to deploy and use

## Prerequisites

- Python 3.8+
- pip (Python package manager)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/llms_with_rag_gradio.git
cd llms_with_rag_gradio
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

4. Set up your environment variables by creating a `.env` file:
```env
API_KEY=your_api_key_here
```

## Project Structure

```
llms_with_rag_gradio/
├── data/                  # Your markdown files
├── src/
│   ├── __init__.py
│   ├── rag.py            # RAG implementation
│   └── utils.py          # Utility functions
├── app.py                # Main Gradio application
├── requirements.txt      # Project dependencies
└── README.md            # This file
```

## Usage

1. Place your markdown files in the `data/` directory.

2. Run the application:
```bash
python app.py
```

3. Open your browser and navigate to `http://localhost:7860` to access the chat interface.

## Configuration

### Environment Variables

Create a `.env` file in the root directory with the following variables:

```env
API_KEY=your_api_key_here
MODEL_NAME=your_preferred_model
```

### Customizing the RAG System

You can modify the RAG parameters in `src/rag.py`:

- Chunk size for document splitting
- Number of retrieved documents
- Similarity search parameters

## Example Usage

1. Start a conversation by typing your question in the chat interface
2. The system will:
   - Retrieve relevant information from your markdown files
   - Generate a response using the LLM
   - Display the response in the chat interface

## How It Works

1. **Document Processing**:
   - Markdown files are loaded from the data directory
   - Documents are split into chunks and embedded
   - Embeddings are stored for efficient retrieval

2. **Query Processing**:
   - User query is embedded
   - Similar chunks are retrieved from the document store
   - Retrieved context is used to enhance the LLM's response

3. **Response Generation**:
   - Context and query are combined into a prompt
   - LLM generates a response based on the enhanced context
   - Response is displayed in the Gradio interface

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with [Gradio](https://gradio.app/)
- LLM integration using [relevant_library]
- RAG implementation inspired by [relevant_sources]

## Support

For support, please open an issue in the GitHub repository or contact [your_contact_info].

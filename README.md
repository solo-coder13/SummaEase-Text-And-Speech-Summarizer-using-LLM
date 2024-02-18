**Empower users with succinct, accessible summaries of text and speech content through the power of language models.**
# SummaEase: Text and Speech Summarizer using Large Language Models

This project aims to develop a comprehensive summarization system that can efficiently extract key insights and valuable information from both written text and spoken language inputs. The system utilizes state-of-the-art large language models (LLMs) and natural language processing (NLP) techniques to generate high-quality summaries. We are developing a groundbreaking system that leverages the potential of large language models (LLMs) to revolutionize how people interact with information. Our key objectives are:

**1. Generate concise, accurate summaries:**

* Employ advanced LLM capabilities to extract the meaning and key points from text and speech data.
* Create summaries that are significantly shorter than the original content while retaining crucial information.
* Ensure summaries are factually accurate and unbiased, reflecting the core content without personal opinions or interpretations.

**2. Enhance information accessibility and efficiency for all:**

* Address the ever-growing information overload by providing a tool to effortlessly grasp the essence of content.
* Cater to diverse users' needs, including those seeking personal knowledge, efficient media consumption, educational advancement, or improved accessibility due to disabilities.
* Foster an inclusive, equitable information landscape where everyone can readily access and understand essential details.

By achieving these objectives, we aim to create a world where information is more manageable, digestible, and readily accessible to everyone. This project has the potential to transform how we consume, learn from, and interact with information, empowering individuals and unlocking new possibilities for knowledge exploration and understanding.


## Features

- **Text Summarization:** Extractive and abstractive summarization techniques.
- **Speech Summarization:** Transcribe spoken language into text for summarization.
- **Personalized Summaries:** Customizable summarization preferences.
- **User-Friendly Interface:** Easy input of text or speech content.

## Mathematical Formulation

### Extractive Summarization

Let \( D \) be the document to be summarized, and let \( S \) be the set of sentences in \( D \). The objective is to select a subset \( S' \subseteq S \) that maximizes the information content of the summary, subject to a length constraint.

### Abstractive Summarization

Let \( D \) be the document to be summarized, and let \( S' \) be the summary to be generated. The objective is to generate a summary \( S' \) that maximizes the semantic similarity to the original document.

## Installation

1. Clone the repository: `git clone https://github.com/solo-coder13/Text-and-Speech-Summarizer-using-LLM.git`
2. Install the required dependencies: `pip install -r requirements.txt`

## Usage

1. Run the text summarizer: `python text_summarizer.py --input_file input.txt --output_file output.txt`
2. Run the speech summarizer: `python speech_summarizer.py --input_audio audio.wav --output_text transcript.txt`
3. Access the user interface: Open `index.html` in a web browser.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.



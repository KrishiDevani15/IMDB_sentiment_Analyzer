# IMDb Sentiment Analyzer

![License](https://img.shields.io/badge/license-MIT-green)
![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)

## Overview

The **IMDb Sentiment Analyzer** is a deep learning application designed to classify movie reviews from IMDb as positive or negative using Long Short-Term Memory (LSTM) networks. Built with TensorFlow, this project leverages the power of LSTM to analyze sentiment in text data effectively. The model is deployed using Gradio for a user-friendly interface and Hugging Face for easy accessibility.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Model Architecture](#model-architecture)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Features

- LSTM-based sentiment analysis
- User-friendly interface powered by Gradio
- Deployment on Hugging Face for easy access
- Pre-trained model for immediate use


## Installation

To set up the project locally, follow these steps:

```bash
git clone https://github.com/KrishiDevani15/IMDB_sentiment_Analyzer.git
cd IMDB_sentiment_Analyzer
```





## Usage/Examples

To run the sentiment analyzer, use the following command:
```Python
python app.py
```
This will start a Gradio interface in your browser where you can input movie reviews and get sentiment predictions.

#### Example Input
- "This movie was fantastic! I loved it!"
- "The plot was boring and the acting was terrible."

#### Example Output
- Positive
- Negative


## Model Architecture
The model utilizes LSTM layers for sequence processing:

- Embedding Layer: Converts words into dense vectors of fixed size.
- LSTM Layer: Captures temporal dependencies in the text.
- Dense Layer: Outputs the final sentiment prediction using a softmax activation function.
## Deployment

This project can be deployed on Hugging Face with the following steps:

- Create a Hugging Face account (if you don't have one).

#### Install Hugging Face CLI and log in:

```bash
  pip install huggingface_hub
  huggingface-cli login
```

#### Upload the model:

```bash
  huggingface-cli repo create imdb-sentiment-analyzer
  cd imdb-sentiment-analyzer
  git lfs install
  git add .
  git commit -m "Initial commit"
  git push
```


## Contributing

Contributions are welcome! If you would like to contribute, please fork the repository and create a pull request with your changes..


## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/KrishiDevani15/IMDB_sentiment_Analyzer/blob/main/LICENSE) file for more details.


## Acknowledgements

 - [Tensorflow](https://github.com/tensorflow/tensorflow.git)
 - [Gradio](https://github.com/gradio-app/gradio.git)
 - [Hugging Face](https://github.com/huggingface/huggingface_hub.git)


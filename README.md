# FineTuningBERT

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

 Project Fine-Tuning and Comparing performance of DistilBERT, BERT, and BERT Large (cased) models using Hugging Face

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

## About The Project

Fine-tuning DistilBERT, BERT, and Large BERT cased models for sentiment analysis of financial data and creating a user interface that allows a user to select one of the models and enter a sentence for analysis.

### Built With
* [![HuggingFace][HuggingFace.com]][HuggingFace-url]
* [![PyTorch][Pytorch.com]][PyTorch-url]
* [![Scikit-Learn][Scikit-Learn.org]][Scikitlearn-url]
* [![Seaborn][Seaborn.com]][Seaborn-url]

## Getting Started

### Prerequisites

Required Libraries/Frameworks: <br>
HuggingFace, PyTorch, Scikit-Learn, Seaborn, Numpy, and Pandas

Recommended: <br>
PyTorch built with CUDA and NVidia GPU

### Installation

1. Clone the Repo
```sh
git clone https://github.com/zjshermanburke/FineTuningBERT.git
```
2. Run all cells in the Jupyter Notebook

## Usage

Run the Python script "Model_UI.py", enter a model (DistilBERT, BERT, or LargeBERT), and when prompted enter a statement. This will return a sentiment (Negative, Positive, or Neutral) and the BERT score.

## License

Distributed under the Unlicense license. See `LICENSE.txt`for more information.

## Contact

Zachary Sherman-Burke - [LinkedIn](https://www.linkedin.com/in/zachary-sherman-burke-6b7589125) - zjshermanburke@gmail.com

Project Link: [https://github.com/zjshermanburke/FineTuningBERT](https://github.com/zjshermanburke/FineTuningBERT)


## Acknowledgments

* [Img Shields](https://shields.io)
* [Best ReadMe Template](https://github.com/othneildrew/Best-README-Template)
* [Choose an Open Source License](https://choosealicense.com)

<!-- Markdown Links and Images-->

<!-- GitHub and LinkedIn-->
[contributors-shield]: https://img.shields.io/github/contributors/zjshermanburke/FineTuningBert.svg?style=for-the-badge
[contributors-url]: https://github.com/zjshermanburke/FineTuningBert/graphs/contributors

[forks-shield]: https://img.shields.io/github/forks/zjshermanburke/FineTuningBert.svg?style=for-the-badge
[forks-url]: https://github.com/zjshermanburke/FineTuningBert/network/members

[stars-shield]: https://img.shields.io/github/stars/zjshermanburke/FineTuningBert.svg?style=for-the-badge
[stars-url]: https://github.com/zjshermanburke/FineTuningBert/stargazers

[issues-shield]: https://img.shields.io/github/issues/zjshermanburke/FineTuningBert.svg?style=for-the-badge
[issues-url]: https://github.com/github/issues/zjshermanburke/FineTuningBERT.svg

[linkedin-url]: https://www.linkedin.com/in/zachary-sherman-burke-6b7589125
[linkedin-shield]: https://img.shields.io/badge/LinkedIn-blue.svg?style=for-the-badge&logo=linkedin&colorB=555


<!-- Built With Badges -->

<!-- [HuggingFace.com]: https://img.shields.io/badge/%F0%9F%A4%97Hugging_Face-ffd21e -->
[HuggingFace.com]: https://img.shields.io/badge/%F0%9F%A4%97Hugging_Face-ffd21e?style=for-the-badge&style=plastic
[HuggingFace-url]: https://huggingface.co/

[PyTorch.com]: https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white&style=plastic
[PyTorch-url]: https://pytorch.org/

[Scikit-Learn.org]: https://img.shields.io/badge/Scikit_Learn-29abe2?style=for-the-badge&logo=scikitlearn&logoColor=f7931e&style=plastic
[ScikitLearn-url]: https://scikit-learn.org/

[Seaborn.com]: https://img.shields.io/badge/Seaborn-white?style=for-the-badge&logo=seaborn&logoColor=f7931e&style=plastic
[Seaborn-url]: https://seaborn.pydata.org/
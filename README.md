# AIHK-DEUS
## Introduction
Prototype for the demonstration of AI agents capable of question set generation and user question answering. This showcases the technical feasibility of the DEUS platform, which aims for the provision of interactive and iterative online learning experience across diverse disciplines.

## Operation Mechanism
The operation mechanism of the ideal AI pipeline we plan is straighforward.

1. The lecture video and the timestamp labels are fed into the model.
2. Audio is extracted from the video in a .wav format.
3. Referring to the given timestamp label, the original audio is divided into multiple files.
4. Each audio file is fed into an ASR (Automatic Speech Recognition) model for voice-to-text conversion which outputs the transcribed text data.
5. The transcribed text is fed into a text summarizer, which shortens the length of the content while maintaining the necessary information.
6. The summary is fed into a keyphrase extractor to extract a set of phrases/words that take important portion on the text.
7. **Question set generation**: Using the keyphrases and the summary, question sets are generated. The model takes reference to the summary as contex while generating questions regarding the keyphrases. Additionally, examples of questions and requirements can be given which the model could use as further reference.
8. **Question answering**: Using the summarized content and the dataset it was fine-tuned with, the model generates responses relevant to the questions asked by a human user.

## Demonstration Acknowledgement
A sample of Andrew Ng's Stanford University Machine Learning course ([What Is Machine Learning](https://youtu.be/PPLop4L2eGk)) is mainly used (excluding ```gpt3-question-generation-2.ipynb```) for this demonstration.

## Descriptions
As this is a simple technical demonstration, programs are written in a discrete manner, rather than establishing a single pipeline for performing multiple tasks. The following is the list of Python file names and the respective function it takes:

```audio-trim-label.py```: Script for audio data preprocessing; given the timestamp details, the code divides and audio file into multiple short-lengthned files.

```asr.py```: Uses the [OpenAI Whisper ASR system](https://github.com/openai/whisper) for voice-to-text transcription. Outputs a .txt file containing the transcript for the given audio input.

```bart-summary.py```: Uses the Facebook BART ([bart-large-cnn](https://huggingface.co/facebook/bart-large-cnn)), a pre-trained natural language generation, translation, and comprehension model for text summarization. Outputs a .txt file containing the summarized version of the given .txt input.

```keyphrase-generation.py```: Uses a Google T5 variation model ([ml6team/keyphrase-generation-t5-small-openkp](https://huggingface.co/ml6team/keyphrase-generation-t5-small-openkp)) optimized for keyphrase extraction from text. Outputs a .txt file containing a list of keyphrases that take important portion on the given .txt input.

```t5-question-generation.py```: Uses a Google T5 variation model ([mrm8488/t5-base-finetuned-question-generation-ap](https://huggingface.co/mrm8488/t5-base-finetuned-question-generation-ap)) optimized for question generation given an answer and a context. Here, each keyphrase generated from ```keyphrase-generation.py``` is input as the answer parameter, with the summary generated from ```bart-summary.py``` input as the context. Outputs a .txt file containing a single generated question[^1].

[^1]: One significant limitation of this model is that it's only capable of generating very basic-level questions; shows optimal performance when the length of the input text for context is short. When you read through the questions generated by this customized T5 model, you'll notice that some questions are very basic while some are completely incomprehensible. The T5 model's performance is optimal when it's fine-tuned with a relevant custom dataset. However, fine-tuning the model wasn't done in this demonstration; this inevitably resulted in a basic-level/incomprehensible question output.

```gpt3-question-generation-1.py```: Uses the [OpenAI GPT-3 model](https://openai.com/api/) for question generation. The parameter details are identical as ```t5-question-generation.py```[^2].
<br>*An API key is necessary to have access to the GPT-3 model API. User account can be easily created on the webpage above.

[^2]: When you read through the questions generated by GPT-3, the results are mostly better than what's generated by the customized T5 model. This does not mean that GPT-3 has better text comprehension and generation abilities relevant to T5. T5's results were inevitable as fine-tuning with a custom dataset wasn't done prior to its usage. Both results would be comparable after a custom dataset is generated based on the lecture contents and fine-tuning models are done.

```gpt3-question-generation-2.ipynb```: Uses the OpenAI GPT-3 model for question generation. This showcases the question generation approach with reference examples and requirements provided to the model. This model allows user inputs for example questions which the model can mimic its structure and the requirements which it should cope with when generating questions.
<br>*An API key is necessary to have access to the GPT-3 model API. User account can be easily created on the webpage above.

```gpt3-question-answering.py```: Uses the OpenAI GPT-3 model for response generation given an input of the user's question. The model uses the summary generated from ```bart-summary.py``` and its own knowledge base for this task. Outputs a response in a string format.
<br>*An API key is necessary to have access to the GPT-3 model API. User account can be easily created on the webpage above.

## Model Acknowledgement
Demonstrating the question generation ability of the model was the most challenging, as different models (GPT-3 and T5) have respective characteristics in terms of approaching this task. Our ideal question generator would incorporate both the GPT-3 and T5 models for optimal task completion.

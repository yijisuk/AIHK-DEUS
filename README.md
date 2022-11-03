# AIHK-DEUS
Prototype for the demonstration of AI agents capable of question set generation and user question answering. This showcases the technical feasibility of the DEUS platform, which aims for the provision of interactive and iterative online learning experience across diverse disciplines.

The operation mechanism of the ideal AI pipeline we plan is straighforward.
<br>1. The lecture video and the timestamp labels are fed into the model.
<br>2. Audio is extracted from the video in a .wav format.
<br>3. Referring to the given timestamp label, the original audio is divided into multiple files.
<br>4. Each audio file is fed into an ASR (Automatic Speech Recognition) model for voice-to-text conversion which outputs the transcribed text data.
<br>5. The transcribed text is fed into a text summarizer to extract the key contents.
<br>6. The summary is fed into a keyword extractor to extract the set of words that take important portion on the text.
<br>7. 

As this is a simple technical demonstration, programs are written in a discrete manner, rather than establishing a single pipeline for performing multiple tasks. The following is the list of Python file names and the respective function it takes:

```audio-trim-label.py```: 
<br>```asr.py```:
<br>```bart-summary.py```:
<br>```keyphrase-generation.py```:
<br>```t5-question-generation.py```:
<br>```gpt3-question-generation.py```:
<br>```gpt3-question-answering.py```:

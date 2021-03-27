Title: Use AI to autotune audio and videos with atypical speech
Date: 2021-03-29
Modified: 2021-03-29
Category: Demo
Tags: Speech-impediment, ASR, wav2vec, kaldi
slug: demo/atypical-speech-autotune-demo
Authors: Shaomei Wu
Summary: A demo for autotuning my own speech in audios and videos to reduce disfluency.

## Auto-tuning Audio with Speech Disfluency

Original audio recording of speech with disfluency (you can hear lots of uh's and um's in my speech):

<audio controls>
<source src="/media/short_intro.wav">
Audio element failed...
</audio>

Original transcription: 

> Hi my name is Shaomei Wu and I um worked at Facebook. Um my research is at the intersection of um AI and um accessibility. So I try to build empowering AI, um, technology for marginalized communities. 

Autotuned version:

<audio controls>
<source src="/media/de_filler_short_intro.wav">
Audio element failed...
</audio>

## Auto-tuning Video with Speech Disfluency

Original video recording of me speaking:

- [Original Video]({static}/media/intro_video_short.mp4)

<video controls height="400">
<source src="/media/intro_video_short.mp4" type="video/mp4">
Video rendering failed...
</video>

Autotuned version:

- [Auto-tuned Video]({static}/media/autotuned_intro_video_short.mp4)

<video controls height="400">
<source src="/media/autotuned_intro_video_short.mp4" type="video/mp4">
Video rendering failed...
</video>


## Resources 

Read the blogpost for more details on how the autotuning works.

The code for producing the results can be found in this [notebook](https://colab.research.google.com/drive/1jn8oTaEJRMl9PEKi7jj8zfwnxctxox8u?usp=sharing). 

 
 

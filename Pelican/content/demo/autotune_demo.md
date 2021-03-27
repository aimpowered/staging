Title: Use AI to autotune audio and videos with atypical speech
Date: 2021-03-29
Modified: 2021-03-29
Category: Demo
Tags: Speech-impediment, ASR, wav2vec, kaldi
slug: demo/atypical-speech-autotune-demo
Authors: Shaomei Wu
Summary: A demo for autotuning my own speech in audio and video to reduce disfluency.

## Auto-tuning Audio with Speech Disfluency

Original audio recording of speech with disfluency:

<audio controls>
<source src="{static}/media/short_intro.wav">
Audio element failed...
</audio>

Original transcription (there are lots of um's): 

> Hi my name is Shaomei Wu and I, um, worked at Facebook. Um, my research is at the intersection of, um, AI and, um, accessibility. So I try to build empowering AI, um, technology for marginalized communities. 

Autotuned version:

<audio controls>
<source src="{static}/media/de_filler_short_intro.wav">
Audio element failed...
</audio>

## Auto-tuning Video with Speech Disfluency

Original video recording of me speaking (12 sec):

<!-- - [Original Video, 12sec]({static}/media/intro_video_short.mp4) -->

<video controls height="400">
<source src="{static}/media/intro_video_short.mp4" type="video/mp4">
Video rendering failed...
</video>

<br>

Autotuned version (10 sec):

<!-- - [Auto-tuned Video, 10sec]({static}/media/autotuned_intro_video_short.mp4) -->

<video controls height="400">
<source src="{static}/media/autotuned_intro_video_short.mp4" type="video/mp4">
Video rendering failed...
</video>


## Resources 

Read the [blogpost](/blog/atypical-speech-autotune.html) for more details on how the autotuning works.

The code for producing the results can be found in this [notebook](https://colab.research.google.com/drive/1jn8oTaEJRMl9PEKi7jj8zfwnxctxox8u?usp=sharing). 

 
 

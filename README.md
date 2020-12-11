# dft-tutorial

## Official EECS189 Project Site - Week 12 Time Series Data
https://www.notion.so/Project-T-0e6f5b376b4e4cfca401b79b09e53124

## Week 12: Topic 48: Encoding Audio with DFT
Notes and tutorial on encoding audio with DFT.  The tutorial includes an application of encoding audio with DFT for voice detection.

# Introduction
This lab will give you a new perspective on your data through the lens of the frequency domain by means of the Fourier Transform and variants of it. The Fourier Transform is a useful mathematical tool that takes a signal and breaks it down into its constituent frequencies. This allows us to look at time-varying data (such as an audio signal) or spatial data (such as a 2D image) by looking at the strength of each frequency that is contributed to the data point rather than just its spatial or time dependent magnitudes (i.e., the magnitude of a waveform at some time t or the brightness of a pixel in an image). You will also learn the power of using the frequency domain as an intermediate representation of time-varying and spatial data for downstream applications such as classification of raw audio signals.

In this lab, we are particularly interested in audio signals. We will first cover some of the basics of the Fourier Transform and analyze it through a series of toy examples. We will then take this understanding and apply it to the much more unstructured problem of classifying spoken digits given only a raw audio signal as input.

# Goals
The goals of this lab are to:
* Gain a practical understanding of the frequency domain representation of data through visualizations
* Gain an intuitive understanding of the benefits of using the frequency domain for certain types of data and applications
* Get hands on experience tackling a difficult real world problem using techniques learned in class

# How to use this repository
* dft/DFT_Tutorial.ipynb --> lab assignment to be completed
* dft/DFT_Tutorial_Soln.ipynb --> solutions to lab assignment
* DFT_note.pdf --> contains lesson notes to teach about Encoding with DFT.  Meant to be read before attempting the acompanying lab and quiz
* DFT_quiz.pdf --> contains quiz questions to asses understanding of acompanying note and lab
* DFT_quiz_soln.pdf --> contains solutions to the acompanying quiz
* DFT_slides.pdf --> acompanying slide deck for an overview of the lab and note

# ASL 🤟 Transcriber

## 💡 Motivation

Nowadays, our dependence on technology has become increasingly evident, especially with the recent circumstances that have propelled us to the era of online education and remote work. It is also estimated that over 5% of the world's population (~432 million adults/34 million children), and that by 2050, over 700 million people (1 in every 10!) will have disabling hearing loss (WHO, 2020).

The **ASL Transcriber** aims to begin bridging the gap between disabilities and online services by **using computer vision to transcribe a user's signing and converts it to the English alphabet counterpart**. This provides a flexible alternative to typing a message out using the keyboard that is more engaging and dynamic for both the signer and the audience.

<br>

## 🕹️ Technologies Used

- **OpenCV:** A Python module to capture real-time webcam data for ASL analysis.
- **Mediapipe (Hand Module):** A machine learning solution to infer twenty-one 3D landmarks of a hand from a single frame, developed by Google.
- **Flask:** A lightweight Python framework to provide a frontend for the application.
- **Heroku:** A cloud application platform to deploy the application.

<br>

## 🔬 Underlying Research

The Mediapipe module we used was first introduced by Google engineers in the 2006 paper _MediaPipe Hands: On-device Real-time Hand Tracking_. Those interested in reading the full research paper can find it [🔗here](https://arxiv.org/pdf/2006.10214.pdf). Mediapipe supports a diverse variety of [other ML solutions](https://google.github.io/mediapipe/) including Face Detection, Face Mesh, Pose Estimation, etc.

<br>

## 📥 Installation

For the easiest installation, clone this repo in the folder you wish to store it:

```
git clone https://github.com/JTao02/ASL_Alphabet_Interpretation.git
```

Once it's cloned, install the dependencies in the requirements.txt:

```
pip install requirements.txt
```

The project can now be run locally!

<br>

## 🔮 Future Direction

There are many directions that this project can be taken in, with additional features we wish to implement including:

- Improving hand detection to including recognizing gestures with motion
- Auto-completing to suggest possible words for the signer to use
- Extending the transcription beyond the English language (ie. enabling ASL outputs to French)
- Integrating face mesh detection to recognize emotion that accompanies current signing to improve word suggestion accuracy

<br>

## 🎉 Contributions

- 🤓 Jason Tao
- 🤓 Brian Hu
- 🤡 Terry Ju
- 🤓 Stephen Luu

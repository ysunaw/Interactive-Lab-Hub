# You're a wizard, [Student Name Here]

<img src="https://pbs.twimg.com/media/Cen7qkHWIAAdKsB.jpg" height="400">

In this lab, we want you to practice wizarding an interactive device as discussed in class. We will focus on audio as the main modality for interaction but there is no reason these general techniques can't extend to video, haptics or other interactive mechanisms. In fact, you are welcome to add those to your project if they enhance your design.


## Text to Speech and Speech to Text

In the home directory of your Pi there is a folder called `text2speech` containing some shell scripts.

```
pi@ixe00:~/text2speech $ ls
Download        festival_demo.sh  GoogleTTS_demo.sh  pico2text_demo.sh
espeak_demo.sh  flite_demo.sh     lookdave.wav

```

you can run these examples by typing 
`./espeakdeom.sh`. Take some time to look at each script and see how it works. You can see a script by typing `cat filename`

```
pi@ixe00:~/text2speech $ cat festival_demo.sh 
#from: https://elinux.org/RPi_Text_to_Speech_(Speech_Synthesis)#Festival_Text_to_Speech

echo "Just what do you think you're doing, Dave?" | festival --tts

```

You can also play audio files directly with `aplay filename`.

After looking through this folder do the same for the `speech2text` folder. In particular, look at `test_words.py` and make sure you understand how the vocab is defined. Then try `./vosk_demo_mic.sh`

## Serving Pages

In Lab 1 we served a webpage with flask. In this lab you may find it useful to serve a webpage for the controller on a remote device. Here is a simple example of a webserver.

```
pi@ixe00:~/$ python server.py
 * Serving Flask app "server" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 162-573-883
```
From a remote browser on the same network, check to make sure your webserver is working by going to [http://ixe00.local:5000]()


## Demo

In the [demo directory](./demo), you will find an example wizard of oz project you may use as a template. **You do not have to** feel free to get creative. In that project, you can see how audio and sensor data is streamed from the Pi to a wizard controller that runs in the browser. You can control what system says from the controller as well.

## Optional

There is an included [dspeech](.dspeech) demo that uses [Mozilla DeepSpeech](https://github.com/mozilla/DeepSpeech) for speech to text. If you're interested in trying it out we suggest you create a seperarate virutalenv. 



# Lab 3 Part 2

Create a system that runs on the Raspberry Pi that takes in one or more sensors and requires participants to speak to it. Document how the system works and include videos of both the system and the controller.

## Prep for Part 2

1. Sketch ideas for what you'll work on in lab on Wednesday.

I plan to create a daily horoscopes device - you can tell it your zodiac sign and it will reply with how you will do today accordingly! 

**Zoom Room feedback**

Most of those in the Zoom room gave me positive feedback (Panda, Renzhi, Zhonghao). Songyu in particular mentioned that in my original design( which was a fortune cookie machine), the user did not get to talk. so i modified it to be more interactive. 

## Prototype your system

The system should:
* use the Raspberry Pi 
* use one or more sensors
* require participants to speak to it. 

*Document how the system works*
The system works with the screen, the microphone and the speaker. The user could tell the zodiac sign using the mic; he/she will then press the button to see what his/her daily holoscope will be. 
The holoscope message is actually randomly generated from a list of answers, which is how I think the way holoscope works. 

Video
https://youtu.be/z6zeC-tuJvk

## Test the system

### What worked well about the system and what didn't?
The system flow was simple and easy to operate. But people know it was randomly generated because it did not look like it understood what people were saying. 

### What worked well about the controller and what didn't?
The button and the screen together were able to do a lot of things. The mic alone did not work very well, so adding the button to show the holoscope message was necessary in my design. 


### What lessons can you take away from the WoZ interactions for designing a more autonomous version of the system?
I have learned that a more autonomous system must show some level of understanding to the user's complex input of the system. And the user could easily get frustrated if the system claims that it's 'autonomous' but it's not. 


### How could you use your system to create a dataset of interaction? What other sensing modalities would make sense to capture?

Currently I am only capturing the button and the microphone speech. To create a dataset of interaction, I could leverage light (to create a more futuristic vibe when it makes the prediction) and potentially 


<!-- source: https://platform.claude.com/cookbook/third-party-elevenlabs-low-latency-stt-claude-tts -->

#  Low Latency Voice Assistant with ElevenLabs and Claude

This notebook demonstrates how to build a low-latency voice assistant using ElevenLabs for speech-to-text and text-to-speech, combined with Claude for intelligent responses. We'll measure the performance gains from streaming responses to minimize latency.

In this notebook, we will demonstrate how to:

1. Convert text to speech using ElevenLabs TTS
2. Transcribe audio using ElevenLabs speech-to-text
3. Generate responses with Claude
4. Optimize latency using Claude's streaming API

---

##  Installation

First, install the required dependencies:



%pip install --upgrade pip



%pip install -r requirements.txt

##  Imports

Import the necessary libraries for ElevenLabs integration, Claude API access, and audio playback:



import io

import os

import time

import anthropic

import elevenlabs

from dotenv import load\_dotenv

from IPython.display import Audio

##  API Keys

Set up your API keys for both ElevenLabs and Anthropic.

**Setup Instructions:**

1. Copy `.env.example` to `.env` in this directory
2. Edit `.env` and add your actual API keys:
   * Get your ElevenLabs API key: [https://elevenlabs.io/app/developers/api-keys(opens in new tab)](https://elevenlabs.io/app/developers/api-keys)
   * Get your Anthropic API key: [https://console.anthropic.com/settings/keys(opens in new tab)](https://console.anthropic.com/settings/keys)

The keys will be automatically loaded from the `.env` file.



# Load environment variables from .env file

load\_dotenv()

ELEVENLABS\_API\_KEY = os.getenv("ELEVENLABS\_API\_KEY")

ANTHROPIC\_API\_KEY = os.getenv("ANTHROPIC\_API\_KEY")

##  Initialize Clients

Create client instances for both ElevenLabs and Anthropic services:



assert ELEVENLABS\_API\_KEY is not None, (

"ERROR: ELEVENLABS\_API\_KEY not found. Please copy .env.example to .env and add your API keys."

)

assert ANTHROPIC\_API\_KEY is not None, (

"ERROR: ANTHROPIC\_API\_KEY not found. Please copy .env.example to .env and add your API keys."

)

elevenlabs\_client = elevenlabs.ElevenLabs(

api\_key=ELEVENLABS\_API\_KEY, base\_url="https://api.elevenlabs.io"

)

anthropic\_client = anthropic.Anthropic(api\_key=ANTHROPIC\_API\_KEY)

##  List Available Models and Voices

Explore the available ElevenLabs models and voices. We'll automatically select the first available voice for the assistant's responses:



print("Available Models and Voices:\n")

for model in elevenlabs\_client.models.list():

print(f"{model.name}: {model.model\_id}")

print()

voices = elevenlabs\_client.voices.search().voices

for voice in voices:

print(f"{voice.name}: {voice.voice\_id}")

# Select the first voice for assistant responses

selected\_voice = voices[0]

VOICE\_ID = selected\_voice.voice\_id

print(f"\nSelected voice: {selected\_voice.name} with ID: {VOICE\_ID}")



```
Available Models and Voices:

Eleven v3 (alpha): eleven_v3
Eleven Multilingual v2: eleven_multilingual_v2
Eleven Flash v2.5: eleven_flash_v2_5
Eleven Turbo v2.5: eleven_turbo_v2_5
Eleven Turbo v2: eleven_turbo_v2
Eleven Flash v2: eleven_flash_v2
Eleven Multilingual v1: eleven_multilingual_v1
Eleven English v1: eleven_monolingual_v1
Eleven English v2: eleven_english_sts_v2
Eleven Multilingual v2: eleven_multilingual_sts_v2

Rachel: 21m00Tcm4TlvDq8ikWAM
Drew: 29vD33N1CtxCmqQRPOHJ
Clyde: 2EiwWnXFnvU5JabPnv8n
Paul: 5Q0t7uMcjvnagumLfvZi
Aria: 9BWtsMINqrJLrRacOk9x
Domi: AZnzlk1XvdvUeBnXmlld
Dave: CYw3kZ02Hs0563khs1Fj
Roger: CwhRBWXzGAHq8TQ4Fs17
Fin: D38z5RcWu1voky8WS1ja
Sarah: EXAVITQu4vr4xnSDxMaL

Selected voice: Rachel with ID: 21m00Tcm4TlvDq8ikWAM
```

##  Generate Input Audio

Create a sample audio file using ElevenLabs text-to-speech. This will simulate user input for our voice assistant:



audio = elevenlabs\_client.text\_to\_speech.convert(

voice\_id=VOICE\_ID, # Use the dynamically selected voice

output\_format="mp3\_44100\_128",

model\_id="eleven\_v3",

text="Hello, Claude. ",

)

audio\_data = io.BytesIO()

for chunk in audio:

audio\_data.write(chunk)

Audio(audio\_data.getvalue())



```
<IPython.lib.display.Audio object>
```

##  Speech Transcription

Transcribe the audio input using ElevenLabs' speech-to-text model. We'll measure the transcription latency:



audio\_data.seek(0)

start\_time = time.time()

transcription = elevenlabs\_client.speech\_to\_text.convert(file=audio\_data, model\_id="scribe\_v1")

end\_time = time.time()

transcription\_time = end\_time - start\_time

print(f"Transcribed text: {transcription.text}")

print(f"Transcription time: {transcription\_time:.2f} seconds")



```
Transcribed text: Hello, Claude.
Transcription time: 0.54 seconds
```

##  Get a Response from Claude

Send the transcribed text to Claude and measure the response time. We're using `claude-haiku-4-5` for fast, high-quality responses:



start\_time = time.time()

message = anthropic\_client.messages.create(

model="claude-haiku-4-5",

max\_tokens=1000,

temperature=0,

messages=[{"role": "user", "content": transcription.text}],

)

end\_time = time.time()

non\_streaming\_response\_time = end\_time - start\_time

print(message.content[0].text)

print(f"\nResponse time: {non\_streaming\_response\_time:.2f} seconds")



```
Hello! It's nice to meet you. How can I help you today?

Response time: 1.03 seconds
```

##  Optimize with Streaming

Improve response latency by using Claude's streaming API. This allows us to receive the first tokens much faster, significantly reducing perceived latency:



start\_time = time.time()

first\_token\_time = None

claude\_full\_response = ""

with anthropic\_client.messages.stream(

model="claude-haiku-4-5",

max\_tokens=1000,

temperature=0,

messages=[{"role": "user", "content": transcription.text}],

) as stream:

for text in stream.text\_stream:

claude\_full\_response += text

print(text, end="", flush=True)

if first\_token\_time is None:

first\_token\_time = time.time()

streaming\_time\_to\_first\_token = first\_token\_time - start\_time

print(

f"\n\nStreaming time to first token: {streaming\_time\_to\_first\_token:.2f} seconds - reducing perceived latency by {(non\_streaming\_response\_time - streaming\_time\_to\_first\_token) \* 100 / non\_streaming\_response\_time:.2f}%"

)



```
Hello! It's nice to meet you. How can I help you today?

Streaming time to first token: 0.71 seconds - reducing perceived latency by 30.71%
```

Text to speech. Similar to above, we can stream the response to reduce the silence.



start\_time = time.time()

first\_audio\_chunk\_time = None

audio\_buffer = io.BytesIO()

audio\_generator = elevenlabs\_client.text\_to\_speech.stream(

voice\_id=VOICE\_ID,

output\_format="mp3\_44100\_128",

text=claude\_full\_response,

model\_id="eleven\_turbo\_v2\_5",

)

for chunk in audio\_generator:

if first\_audio\_chunk\_time is None:

first\_audio\_chunk\_time = time.time()

audio\_buffer.write(chunk)

streaming\_tts\_time\_to\_first\_chunk = first\_audio\_chunk\_time - start\_time

print(f"Streaming TTS time to first audio chunk: {streaming\_tts\_time\_to\_first\_chunk:.2f} seconds")

Audio(audio\_buffer.getvalue())



```
Streaming TTS time to first audio chunk: 0.39 seconds

<IPython.lib.display.Audio object>
```

##  Streaming Claude Directly to TTS (Sentence-by-Sentence)

We've optimized Claude's streaming and TTS separately, but can we combine them? Let's stream Claude's response and synthesize audio as soon as we have complete sentences.

This approach detects sentence boundaries (using punctuation like `.`, `!`, `?`) and immediately sends each sentence to TTS, further reducing latency.



import re

sentence\_pattern = re.compile(r"[.!?]+")

sentence\_buffer = ""

audio\_chunks = []

start\_time = time.time()

first\_audio\_time = None

with anthropic\_client.messages.stream(

model="claude-haiku-4-5",

max\_tokens=1000,

temperature=0,

messages=[{"role": "user", "content": transcription.text}],

) as stream:

for text in stream.text\_stream:

print(text, end="", flush=True)

sentence\_buffer += text

if sentence\_pattern.search(sentence\_buffer):

sentences = sentence\_pattern.split(sentence\_buffer)

# Process all complete sentences (all but the last element)

for i in range(len(sentences) - 1):

complete\_sentence = sentences[i].strip()

if complete\_sentence:

audio\_gen = elevenlabs\_client.text\_to\_speech.stream(

voice\_id=VOICE\_ID,

output\_format="mp3\_44100\_128", # Free tier format

text=complete\_sentence,

model\_id="eleven\_turbo\_v2\_5",

)

sentence\_audio = io.BytesIO()

for chunk in audio\_gen:

if first\_audio\_time is None:

first\_audio\_time = time.time()

sentence\_audio.write(chunk)

audio\_chunks.append(sentence\_audio.getvalue())

sentence\_buffer = sentences[-1]

if sentence\_buffer.strip():

audio\_gen = elevenlabs\_client.text\_to\_speech.stream(

voice\_id=VOICE\_ID,

output\_format="mp3\_44100\_128",

text=sentence\_buffer.strip(),

model\_id="eleven\_turbo\_v2\_5",

)

sentence\_audio = io.BytesIO()

for chunk in audio\_gen:

sentence\_audio.write(chunk)

audio\_chunks.append(sentence\_audio.getvalue())

sentence\_streaming\_time\_to\_first\_audio = first\_audio\_time - start\_time

print(f"\n\nTime to first audio: {sentence\_streaming\_time\_to\_first\_audio:.2f} seconds")

combined\_pcm = b"".join(audio\_chunks)

Audio(combined\_pcm)



```
Hello! It's nice to meet you. How can I help you today?

Time to first audio: 1.48 seconds

<IPython.lib.display.Audio object>
```

###  The Problem: Disconnected Audio

While this approach achieves excellent latency, there's a quality issue. Each sentence is synthesized independently, which causes the audio to sound disconnected and unnatural. The prosody (rhythm, stress, intonation) doesn't flow smoothly between sentences.

This happens because the TTS model doesn't have context about what comes next, so each sentence is treated as a standalone utterance.

##  WebSocket Streaming: The Best of Both Worlds

ElevenLabs offers a WebSocket API that solves this problem perfectly. Instead of waiting for complete sentences, we can stream text chunks directly to the TTS engine as they arrive from Claude.

The WebSocket API:

* Accepts streaming text input (no sentence buffering needed)
* Maintains context across chunks for natural prosody
* Returns audio chunks as soon as they're ready
* Achieves the lowest possible latency with the best audio quality

Let's implement this ultimate optimization:

##  Building a Production Voice Assistant

The techniques demonstrated in this notebook provide the foundation for building a real-time voice assistant. The WebSocket streaming approach minimizes latency while maintaining natural audio quality.

###  Key Implementation Challenges

When building a production system, you'll need to solve several additional challenges beyond the basic streaming:

1. **Continuous Audio Playback**: Audio chunks must play seamlessly without gaps or crackling. This requires careful buffer management and pre-buffering strategies.
2. **Microphone Input**: Real-time recording from the microphone with proper handling of audio formats and sample rates.
3. **Conversation State**: Maintaining conversation history across turns so Claude can reference previous context.
4. **Audio Quality**: Converting between different audio formats (PCM, WAV) and avoiding artifacts from encoding.

###  Complete Implementation

We've built a complete voice assistant script that demonstrates all these techniques:

**`stream_voice_assistant_websocket.py`** - A production-ready conversational voice assistant featuring:

* Microphone recording with Enter-to-stop control
* ElevenLabs speech-to-text transcription
* Claude streaming with conversation history
* WebSocket-based TTS with minimal latency
* Custom audio queue for gapless playback
* Continuous conversation loop

Run the script to experience a fully functional voice assistant:



python stream\_voice\_assistant\_websocket.py

This demonstrates how the streaming optimizations from this notebook translate into a real-world application with production-quality audio handling.

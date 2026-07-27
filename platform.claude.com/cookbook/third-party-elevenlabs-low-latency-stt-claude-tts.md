<!-- source: https://platform.claude.com/cookbook/third-party-elevenlabs-low-latency-stt-claude-tts -->

# Low Latency Voice Assistant with ElevenLabs and Claude

This notebook demonstrates how to build a low-latency voice assistant using ElevenLabs for speech-to-text and text-to-speech, combined with Claude for intelligent responses. We'll measure the performance gains from streaming responses to minimize latency.

In this notebook, we will demonstrate how to:

1. Convert text to speech using ElevenLabs TTS
2. Transcribe audio using ElevenLabs speech-to-text
3. Generate responses with Claude
4. Optimize latency using Claude's streaming API

---

## Installation

First, install the required dependencies:

python

```
%pip install --upgrade pip
```

python

```
%pip install -r requirements.txt
```

## Imports

Import the necessary libraries for ElevenLabs integration, Claude API access, and audio playback:

python

```
import io
import os
import time

import anthropic
import elevenlabs
from dotenv import load_dotenv
from IPython.display import Audio
```

## API Keys

Set up your API keys for both ElevenLabs and Anthropic.

**Setup Instructions:**

1. Copy `.env.example` to `.env` in this directory
2. Edit `.env` and add your actual API keys:
   * Get your ElevenLabs API key: <https://elevenlabs.io/app/developers/api-keys>
   * Get your Anthropic API key: <https://console.anthropic.com/settings/keys>

The keys will be automatically loaded from the `.env` file.

python

```
# Load environment variables from .env file

load_dotenv()

ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
```

## Initialize Clients

Create client instances for both ElevenLabs and Anthropic services:

python

```
assert ELEVENLABS_API_KEY is not None, (
    "ERROR: ELEVENLABS_API_KEY not found. Please copy .env.example to .env and add your API keys."
)
assert ANTHROPIC_API_KEY is not None, (
    "ERROR: ANTHROPIC_API_KEY not found. Please copy .env.example to .env and add your API keys."
)

elevenlabs_client = elevenlabs.ElevenLabs(
    api_key=ELEVENLABS_API_KEY, base_url="https://api.elevenlabs.io"
)

anthropic_client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
```

## List Available Models and Voices

Explore the available ElevenLabs models and voices. We'll automatically select the first available voice for the assistant's responses:

python

```
print("Available Models and Voices:\n")
for model in elevenlabs_client.models.list():
    print(f"{model.name}: {model.model_id}")

print()

voices = elevenlabs_client.voices.search().voices
for voice in voices:
    print(f"{voice.name}: {voice.voice_id}")

# Select the first voice for assistant responses
selected_voice = voices[0]
VOICE_ID = selected_voice.voice_id

print(f"\nSelected voice: {selected_voice.name} with ID: {VOICE_ID}")
```

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

## Generate Input Audio

Create a sample audio file using ElevenLabs text-to-speech. This will simulate user input for our voice assistant:

python

```
audio = elevenlabs_client.text_to_speech.convert(
    voice_id=VOICE_ID,  # Use the dynamically selected voice
    output_format="mp3_44100_128",
    model_id="eleven_v3",
    text="Hello, Claude. ",
)

audio_data = io.BytesIO()
for chunk in audio:
    audio_data.write(chunk)

Audio(audio_data.getvalue())
```

```
<IPython.lib.display.Audio object>
```

## Speech Transcription

Transcribe the audio input using ElevenLabs' speech-to-text model. We'll measure the transcription latency:

python

```
audio_data.seek(0)

start_time = time.time()

transcription = elevenlabs_client.speech_to_text.convert(file=audio_data, model_id="scribe_v1")

end_time = time.time()
transcription_time = end_time - start_time

print(f"Transcribed text: {transcription.text}")
print(f"Transcription time: {transcription_time:.2f} seconds")
```

```
Transcribed text: Hello, Claude.
Transcription time: 0.54 seconds
```

## Get a Response from Claude

Send the transcribed text to Claude and measure the response time. We're using `claude-haiku-4-5` for fast, high-quality responses:

python

```
start_time = time.time()

message = anthropic_client.messages.create(
    model="claude-haiku-4-5",
    max_tokens=1000,
    temperature=0,
    messages=[{"role": "user", "content": transcription.text}],
)

end_time = time.time()
non_streaming_response_time = end_time - start_time

print(message.content[0].text)
print(f"\nResponse time: {non_streaming_response_time:.2f} seconds")
```

```
Hello! It's nice to meet you. How can I help you today?

Response time: 1.03 seconds
```

## Optimize with Streaming

Improve response latency by using Claude's streaming API. This allows us to receive the first tokens much faster, significantly reducing perceived latency:

python

```
start_time = time.time()
first_token_time = None

claude_full_response = ""

with anthropic_client.messages.stream(
    model="claude-haiku-4-5",
    max_tokens=1000,
    temperature=0,
    messages=[{"role": "user", "content": transcription.text}],
) as stream:
    for text in stream.text_stream:
        claude_full_response += text
        print(text, end="", flush=True)
        if first_token_time is None:
            first_token_time = time.time()

streaming_time_to_first_token = first_token_time - start_time
print(
    f"\n\nStreaming time to first token: {streaming_time_to_first_token:.2f} seconds - reducing perceived latency by {(non_streaming_response_time - streaming_time_to_first_token) * 100 / non_streaming_response_time:.2f}%"
)
```

```
Hello! It's nice to meet you. How can I help you today?

Streaming time to first token: 0.71 seconds - reducing perceived latency by 30.71%
```

Text to speech. Similar to above, we can stream the response to reduce the silence.

python

```
start_time = time.time()
first_audio_chunk_time = None

audio_buffer = io.BytesIO()

audio_generator = elevenlabs_client.text_to_speech.stream(
    voice_id=VOICE_ID,
    output_format="mp3_44100_128",
    text=claude_full_response,
    model_id="eleven_turbo_v2_5",
)

for chunk in audio_generator:
    if first_audio_chunk_time is None:
        first_audio_chunk_time = time.time()
    audio_buffer.write(chunk)

streaming_tts_time_to_first_chunk = first_audio_chunk_time - start_time
print(f"Streaming TTS time to first audio chunk: {streaming_tts_time_to_first_chunk:.2f} seconds")

Audio(audio_buffer.getvalue())
```

```
Streaming TTS time to first audio chunk: 0.39 seconds

<IPython.lib.display.Audio object>
```

## Streaming Claude Directly to TTS (Sentence-by-Sentence)

We've optimized Claude's streaming and TTS separately, but can we combine them? Let's stream Claude's response and synthesize audio as soon as we have complete sentences.

This approach detects sentence boundaries (using punctuation like `.`, `!`, `?`) and immediately sends each sentence to TTS, further reducing latency.

python

```
import re

sentence_pattern = re.compile(r"[.!?]+")
sentence_buffer = ""
audio_chunks = []

start_time = time.time()
first_audio_time = None

with anthropic_client.messages.stream(
    model="claude-haiku-4-5",
    max_tokens=1000,
    temperature=0,
    messages=[{"role": "user", "content": transcription.text}],
) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)
        sentence_buffer += text

        if sentence_pattern.search(sentence_buffer):
            sentences = sentence_pattern.split(sentence_buffer)

            # Process all complete sentences (all but the last element)
            for i in range(len(sentences) - 1):
                complete_sentence = sentences[i].strip()
                if complete_sentence:
                    audio_gen = elevenlabs_client.text_to_speech.stream(
                        voice_id=VOICE_ID,
                        output_format="mp3_44100_128",  # Free tier format
                        text=complete_sentence,
                        model_id="eleven_turbo_v2_5",
                    )

                    sentence_audio = io.BytesIO()
                    for chunk in audio_gen:
                        if first_audio_time is None:
                            first_audio_time = time.time()
                        sentence_audio.write(chunk)

                    audio_chunks.append(sentence_audio.getvalue())

            sentence_buffer = sentences[-1]

if sentence_buffer.strip():
    audio_gen = elevenlabs_client.text_to_speech.stream(
        voice_id=VOICE_ID,
        output_format="mp3_44100_128",
        text=sentence_buffer.strip(),
        model_id="eleven_turbo_v2_5",
    )
    sentence_audio = io.BytesIO()
    for chunk in audio_gen:
        sentence_audio.write(chunk)
    audio_chunks.append(sentence_audio.getvalue())

sentence_streaming_time_to_first_audio = first_audio_time - start_time
print(f"\n\nTime to first audio: {sentence_streaming_time_to_first_audio:.2f} seconds")

combined_pcm = b"".join(audio_chunks)
Audio(combined_pcm)
```

```
Hello! It's nice to meet you. How can I help you today?

Time to first audio: 1.48 seconds

<IPython.lib.display.Audio object>
```

### The Problem: Disconnected Audio

While this approach achieves excellent latency, there's a quality issue. Each sentence is synthesized independently, which causes the audio to sound disconnected and unnatural. The prosody (rhythm, stress, intonation) doesn't flow smoothly between sentences.

This happens because the TTS model doesn't have context about what comes next, so each sentence is treated as a standalone utterance.

## WebSocket Streaming: The Best of Both Worlds

ElevenLabs offers a WebSocket API that solves this problem perfectly. Instead of waiting for complete sentences, we can stream text chunks directly to the TTS engine as they arrive from Claude.

The WebSocket API:

* Accepts streaming text input (no sentence buffering needed)
* Maintains context across chunks for natural prosody
* Returns audio chunks as soon as they're ready
* Achieves the lowest possible latency with the best audio quality

Let's implement this ultimate optimization:

## Building a Production Voice Assistant

The techniques demonstrated in this notebook provide the foundation for building a real-time voice assistant. The WebSocket streaming approach minimizes latency while maintaining natural audio quality.

### Key Implementation Challenges

When building a production system, you'll need to solve several additional challenges beyond the basic streaming:

1. **Continuous Audio Playback**: Audio chunks must play seamlessly without gaps or crackling. This requires careful buffer management and pre-buffering strategies.
2. **Microphone Input**: Real-time recording from the microphone with proper handling of audio formats and sample rates.
3. **Conversation State**: Maintaining conversation history across turns so Claude can reference previous context.
4. **Audio Quality**: Converting between different audio formats (PCM, WAV) and avoiding artifacts from encoding.

### Complete Implementation

We've built a complete voice assistant script that demonstrates all these techniques:

**`stream_voice_assistant_websocket.py`** - A production-ready conversational voice assistant featuring:

* Microphone recording with Enter-to-stop control
* ElevenLabs speech-to-text transcription
* Claude streaming with conversation history
* WebSocket-based TTS with minimal latency
* Custom audio queue for gapless playback
* Continuous conversation loop

Run the script to experience a fully functional voice assistant:

```
python stream_voice_assistant_websocket.py
```

This demonstrates how the streaming optimizations from this notebook translate into a real-world application with production-quality audio handling.

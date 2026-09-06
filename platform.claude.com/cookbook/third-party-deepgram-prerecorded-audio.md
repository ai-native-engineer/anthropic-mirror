<!-- source: https://platform.claude.com/cookbook/third-party-deepgram-prerecorded-audio -->

#  Transcribe an audio file with Deepgram & use Anthropic to prepare interview questions!

**Make a copy of this notebook into your own drive, and follow the instructions below!** 🥳🥳🥳

---

#  Get started:

Running the following three cells will allow you to transcribe any audio you wish. The comments below point out the variables you can manipulate to modify your output as you wish.

Before running this notebook, you'll need to have a couple audio URLs to transcribe. You can use any audio files you wish.

And by the way, if you haven't yet signed up for Deepgram, check out this link here: [https://dpgr.am/prerecorded-notebook-signup(opens in new tab)](https://dpgr.am/prerecorded-notebook-signup)

#  Step 1: Dependencies

Run this cell to download all necessary dependencies.

Note: You can run a cell by clicking the play button on the left or by clicking on the cell and pressing `shift`+`ENTER` at the same time. (Or `shift` + `return` on Mac).

%pip install requests ffmpeg-python

%pip install deepgram-sdk --upgrade

%pip install requests

%pip install anthropic

#  Step 2: Audio URL files

Find some audio files hosted on a server so you can use this notebook. OR An example file is provided by Deepgram is code below.

# Have you completed Step 2 above? 👀

# Do you see your audio file in the folder on the left? 📂

#  Step 3: Transcription

Fill in the following variables:

* `DG_KEY` = Your personal Deepgram API key
* `AUDIO_FILE_URL` = a URL for an audio file you wish to transcribe.

Now run the cell! (`Shift` + `Enter`)

---

And by the way, if you're already a Deepgram user, and you're getting an error in this cell the most common fixes are:

1. You may need to update your installation of the deepgram-sdk.
2. You may need to check how many credits you have left in your Deepgram account.

import requests

from deepgram import DeepgramClient, FileSource, PrerecordedOptions

# Deepgram API key

DG\_KEY = "🔑🔑🔑 Your API Key here! 🔑🔑🔑"

# URL of the audio file

AUDIO\_FILE\_URL = "https://static.deepgram.com/examples/nasa-spacewalk-interview.wav"

# Path to save the transcript JSON file

TRANSCRIPT\_FILE = "transcript.json"

def main():

try:

# STEP 1: Create a Deepgram client using the API key

deepgram = DeepgramClient(DG\_KEY)

# Download the audio file from the URL

response = requests.get(AUDIO\_FILE\_URL, timeout=60)

if response.status\_code == 200:

buffer\_data = response.content

else:

print("Failed to download audio file")

return

payload: FileSource = {

"buffer": buffer\_data,

}

# STEP 2: Configure Deepgram options for audio analysis

options = PrerecordedOptions(

model="nova-2",

smart\_format=True,

)

# STEP 3: Call the transcribe\_file method with the text payload and options

response = deepgram.listen.prerecorded.v("1").transcribe\_file(payload, options)

# STEP 4: Write the response JSON to a file

with open(TRANSCRIPT\_FILE, "w") as transcript\_file:

transcript\_file.write(response.to\_json(indent=4))

print("Transcript JSON file generated successfully.")

except Exception as e:

print(f"Exception: {e}")

if \_\_name\_\_ == "\_\_main\_\_":

main()

If the cell above succeeds, you should see JSON output file(s) in the content directory. Note: There may be a small delay between when the cell finishes running and when the JSON file actually appears. This is normal. Just wait a few moments for the file(s) to appear.

#  Step 4: Check out your transcription

The function below parses the output JSON and prints out the transcription of one of the files you just transcribed! (Make sure
the file you're trying to examine is indeed already loaded into the content directory.)

**Set the `OUTPUT` variable to the name of the file you wish to see the transcription of.**

Then run this cell (`Shift`+`Enter`) to see a sentence-by-sentence transcription of your audio!

import json

# Set this variable to the path of the output file you wish to read

OUTPUT = "transcript.json"

# The JSON is loaded with information, but if you just want to read the

# transcript, run the code below!

def print\_transcript(transcription\_file):

with open(transcription\_file) as file:

data = json.load(file)

result = data["results"]["channels"][0]["alternatives"][0]["transcript"]

result = result.split(".")

for sentence in result:

print(sentence + ".")

print\_transcript(OUTPUT)

If the cell above succeeds you should see a plain text version of your audio transcription.

#  Step 5: Prepare Interview Questions using Anthropic

Now we can send off our transcript to Anthropic for analysis to help us prepare some interview questions. Run the cell below (`Shift`+`Enter`) to get a suggested set of interview questions provided by Anthropic based on your audio transcript above.

import json

import anthropic

transcription\_file = "transcript.json"

# Function to get the transcript from the JSON file

def get\_transcript(transcription\_file):

with open(transcription\_file) as file:

data = json.load(file)

result = data["results"]["channels"][0]["alternatives"][0]["transcript"]

return result

# Load the transcript from the JSON file

message\_text = get\_transcript(transcription\_file)

# Initialize the Claude API client

client = anthropic.Anthropic(

# Defaults to os.environ.get("ANTHROPIC\_API\_KEY")

# Claude API key

api\_key="🔑🔑🔑 Your API Key here! 🔑🔑🔑"

)

# Prepare the text for the API request

formatted\_messages = [{"role": "user", "content": message\_text}]

# Generate thoughtful, open-ended interview questions

response = client.messages.create(

model="claude-opus-4-8",

max\_tokens=1000,

temperature=0.5,

system="Your task is to generate a series of thoughtful, open-ended questions for an interview based on the given context. The questions should be designed to elicit insightful and detailed responses from the interviewee, allowing them to showcase their knowledge, experience, and critical thinking skills. Avoid yes/no questions or those with obvious answers. Instead, focus on questions that encourage reflection, self-assessment, and the sharing of specific examples or anecdotes.",

messages=formatted\_messages,

)

# Print the generated questions

# Join the text of each TextBlock into a single string

content = "".join(block.text for block in response.content)

# Split the content by '\n\n'

parts = content.split("\n\n")

# Print each part with an additional line break

for part in parts:

print(part)

print("\n")

If this cell succeeded you should see a list of interview questions based on your original audio file. Now you can transcribe audio with Deepgram and use Anthropic to get a set of interview questions.

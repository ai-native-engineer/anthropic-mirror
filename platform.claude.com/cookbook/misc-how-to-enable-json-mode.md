<!-- source: https://platform.claude.com/cookbook/misc-how-to-enable-json-mode -->

# Prompting Claude for "JSON Mode"

Claude doesn't have a formal "JSON Mode" with constrained sampling. But not to worry -- you can still get reliable JSON from Claude! This recipe will show you how.

First, let's look at Claude's default behavior.

python

```
%pip install anthropic
```

python

```
import json
import re
from pprint import pprint

from anthropic import Anthropic
```

python

```
client = Anthropic()
MODEL_NAME = "claude-opus-4-1"
```

python

```
message = (
    client.messages.create(
        model=MODEL_NAME,
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": "Give me a JSON dict with names of famous athletes & their sports.",
            },
        ],
    )
    .content[0]
    .text
)
print(message)
```

```
Here is a JSON dictionary with names of famous athletes and their respective sports:

{
  "athletes": [
    {
      "name": "Usain Bolt",
      "sport": "Track and Field"
    },
    {
      "name": "Michael Phelps",
      "sport": "Swimming"
    },
    {
      "name": "Serena Williams",
      "sport": "Tennis"
    },
    {
      "name": "LeBron James",
      "sport": "Basketball"
    },
    {
      "name": "Lionel Messi",
      "sport": "Soccer"
    },
    {
      "name": "Simone Biles",
      "sport": "Gymnastics"
    },
    {
      "name": "Tom Brady",
      "sport": "American Football"
    },
    {
      "name": "Muhammad Ali",
      "sport": "Boxing"
    },
    {
      "name": "Nadia Comaneci",
      "sport": "Gymnastics"
    },
    {
      "name": "Michael Jordan",
      "sport": "Basketball"
    },
    {
      "name": "Pelé",
      "sport": "Soccer"
    },
    {
      "name": "Roger Federer",
      "sport": "Tennis"
    }
  ]
}
```

Claude followed instructions and outputted a nice dictionary, which we can extract with code:

python

```
def extract_json(response):
    json_start = response.index("{")
    json_end = response.rfind("}")
    return json.loads(response[json_start : json_end + 1])

extract_json(message)
```

```
{'athletes': [{'name': 'Usain Bolt', 'sport': 'Track and Field'},
  {'name': 'Michael Phelps', 'sport': 'Swimming'},
  {'name': 'Serena Williams', 'sport': 'Tennis'},
  {'name': 'LeBron James', 'sport': 'Basketball'},
  {'name': 'Lionel Messi', 'sport': 'Soccer'},
  {'name': 'Simone Biles', 'sport': 'Gymnastics'},
  {'name': 'Tom Brady', 'sport': 'American Football'},
  {'name': 'Muhammad Ali', 'sport': 'Boxing'},
  {'name': 'Nadia Comaneci', 'sport': 'Gymnastics'},
  {'name': 'Michael Jordan', 'sport': 'Basketball'},
  {'name': 'Pelé', 'sport': 'Soccer'},
  {'name': 'Roger Federer', 'sport': 'Tennis'}]}
```

But what if we want Claude to skip the preamble and go straight to the JSON? One simple way is to prefill Claude's response and include a "{" character.

python

```
message = (
    client.messages.create(
        model=MODEL_NAME,
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": "Give me a JSON dict with names of famous athletes & their sports.",
            },
            {"role": "assistant", "content": "Here is the JSON requested:\n{"},
        ],
    )
    .content[0]
    .text
)
print(message)
```

```
"athletes":[
      {
         "name":"Michael Jordan",
         "sport":"Basketball"
      },
      {
         "name":"Babe Ruth",
         "sport":"Baseball"
      },
      {
         "name":"Muhammad Ali",
         "sport":"Boxing"
      },
      {
         "name":"Serena Williams",
         "sport":"Tennis"
      },
      {
         "name":"Wayne Gretzky",
         "sport":"Hockey"
      },
      {
         "name":"Michael Phelps",
         "sport":"Swimming"
      },
      {
         "name":"Usain Bolt",
         "sport":"Track and Field"
      },
      {
         "name":"Mia Hamm",
         "sport":"Soccer"
      },
      {
         "name":"Michael Schumacher",
         "sport":"Formula 1 Racing"
      },
      {
         "name":"Simone Biles",
         "sport":"Gymnastics"
      }
   ]
}
```

Now all we have to do is add back the "{" that we prefilled and we can extract the JSON.

python

```
output_json = json.loads("{" + message[: message.rfind("}") + 1])
output_json
```

```
{'athletes': [{'name': 'Michael Jordan', 'sport': 'Basketball'},
  {'name': 'Babe Ruth', 'sport': 'Baseball'},
  {'name': 'Muhammad Ali', 'sport': 'Boxing'},
  {'name': 'Serena Williams', 'sport': 'Tennis'},
  {'name': 'Wayne Gretzky', 'sport': 'Hockey'},
  {'name': 'Michael Phelps', 'sport': 'Swimming'},
  {'name': 'Usain Bolt', 'sport': 'Track and Field'},
  {'name': 'Mia Hamm', 'sport': 'Soccer'},
  {'name': 'Michael Schumacher', 'sport': 'Formula 1 Racing'},
  {'name': 'Simone Biles', 'sport': 'Gymnastics'}]}
```

For very long and complicated prompts, which contain multiple JSON outputs so that a string search for "{" and "}" don't do the trick, you can also have Claude output each JSON item in specified tags for future extraction.

python

```
message = (
    client.messages.create(
        model=MODEL_NAME,
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": """Give me a JSON dict with the names of 5 famous athletes & their sports.
Put this dictionary in <athlete_sports> tags.

Then, for each athlete, output an additional JSON dictionary. In each of these additional dictionaries:
- Include two keys: the athlete's first name and last name.
- For the values, list three words that start with the same letter as that name.
Put each of these additional dictionaries in separate <athlete_name> tags.""",
            },
            {"role": "assistant", "content": "Here is the JSON requested:"},
        ],
    )
    .content[0]
    .text
)
print(message)
```

```
<athlete_sports>
{
  "Michael Jordan": "Basketball",
  "Serena Williams": "Tennis",
  "Lionel Messi": "Soccer",
  "Usain Bolt": "Track and Field",
  "Michael Phelps": "Swimming"
}
</athlete_sports>

<athlete_name>
{
  "first": ["Magnificent", "Motivating", "Memorable"],
  "last": ["Joyful", "Jumping", "Jocular"]
}
</athlete_name>

<athlete_name>
{
  "first": ["Skillful", "Strong", "Superstar"],
  "last": ["Winning", "Willful", "Wise"]
}
</athlete_name>

<athlete_name>
{
  "first": ["Legendary", "Lively", "Leaping"],
  "last": ["Magical", "Marvelous", "Masterful"]
}
</athlete_name>

<athlete_name>
{
  "first": ["Unbeatable", "Unbelievable", "Unstoppable"],
  "last": ["Brave", "Bold", "Brilliant"]
}
</athlete_name>

<athlete_name>
{
  "first": ["Marvelous", "Methodical", "Medalist"],
  "last": ["Powerful", "Persevering", "Precise"]
}
</athlete_name>
```

Now, we can use an extraction regex to get all the dictionaries.

python

```
import re

def extract_between_tags(tag: str, string: str, strip: bool = False) -> list[str]:
    ext_list = re.findall(f"<{tag}>(.+?)</{tag}>", string, re.DOTALL)
    if strip:
        ext_list = [e.strip() for e in ext_list]
    return ext_list

athlete_sports_dict = json.loads(extract_between_tags("athlete_sports", message)[0])
athlete_name_dicts = [json.loads(d) for d in extract_between_tags("athlete_name", message)]
```

python

```
pprint(athlete_sports_dict)
```

```
{'Lionel Messi': 'Soccer',
 'Michael Jordan': 'Basketball',
 'Michael Phelps': 'Swimming',
 'Serena Williams': 'Tennis',
 'Usain Bolt': 'Track and Field'}
```

python

```
pprint(athlete_name_dicts, width=1)
```

```
[{'first': ['Magnificent',
            'Motivating',
            'Memorable'],
  'last': ['Joyful',
           'Jumping',
           'Jocular']},
 {'first': ['Skillful',
            'Strong',
            'Superstar'],
  'last': ['Winning',
           'Willful',
           'Wise']},
 {'first': ['Legendary',
            'Lively',
            'Leaping'],
  'last': ['Magical',
           'Marvelous',
           'Masterful']},
 {'first': ['Unbeatable',
            'Unbelievable',
            'Unstoppable'],
  'last': ['Brave',
           'Bold',
           'Brilliant']},
 {'first': ['Marvelous',
            'Methodical',
            'Medalist'],
  'last': ['Powerful',
           'Persevering',
           'Precise']}]
```

So to recap:

* You can use string parsing to extract the text between "`json" and "`" to get the JSON.
* You can remove preambles *before* the JSON via a partial Assistant message. (However, this removes the possibility of having Claude do "Chain of Thought" for increased intelligence before beginning to output the JSON.)
* You can get rid of text that comes *after* the JSON by using a stop sequence.
* You can instruct Claude to output JSON in XML tags to make it easy to collect afterward for more complex prompts.

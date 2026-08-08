<!-- source: https://platform.claude.com/cookbook/misc-how-to-enable-json-mode -->

#  Prompting Claude for "JSON Mode"

Claude doesn't have a formal "JSON Mode" with constrained sampling. But not to worry -- you can still get reliable JSON from Claude! This recipe will show you how.

First, let's look at Claude's default behavior.



%pip install anthropic



import json

import re

from pprint import pprint

from anthropic import Anthropic



client = Anthropic()

MODEL\_NAME = "claude-opus-4-1"



message = (

client.messages.create(

model=MODEL\_NAME,

max\_tokens=1024,

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



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



def extract\_json(response):

json\_start = response.index("{")

json\_end = response.rfind("}")

return json.loads(response[json\_start : json\_end + 1])

extract\_json(message)



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



message = (

client.messages.create(

model=MODEL\_NAME,

max\_tokens=1024,

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



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



output\_json = json.loads("{" + message[: message.rfind("}") + 1])

output\_json



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



message = (

client.messages.create(

model=MODEL\_NAME,

max\_tokens=1024,

messages=[

{

"role": "user",

"content": """Give me a JSON dict with the names of 5 famous athletes & their sports.

Put this dictionary in <athlete\_sports> tags.

Then, for each athlete, output an additional JSON dictionary. In each of these additional dictionaries:

- Include two keys: the athlete's first name and last name.

- For the values, list three words that start with the same letter as that name.

Put each of these additional dictionaries in separate <athlete\_name> tags.""",

},

{"role": "assistant", "content": "Here is the JSON requested:"},

],

)

.content[0]

.text

)

print(message)



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



import re

def extract\_between\_tags(tag: str, string: str, strip: bool = False) -> list[str]:

ext\_list = re.findall(f"<{tag}>(.+?)</{tag}>", string, re.DOTALL)

if strip:

ext\_list = [e.strip() for e in ext\_list]

return ext\_list

athlete\_sports\_dict = json.loads(extract\_between\_tags("athlete\_sports", message)[0])

athlete\_name\_dicts = [json.loads(d) for d in extract\_between\_tags("athlete\_name", message)]



pprint(athlete\_sports\_dict)



```
{'Lionel Messi': 'Soccer',
 'Michael Jordan': 'Basketball',
 'Michael Phelps': 'Swimming',
 'Serena Williams': 'Tennis',
 'Usain Bolt': 'Track and Field'}
```



pprint(athlete\_name\_dicts, width=1)



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

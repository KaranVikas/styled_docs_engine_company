from document_schema import schema
from document_model import InputTextBlock
from document_renderer import convert_document
import json

sample_input = {
  "blocks": [
    {
      "type": "heading",
      "level": 2,
      "text": "Assessment: CONSENT - Be Cyber Kind",
      "bold": True
    },
    {
      "type": "paragraph",
      "text": "Name:",
      "underline": True
    },
    {
      "type": "paragraph",
      "text": "1. Draw an example of when it is important to say no. Then write a sentence to explain your picture.",
      "underline": True
    },
    {
      "type": "paragraph",
      "text": "It is important to say no when:"
    },
    {
      "type": "paragraph",
      "text": "1"
    },
    {
      "type": "paragraph",
      "text": "2. List three ways you can tell someone “No”.",
      "underline": True
    },
    {
      "type": "bulletList",
      "children": [
        {
          "type": "paragraph",
          "text": "1."
        },
        {
          "type": "paragraph",
          "text": "2."
        },
        {
          "type": "paragraph",
          "text": "3."
        }
      ]
    },
    {
      "type": "paragraph",
      "text": "3. Draw a picture of how you might feel when you need to say no and when you might want to say yes.",
      "underline": True
    },
    {
      "type": "bulletList",
      "children": [
        {
          "type": "paragraph",
          "text": "Draw “No” picture here:"
        },
        {
          "type": "paragraph",
          "text": "Draw “Yes” picture here:"
        }
      ]
    },
    {
      "type": "heading",
      "level": 3,
      "text": "Assessment: CONSENT - Be Cyber Kind",
      "bold": True
    },
    {
      "type": "paragraph",
      "text": "4. Fill in the blank with the missing words from the list below.",
      "underline": True
    },
    {
      "type": "bulletList",
      "children": [
        {
          "type": "paragraph",
          "text": "A) __________ is another way to show someone you want to say no."
        },
        {
          "type": "paragraph",
          "text": "B) Consent means saying, __________."
        },
        {
          "type": "paragraph",
          "text": "C) It is important to say “No” when we feel __________."
        }
      ]
    },
    {
      "type": "paragraph",
      "text": "Word List:",
      "underline": True
    },
    {
      "type": "bulletList",
      "children": [
        {
          "type": "paragraph",
          "text": "Body language"
        },
        {
          "type": "paragraph",
          "text": "“Yes”"
        },
        {
          "type": "paragraph",
          "text": "unsafe"
        }
      ]
    }
  ]
}



parsed_blocks = [InputTextBlock(**b) for b in sample_input["blocks"]]
doc = convert_document(parsed_blocks, schema)

print(json.dumps(doc.to_json(), indent=2))

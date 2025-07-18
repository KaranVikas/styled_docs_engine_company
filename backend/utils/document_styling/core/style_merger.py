# styles/document_template.py

# Template for the Lesson doc
# DEFAULT_STYLE_TEMPLATE = {
#     "textStyle": {
#         "fontFamily": "Arial",
#         "fontSize": "14px",
#         "color": "#333333"
#     },
#     "headingStyles": {
#         1: {
#             "fontFamily": "Catamaran",
#             "fontSize": "20pt",
#             "color":"rgb(0, 0, 0)"
#         },
#         2: {
#             "fontFamily": "Cabin, sans-serif",
#             "fontSize": "11pt",
#             "color":"rgb(75, 58, 211)"
#         },
#         3: {
#             "fontFamily": "Catamaran, sans-serif",
#             "fontSize": "8pt",
#             "color":"rgb(0, 0, 0)"
#         }
#     },
#     "paragraph": {
#         "textAlign": "justify",
#         "indent": 1,
#         "lineHeight": 1.4,
#         "dir": "ltr"
#     },
#     "heading": {
#         "textAlign": "left",
#         "indent": 0,
#         "lineHeight": 1.2,
#         "dir": "ltr",
#         "level": 2
#     }
# }

# DEFAULT_STYLE_TEMPLATE = {
#     "textStyle": {
#         "fontFamily": "Cabin, sans-serif",
#         "fontSize": "11pt",
#         "color": "rgb(0, 0, 0)"
#     },
#     "headingStyles": {
#         1: {
#             "fontFamily": "Catamaran",
#             "fontSize": "20pt",
#             "color": "rgb(0, 0, 0)"
#         },
#         2: {
#             "fontFamily": "Cabin, sans-serif",
#             "fontSize": "11pt",
#             "color": "rgb(75, 58, 211)"
#         },
#         3: {
#             "fontFamily": "Catamaran, sans-serif",
#             "fontSize": "8pt",
#             "color": "rgb(0, 0, 0)"
#         }
#     },
#     "paragraph": {
#         "textAlign": None,
#         "indent": 0,
#         "lineHeight": 1.4,
#         "dir": "auto"
#     },
#     "heading": {
#         "textAlign": "left",
#         "indent": 0,
#         "lineHeight": 1.2,
#         "dir": "ltr",
#         "level": 2
#     }
# }

# Template for the Doc lesson

# Default template for the --> Assement sheet

DEFAULT_STYLE_TEMPLATE = {
    "textStyle": {
        "fontFamily": "Cabin, sans-serif",     # Keep default as a base text style
        "fontSize": "11pt",
        "color": "rgb(0, 0, 0)"
    },
    "headingStyles": {
        1: {
            "fontFamily": "Catamaran",         # Keep as-is (was seen in other heading examples)
            "fontSize": "20pt",
            "color": "rgb(0, 0, 0)"
        },
        2: {
            "fontFamily": "Cabin, sans-serif",
            "fontSize": "11pt",
            "color": "rgb(75, 58, 211)"
        },
        3: {
            "fontFamily": "Catamaran, sans-serif",
            "fontSize": "8pt",
            "color": "rgb(0, 0, 0)"
        }
    },
    "paragraph": {
        "textAlign": None,                     # Matches JSON
        "indent": 0,                           # Matches JSON
        "lineHeight": 1,                       # Based on your JSON ("1" → as number)
        "dir": "auto"                          # Matches JSON
    },
    "heading": {
        "textAlign": None,                     # Your JSON did not specify heading alignment
        "indent": 0,                           # Align with paragraph (no override found)
        "lineHeight": 1,                       # No headings present, but matching paragraph
        "dir": "auto",                         # Adjusted to match paragraph direction
        "level": 2                             # Can be changed dynamically per use-case
    }
}
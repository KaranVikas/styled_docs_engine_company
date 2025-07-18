from prosemirror.schema.basic.schema_basic import nodes as base_nodes, marks as base_marks
from prosemirror.schema.basic import Schema
from typing import Optional
from template_loader import get_default_attrs
from template_loader import get_heading_text_style
from prosemirror.model import schema

nodes = {
    "doc": {"content": "block+", "group": "block"},
    # using custom paragraph for customized template
    # "paragraph": {
    #     "content": "inline*",
    #     "group": "block",
    #     "attrs": {
    #         "textAlign": {"default": None},
    #         "indent": {"default": 0},
    #         "lineHeight": {"default": None},
    #         "dir": {"default": "auto"}
    #     }
    # },

    "text": {"group": "inline"},
    "heading": {
        "content": "inline*",
        "group": "block",
        "attrs": {
            "textAlign": {"default": "Right"},
            "indent": {"default": 0},
            "lineHeight": {"default": 0},
            "dir": {"default": "auto"},
            "level": {"default": 1}
        }
    },
    # "orderedList": {
    #     "group": "block",
    #     "attrs": {"start": {"default": 1}, "type": {"default": None}},
    #     "content": "listItem+"
    # },
    "listItem": {
        "content": "paragraph",
        "group": "block"
    },
    #  "hard_break": {
    #     "inline": True,
    #     "group": "inline",
    #     "selectable": False,
    #     "parseDOM": [{"tag": "br"}],
    #     "toDOM": lambda _: ["br"],
    # },

}

base_nodes["paragraph"] = {
    "content": "inline*",
    "group": "block",
    "attrs": {
        "textAlign": {"default": None},
        "indent": {"default": 0},
        "lineHeight": {"default": None},
        "dir": {"default": "auto"},
    },
    "parseDOM": [{"tag": "p"}],
    "toDOM": lambda node: [
        "p",
        {
            "style": "; ".join(filter(None, [
                f"text-align: {node.attrs.get('textAlign')}" if node.attrs.get("textAlign") else "",
                f"text-indent: {node.attrs.get('indent')}em" if node.attrs.get("indent") else "",
                f"line-height: {node.attrs.get('lineHeight')}" if node.attrs.get("lineHeight") else "",
                f"direction: {node.attrs.get('dir')}" if node.attrs.get("dir") else "",
            ]))
        },
        0
    ]
}

base_nodes["image"] = {
    "inline": True,
    "attrs": {
        "src": {},
        "alt": {"default": None},
        "title": {"default": None}
    },
    "group": "inline",
    "draggable": True,
    "parseDOM": [{"tag": "img", "getAttrs": lambda dom: {
        "src": dom.get("src"),
        "alt": dom.get("alt"),
        "title": dom.get("title")
    }}],
    "toDOM": lambda node: ["img", node.attrs]
}

# base_nodes["horizontal_rule"] = {
#     "group": "block",
#     "parseDOM": [{"tag": "hr"}],
#     "toDOM": lambda _: ["hr"]
# }

# Add underline mark with HTML mapping
base_marks["underline"] = {
    "parseDOM": [{"tag": "u"}],
    "toDOM": lambda _: ["u", 0]
}

# Rename marks for semantic clarity
base_marks["bold"] = base_marks.pop("strong")
base_marks["italic"] = base_marks.pop("em")

base_marks["highlight"] = {
    "attrs": {
        "color": {"default": "#FFFF00"}
    },
    "parseDOM": [{"style": "background-color"}],
    "toDOM": lambda mark: ["span", {"style": f"background-color: {mark.attrs.get('color', '#FFFF00')}"}, 0]
}

base_marks["textStyle"] = {
    "attrs": {
        "fontFamily": {"default": None},
        "fontSize": {"default": None},
        "color": {"default": None}
    },
    "parseDOM": [{"style": "font-family"}, {"style": "font-size"}, {"style": "color"}],
    "toDOM": lambda mark: [
        "span",
        {
            "style": "; ".join(
                f"{k.replace('font', 'font-') if 'font' in k else k}: {v}"
                for k, v in mark.attrs.items() if v
            )
        },
        0
    ]
}

base_nodes["image"] = {
    "inline": True,
    "attrs": {
        "src": {},
        "alt": {"default": None},
        "title": {"default": None},
        "flipX": {"default": False},
        "flipY": {"default": False},
        "width": {"default": None},
        "align": {"default": "center"},
    },
    "group": "inline",
    "draggable": True,
    "parseDOM": [
        {
            "tag": "img",
            "getAttrs": lambda dom: {
                "src": dom.get("src"),
                "alt": dom.get("alt"),
                "title": dom.get("title"),
                "width": dom.get("width"),
                "flipX": dom.get("data-flip-x") == "true",
                "flipY": dom.get("data-flip-y") == "true",
                "align": dom.get("data-align", "center"),
            },
        }
    ],
    "toDOM": lambda node: [
        "img",
        {
            "src": node.attrs["src"],
            "alt": node.attrs["alt"],
            "title": node.attrs["title"],
            "width": node.attrs["width"],
            "data-flip-x": str(node.attrs["flipX"]).lower(),
            "data-flip-y": str(node.attrs["flipY"]).lower(),
            "data-align": node.attrs["align"],
            "style": "; ".join(
                filter(None, [
                    "transform: scaleX(-1)" if node.attrs["flipX"] else "",
                    "transform: scaleY(-1)" if node.attrs["flipY"] else "",
                    f"text-align: {node.attrs['align']}" if node.attrs["align"] else "",
                    f"width: {node.attrs['width']}" if node.attrs["width"] else "",
                ])
            ),
        },
    ]
}

base_nodes["orderedList"] = {
    "group": "block",
    "attrs": {
        "start": {"default": 1},
        "type": {"default": None}
    },
    "content": "listItem+"
}

base_nodes["listItem"] = {
    "content": "paragraph",
    "group": "block"
}

base_nodes["bulletList"] = {
    "group": "block",
    "content": "listItem+"
}

base_nodes["horizontalRule"] = {
    "group": "block",
    "parseDOM": [{"tag": "hr"}],
    "toDOM": lambda _: ["hr"]
}

# base_nodes["hardBreak"] = {
#     "inline": True,
#     "group": "inline",
#     "selectable": False,
#     "parseDOM": [{"tag": "br"}],
#     "toDOM": lambda _: ["br"]
# }

schema = Schema({"nodes": base_nodes, "marks": base_marks})


def get_marks(styles: Optional[dict], underline: bool, bold: bool, italic: bool, highlight: Optional[str], link: dict,
              schema, block_type: None, heading_level=None):
    marks = []

    # Choose appropriate textStyle
    if block_type == "heading" and heading_level is not None:
        final_styles = get_heading_text_style(heading_level)
    else:
        final_styles = get_default_attrs("textStyle")

    if styles:
        final_styles.update(styles)

    if any(final_styles.values()):
        marks.append(schema.mark("textStyle", final_styles))

    # Apply font-based styles
    if styles and any(styles.values()):
        marks.append(schema.mark("textStyle", styles))

    # Apply underline mark if set
    if underline:
        marks.append(schema.mark("underline"))

    if bold:
        marks.append(schema.mark("bold"))

    if italic:
        marks.append(schema.mark("italic"))

    if highlight:
        marks.append(schema.mark("highlight", {"color": highlight}))

    if link and "href" in link:
        marks.append(schema.mark("link", {
            "href": link["href"],
            "title": link.get("title")
        }))

    return marks
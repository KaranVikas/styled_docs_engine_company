from document_schema import get_marks
from prosemirror.model import Node
from document_model import InputTextBlock
from template_loader import get_default_attrs, apply_with_overrides


def get_paragraph_attrs(block):
    return {
        "textAlign": getattr(block, "textAlign", None),
        "indent": getattr(block, "indent", 0),
        "lineHeight": getattr(block, "lineHeight", None),
        "dir": getattr(block, "dir", "auto")
    }


def convert_block(block: InputTextBlock, schema):
    # Handle block-level image

    text = block.text or ""
    marks = get_marks(
        block.styles,
        block.underline,
        block.italic,
        block.bold,
        block.highlight,
        block.link,
        schema,
        block_type="paragraph",
    )

    if block.type == "image":
        return schema.node("image", block.attrs or {})

    # Heading block
    if block.type == "heading":
        # 1. Safely get default heading attributes
        default_attrs = get_default_attrs("heading")
        level = block.level or default_attrs.get("level", 2)

        # 2. Now build heading_attrs using fallback defaults
        heading_attrs = {
            "textAlign": getattr(block, "textAlign", default_attrs.get("textAlign")),
            "indent": getattr(block, "indent", default_attrs.get("indent")),
            "lineHeight": getattr(block, "lineHeight", default_attrs.get("lineHeight")),
            "dir": getattr(block, "dir", default_attrs.get("dir")),
            "level": level
        }

        # 3. Get marks for this heading level
        marks = get_marks(
            styles=block.styles,
            underline=block.underline,
            italic=block.italic,
            bold=block.bold,
            highlight=block.highlight,
            link=block.link,
            schema=schema,
            block_type="heading",
            heading_level=level
        )

        return schema.node("heading", heading_attrs, [
            schema.text(block.text or "", marks)
        ])

    # Paragraph block
    if block.type == "paragraph":
        default_attrs = get_default_attrs("paragraph")

        print("default_attrs", default_attrs)

        # paragraph_attrs = apply_with_overrides(default_attrs, block)

        # print("paragraph_attr",paragraph_attrs)

        content = []

        # Add main block text (if any)
        if block.text:
            content.append(schema.text(block.text, marks))
            # print(schema.text(block.text, marks).to_json())
        # Add inline children (recursively)
        if block.children:
            content.extend(convert_inline_children(block.children, schema))

        return schema.node("paragraph", default_attrs, content)

    if block.type == "hardBreak":
        return schema.node("paragraph", {}, [
            schema.node("hard_break")
        ])
    # Ordered list block
    elif block.type == "orderedList":
        items = []
        for child in block.children or []:
            child_marks = get_marks(
                styles=getattr(child, "styles", None),
                underline=getattr(child, "underline", False),
                bold=getattr(child, "bold", False),
                italic=getattr(child, "italic", False),
                highlight=getattr(child, "highlight", None),
                link=getattr(child, "link", None),
                schema=schema,
                block_type="heading",
                # heading_level=level
            )
            print("order_list Attributes ", get_paragraph_attrs(child))
            paragraph = schema.node("paragraph", get_paragraph_attrs(child), [
                schema.text(child.text or "", child_marks)
            ])
            list_item = schema.node("listItem", {}, [paragraph])
            items.append(list_item)

        return schema.node("orderedList", {"start": block.start or 1}, items)

    # Bullet list block
    elif block.type == "bulletList":
        items = []
        for child in block.children or []:
            child_marks = get_marks(
                styles=getattr(child, "styles", None),
                underline=getattr(child, "underline", False),
                bold=getattr(child, "bold", False),
                italic=getattr(child, "italic", False),
                highlight=getattr(child, "highlight", None),
                link=getattr(child, "link", None),
                schema=schema,
                block_type="heading"
            )

            paragraph = schema.node("paragraph", get_paragraph_attrs(child), [
                schema.text(child.text or "", child_marks)
            ])
            list_item = schema.node("listItem", {}, [paragraph])
            items.append(list_item)

        return schema.node("bulletList", {}, items)

    # Horizontal rule
    elif block.type == "horizontalRule":
        return schema.node("horizontalRule")

    # Fallback for unknown block types
    else:
        print(f"❌ Unrecognized block type: {block.type}")
        return None


def convert_inline_children(children, schema):
    inline_content = []

    for child in children:
        if child.type == "text":
            marks = get_marks(
                styles=getattr(child, "styles", None),
                underline=getattr(child, "underline", False),
                bold=getattr(child, "bold", False),
                italic=getattr(child, "italic", False),
                highlight=getattr(child, "highlight", None),
                link=getattr(child, "link", None),
                block_type="paragraph",
                schema=schema
            )
            inline_content.append(schema.text(child.text or "", marks))

        elif child.type == "image":
            inline_content.append(schema.node("image", child.attrs or {}))
        # this change dont let my code run
        # elif child.type == "hardBreak":
        #     inline_content.append(schema.node("hardBreak"))

        else:
            print(f"⚠️ Unsupported inline child type: {child.type}")

    return inline_content


def convert_document(blocks: list[InputTextBlock], schema) -> Node:
    return schema.node("doc", {}, [
        block_node for block in blocks
        if (block_node := convert_block(block, schema)) is not None
    ])

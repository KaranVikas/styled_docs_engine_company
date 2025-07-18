from style_merger import DEFAULT_STYLE_TEMPLATE

def get_default_attrs(block_type: str) -> dict:
  return DEFAULT_STYLE_TEMPLATE.get(block_type, {}).copy()

def apply_with_overrides(default_attrs: dict, block) -> dict:
  """Update default values with what's in the block input."""

  result = default_attrs.copy()

  for key in result:
    result[key] = getattr(block, key, result[key])
  return result

def get_heading_text_style(level: int) -> dict:
    return DEFAULT_STYLE_TEMPLATE.get("headingStyles", {}).get(level, DEFAULT_STYLE_TEMPLATE["textStyle"])
# --- Заменить/вставить эту реализацию вместо старой extract_description_from_yaml/fallback_parse ---

def extract_description_from_yaml(data: dict, raw_text: str) -> str:
    """
    Try many strategies to get the description:
      1) Prefer parsed YAML value: data['blueprint']['description']
      2) Try regex for block scalars: description: |  or description: >
      3) Try inline quoted description: description: "..."
      4) Try with indentation (in case description sits under blueprint: with indentation)
    Returns a cleaned string (no leading indentation in lines).
    """
    # 1) Parsed YAML value (best)
    try:
        if isinstance(data, dict):
            bp = data.get("blueprint", {})
            desc = bp.get("description")
            if desc is not None:
                return str(desc)
    except Exception:
        pass

    if not raw_text:
        return ""

    text = raw_text

    # 2) Block scalar (| or >) with possible indentation before the key
    m = re.search(r'^[ \t\-]*description:\s*(?:\|\-?|>\-?)\s*\n((?:[ \t]+.*\n)+)', text, flags=re.IGNORECASE | re.MULTILINE)
    if m:
        block = m.group(1)
        # remove common indentation
        lines = [re.sub(r'^[ \t]+', '', ln.rstrip()) for ln in block.splitlines()]
        return "\n".join(lines).strip()

    # 3) Inline quoted description e.g. description: "text..." or 'text...'
    m2 = re.search(r'^[ \t]*description:\s*[\'"](.+?)[\'"]\s*$', text, flags=re.IGNORECASE | re.MULTILINE)
    if m2:
        return m2.group(1).strip()

    # 4) Sometimes description is after 'blueprint:' with indentation - try a bit more liberal match
    m3 = re.search(r'blueprint:\s*(?:\n[ \t]+.*?)*?\n[ \t]*description:\s*(?:\|\-?|>\-?)\s*\n((?:[ \t]+.*\n)+)', text, flags=re.IGNORECASE | re.DOTALL)
    if m3:
        block = m3.group(1)
        lines = [re.sub(r'^[ \t]+', '', ln.rstrip()) for ln in block.splitlines()]
        return "\n".join(lines).strip()

    # 5) Very liberal: take everything after 'description:' until next top-level key or EOF
    m4 = re.search(r'^[ \t]*description:\s*\n((?:[ \t].*\n)+)', text, flags=re.IGNORECASE | re.MULTILINE)
    if m4:
        block = m4.group(1)
        lines = [re.sub(r'^[ \t]+', '', ln.rstrip()) for ln in block.splitlines()]
        return "\n".join(lines).strip()

    return ""

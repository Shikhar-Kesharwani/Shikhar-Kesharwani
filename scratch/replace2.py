import re

with open("C:/Users/HP/Downloads/ascii/andrew_style.py", "r") as f:
    text = f.read()

# Helper function
helper = """
    def get_discrete_anim(attr, row_len, char_width, base_val, kt1, kt2):
        if row_len < 1: row_len = 1
        vals = ["0", "0"] if attr == "width" else [f"{base_val:.1f}", f"{base_val:.1f}"]
        times = ["0", f"{kt1:.4f}"]
        step = (kt2 - kt1) / row_len
        for i in range(1, row_len + 1):
            v = i * char_width + 10 if attr == "width" else base_val + (i-1) * char_width
            vals.append(f"{v:.1f}")
            times.append(f"{kt1 + i * step:.4f}")
        vals.append(vals[-1])
        times.append("1")
        return "; ".join(vals), "; ".join(times)
"""

text = text.replace("def build_svg():\n    parts = []", "def build_svg():\n" + helper + "\n    parts = []")

ascii_old = """        parts.append(f'<clipPath id="{clip_id}">')
        parts.append(f'<rect x="15" y="{y - ASCII_FS}" width="0" height="{ASCII_LH + 5}">'
                     f'<animate attributeName="width" '
                     f'values="0; 0; {row_px + 10:.1f}; {row_px + 10:.1f}" '
                     f'keyTimes="0; {_kt1:.4f}; {_kt2:.4f}; 1" '
                     f'dur="{TOTAL_DUR:.3f}s" fill="freeze" />'
                     f'</rect></clipPath>')
                     
        parts.append(f"<text x='15' y='{y}' class='text' font-size='{ASCII_FS}px' "
                     f"clip-path='url(#{clip_id})'>{esc(row)}</text>")
                     
        # Add the moving block cursor that rides the wipe edge
        parts.append(f'<rect x="15" y="{y - ASCII_FS + 2}" width="5" height="{ASCII_LH - 1}" class="add" opacity="0">'
                     f'<animate attributeName="x" '
                     f'values="15; 15; {15 + row_px:.1f}; {15 + row_px:.1f}" '
                     f'keyTimes="0; {_kt1:.4f}; {_kt2:.4f}; 1" '
                     f'dur="{TOTAL_DUR:.3f}s" fill="freeze" />'
                     f'<animate attributeName="opacity" '
                     f'values="0; 1; 0; 0" '
                     f'keyTimes="0; {_kt1:.4f}; {_kt2:.4f}; 1" '
                     f'dur="{TOTAL_DUR:.3f}s" fill="freeze" />'
                     f'</rect>')"""

ascii_new = """        v_width, k_width = get_discrete_anim("width", row_len, ASCII_CW, 0, _kt1, _kt2)
        v_x, k_x = get_discrete_anim("x", row_len, ASCII_CW, 15, _kt1, _kt2)
        
        parts.append(f'<clipPath id="{clip_id}">')
        parts.append(f'<rect x="15" y="{y - ASCII_FS}" width="0" height="{ASCII_LH + 5}">'
                     f'<animate attributeName="width" calcMode="discrete" '
                     f'values="{v_width}" keyTimes="{k_width}" '
                     f'dur="{TOTAL_DUR:.3f}s" fill="freeze" />'
                     f'</rect></clipPath>')
                     
        parts.append(f"<text x='15' y='{y}' class='text' font-size='{ASCII_FS}px' "
                     f"clip-path='url(#{clip_id})'>{esc(row)}</text>")
                     
        # Add the moving block cursor that rides the wipe edge
        parts.append(f'<rect x="15" y="{y - ASCII_FS + 2}" width="5" height="{ASCII_LH - 1}" class="add" opacity="0">'
                     f'<animate attributeName="x" calcMode="discrete" '
                     f'values="{v_x}" keyTimes="{k_x}" '
                     f'dur="{TOTAL_DUR:.3f}s" fill="freeze" />'
                     f'<animate attributeName="opacity" calcMode="discrete" '
                     f'values="0; 1; 1; 0; 0" '
                     f'keyTimes="0; {_kt1:.4f}; {_kt2:.4f}; {min(_kt2 + 0.0001, 1):.4f}; 1" '
                     f'dur="{TOTAL_DUR:.3f}s" fill="freeze" />'
                     f'</rect>')"""

text = text.replace(ascii_old, ascii_new)

info_old = """        parts.append(f'<clipPath id="{clip_id}">')
        parts.append(f'<rect x="{px}" y="{y - 14}" width="0" height="20">'
                     f'<animate attributeName="width" '
                     f'values="0; 0; {row_px + 20:.1f}; {row_px + 20:.1f}" '
                     f'keyTimes="0; {_kt1:.4f}; {_kt2:.4f}; 1" '
                     f'dur="{TOTAL_DUR:.3f}s" fill="freeze" />'
                     f'</rect></clipPath>')
                     
        parts.append(f"<text clip-path='url(#{clip_id})'>{body}</text>")"""

info_new = """        v_width, k_width = get_discrete_anim("width", row_len, CW, 0, _kt1, _kt2)
        
        parts.append(f'<clipPath id="{clip_id}">')
        parts.append(f'<rect x="{px}" y="{y - 14}" width="0" height="20">'
                     f'<animate attributeName="width" calcMode="discrete" '
                     f'values="{v_width}" keyTimes="{k_width}" '
                     f'dur="{TOTAL_DUR:.3f}s" fill="freeze" />'
                     f'</rect></clipPath>')
                     
        parts.append(f"<text clip-path='url(#{clip_id})'>{body}</text>")"""

text = text.replace(info_old, info_new)

text = text.replace("ROW_DUR = 0.05", "ROW_DUR = 0.15")

with open("C:/Users/HP/Downloads/ascii/andrew_style.py", "w") as f:
    f.write(text)

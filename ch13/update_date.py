from datetime import date
from pathlib import Path

page = Path(__file__).parent / "index.html"
text = page.read_text(encoding="utf-8")
today = date.today().isoformat()

marker = '<p id="updated">'
start = text.find(marker)
end = text.find("</p>", start)
text = text[:start] + marker + "更新日: " + today + text[end:]

page.write_text(text, encoding="utf-8")
print("更新日を", today, "にしました")

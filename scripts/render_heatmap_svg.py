import json
from datetime import datetime

def main():
    with open('data/contributions.json', 'r') as f:
        data = json.load(f)
        
    days = data['days']
    if not days:
        print("No days found in data.")
        return
        
    # GitHub dark mode palette
    PALETTE = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353", "#69f0a0"]
    
    box_size = 12
    box_gap = 4
    
    width = 860
    height = 150
    
    parts = []
    parts.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">')
    
    css = """
    <style>
    @keyframes slideDown {
      0% { transform: translateY(-10px); opacity: 0; }
      100% { transform: translateY(0); opacity: 1; }
    }
    .box {
      opacity: 0;
    }
    .text {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
      fill: #8b949e;
      font-size: 14px;
    }
    .stat-val {
      fill: #c9d1d9;
      font-weight: bold;
    }
    </style>
    """
    parts.append(css)
    
    # Parse dates and sort
    days.sort(key=lambda x: x['date'])
    first_dt = datetime.strptime(days[0]['date'], "%Y-%m-%d")
    
    # We want Sunday=0, Monday=1... Saturday=6
    start_dow = (first_dt.weekday() + 1) % 7 
    
    # Figure out total columns needed for centering
    last_dt = datetime.strptime(days[-1]['date'], "%Y-%m-%d")
    total_delta = (last_dt - first_dt).days
    total_cols = (start_dow + total_delta) // 7 + 1
    
    graph_width = total_cols * (box_size + box_gap) - box_gap
    offset_x = (width - graph_width) / 2
    offset_y = 30
    
    parts.append(f'<g transform="translate({offset_x}, {offset_y})">')
    
    for d in days:
        dt = datetime.strptime(d['date'], "%Y-%m-%d")
        delta = (dt - first_dt).days
        
        total_days = start_dow + delta
        col = total_days // 7
        row = total_days % 7
        
        level = min(d['level'], 5)
        color = PALETTE[level]
        
        x = col * (box_size + box_gap)
        y = row * (box_size + box_gap)
        
        # Diagonal delay calculation for stylish animation
        delay = (col * 0.02) + (row * 0.02)
        
        parts.append(f'<rect class="box" x="{x}" y="{y}" width="{box_size}" height="{box_size}" rx="2" fill="{color}" style="animation: slideDown 0.6s ease-out forwards {delay}s;" />')
        
    parts.append('</g>')
    
    # Footer removed
    parts.append('</svg>')
    
    with open('contrib-heatmap.svg', 'w') as f:
        f.write("\\n".join(parts))
        
    print("Successfully rendered contrib-heatmap.svg")

if __name__ == "__main__":
    main()

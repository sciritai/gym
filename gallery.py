import os
import base64

def create_portable_gallery():
    # Find all gif files
    gifs = [f for f in os.listdir('.') if f.endswith('.gif')]
    gifs.sort()

    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Portable Gym Library</title>
        <style>
            body { font-family: 'Segoe UI', sans-serif; background: #121212; color: white; margin: 0; padding: 20px; }
            h1 { text-align: center; color: #ffcc00; }
            .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 20px; max-width: 1200px; margin: 0 auto; }
            .card { background: #1e1e1e; padding: 10px; border-radius: 12px; cursor: pointer; border: 1px solid #333; }
            img { width: 100%; border-radius: 8px; }
            p { margin: 10px 0 0; font-weight: 600; font-size: 0.8em; color: #bbb; text-align: center; }
            #overlay {
                display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%;
                background: rgba(0,0,0,0.95); z-index: 1000; justify-content: center; align-items: center; flex-direction: column;
            }
            #overlay img { max-width: 90%; max-height: 80%; border: 2px solid #ffcc00; }
        </style>
    </head>
    <body>
        <h1>PORTABLE LOKI LIBRARY</h1>
        <div class="grid">
    """

    for gif in gifs:
        print(f"Embedding {gif}...")
        with open(gif, "rb") as image_file:
            # Convert binary image data to base64 string
            encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
            data_uri = f"data:image/gif;base64,{encoded_string}"
            
        clean_name = gif.replace('_', ' ').replace('.gif', '').title()
        display_name = ' '.join(clean_name.split()[1:]) if clean_name[0].isdigit() else clean_name
        
        html_content += f"""
            <div class="card" onclick="openFullPage('{data_uri}', '{display_name}')">
                <img src="{data_uri}">
                <p>{display_name}</p>
            </div>"""

    html_content += """
        </div>
        <div id="overlay" onclick="closeFullPage()">
            <img id="overlay-img" src="">
            <div id="overlay-title" style="margin-top:20px; color:#ffcc00; font-size:1.5em;"></div>
        </div>
        <script>
            function openFullPage(src, title) {
                document.getElementById('overlay-img').src = src;
                document.getElementById('overlay-title').innerText = title;
                document.getElementById('overlay').style.display = 'flex';
            }
            function closeFullPage() {
                document.getElementById('overlay').style.display = 'none';
            }
        </script>
    </body>
    </html>
    """

    with open("portable_library.html", "w") as f:
        f.write(html_content)
    print("Success! Created 'portable_library.html'. You can now move this file anywhere.")

if __name__ == "__main__":
    create_portable_gallery()
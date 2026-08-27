from js import Response, URL
import yt_dlp

async def on_fetch(request, env, ctx):
    url = URL.new(request.url).searchParams.get("url")
    if not url:
        return Response.new("Please provide a ?url= parameter", status=400)
    
    # Basic yt-dlp extraction logic
    ydl_opts = {'format': 'best'}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        video_url = info.get('url', 'No direct link found')
        
    return Response.new(f"Direct video stream URL: {video_url}")

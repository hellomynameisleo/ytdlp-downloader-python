import os
import subprocess
from colorama import Fore, Style, init

# Initialize colorama
init()

# Set the path to your ytdlp installation directory
ytdlp_path = os.path.dirname(os.path.abspath(__file__))
downloadpath = os.path.expanduser("~/Downloads/")

# Check if ytdlp directory exists
if not os.path.exists(ytdlp_path):
    print("ytdlp directory does not exist.")
    print("Please set the correct path to your ytdlp installation directory.")
    exit(1)

# Update ytdlp
print("Updating ytdlp...")
os.chdir(ytdlp_path)
subprocess.call(['curl', '-L', '-o', os.path.join(ytdlp_path, 'yt-dlp.exe'), 'https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp.exe'])
os.chdir(os.path.dirname(os.path.abspath(__file__)))
print()

while True:
    options_choice = input("Choose an option for download options:\n"
                           "1. Best audio in AAC\n-f ba -x --audio-format aac\n\n"  # Downloads the video with best audio then extracts the audio and converts to AAC format
                           "2. Best audio\n-f bestaudio/best -v --extract-audio --audio-quality 0\n\n"  # Downloads the video with best audio then extracts the audio
                           "3. Best audio, download whole playlist\n-f bestaudio/best -v --extract-audio --audio-quality 0 --yes-playlist\n\n"  # Downloads the video with best audio then extracts the audio, downloads the whole playlist
                           "4. Best quality video and audio into single file\n-f bestvideo+bestaudio\n\n"  # Downloads the best quality video and audio streams separately and then merges them into a single file
                           "Enter option number (1, 2, 3, or 4): ")

    if options_choice == "1":
        download_options = ["-f", "ba", "-x", "--audio-format", "aac"]
        break
    elif options_choice == "2":
        download_options = ["-f", "bestaudio/best", "-v", "--extract-audio", "--audio-quality", "0"]
        break
    elif options_choice == "3":
        download_options = ["-f", "bestaudio/best", "-v", "--extract-audio", "--audio-quality", "0", "--yes-playlist"]
        break
    elif options_choice == "4":
        download_options = ["-f", "bestvideo+bestaudio"]
        break
    else:
        print(Fore.YELLOW + options_choice, end=" ")
        print(Fore.RED + "is a Invalid option. Please select a valid option.")
        print(Style.RESET_ALL)

print(Fore.GREEN + "Selected download options:", download_options)
print(Style.RESET_ALL)

while True:
    # Prompt for YouTube URLs
    youtube_urls_input = input("Enter YouTube URLs, separated by a space for multiple (or type 'exit' to quit): ")

    # Check if the user wants to exit
    if youtube_urls_input.lower() == "exit":
        print("Exiting...")
        break

    youtube_urls = youtube_urls_input.split()

    for youtube_url in youtube_urls:
        print(f"Downloading {youtube_url}")

        # Download video with specified options
        os.chdir(ytdlp_path)
        subprocess.call(['yt-dlp.exe', youtube_url, '--output', '%(title)s.%(ext)s', '--paths', downloadpath] + download_options)
        print(f"Finished downloading '{youtube_url}' to '{downloadpath}'")
        print()

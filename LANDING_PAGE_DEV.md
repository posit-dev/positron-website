# Landing Page Development

## Quick Start

To see live changes while editing the landing page:

1. **Start the Quarto preview server** (in one terminal):
   ```bash
   quarto preview
   ```

2. **Run the watch script** (in another terminal):
   ```bash
   ./watch-landing.sh
   ```

3. **Edit your files**:
   - `index.html` - Landing page structure
   - `landing.css` - Landing page styles

The watch script will automatically copy your changes to both the `_site` directory and the `.conductor/seoul` directory (used by Quarto preview).

## How it Works

The `watch-landing.sh` script:
- Watches for changes to `index.html` and `landing.css`
- Automatically copies them to the appropriate directories
- Works on macOS, Linux, and Windows (with WSL)
- Falls back to polling if file watching tools aren't installed

## Optional: Better Performance

For instant file watching (recommended):
- **macOS**: `brew install fswatch`
- **Ubuntu/Debian**: `sudo apt-get install inotify-tools`
- **Other Linux**: Install `inotify-tools` via your package manager

## Troubleshooting

If the script doesn't work:
1. Make sure it's executable: `chmod +x watch-landing.sh`
2. Run it from the project root directory
3. Check that `index.html` and `landing.css` exist in the current directory

## Notes

- The landing page uses plain HTML/CSS (no Quarto processing needed)
- Images referenced in the HTML should be in the `images/` directory
- The script will create the necessary directories if they don't exist
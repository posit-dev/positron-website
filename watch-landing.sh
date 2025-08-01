#!/bin/bash

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}🚀 Starting landing page watcher...${NC}"
echo -e "${YELLOW}Watching for changes to index.html and landing.css${NC}"
echo -e "${YELLOW}Press Ctrl+C to stop${NC}\n"

# Function to copy files
copy_files() {
    echo -e "${GREEN}📋 Copying files...${NC}"
    
    # Copy to _site directory
    cp index.html _site/ 2>/dev/null && echo "  ✓ Copied index.html to _site/"
    cp landing.css _site/ 2>/dev/null && echo "  ✓ Copied landing.css to _site/"
    
    # Copy to conductor directory if it exists
    if [ -d ".conductor/seoul" ]; then
        cp index.html .conductor/seoul/ 2>/dev/null && echo "  ✓ Copied index.html to .conductor/seoul/"
        cp landing.css .conductor/seoul/ 2>/dev/null && echo "  ✓ Copied landing.css to .conductor/seoul/"
    fi
    
    echo -e "${GREEN}✨ Files updated!${NC}\n"
}

# Initial copy
copy_files

# Watch for changes based on the OS
if command -v fswatch >/dev/null 2>&1; then
    # macOS with fswatch
    echo "Using fswatch (macOS)..."
    fswatch -o index.html landing.css | while read f; do
        copy_files
    done
elif command -v inotifywait >/dev/null 2>&1; then
    # Linux with inotify-tools
    echo "Using inotifywait (Linux)..."
    while true; do
        inotifywait -e modify,create index.html landing.css
        copy_files
    done
else
    # Fallback: simple polling
    echo "No file watcher found. Using polling (checking every 2 seconds)..."
    echo "For better performance:"
    echo "  - macOS: Install fswatch with 'brew install fswatch'"
    echo "  - Linux: Install inotify-tools with 'apt-get install inotify-tools'"
    echo ""
    
    # Get initial timestamps
    if [[ "$OSTYPE" == "darwin"* ]]; then
        # macOS
        last_index=$(stat -f %m index.html 2>/dev/null || echo 0)
        last_css=$(stat -f %m landing.css 2>/dev/null || echo 0)
    else
        # Linux/Other
        last_index=$(stat -c %Y index.html 2>/dev/null || echo 0)
        last_css=$(stat -c %Y landing.css 2>/dev/null || echo 0)
    fi
    
    while true; do
        sleep 2
        
        # Get current timestamps
        if [[ "$OSTYPE" == "darwin"* ]]; then
            # macOS
            current_index=$(stat -f %m index.html 2>/dev/null || echo 0)
            current_css=$(stat -f %m landing.css 2>/dev/null || echo 0)
        else
            # Linux/Other
            current_index=$(stat -c %Y index.html 2>/dev/null || echo 0)
            current_css=$(stat -c %Y landing.css 2>/dev/null || echo 0)
        fi
        
        # Check if files have changed
        if [ "$current_index" != "$last_index" ] || [ "$current_css" != "$last_css" ]; then
            copy_files
            last_index=$current_index
            last_css=$current_css
        fi
    done
fi
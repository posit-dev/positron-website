# GitHub Stats Automation

This directory contains scripts to automatically update GitHub repository statistics displayed on the Positron website.

## Overview

The `update-github-stats.js` script fetches the latest statistics from the GitHub API and saves them to a JSON file (`data/github-stats.json`) with current values for:
- Number of stars
- Number of forks  
- Number of contributors

## How it works

1. **Data Collection**: The script fetches data from the GitHub API for the `posit-dev/positron` repository, handling pagination for accurate contributor counts
2. **Data Storage**: Statistics are saved to `data/github-stats.json` with a timestamp
3. **Client-side Updates**: The landing page includes `js/github-stats.js` which fetches the JSON data and updates elements with `data-stat` attributes
4. **Graceful Fallback**: If JavaScript is disabled or the JSON fetch fails, the static HTML values are displayed
5. **Automation**: A GitHub Action runs this script daily at 2:00 AM UTC to keep the stats current

## Architecture Benefits

- **Separation of Concerns**: Stats fetching is decoupled from HTML structure
- **Robust Updates**: No regex parsing of HTML needed; uses data attributes instead
- **Progressive Enhancement**: Works without JavaScript, enhances with it
- **Easy Maintenance**: Adding new stats only requires updating the JSON and adding data attributes

## Manual execution

To run the script manually:

```bash
node scripts/update-github-stats.js
```

For authenticated requests with higher rate limits, provide a GitHub token:

```bash
GITHUB_TOKEN=your_token_here node scripts/update-github-stats.js
```

## GitHub Action

The automation is handled by `.github/workflows/update-github-stats.yml` which:
- Runs daily at 2:00 AM UTC
- Can be manually triggered via workflow dispatch
- Automatically commits changes if stats have been updated
- Uses `[skip ci]` in commit messages to avoid triggering other workflows

## Maintenance

If the HTML structure changes, you may need to update the regex patterns in `update-github-stats.js` to match the new structure.
# GitHub Stats Implementation Guide

## Overview

The Positron website displays real-time GitHub repository statistics (stars, forks, contributors) using a flexible system that supports both live API fetching and static fallbacks.

## Architecture

### Components

1. **Static JSON File** (`data/github-stats.json`)
   - Updated daily via GitHub Actions
   - Serves as fallback when API is unavailable
   - No rate limit concerns

2. **Client-side JavaScript** (`js/github-stats-unified.js`)
   - Supports three modes: `live`, `static`, and `auto`
   - Implements caching to reduce API calls
   - Gracefully handles rate limits

3. **Configuration** (`js/github-stats-config.js`)
   - Simple configuration file to set fetching mode
   - Can be modified without touching main script

4. **GitHub Action** (`.github/workflows/update-github-stats.yml`)
   - Runs daily to update static JSON
   - Ensures fallback data is always fresh

### Fetching Modes

#### 1. Live Mode (`'live'`)
- Fetches directly from GitHub API
- Real-time data
- Subject to rate limits (60 requests/hour for unauthenticated)
- Best for development or low-traffic sites

```javascript
window.GITHUB_STATS_MODE = 'live';
```

#### 2. Static Mode (`'static'`)
- Uses pre-generated JSON file only
- No API calls from client
- Updated daily via GitHub Actions
- Best for high-traffic sites

```javascript
window.GITHUB_STATS_MODE = 'static';
```

#### 3. Auto Mode (`'auto'`) - Default
- Tries live API first
- Falls back to static if rate limited
- Best balance of freshness and reliability

```javascript
window.GITHUB_STATS_MODE = 'auto'; // or omit for default
```

## Rate Limit Considerations

### GitHub API Limits
- **Unauthenticated**: 60 requests/hour per IP
- **Authenticated**: 5,000 requests/hour (not used in client)

### Our Implementation
- **Caching**: 1-hour client-side cache via localStorage
- **Smart Fetching**: Contributors limited to first 100 (1-2 API calls)
- **Fallback**: Automatic switch to static data when rate limited

### Traffic Calculations
With 1-hour caching:
- Each unique visitor: 2 API calls (repo info + contributors)
- Supports ~30 unique visitors/hour in live mode
- Unlimited in static mode

## HTML Implementation

Elements use data attributes for identification:

```html
<!-- Simple stat -->
<span data-stat="forks">108</span>

<!-- Formatted stat -->
<div data-stat="stars" data-format="short-plus">3.4k+</div>

<!-- Stat with nested elements -->
<span data-stat="stars" data-format="short">
  <svg>...</svg>
  <span class="stat-number">3.4k</span>
</span>
```

## Debugging

Open browser console and use:

```javascript
// Check current mode
GitHubStats.getMode()

// Force refresh
GitHubStats.refresh()

// Clear cache
GitHubStats.clearCache()

// Check if stats loaded
document.body.getAttribute('data-github-stats-loaded')
```

## Adding New Stats

1. Update `scripts/update-github-stats.js` to fetch new stat
2. Add to JSON structure
3. Add HTML element with appropriate `data-stat` attribute
4. Stats will automatically update

## Performance Tips

1. **High Traffic Sites**: Use `'static'` mode
2. **Low Traffic Sites**: Use `'auto'` or `'live'` mode
3. **Development**: Use `'live'` mode with `GitHubStats.clearCache()`

## Security Notes

- No authentication tokens in client-side code
- API calls are read-only
- CORS handled by GitHub's API
- Fallback ensures site never breaks

## Future Enhancements

Possible improvements:
1. WebSocket for real-time updates
2. Service Worker for better caching
3. GraphQL API for more efficient queries
4. Server-side proxy for authenticated requests
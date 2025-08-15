/**
 * GitHub Stats Configuration
 * 
 * This file allows you to configure how GitHub stats are fetched.
 * Options:
 * - 'live': Fetch directly from GitHub API (real-time but subject to rate limits)
 * - 'static': Use pre-generated JSON file (updated daily via GitHub Actions)
 * - 'auto': Try live first, fall back to static if rate limited (default)
 */

window.GITHUB_STATS_MODE = 'auto'; // Change to 'live' or 'static' as needed
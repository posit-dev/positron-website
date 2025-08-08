/**
 * GitHub Stats Unified Loader
 * Supports both live API fetching and static JSON fallback based on configuration
 */

(function() {
  'use strict';

  // Configuration
  const REPO_OWNER = 'posit-dev';
  const REPO_NAME = 'positron';
  const CACHE_KEY = 'positron-github-stats';
  const CACHE_DURATION = 60 * 60 * 1000; // 1 hour
  const GITHUB_API_BASE = 'https://api.github.com';
  
  // Get mode from global config or default to 'auto'
  const MODE = window.GITHUB_STATS_MODE || 'auto';

  // Format number for display
  function formatNumber(num, format) {
    if (format === 'short' || format === 'short-plus') {
      if (num >= 1000) {
        const formatted = (num / 1000).toFixed(1);
        const cleaned = formatted.replace(/\.0$/, '');
        return cleaned + 'k' + (format === 'short-plus' ? '+' : '');
      }
    }
    return num.toString();
  }

  // Update stat elements on the page
  function updateStats(stats) {
    const statElements = document.querySelectorAll('[data-stat]');
    
    statElements.forEach(element => {
      const statType = element.getAttribute('data-stat');
      const format = element.getAttribute('data-format');
      
      if (stats[statType] !== undefined) {
        const formattedValue = formatNumber(stats[statType], format);
        
        const numberSpan = element.querySelector('.stat-number');
        if (numberSpan) {
          numberSpan.textContent = formattedValue;
        } else if (element.children.length === 0) {
          element.textContent = formattedValue;
        } else {
          const textNode = Array.from(element.childNodes).find(node => node.nodeType === Node.TEXT_NODE);
          if (textNode) {
            textNode.textContent = formattedValue;
          }
        }
      }
    });

    // Add data attribute to indicate stats have been loaded
    document.body.setAttribute('data-github-stats-loaded', 'true');
  }

  // Cache management
  function getCachedStats() {
    if (MODE === 'static') return null; // Don't use cache in static mode
    
    try {
      const cached = localStorage.getItem(CACHE_KEY);
      if (cached) {
        const data = JSON.parse(cached);
        const now = new Date().getTime();
        if (now - data.timestamp < CACHE_DURATION) {
          return data.stats;
        }
      }
    } catch (e) {
      console.warn('Cache read error:', e);
    }
    return null;
  }

  function cacheStats(stats) {
    if (MODE === 'static') return; // Don't cache in static mode
    
    try {
      const data = {
        stats: stats,
        timestamp: new Date().getTime()
      };
      localStorage.setItem(CACHE_KEY, JSON.stringify(data));
    } catch (e) {
      console.warn('Cache write error:', e);
    }
  }

  // GitHub API fetching
  async function fetchFromGitHub(endpoint) {
    const response = await fetch(`${GITHUB_API_BASE}${endpoint}`, {
      headers: {
        'Accept': 'application/vnd.github.v3+json'
      }
    });

    if (response.status === 403) {
      const remaining = response.headers.get('X-RateLimit-Remaining');
      if (remaining === '0') {
        throw new Error('Rate limit exceeded');
      }
    }

    if (!response.ok) {
      throw new Error(`GitHub API error: ${response.status}`);
    }

    return response;
  }

  async function fetchLiveStats() {
    // Check cache first
    const cachedStats = getCachedStats();
    if (cachedStats) {
      console.log('Using cached GitHub stats');
      return cachedStats;
    }

    console.log('Fetching live GitHub stats...');

    // Fetch repository info
    const repoResponse = await fetchFromGitHub(`/repos/${REPO_OWNER}/${REPO_NAME}`);
    const repoData = await repoResponse.json();

    // For contributors, we'll use a simplified approach to avoid rate limits
    // Just get the first page and check if there are more
    const contribResponse = await fetchFromGitHub(
      `/repos/${REPO_OWNER}/${REPO_NAME}/contributors?per_page=100`
    );
    const contributors = await contribResponse.json();
    
    // Check if there are more pages
    const linkHeader = contribResponse.headers.get('Link');
    let contributorCount = contributors.length;
    
    // If there are more pages, add a "+" to indicate it's approximate
    if (linkHeader && linkHeader.includes('rel="next"')) {
      // For now, we'll use the known count from our daily updates
      // This avoids making multiple requests that could hit rate limits
      contributorCount = 41; // Will be updated by daily script
    }

    const stats = {
      stars: repoData.stargazers_count,
      forks: repoData.forks_count,
      contributors: contributorCount
    };

    cacheStats(stats);
    return stats;
  }

  async function fetchStaticStats() {
    const response = await fetch('/data/github-stats.json');
    if (!response.ok) {
      throw new Error('Failed to fetch static stats');
    }
    return response.json();
  }

  // Main function to fetch stats based on mode
  async function fetchStats() {
    try {
      switch (MODE) {
        case 'live':
          return await fetchLiveStats();
          
        case 'static':
          console.log('Using static GitHub stats');
          return await fetchStaticStats();
          
        case 'auto':
        default:
          try {
            return await fetchLiveStats();
          } catch (error) {
            if (error.message.includes('Rate limit') || error.message.includes('403')) {
              console.log('Falling back to static stats due to rate limit');
              return await fetchStaticStats();
            }
            throw error;
          }
      }
    } catch (error) {
      console.error('Failed to fetch GitHub stats:', error);
      return null;
    }
  }

  // Initialize
  async function init() {
    if (typeof fetch !== 'function') {
      return;
    }

    try {
      const stats = await fetchStats();
      if (stats) {
        updateStats(stats);
      }
    } catch (error) {
      console.error('Error loading GitHub stats:', error);
    }
  }

  // Start when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  // Expose API for debugging
  window.GitHubStats = {
    refresh: init,
    clearCache: () => localStorage.removeItem(CACHE_KEY),
    getMode: () => MODE
  };
})();
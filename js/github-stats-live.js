/**
 * GitHub Stats Live Loader
 * Fetches repository statistics directly from GitHub API with caching and rate limit handling
 */

(function() {
  'use strict';

  const REPO_OWNER = 'posit-dev';
  const REPO_NAME = 'positron';
  const CACHE_KEY = 'positron-github-stats';
  const CACHE_DURATION = 60 * 60 * 1000; // 1 hour in milliseconds
  const GITHUB_API_BASE = 'https://api.github.com';

  // Format number for display (e.g., 3456 -> 3.5k)
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
        
        // Check if element has child elements (like the star icon)
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
  }

  // Check if cached data is still valid
  function getCachedStats() {
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
      // Ignore localStorage errors
    }
    return null;
  }

  // Save stats to cache
  function cacheStats(stats) {
    try {
      const data = {
        stats: stats,
        timestamp: new Date().getTime()
      };
      localStorage.setItem(CACHE_KEY, JSON.stringify(data));
    } catch (e) {
      // Ignore localStorage errors (e.g., quota exceeded)
    }
  }

  // Fetch repository info from GitHub API
  async function fetchRepoInfo() {
    const response = await fetch(`${GITHUB_API_BASE}/repos/${REPO_OWNER}/${REPO_NAME}`, {
      headers: {
        'Accept': 'application/vnd.github.v3+json'
      }
    });

    if (!response.ok) {
      throw new Error(`GitHub API error: ${response.status}`);
    }

    const data = await response.json();
    return {
      stars: data.stargazers_count,
      forks: data.forks_count
    };
  }

  // Fetch contributor count with pagination
  async function fetchContributorCount() {
    let totalContributors = 0;
    let page = 1;
    let hasMore = true;

    // GitHub API returns max 100 per page, and we need to handle pagination
    // However, to avoid rate limits, we'll just fetch the first page and check headers
    while (hasMore && page <= 2) { // Limit to 2 pages to be conservative
      const response = await fetch(
        `${GITHUB_API_BASE}/repos/${REPO_OWNER}/${REPO_NAME}/contributors?page=${page}&per_page=100`,
        {
          headers: {
            'Accept': 'application/vnd.github.v3+json'
          }
        }
      );

      if (!response.ok) {
        throw new Error(`GitHub API error: ${response.status}`);
      }

      const contributors = await response.json();
      totalContributors += contributors.length;

      // Check if there's a next page
      const linkHeader = response.headers.get('Link');
      hasMore = linkHeader && linkHeader.includes('rel="next"');
      page++;
    }

    return totalContributors;
  }

  // Fetch stats from GitHub API
  async function fetchLiveStats() {
    try {
      // Check cache first
      const cachedStats = getCachedStats();
      if (cachedStats) {
        console.log('Using cached GitHub stats');
        return cachedStats;
      }

      console.log('Fetching fresh GitHub stats...');
      
      // Fetch repo info and contributor count in parallel
      const [repoInfo, contributorCount] = await Promise.all([
        fetchRepoInfo(),
        fetchContributorCount()
      ]);

      const stats = {
        stars: repoInfo.stars,
        forks: repoInfo.forks,
        contributors: contributorCount
      };

      // Cache the results
      cacheStats(stats);

      return stats;
    } catch (error) {
      console.warn('Failed to fetch live GitHub stats:', error);
      
      // Check if we're rate limited
      if (error.message.includes('403')) {
        console.log('GitHub API rate limit hit, falling back to static data');
      }
      
      // Fall back to static JSON file
      return fetchStaticStats();
    }
  }

  // Fetch stats from static JSON file (fallback)
  async function fetchStaticStats() {
    try {
      const response = await fetch('/data/github-stats.json');
      if (!response.ok) {
        throw new Error('Failed to fetch static stats');
      }
      const data = await response.json();
      console.log('Using static GitHub stats as fallback');
      return data;
    } catch (error) {
      console.error('Failed to fetch static stats:', error);
      return null;
    }
  }

  // Main initialization function
  async function init() {
    // Skip if fetch is not available
    if (typeof fetch !== 'function') {
      return;
    }

    try {
      const stats = await fetchLiveStats();
      if (stats) {
        updateStats(stats);
      }
    } catch (error) {
      console.error('Error initializing GitHub stats:', error);
    }
  }

  // Initialize when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
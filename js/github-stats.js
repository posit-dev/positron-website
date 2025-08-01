/**
 * GitHub Stats Loader
 * Fetches and updates GitHub repository statistics on the page
 */

(function() {
  'use strict';

  // Format number for display (e.g., 3456 -> 3.5k)
  function formatNumber(num, format) {
    if (format === 'short' || format === 'short-plus') {
      if (num >= 1000) {
        const formatted = (num / 1000).toFixed(1);
        // Remove trailing .0
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
          // Update just the number span if it exists
          numberSpan.textContent = formattedValue;
        } else if (element.children.length === 0) {
          // If no children, update the entire text content
          element.textContent = formattedValue;
        } else {
          // If has children but no stat-number span, update just the text node
          const textNode = Array.from(element.childNodes).find(node => node.nodeType === Node.TEXT_NODE);
          if (textNode) {
            textNode.textContent = formattedValue;
          }
        }
      }
    });
  }

  // Fetch stats from JSON file
  function fetchStats() {
    // Use fetch if available, otherwise skip (graceful degradation)
    if (typeof fetch !== 'function') {
      return;
    }

    fetch('/data/github-stats.json')
      .then(response => {
        if (!response.ok) {
          throw new Error('Failed to fetch stats');
        }
        return response.json();
      })
      .then(data => {
        updateStats(data);
      })
      .catch(error => {
        // Silently fail - the static values in HTML will be displayed
        console.warn('Could not load GitHub stats:', error);
      });
  }

  // Initialize when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', fetchStats);
  } else {
    fetchStats();
  }
})();
#!/usr/bin/env node

const https = require('https');
const fs = require('fs');
const path = require('path');

// GitHub API configuration
const GITHUB_API_BASE = 'https://api.github.com';
const REPO_OWNER = 'posit-dev';
const REPO_NAME = 'positron';
const USER_AGENT = 'Positron-Website-Stats-Updater';

// Helper function to make GitHub API requests
function fetchFromGitHub(endpoint) {
  return new Promise((resolve, reject) => {
    const options = {
      hostname: 'api.github.com',
      path: endpoint,
      method: 'GET',
      headers: {
        'User-Agent': USER_AGENT,
        'Accept': 'application/vnd.github.v3+json'
      }
    };

    // Add GitHub token if available (for higher rate limits)
    if (process.env.GITHUB_TOKEN) {
      options.headers['Authorization'] = `token ${process.env.GITHUB_TOKEN}`;
    }

    https.get(options, (res) => {
      let data = '';
      
      res.on('data', (chunk) => {
        data += chunk;
      });

      res.on('end', () => {
        if (res.statusCode === 200) {
          resolve({ data: JSON.parse(data), headers: res.headers });
        } else {
          reject(new Error(`GitHub API error: ${res.statusCode} - ${data}`));
        }
      });
    }).on('error', reject);
  });
}

// Fetch repository stats
async function getRepoStats() {
  try {
    const response = await fetchFromGitHub(`/repos/${REPO_OWNER}/${REPO_NAME}`);
    return {
      stars: response.data.stargazers_count,
      forks: response.data.forks_count
    };
  } catch (error) {
    console.error('Error fetching repository stats:', error);
    throw error;
  }
}

// Fetch contributor count (handling pagination)
async function getContributorCount() {
  let totalContributors = 0;
  let page = 1;
  let hasNextPage = true;

  try {
    while (hasNextPage) {
      const response = await fetchFromGitHub(`/repos/${REPO_OWNER}/${REPO_NAME}/contributors?page=${page}&per_page=100`);
      totalContributors += response.data.length;
      
      // Check if there's a next page
      const linkHeader = response.headers.link;
      hasNextPage = linkHeader && linkHeader.includes('rel="next"');
      page++;
    }
    
    return totalContributors;
  } catch (error) {
    console.error('Error fetching contributors:', error);
    throw error;
  }
}

// Save stats to JSON file
function saveStats(stats) {
  const dataDir = path.join(__dirname, '..', 'data');
  const statsFile = path.join(dataDir, 'github-stats.json');
  
  // Ensure data directory exists
  if (!fs.existsSync(dataDir)) {
    fs.mkdirSync(dataDir, { recursive: true });
  }
  
  // Add timestamp
  stats.lastUpdated = new Date().toISOString();
  
  // Write to file
  fs.writeFileSync(statsFile, JSON.stringify(stats, null, 2) + '\n', 'utf8');
  
  console.log(`✅ Updated ${statsFile} with latest GitHub stats`);
}

// Main function
async function main() {
  console.log('🔄 Fetching latest GitHub stats...');
  
  try {
    // Fetch all stats
    const [repoStats, contributorCount] = await Promise.all([
      getRepoStats(),
      getContributorCount()
    ]);
    
    const stats = {
      stars: repoStats.stars,
      forks: repoStats.forks,
      contributors: contributorCount
    };
    
    console.log('📊 Current stats:');
    console.log(`  Stars: ${stats.stars}`);
    console.log(`  Forks: ${stats.forks}`);
    console.log(`  Contributors: ${stats.contributors}`);
    
    // Save to JSON file
    saveStats(stats);
    
    console.log('✨ Stats update complete!');
    
  } catch (error) {
    console.error('❌ Failed to update stats:', error.message);
    process.exit(1);
  }
}

// Run the script
main();
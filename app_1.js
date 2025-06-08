// Application state
let savedStrategies = [];

// Sample earnings data
const companiesData = [
    {"symbol": "MSFT", "name": "Microsoft Corporation", "earningsDate": "2025-07-15", "marketCap": "$3.5T"},
    {"symbol": "NVDA", "name": "NVIDIA Corporation", "earningsDate": "2025-07-18", "marketCap": "$3.5T"},
    {"symbol": "AAPL", "name": "Apple Inc.", "earningsDate": "2025-07-22", "marketCap": "$3.0T"},
    {"symbol": "GOOGL", "name": "Alphabet Inc.", "earningsDate": "2025-07-25", "marketCap": "$2.1T"},
    {"symbol": "AMZN", "name": "Amazon.com Inc.", "earningsDate": "2025-07-29", "marketCap": "$1.8T"},
    {"symbol": "META", "name": "Meta Platforms Inc.", "earningsDate": "2025-08-01", "marketCap": "$1.4T"},
    {"symbol": "TSLA", "name": "Tesla Inc.", "earningsDate": "2025-08-05", "marketCap": "$1.2T"},
    {"symbol": "BRK.B", "name": "Berkshire Hathaway", "earningsDate": "2025-08-08", "marketCap": "$900B"},
    {"symbol": "TSM", "name": "Taiwan Semiconductor", "earningsDate": "2025-08-12", "marketCap": "$850B"},
    {"symbol": "LLY", "name": "Eli Lilly and Company", "earningsDate": "2025-08-15", "marketCap": "$750B"},
    {"symbol": "V", "name": "Visa Inc.", "earningsDate": "2025-08-19", "marketCap": "$600B"},
    {"symbol": "JPM", "name": "JPMorgan Chase & Co.", "earningsDate": "2025-08-22", "marketCap": "$580B"},
    {"symbol": "WMT", "name": "Walmart Inc.", "earningsDate": "2025-08-26", "marketCap": "$560B"},
    {"symbol": "MA", "name": "Mastercard Inc.", "earningsDate": "2025-08-29", "marketCap": "$540B"},
    {"symbol": "UNH", "name": "UnitedHealth Group", "earningsDate": "2025-09-02", "marketCap": "$520B"},
    {"symbol": "ORCL", "name": "Oracle Corporation", "earningsDate": "2025-09-05", "marketCap": "$500B"},
    {"symbol": "HD", "name": "The Home Depot", "earningsDate": "2025-09-09", "marketCap": "$480B"},
    {"symbol": "PG", "name": "Procter & Gamble", "earningsDate": "2025-09-12", "marketCap": "$460B"},
    {"symbol": "JNJ", "name": "Johnson & Johnson", "earningsDate": "2025-09-16", "marketCap": "$440B"},
    {"symbol": "COST", "name": "Costco Wholesale", "earningsDate": "2025-09-19", "marketCap": "$420B"}
];

// DOM elements
let currentTab = 'dashboard';

// Initialize the application
document.addEventListener('DOMContentLoaded', function() {
    console.log('DOM loaded, initializing app...');
    initializeApp();
    setupEventListeners();
    updateDashboardMetrics();
    renderEarningsCalendar('week');
    setMinDate();
});

function initializeApp() {
    // Set initial active tab
    showTab('dashboard');
    console.log('App initialized');
}

function setMinDate() {
    // Set minimum date for earnings date to today
    const today = new Date();
    const todayString = today.toISOString().split('T')[0];
    const earningsDateInput = document.getElementById('earningsDate');
    if (earningsDateInput) {
        earningsDateInput.min = todayString;
    }
}

function setupEventListeners() {
    console.log('Setting up event listeners...');
    
    // Tab navigation
    document.querySelectorAll('.nav-tab').forEach(tab => {
        tab.addEventListener('click', function(e) {
            e.preventDefault();
            const tabName = this.getAttribute('data-tab');
            console.log('Tab clicked:', tabName);
            showTab(tabName);
        });
    });

    // Calculate button
    const calculateBtn = document.getElementById('calculateBtn');
    if (calculateBtn) {
        calculateBtn.addEventListener('click', function(e) {
            e.preventDefault();
            console.log('Calculate button clicked');
            calculateStrategy();
        });
    }

    // Save strategy button
    const saveStrategyBtn = document.getElementById('saveStrategyBtn');
    if (saveStrategyBtn) {
        saveStrategyBtn.addEventListener('click', function(e) {
            e.preventDefault();
            console.log('Save strategy button clicked');
            saveStrategy();
        });
    }

    // Filter buttons for earnings calendar
    document.querySelectorAll('.filter-btn').forEach(btn => {
        btn.addEventListener('click', function(e) {
            e.preventDefault();
            document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
            this.classList.add('active');
            const filter = this.getAttribute('data-filter');
            renderEarningsCalendar(filter);
        });
    });

    // Clear error messages on input
    ['stockSymbol', 'earningsDate', 'strikePrice', 'callPremium', 'putPremium'].forEach(fieldId => {
        const field = document.getElementById(fieldId);
        if (field) {
            field.addEventListener('input', function() {
                clearFieldError(fieldId);
            });
        }
    });
}

function showTab(tabName) {
    console.log('Showing tab:', tabName);
    
    // Hide all tab content
    document.querySelectorAll('.tab-content').forEach(content => {
        content.classList.remove('active');
    });

    // Remove active class from all tabs
    document.querySelectorAll('.nav-tab').forEach(tab => {
        tab.classList.remove('active');
    });

    // Show selected tab content
    const tabContent = document.getElementById(tabName);
    if (tabContent) {
        tabContent.classList.add('active');
    }

    // Add active class to selected tab
    const activeTab = document.querySelector(`[data-tab="${tabName}"]`);
    if (activeTab) {
        activeTab.classList.add('active');
    }

    currentTab = tabName;

    // Update content based on tab
    if (tabName === 'strategies') {
        renderSavedStrategies();
    }
}

function clearErrorMessages() {
    const errorElements = document.querySelectorAll('.error-message');
    errorElements.forEach(element => {
        element.textContent = '';
    });
}

function clearFieldError(fieldId) {
    const errorElement = document.getElementById(`${fieldId}-error`);
    if (errorElement) {
        errorElement.textContent = '';
    }
}

function showError(fieldId, message) {
    const errorElement = document.getElementById(`${fieldId}-error`);
    if (errorElement) {
        errorElement.textContent = message;
        console.log(`Error for ${fieldId}: ${message}`);
    }
}

function validateForm() {
    console.log('Validating form...');
    clearErrorMessages();
    let isValid = true;

    // Get form elements
    const stockSymbolEl = document.getElementById('stockSymbol');
    const earningsDateEl = document.getElementById('earningsDate');
    const strikePriceEl = document.getElementById('strikePrice');
    const callPremiumEl = document.getElementById('callPremium');
    const putPremiumEl = document.getElementById('putPremium');

    // Get form values with null checks
    const stockSymbol = stockSymbolEl ? stockSymbolEl.value.trim() : '';
    const earningsDate = earningsDateEl ? earningsDateEl.value.trim() : '';
    const strikePrice = strikePriceEl ? strikePriceEl.value.trim() : '';
    const callPremium = callPremiumEl ? callPremiumEl.value.trim() : '';
    const putPremium = putPremiumEl ? putPremiumEl.value.trim() : '';

    console.log('Form values:', { stockSymbol, earningsDate, strikePrice, callPremium, putPremium });

    // Validate Stock Symbol
    if (!stockSymbol) {
        showError('stockSymbol', 'Stock symbol is required');
        isValid = false;
    } else if (stockSymbol.length < 1 || stockSymbol.length > 10) {
        showError('stockSymbol', 'Stock symbol must be 1-10 characters');
        isValid = false;
    }

    // Validate Earnings Date
    if (!earningsDate) {
        showError('earningsDate', 'Earnings date is required');
        isValid = false;
    } else {
        const selectedDate = new Date(earningsDate);
        const today = new Date();
        today.setHours(0, 0, 0, 0);
        
        if (isNaN(selectedDate.getTime())) {
            showError('earningsDate', 'Please enter a valid date');
            isValid = false;
        } else if (selectedDate < today) {
            showError('earningsDate', 'Earnings date must be today or in the future');
            isValid = false;
        }
    }

    // Validate Strike Price
    if (!strikePrice) {
        showError('strikePrice', 'Strike price is required');
        isValid = false;
    } else {
        const strikePriceNum = parseFloat(strikePrice);
        if (isNaN(strikePriceNum) || strikePriceNum <= 0) {
            showError('strikePrice', 'Strike price must be a positive number');
            isValid = false;
        } else if (strikePriceNum > 10000) {
            showError('strikePrice', 'Strike price seems too high (max: $10,000)');
            isValid = false;
        }
    }

    // Validate Call Premium
    if (!callPremium) {
        showError('callPremium', 'Call premium is required');
        isValid = false;
    } else {
        const callPremiumNum = parseFloat(callPremium);
        if (isNaN(callPremiumNum) || callPremiumNum <= 0) {
            showError('callPremium', 'Call premium must be a positive number');
            isValid = false;
        } else if (callPremiumNum > 1000) {
            showError('callPremium', 'Call premium seems too high (max: $1,000)');
            isValid = false;
        }
    }

    // Validate Put Premium
    if (!putPremium) {
        showError('putPremium', 'Put premium is required');
        isValid = false;
    } else {
        const putPremiumNum = parseFloat(putPremium);
        if (isNaN(putPremiumNum) || putPremiumNum <= 0) {
            showError('putPremium', 'Put premium must be a positive number');
            isValid = false;
        } else if (putPremiumNum > 1000) {
            showError('putPremium', 'Put premium seems too high (max: $1,000)');
            isValid = false;
        }
    }

    console.log('Form validation result:', isValid);
    return isValid;
}

function calculateStrategy() {
    console.log('Calculate strategy called');
    
    if (!validateForm()) {
        console.log('Form validation failed');
        return;
    }

    console.log('Form validation passed, calculating...');

    // Get validated values
    const strikePrice = parseFloat(document.getElementById('strikePrice').value);
    const callPremium = parseFloat(document.getElementById('callPremium').value);
    const putPremium = parseFloat(document.getElementById('putPremium').value);

    console.log('Calculation inputs:', { strikePrice, callPremium, putPremium });

    // Calculate straddle metrics
    const totalPremium = callPremium + putPremium;
    const maxLoss = -totalPremium;
    const upperBreakeven = strikePrice + totalPremium;
    const lowerBreakeven = strikePrice - totalPremium;

    console.log('Calculation results:', { totalPremium, maxLoss, upperBreakeven, lowerBreakeven });

    // Display results
    const maxLossEl = document.getElementById('maxLoss');
    const maxGainEl = document.getElementById('maxGain');
    const upperBreakevenEl = document.getElementById('upperBreakeven');
    const lowerBreakevenEl = document.getElementById('lowerBreakeven');

    if (maxLossEl) maxLossEl.textContent = `$${maxLoss.toFixed(2)}`;
    if (maxGainEl) maxGainEl.textContent = 'Unlimited';
    if (upperBreakevenEl) upperBreakevenEl.textContent = `$${upperBreakeven.toFixed(2)}`;
    if (lowerBreakevenEl) lowerBreakevenEl.textContent = `$${lowerBreakeven.toFixed(2)}`;

    // Show results section
    const resultsSection = document.getElementById('resultsSection');
    if (resultsSection) {
        resultsSection.classList.remove('hidden');
        console.log('Results section shown');
    }
}

function saveStrategy() {
    console.log('Save strategy called');
    
    const stockSymbol = document.getElementById('stockSymbol').value.trim().toUpperCase();
    const earningsDate = document.getElementById('earningsDate').value;
    const strikePrice = parseFloat(document.getElementById('strikePrice').value);
    const callPremium = parseFloat(document.getElementById('callPremium').value);
    const putPremium = parseFloat(document.getElementById('putPremium').value);
    const notes = document.getElementById('notes').value.trim();

    const totalPremium = callPremium + putPremium;
    const maxLoss = -totalPremium;
    const upperBreakeven = strikePrice + totalPremium;
    const lowerBreakeven = strikePrice - totalPremium;

    const strategy = {
        id: Date.now(),
        stockSymbol,
        earningsDate,
        strikePrice,
        callPremium,
        putPremium,
        totalPremium,
        maxLoss,
        upperBreakeven,
        lowerBreakeven,
        notes,
        createdAt: new Date().toISOString()
    };

    savedStrategies.push(strategy);
    console.log('Strategy saved:', strategy);
    
    // Clear form
    const form = document.getElementById('straddleForm');
    if (form) {
        form.reset();
    }
    
    // Hide results section
    const resultsSection = document.getElementById('resultsSection');
    if (resultsSection) {
        resultsSection.classList.add('hidden');
    }
    
    // Clear any error messages
    clearErrorMessages();
    
    // Update dashboard metrics
    updateDashboardMetrics();
    
    // Show success message
    alert('Strategy saved successfully!');
    
    // Switch to strategies tab
    showTab('strategies');
}

function renderSavedStrategies() {
    const container = document.getElementById('strategiesTable');
    if (!container) return;
    
    if (savedStrategies.length === 0) {
        container.innerHTML = `
            <div class="empty-state">
                <p>No saved strategies yet. Create your first strategy using the Straddle Calculator.</p>
            </div>
        `;
        return;
    }

    const tableHTML = `
        <table>
            <thead>
                <tr>
                    <th>Symbol</th>
                    <th>Earnings Date</th>
                    <th>Strike Price</th>
                    <th>Total Premium</th>
                    <th>Max Loss</th>
                    <th>Breakeven Range</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody>
                ${savedStrategies.map(strategy => `
                    <tr>
                        <td><strong>${strategy.stockSymbol}</strong></td>
                        <td>${formatDate(strategy.earningsDate)}</td>
                        <td>$${strategy.strikePrice.toFixed(2)}</td>
                        <td>$${strategy.totalPremium.toFixed(2)}</td>
                        <td class="loss">$${strategy.maxLoss.toFixed(2)}</td>
                        <td>$${strategy.lowerBreakeven.toFixed(2)} - $${strategy.upperBreakeven.toFixed(2)}</td>
                        <td>
                            <button class="btn btn--secondary btn--sm" onclick="deleteStrategy(${strategy.id})">Delete</button>
                        </td>
                    </tr>
                `).join('')}
            </tbody>
        </table>
    `;

    container.innerHTML = tableHTML;
}

function deleteStrategy(id) {
    savedStrategies = savedStrategies.filter(strategy => strategy.id !== id);
    renderSavedStrategies();
    updateDashboardMetrics();
}

function updateDashboardMetrics() {
    const totalStrategies = savedStrategies.length;
    const activeStrategies = savedStrategies.filter(strategy => new Date(strategy.earningsDate) > new Date()).length;
    const totalPremiumAtRisk = savedStrategies.reduce((sum, strategy) => sum + Math.abs(strategy.maxLoss), 0);

    const metricValues = document.querySelectorAll('.metric-value');
    if (metricValues[0]) metricValues[0].textContent = totalStrategies;
    if (metricValues[1]) metricValues[1].textContent = activeStrategies;
    if (metricValues[2]) metricValues[2].textContent = `$${totalPremiumAtRisk.toFixed(2)}`;
}

function renderEarningsCalendar(filter) {
    const container = document.getElementById('earningsTable');
    if (!container) return;
    
    const currentDate = new Date();
    
    let filteredCompanies = [];
    
    switch(filter) {
        case 'week':
            const nextWeek = new Date(currentDate.getTime() + 7 * 24 * 60 * 60 * 1000);
            filteredCompanies = companiesData.filter(company => {
                const earningsDate = new Date(company.earningsDate);
                return earningsDate >= currentDate && earningsDate <= nextWeek;
            });
            break;
        case 'month':
            const nextMonth = new Date(currentDate.getFullYear(), currentDate.getMonth() + 1, currentDate.getDate());
            filteredCompanies = companiesData.filter(company => {
                const earningsDate = new Date(company.earningsDate);
                return earningsDate >= currentDate && earningsDate <= nextMonth;
            });
            break;
        case 'quarter':
            const nextQuarter = new Date(currentDate.getFullYear(), currentDate.getMonth() + 3, currentDate.getDate());
            filteredCompanies = companiesData.filter(company => {
                const earningsDate = new Date(company.earningsDate);
                return earningsDate >= currentDate && earningsDate <= nextQuarter;
            });
            break;
    }

    // Sort by earnings date
    filteredCompanies.sort((a, b) => new Date(a.earningsDate) - new Date(b.earningsDate));

    if (filteredCompanies.length === 0) {
        container.innerHTML = `
            <div class="empty-state">
                <p>No earnings found for the selected period.</p>
            </div>
        `;
        return;
    }

    const tableHTML = `
        <table>
            <thead>
                <tr>
                    <th>Company</th>
                    <th>Symbol</th>
                    <th>Earnings Date</th>
                    <th>Market Cap</th>
                </tr>
            </thead>
            <tbody>
                ${filteredCompanies.map(company => `
                    <tr>
                        <td><strong>${company.name}</strong></td>
                        <td>${company.symbol}</td>
                        <td>${formatDate(company.earningsDate)}</td>
                        <td>${company.marketCap}</td>
                    </tr>
                `).join('')}
            </tbody>
        </table>
    `;

    container.innerHTML = tableHTML;
}

function formatDate(dateString) {
    const date = new Date(dateString);
    return date.toLocaleDateString('en-US', { 
        year: 'numeric', 
        month: 'short', 
        day: 'numeric' 
    });
}
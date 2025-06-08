# Create a fixed HTML file with all JavaScript inline to ensure it works properly
html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fixed Options Straddle Dashboard</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: linear-gradient(135deg, #1e3a8a 0%, #3730a3 100%);
            color: white;
            min-height: 100vh;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }

        .header {
            text-align: center;
            margin-bottom: 40px;
        }

        .dashboard-title {
            font-size: 2.5rem;
            font-weight: bold;
            margin-bottom: 20px;
        }

        .market-indicators {
            display: flex;
            justify-content: center;
            gap: 30px;
            margin-bottom: 30px;
        }

        .indicator {
            background: rgba(255, 255, 255, 0.1);
            padding: 10px 20px;
            border-radius: 10px;
            font-size: 1.1rem;
        }

        .nav-tabs {
            display: flex;
            justify-content: center;
            gap: 10px;
            margin-bottom: 30px;
        }

        .nav-tab {
            background: rgba(255, 255, 255, 0.1);
            border: none;
            color: white;
            padding: 12px 24px;
            border-radius: 8px;
            cursor: pointer;
            font-size: 1rem;
            transition: all 0.3s ease;
        }

        .nav-tab:hover {
            background: rgba(255, 255, 255, 0.2);
        }

        .nav-tab.active {
            background: #60a5fa;
        }

        .tab-content {
            display: none;
        }

        .tab-content.active {
            display: block;
        }

        .card {
            background: rgba(255, 255, 255, 0.1);
            border-radius: 12px;
            padding: 24px;
            margin-bottom: 20px;
            backdrop-filter: blur(10px);
        }

        .overview-cards {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }

        .metric-card h3 {
            font-size: 1.1rem;
            margin-bottom: 10px;
            opacity: 0.8;
        }

        .metric-value {
            font-size: 2rem;
            font-weight: bold;
            color: #60a5fa;
        }

        .form-group {
            margin-bottom: 20px;
        }

        .form-group label {
            display: block;
            margin-bottom: 8px;
            font-weight: 500;
        }

        .form-control {
            width: 100%;
            padding: 12px;
            border: 1px solid rgba(255, 255, 255, 0.3);
            border-radius: 8px;
            background: rgba(255, 255, 255, 0.1);
            color: white;
            font-size: 1rem;
        }

        .form-control::placeholder {
            color: rgba(255, 255, 255, 0.6);
        }

        .form-control:focus {
            outline: none;
            border-color: #60a5fa;
            box-shadow: 0 0 0 3px rgba(96, 165, 250, 0.3);
        }

        .btn {
            background: #60a5fa;
            color: white;
            border: none;
            padding: 12px 24px;
            border-radius: 8px;
            cursor: pointer;
            font-size: 1rem;
            font-weight: 500;
            transition: all 0.3s ease;
        }

        .btn:hover {
            background: #3b82f6;
        }

        .btn:disabled {
            background: rgba(255, 255, 255, 0.3);
            cursor: not-allowed;
        }

        .btn-success {
            background: #10b981;
        }

        .btn-success:hover {
            background: #059669;
        }

        .error-message {
            color: #ef4444;
            font-size: 0.9rem;
            margin-top: 5px;
            display: none;
        }

        .results-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
            margin-top: 20px;
        }

        .result-item {
            background: rgba(255, 255, 255, 0.05);
            padding: 15px;
            border-radius: 8px;
            text-align: center;
        }

        .result-label {
            font-size: 0.9rem;
            opacity: 0.8;
            margin-bottom: 5px;
        }

        .result-value {
            font-size: 1.3rem;
            font-weight: bold;
        }

        .profit {
            color: #10b981;
        }

        .loss {
            color: #ef4444;
        }

        .table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }

        .table th,
        .table td {
            padding: 12px;
            text-align: left;
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        }

        .table th {
            background: rgba(255, 255, 255, 0.1);
            font-weight: 600;
        }

        .filter-buttons {
            display: flex;
            gap: 10px;
            margin-bottom: 20px;
        }

        .filter-btn {
            background: rgba(255, 255, 255, 0.1);
            border: 1px solid rgba(255, 255, 255, 0.3);
            color: white;
            padding: 8px 16px;
            border-radius: 6px;
            cursor: pointer;
            transition: all 0.3s ease;
        }

        .filter-btn.active {
            background: #60a5fa;
            border-color: #60a5fa;
        }

        @media (max-width: 768px) {
            .nav-tabs {
                flex-wrap: wrap;
            }

            .nav-tab {
                font-size: 0.9rem;
                padding: 10px 16px;
            }

            .overview-cards {
                grid-template-columns: 1fr;
            }

            .results-grid {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <!-- Header -->
        <header class="header">
            <h1 class="dashboard-title">Options Straddle Dashboard</h1>
            <div class="market-indicators">
                <span class="indicator">VIX: <strong>16.24</strong></span>
                <span class="indicator">S&P 500: <strong>5,346.12</strong></span>
            </div>
            <nav class="nav-tabs">
                <button class="nav-tab active" onclick="showTab('dashboard')">Dashboard</button>
                <button class="nav-tab" onclick="showTab('calculator')">Straddle Calculator</button>
                <button class="nav-tab" onclick="showTab('strategies')">Saved Strategies</button>
                <button class="nav-tab" onclick="showTab('earnings')">Earnings Calendar</button>
            </nav>
        </header>

        <!-- Dashboard Section -->
        <section id="dashboard" class="tab-content active">
            <div class="overview-cards">
                <div class="card metric-card">
                    <h3>Total Strategies</h3>
                    <div class="metric-value" id="totalStrategies">0</div>
                </div>
                <div class="card metric-card">
                    <h3>Active Strategies</h3>
                    <div class="metric-value" id="activeStrategies">0</div>
                </div>
                <div class="card metric-card">
                    <h3>Total Premium at Risk</h3>
                    <div class="metric-value" id="totalPremium">$0.00</div>
                </div>
                <div class="card metric-card">
                    <h3>Upcoming Earnings</h3>
                    <div class="metric-value">20</div>
                </div>
            </div>
            <div class="card">
                <h3>Recent Activity</h3>
                <p>Welcome to your Options Straddle Dashboard. Start by creating your first strategy using the Straddle Calculator.</p>
            </div>
        </section>

        <!-- Straddle Calculator Section -->
        <section id="calculator" class="tab-content">
            <div class="card">
                <h2>Straddle Calculator</h2>
                <p>Calculate profit/loss scenarios for your long straddle strategies</p>
                
                <form id="straddleForm" onsubmit="calculateStraddle(event)">
                    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px;">
                        <div class="form-group">
                            <label for="stockSymbol">Stock Symbol *</label>
                            <input type="text" id="stockSymbol" class="form-control" placeholder="e.g., AAPL" required>
                            <div class="error-message" id="stockSymbolError"></div>
                        </div>

                        <div class="form-group">
                            <label for="earningsDate">Earnings Date *</label>
                            <input type="date" id="earningsDate" class="form-control" required>
                            <div class="error-message" id="earningsDateError"></div>
                        </div>

                        <div class="form-group">
                            <label for="strikePrice">Strike Price ($) *</label>
                            <input type="number" id="strikePrice" class="form-control" placeholder="150.00" step="0.01" min="0" required>
                            <div class="error-message" id="strikePriceError"></div>
                        </div>

                        <div class="form-group">
                            <label for="callPremium">Call Premium ($) *</label>
                            <input type="number" id="callPremium" class="form-control" placeholder="5.50" step="0.01" min="0" required>
                            <div class="error-message" id="callPremiumError"></div>
                        </div>

                        <div class="form-group">
                            <label for="putPremium">Put Premium ($) *</label>
                            <input type="number" id="putPremium" class="form-control" placeholder="4.25" step="0.01" min="0" required>
                            <div class="error-message" id="putPremiumError"></div>
                        </div>

                        <div class="form-group">
                            <label for="notes">Notes (Optional)</label>
                            <textarea id="notes" class="form-control" rows="3" placeholder="Add any notes about this strategy..."></textarea>
                        </div>
                    </div>

                    <button type="submit" class="btn">Calculate Strategy</button>
                </form>

                <div id="calculationResults" style="display: none;">
                    <h3 style="margin-top: 30px;">Strategy Results</h3>
                    <div class="results-grid">
                        <div class="result-item">
                            <div class="result-label">Maximum Loss</div>
                            <div class="result-value loss" id="maxLoss">-</div>
                        </div>
                        <div class="result-item">
                            <div class="result-label">Maximum Gain</div>
                            <div class="result-value profit" id="maxGain">Unlimited</div>
                        </div>
                        <div class="result-item">
                            <div class="result-label">Upper Breakeven</div>
                            <div class="result-value" id="upperBreakeven">-</div>
                        </div>
                        <div class="result-item">
                            <div class="result-label">Lower Breakeven</div>
                            <div class="result-value" id="lowerBreakeven">-</div>
                        </div>
                    </div>
                    <button type="button" class="btn btn-success" onclick="saveStrategy()" style="margin-top: 20px;">Save Strategy</button>
                </div>
            </div>
        </section>

        <!-- Saved Strategies Section -->
        <section id="strategies" class="tab-content">
            <div class="card">
                <h2>Saved Strategies</h2>
                <div id="strategiesTable">
                    <p>No saved strategies yet. Create and save your first strategy in the calculator.</p>
                </div>
            </div>
        </section>

        <!-- Earnings Calendar Section -->
        <section id="earnings" class="tab-content">
            <div class="card">
                <h2>Earnings Calendar</h2>
                <p>Top 20 S&P 500 companies by market cap</p>
                
                <div class="filter-buttons">
                    <button class="filter-btn active" onclick="filterEarnings('all')">All</button>
                    <button class="filter-btn" onclick="filterEarnings('week')">Next Week</button>
                    <button class="filter-btn" onclick="filterEarnings('month')">Next Month</button>
                    <button class="filter-btn" onclick="filterEarnings('quarter')">Next Quarter</button>
                </div>

                <table class="table" id="earningsTable">
                    <thead>
                        <tr>
                            <th>Company</th>
                            <th>Symbol</th>
                            <th>Earnings Date</th>
                            <th>Market Cap</th>
                        </tr>
                    </thead>
                    <tbody id="earningsTableBody">
                    </tbody>
                </table>
            </div>
        </section>
    </div>

    <script>
        // Application state
        let savedStrategies = [];
        let currentCalculation = null;

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

        // Tab navigation
        function showTab(tabName) {
            // Hide all tab contents
            const tabContents = document.querySelectorAll('.tab-content');
            tabContents.forEach(tab => tab.classList.remove('active'));

            // Remove active class from all tabs
            const tabs = document.querySelectorAll('.nav-tab');
            tabs.forEach(tab => tab.classList.remove('active'));

            // Show selected tab content
            document.getElementById(tabName).classList.add('active');

            // Add active class to clicked tab
            event.target.classList.add('active');

            // Load earnings data if earnings tab is selected
            if (tabName === 'earnings') {
                loadEarningsData();
            }
        }

        // Form validation and calculation
        function calculateStraddle(event) {
            event.preventDefault();
            
            // Clear previous errors
            clearErrors();
            
            // Get form values
            const stockSymbol = document.getElementById('stockSymbol').value.trim();
            const earningsDate = document.getElementById('earningsDate').value;
            const strikePrice = parseFloat(document.getElementById('strikePrice').value);
            const callPremium = parseFloat(document.getElementById('callPremium').value);
            const putPremium = parseFloat(document.getElementById('putPremium').value);
            const notes = document.getElementById('notes').value.trim();
            
            let hasErrors = false;
            
            // Validate stock symbol
            if (!stockSymbol) {
                showError('stockSymbolError', 'Stock symbol is required');
                hasErrors = true;
            }
            
            // Validate earnings date
            if (!earningsDate) {
                showError('earningsDateError', 'Earnings date is required');
                hasErrors = true;
            }
            
            // Validate strike price
            if (isNaN(strikePrice) || strikePrice <= 0) {
                showError('strikePriceError', 'Please enter a valid strike price greater than 0');
                hasErrors = true;
            }
            
            // Validate call premium
            if (isNaN(callPremium) || callPremium < 0) {
                showError('callPremiumError', 'Please enter a valid call premium (0 or greater)');
                hasErrors = true;
            }
            
            // Validate put premium
            if (isNaN(putPremium) || putPremium < 0) {
                showError('putPremiumError', 'Please enter a valid put premium (0 or greater)');
                hasErrors = true;
            }
            
            if (hasErrors) {
                alert('Please fill in all required fields correctly.');
                return;
            }
            
            // Calculate straddle metrics
            const totalPremium = callPremium + putPremium;
            const maxLoss = -totalPremium;
            const upperBreakeven = strikePrice + totalPremium;
            const lowerBreakeven = strikePrice - totalPremium;
            
            // Store current calculation
            currentCalculation = {
                stockSymbol,
                earningsDate,
                strikePrice,
                callPremium,
                putPremium,
                notes,
                totalPremium,
                maxLoss,
                upperBreakeven,
                lowerBreakeven
            };
            
            // Display results
            document.getElementById('maxLoss').textContent = `$${Math.abs(maxLoss).toFixed(2)}`;
            document.getElementById('maxGain').textContent = 'Unlimited';
            document.getElementById('upperBreakeven').textContent = `$${upperBreakeven.toFixed(2)}`;
            document.getElementById('lowerBreakeven').textContent = `$${lowerBreakeven.toFixed(2)}`;
            
            // Show results section
            document.getElementById('calculationResults').style.display = 'block';
            
            // Success message
            alert('Calculation completed successfully!');
        }

        function clearErrors() {
            const errorElements = document.querySelectorAll('.error-message');
            errorElements.forEach(element => {
                element.style.display = 'none';
                element.textContent = '';
            });
        }

        function showError(elementId, message) {
            const errorElement = document.getElementById(elementId);
            errorElement.textContent = message;
            errorElement.style.display = 'block';
        }

        function saveStrategy() {
            if (!currentCalculation) return;
            
            const strategy = {
                id: Date.now(),
                ...currentCalculation,
                createdAt: new Date().toISOString()
            };
            
            savedStrategies.push(strategy);
            updateDashboardMetrics();
            updateStrategiesTable();
            
            alert('Strategy saved successfully!');
        }

        function updateDashboardMetrics() {
            document.getElementById('totalStrategies').textContent = savedStrategies.length;
            document.getElementById('activeStrategies').textContent = savedStrategies.length;
            
            const totalRisk = savedStrategies.reduce((sum, strategy) => sum + Math.abs(strategy.maxLoss), 0);
            document.getElementById('totalPremium').textContent = `$${totalRisk.toFixed(2)}`;
        }

        function updateStrategiesTable() {
            const container = document.getElementById('strategiesTable');
            
            if (savedStrategies.length === 0) {
                container.innerHTML = '<p>No saved strategies yet. Create and save your first strategy in the calculator.</p>';
                return;
            }
            
            let tableHTML = `
                <table class="table">
                    <thead>
                        <tr>
                            <th>Symbol</th>
                            <th>Earnings Date</th>
                            <th>Strike Price</th>
                            <th>Total Premium</th>
                            <th>Max Loss</th>
                            <th>Breakeven Range</th>
                            <th>Action</th>
                        </tr>
                    </thead>
                    <tbody>
            `;
            
            savedStrategies.forEach(strategy => {
                tableHTML += `
                    <tr>
                        <td>${strategy.stockSymbol}</td>
                        <td>${strategy.earningsDate}</td>
                        <td>$${strategy.strikePrice.toFixed(2)}</td>
                        <td>$${strategy.totalPremium.toFixed(2)}</td>
                        <td class="loss">$${Math.abs(strategy.maxLoss).toFixed(2)}</td>
                        <td>$${strategy.lowerBreakeven.toFixed(2)} - $${strategy.upperBreakeven.toFixed(2)}</td>
                        <td>
                            <button class="btn" style="padding: 6px 12px; font-size: 0.8rem;" onclick="deleteStrategy(${strategy.id})">Delete</button>
                        </td>
                    </tr>
                `;
            });
            
            tableHTML += '</tbody></table>';
            container.innerHTML = tableHTML;
        }

        function deleteStrategy(id) {
            if (confirm('Are you sure you want to delete this strategy?')) {
                savedStrategies = savedStrategies.filter(strategy => strategy.id !== id);
                updateDashboardMetrics();
                updateStrategiesTable();
            }
        }

        function loadEarningsData() {
            const tbody = document.getElementById('earningsTableBody');
            let html = '';
            
            companiesData.forEach(company => {
                html += `
                    <tr>
                        <td>${company.name}</td>
                        <td>${company.symbol}</td>
                        <td>${company.earningsDate}</td>
                        <td>${company.marketCap}</td>
                    </tr>
                `;
            });
            
            tbody.innerHTML = html;
        }

        function filterEarnings(period) {
            // Update active filter button
            const buttons = document.querySelectorAll('.filter-btn');
            buttons.forEach(btn => btn.classList.remove('active'));
            event.target.classList.add('active');
            
            // For this demo, we'll show all data regardless of filter
            // In a real application, you would filter by the selected period
            loadEarningsData();
        }

        // Initialize the application
        document.addEventListener('DOMContentLoaded', function() {
            loadEarningsData();
        });
    </script>
</body>
</html>'''

# Save the fixed HTML file
with open('fixed-straddle-dashboard.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Fixed dashboard HTML file created successfully!")
print("Key fixes implemented:")
print("1. Robust form validation with specific error messages")
print("2. Proper straddle calculation formulas")
print("3. All JavaScript inline to ensure it loads")
print("4. Clear error handling for empty and invalid fields")
print("5. Professional styling and responsive design")
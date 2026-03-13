-- CREATE TABLE telco_churn (
--     customer_id VARCHAR(20),
--     count INTEGER,
--     country VARCHAR(50),
--     state VARCHAR(50),
--     city VARCHAR(100),
--     zip_code INTEGER,
--     lat_long VARCHAR(50),
--     latitude DECIMAL(10,6),
--     longitude DECIMAL(10,6),
--     gender VARCHAR(10),
--     senior_citizen VARCHAR(5),
--     partner VARCHAR(5),
--     dependents VARCHAR(5),
--     tenure_months INTEGER,
--     phone_service VARCHAR(5),
--     multiple_lines VARCHAR(20),
--     internet_service VARCHAR(20),
--     online_security VARCHAR(20),
--     online_backup VARCHAR(20),
--     device_protection VARCHAR(20),
--     tech_support VARCHAR(20),
--     streaming_tv VARCHAR(20),
--     streaming_movies VARCHAR(20),
--     contract VARCHAR(20),
--     paperless_billing VARCHAR(5),
--     payment_method VARCHAR(30),
--     monthly_charges DECIMAL(10,2),
--     total_charges DECIMAL(10,2),
--     churn_label VARCHAR(5),
--     churn_value INTEGER,
--     churn_score INTEGER,
--     cltv INTEGER,
--     churn_reason VARCHAR(100)
-- );

--SELECT COUNT(*) FROM telco_churn;
--SELECT * FROM telco_churn LIMIT 5;

--Query 1 — Overall Churn Rate:
-- SELECT 
--     churn_label,
--     COUNT(*) AS customer_count,
--     ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(), 2) AS churn_rate_pct
-- FROM telco_churn
-- GROUP BY churn_label;

--Query 2 — Churn by Contract Type:
-- SELECT 
--     contract,
--     COUNT(*) AS total_customers,
--     SUM(CASE WHEN churn_label = 'Yes' THEN 1 ELSE 0 END) AS churned,
--     ROUND(SUM(CASE WHEN churn_label = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS churn_rate_pct
-- FROM telco_churn
-- GROUP BY contract
-- ORDER BY churn_rate_pct DESC;

--Query 3 — Revenue Lost to Churn:
-- SELECT 
--     churn_label,
--     ROUND(SUM(monthly_charges)::numeric, 2) AS total_monthly_revenue,
--     ROUND(AVG(monthly_charges)::numeric, 2) AS avg_monthly_charges,
--     COUNT(*) AS customers
-- FROM telco_churn
-- GROUP BY churn_label;

--Query 4 — Churn by Tenure Group:
-- SELECT 
--     CASE 
--         WHEN tenure_months <= 12 THEN '0-12 Months'
--         WHEN tenure_months <= 24 THEN '13-24 Months'
--         WHEN tenure_months <= 48 THEN '25-48 Months'
--         ELSE '49+ Months'
--     END AS tenure_group,
--     COUNT(*) AS total_customers,
--     SUM(CASE WHEN churn_label = 'Yes' THEN 1 ELSE 0 END) AS churned,
--     ROUND(SUM(CASE WHEN churn_label = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS churn_rate_pct
-- FROM telco_churn
-- GROUP BY tenure_group
-- ORDER BY churn_rate_pct DESC;

--Query 5 — Top Churn Reasons:
-- SELECT 
--     churn_reason,
--     COUNT(*) AS frequency,
--     ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(), 2) AS pct_of_churned
-- FROM telco_churn
-- WHERE churn_label = 'Yes'
-- GROUP BY churn_reason
-- ORDER BY frequency DESC
-- LIMIT 10;

--Query 6 — Churn by Internet Service:
SELECT 
    internet_service,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN churn_label = 'Yes' THEN 1 ELSE 0 END) AS churned,
    ROUND(SUM(CASE WHEN churn_label = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS churn_rate_pct
FROM telco_churn
GROUP BY internet_service
ORDER BY churn_rate_pct DESC;
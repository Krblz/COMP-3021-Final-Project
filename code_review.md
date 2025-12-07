# Code review for security vulnerabilities

## Vulnerabilities found

### 1. Hardcoded API Key (Line 7)
**Location:** Line 7
**Issue:** API keys should never be hardcoded in source code.

**Recommendation:** Store API keys in environment variables such as a `.env` file.

**OWASP Category:** A07:2021 – Identification and Authentication Failures

### 2. No Authentication/Authorization (Lines 40-50)
**Location:** Lines 40-50 (get_account_number, get_balance functions)
**Issue:** There is no authentication/authorization. Anyone can access any account and gain access to sensitive personal data. 

**Recommendation:** Implement user authentication such as what we did with Firebase and verify users can only access accounts they own (same user access)

**OWASP Category:** A01:2021 – Broken Access Control

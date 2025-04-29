# 🧪 HPE CodeGen – Developer Capability Testing

This repository contains a practical test suite to evaluate the capabilities of **HPE CodeGen** as a real-world AI development assistant.

---

## 🎯 Objective

Assess HPE CodeGen across:

- ✅ Code generation
- ✅ Concept explanation
- ✅ Code understanding & annotation
- ✅ Modernizing legacy code
- ✅ Responsive design conversion
- ✅ Language-to-language migration

---

## ✅ 1. Prime Number Generator

**Prompt:**
```python
Generate a Python function to find all prime numbers between 1 and 100.
```

**Expected Outcome:**
- Efficient prime-checking logic
- Clean, readable Python code

---

## ✅ 2. Concept Explanation Across Languages

**Prompt:**
```text
Explain how a 'for' loop works in Python, JavaScript, and Java. Provide example code snippets.
```

**Expected Outcome:**
- Syntax and logic explanation for each language
- Realistic code examples

---

## ✅ 3. Portfolio Website with Bootstrap

**Prompt:**
```html
Generate code for a single-page portfolio website using Bootstrap 5.
Include:
- Hero section (name, title, CTA)
- About section
- Projects section (4–6 cards)
- Skills grid
- Contact form
- Footer with social links
Make it responsive, clean, and semantic.
```

**Expected Outcome:**
- Mobile-friendly layout
- Bootstrap 5 grid usage
- Semantic HTML sections

---

## ✅ 4. Python Code Summarization & Annotation

**File:** [`user_auth_system.py`](./user_auth_system.py)

**What it contains:**
- User registration and login functions
- Secure password hashing using hashlib + uuid

**Prompts:**
```python
Summarize the uploaded file.

Extract and explain the 'register_user' function line-by-line.

Annotate the function with detailed comments.
```

**Expected Outcome:**
- Logical summarization
- Accurate and readable annotation

---

## ✅ 5. Modernize Outdated JavaScript

**File:** [`legacy_file_processor.js`](./legacy_file_processor.js)

**What it contains:**
- Node.js file operations
- var-based declarations and nested callbacks

**Prompts:**
```javascript
Summarize the uploaded file.

Modernize it using let/const, arrow functions, async/await.

Convert it to TypeScript.
```

**Expected Outcome:**
- Refactored ES6+ syntax
- TypeScript version with proper annotations

---

## ✅ 6. Solve a Leetcode Problem

**Prompt:**
```python
Problem: Two Sum
Input: nums = [2,7,11,15], target = 9
Output: [0,1]

Solve this in Python.
```

**Expected Outcome:**
- Optimal O(n) solution
- Handles edge cases

---

## ✅ 7. Make Website Responsive

**File:** [`desktop_only_site.zip`](./desktop_only_site.zip)

**Prompt:**
```html
Convert the uploaded static website to a responsive layout using Bootstrap 5.
Specifically:
- Replace the fixed-width `.container` (e.g., 960px) with Bootstrap's `container` class.
- Use Bootstrap's grid system (`row`, `col-md-*`, `col-sm-*`) to layout the `.card` elements in a responsive grid.
- On desktop: display cards in 2 columns.
- On mobile: cards should stack vertically with full width.
- Ensure the typography, spacing, and alignment remain clean on all devices.
Output full HTML and CSS using Bootstrap 5. Include responsive meta tags and verify layout changes through media queries or grid classes.
```

**Expected Outcome:**
- Bootstrap layout implementation
- Verified responsiveness in dev tools

---

## ✅ 8. Migrate PHP to Node.js

**File:** [`auth.php`](./auth.php)

**Prompt:**
```js
Migrate this PHP auth system to a Node.js Express REST API.
Use secure password hashing and expose /register and /login routes.
```

**Expected Outcome:**
- Express-based routing
- bcrypt password hashing
- Secure, clean migration

---

## 📁 Repository Contents

| File | Description |
|:--|:--|
| `user_auth_system.py` | Python file for summarization and annotation |
| `legacy_file_processor.js` | Old JavaScript for modernization test |
| `desktop_only_site.zip` | Desktop-only site to convert into responsive |
| `auth.php` | Legacy PHP authentication script for migration |

---

## ✅ Get Started

Upload these files in HPE CodeGen, use the prompts provided, and analyze how well it performs each task.

---

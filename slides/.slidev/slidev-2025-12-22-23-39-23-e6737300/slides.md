---
theme: seriph
background: https://images.unsplash.com/photo-1517694712202-14dd9538aa97?ixlib=rb-1.2.1&auto=format&fit=crop&w=1950&q=80
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## GitHub Copilot Labs
  Hands-on exercises from the Copilot Prompts Workshop.
drawings:
  persist: false
transition: slide-left
title: Copilot Workshop Labs
---

# Copilot Workshop Labs

Hands-on exercises to master AI-Assisted Development

<div class="pt-12">
  <span @click="$slidev.nav.next" class="px-2 py-1 rounded cursor-pointer" hover="bg-white bg-opacity-10">
    Start Labs <carbon:arrow-right class="inline"/>
  </span>
</div>

---
layout: default
---

# Lab Overview

We will cover the following practical exercises:

1.  **Lab 01:** Basic Prompting & Algorithms
2.  **Lab 02:** Web Server Generation
3.  **Lab 03:** Data Manipulation & SQL
4.  **Lab 04:** Unit Testing
5.  **Lab 05:** Refactoring & Legacy Code
6.  **Lab 06:** Using Copilot Chat

---
layout: section
---

# Lab 01: Basic Prompting

---
layout: two-cols
---

# Lab 01: Algorithms

**Goal:** Use comment-driven development to generate algorithmic logic.

### Instructions:
1. Create a file named `algorithms.js`.
2. Type the comment below.
3. Wait for the suggestion (Ghost text).
4. Press `Tab` to accept.

::right::

```javascript
// Lab 01 Step 1
// Create a function that calculates the factorial of a number
// Handle negative numbers by returning null

// Lab 01 Step 2
// Create a function that checks if a string is a palindrome
// Ignore case and non-alphanumeric characters
```

<div class="mt-4 text-sm opacity-75">
  <strong>Tip:</strong> If the suggestion isn't what you want, try pressing <code>Alt + ]</code> (or <code>Option + ]</code> on Mac) to cycle through alternatives.
</div>

---
layout: section
---

# Lab 02: Web Server

---
layout: default
---

# Lab 02: Express Server

**Goal:** Scaffold a complete web server file using a "Top-Down" prompt strategy.

### Instructions:
1. Create a file named `server.js`.
2. Write a detailed block comment at the top of the file describing the requirements.

```javascript
/*
  Create an Express web server on port 3000.
  It should have the following endpoints:
  1. GET /api/users - returns a list of mock users
  2. GET /api/users/:id - returns a specific user
  3. POST /api/users - creates a new user
  4. Middleware to parse JSON bodies
  5. Error handling for 404 routes
*/

const express = require('express');
// Let Copilot generate the rest...
```

---
layout: section
---

# Lab 03: Data & SQL

---
layout: two-cols
---

# Lab 03: SQL Queries

**Goal:** Generate complex SQL without memorizing syntax.

### Instructions:
1. Create `queries.sql`.
2. Define your schema context (or assume a standard schema).
3. Ask for the query in natural language.

::right::

```sql
-- Table: Employees (id, name, department_id, salary, hire_date)
-- Table: Departments (id, name, location)

-- 1. Select the top 3 departments with the highest average salary
-- Include the department name and the average salary rounded to 2 decimals


-- 2. Find employees hired in the last 6 months who earn more than 50000
```

---
layout: default
---

# Lab 03: Data Generation (Bonus)

**Goal:** Generate mock data for testing.

### Instructions:
1. Create a JSON file `data.json` or a variable in JavaScript.
2. Start typing the structure and let Copilot fill the pattern.

```javascript
const products = [
    { id: 1, name: "Laptop", price: 999, category: "Electronics" },
    // Press Enter and wait for Copilot to suggest the next item...
    // It should recognize the pattern and suggest relevant products.
];
```

---
layout: section
---

# Lab 04: Unit Testing

---
layout: default
---

# Lab 04: Generating Tests

**Goal:** Write a test suite for existing code.

### Instructions:
1. Open the `algorithms.js` file from Lab 01.
2. Create a new file `algorithms.test.js`.
3. Import the functions.
4. Use natural language to describe the test cases.

```javascript
const { factorial, isPalindrome } = require('./algorithms');

// Test suite for factorial function
// 1. Should return 120 for input 5
// 2. Should return 1 for input 0
// 3. Should return null for negative numbers
describe('factorial', () => {
    // Let Copilot fill the body
});
```

---
layout: section
---

# Lab 05: Refactoring

---
layout: two-cols
---

# Lab 05: Improving Code

**Goal:** Use Copilot to modernize or clean up code.

### Instructions:
1. Paste the "Legacy Code" into a file.
2. Highlight the code.
3. Open Copilot Chat (`Ctrl+I` or `Cmd+I`).
4. Type `/fix` or "Refactor this to use Arrow Functions and map".

::right::

### Legacy Code Input:

```javascript
function getNames(users) {
  var names = [];
  for (var i = 0; i < users.length; i++) {
    if (users[i].age > 18) {
      names.push(users[i].name);
    }
  }
  return names;
}
```

---
layout: section
---

# Lab 06: Copilot Chat

---
layout: default
---

# Lab 06: Explain & Document

**Goal:** Understand complex code and generate documentation.

### Instructions:
1. Select a complex function or a Regular Expression.
2. Right-click > **Copilot** > **Explain This**.
3. Observe the explanation in the Chat panel.

### Documentation:
1. Highlight a function.
2. Type `/doc` in the Chat input.
3. Copilot will generate JSDoc/DocString comments for the selected code.

---
layout: end
---

# Happy Coding!

Continue exploring the labs in the repository.

[Workshop Repository](https://github.com/nirgeier/Copilot-Prompts-Workshop)
```
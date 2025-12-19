# Lab 11 - Reusable Prompts Hands-On

### Exercise 1: Create the Directory Structure

1.  Open your terminal.
2.  Create the directory `.github/prompts`.

### Exercise 2: Create a "Code Review" Prompt

1.  Create a file named `.github/prompts/review.prompt.md`.
2.  Add the following content:

    ```markdown
    You are a strict code reviewer.
    Review the selected code for:
    1. Security vulnerabilities.
    2. Performance bottlenecks.
    3. Adherence to PEP 8 (Python) standards.
    
    Provide your feedback in a markdown table with columns:
    - Severity (High/Medium/Low)
    - Issue
    - Suggestion
    ```

### Exercise 3: Use the Prompt

1.  Open `calculator/calculator.py`.
2.  Select the `divide` function.
3.  Open Copilot Chat.
4.  Type `#review` (or the name of your file) and press Enter.
    *   *Note: If `#review` doesn't auto-complete, you can manually attach the file using the paperclip icon or by typing `#file:.github/prompts/review.prompt.md`.*
5.  Observe the structured output.

# Lab 04 - Chat Hands-On

## Steps to Use Chat
### 01. Open Chat:
* You can open the Chat panel in several ways:
    * Press `Cmd+Shift+C` (macOS) or `Ctrl+Shift+C` (Windows/Linux).
    * Use the Icon from the `Github Copilot` top icon.
    * Right-click in the editor and select `GitHub Copilot: Open Chat`. 
* Once the Chat panel is open, you can type your requests in the input box at the bottom.

### 02. Use Chat

* In this task, we will use Chat to generate a `main.py` file that tests all functions in our `calculator.py` file.
* In the Chat input box, write the following prompt:
    
    ```
    1. Generate a main.py file that tests all functions in calculator.py
    2. Explain how to use the add function in calculator.py
    3. Print out instructions on how to run the tests
    ```

### 03. Adding tests

* In the chat windows, Choose the `Agent Mode`
* Open the `calculator/calculator.py` file or add it as context to the chat.
* Type the following prompt:
    ```
    1. Add square and root functions to the calculator.py file
    2. Add tests for power and square root functions in main.py
    3. Ensure the square root function handles negative inputs by raising a ValueError
    4. Print out instructions on how to run the tests
    
    ```

# Lab 12 - Custom Agents Hands-On

* In this lab we will design the **System Prompt** and **Metadata** for a custom agent you might want to build.

### Exercise 1: Define the Metadata

1.  Create a file `my-agent-metadata.json`.
2.  Define the `chatParticipants` contribution.
    *   **Name**: What will users type? (e.g., `@doc-writer`)
    *   **Description**: What does it do?
    *   **Commands**: Does it have sub-commands? (e.g., `/explain`, `/fix`)

### Exercise 2: Craft the System Prompt

1.  Create a file `my-agent-prompt.md`.
2.  Write the instructions that define your agent's behavior.
    *   **Role**: Who is the agent?
    *   **Tone**: Professional, funny, concise?
    *   **Constraints**: What should it *not* do?
    *   **Context**: What does it need to know about the user's code?

### Exercise 3: Simulation

1.  Open the Chat view.
2.  Paste your **System Prompt** from Exercise 2.
3.  Then, act as the user and ask a question.
4.  See if Copilot (simulating your agent) behaves as expected.

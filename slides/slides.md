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
    Lets Start<carbon:arrow-right class="inline"/>
  </span>
</div>

---

# Table of Contents

1. Suggestions Inline  
2. Inline Chat  
3. Chat  
4. Builtin Prompts  
5. Plan Mode  
6. Agent Mode  
7. Custom Instructions  
8. Advanced Instructions  
9. Reusable Prompts  
10. Custom Agents & Chat Extensions  
11. Custom Prompts  
12. Prompt Engineering  
13. Finalization

---

# Suggestions Inline

Copilot provides real-time code suggestions as you type.

- Context-aware suggestions based on your code
- Supports 40+ programming languages and frameworks
- Works offline with cached models for basic suggestions
- Integrates seamlessly into your IDE workflow

---

# Single Inline Suggestion

- Copilot offers a single suggestion inline as you type
- Appears as faded gray text in your editor
- Accept with `Tab` or customize shortcut in settings
- Reject by continuing to type or pressing `Esc`
- Suggestions appear after 1-2 second pause
- Works for completing functions, loops, and entire code blocks
- Example: Type `def fibonacci(` and Copilot suggests the full implementation
- Particularly effective for common patterns and boilerplate code

---

# Multiple Inline Suggestion

- View multiple suggestions using shortcut (`Ctrl+Space` or `Alt+]`)
- Cycle through options with `Alt+]` (next) and `Alt+[` (previous)
- Choose from up to 10 different suggestions
- Each suggestion offers different approaches to solve the same problem
- Compare implementations: recursive vs iterative, verbose vs concise
- Helps you learn alternative coding patterns
- Example: Multiple ways to implement sorting, API calls, or error handling
- Accept your preferred option with `Tab`, reject all with `Esc`

---

# Contextual Suggestions

- Suggestions adapt to surrounding code.
- Copilot leverages file context, comments, and function names.
- Uses entire codebase for better accuracy
- Understands imports and dependencies
- Adapts to your coding style over time

---

# Inline Chat

Interact with Copilot directly in your editor for deeper assistance.

- Quick access via keyboard shortcut (`Cmd+I` or `Ctrl+I`)
- Refactor code in place without leaving your file
- Ask questions about selected code segments
- Generate, explain, or fix code instantly

---

## Type Hints

- Ask Copilot for type hints in ambiguous code
- Essential for type-safe Python, TypeScript, and strongly-typed languages
- Example:  
  ```python
  def add(a: int, b: int) -> int:
      return a + b
  ```
- Copilot infers types from context and usage patterns
- Suggests complex types: `List[Dict[str, Any]]`, `Optional[User]`, `Union[str, int]`
- Improves IDE autocomplete and catches type errors early
- Works with generics, protocols, and custom type definitions
- Request: "Add type hints to this function"

---

## Docstrings

- Generate comprehensive docstrings for functions, classes, and modules
- Supports multiple formats: Google, NumPy, reStructuredText, Sphinx
- Example Google-style docstring:
  ```python
  def process_data(filepath: str, encoding: str = 'utf-8') -> pd.DataFrame:
      """Process data from CSV file and return cleaned DataFrame.
      
      Args:
          filepath: Path to the CSV file
          encoding: File encoding (default: 'utf-8')
      
      Returns:
          Cleaned pandas DataFrame with validated data
      
      Raises:
          FileNotFoundError: If filepath doesn't exist
          ValueError: If CSV format is invalid
      """
  ```
- Request: "Generate a docstring for this function"
- Automatically includes parameters, return types, and exceptions

---

## Error Handling

- Request error handling strategies.
- Copilot suggests try-catch blocks automatically
- Recommends specific exception types
- Example:  
  ```python
  try:
      result = process_data(file_path)
  except FileNotFoundError as e:
      logger.error(f"File not found: {e}")
      return None
  except ValueError as e:
      logger.error(f"Invalid data: {e}")
      raise
  ```

---

# Chat

Copilot Chat enables conversational coding.

- Full-featured chat panel for complex queries
- Access via side panel or dedicated window
- Maintains conversation context and history
- Supports code references and file attachments
- Can execute multi-step tasks

---

## Chat Modes

- **General Q&A:** Ask programming questions, get best practices
- **Code Explanation:** Understand complex code logic step-by-step
- **Refactoring Suggestions:** Improve code quality and structure
- **Debugging:** Identify and fix issues in your code
- **Documentation:** Generate README, API docs, and comments
- **Learning:** Explore new frameworks and languages

---

## Generate Apps

- Ask Copilot to scaffold applications.
- Generate complete project structures from scratch
- Example: "Create a Flask REST API with authentication"
- Example: "Build a React app with TypeScript and Tailwind"
- Includes boilerplate, configuration, and dependencies
- Supports multiple frameworks: Express, Django, Next.js, etc.
- Can add specific features like authentication, database models, API routes

---

## Add Tests

- Request unit, integration, or end-to-end tests instantly
- Example: "Add pytest tests for this function"
- Copilot generates complete test suites with:
  - Test fixtures and setup/teardown
  - Multiple test cases covering different scenarios
  - Edge cases and boundary conditions
  - Mocking external dependencies
  - Assertions for expected behavior
- Supports all major frameworks: pytest, Jest, JUnit, Mocha, RSpec
- Creates parameterized tests for testing multiple inputs
- Includes both positive and negative test cases
- Request: "Add tests with 90% code coverage"

---

# Builtin Prompts

Predefined prompts for common coding tasks.

- Builtin prompts accelerate repetitive tasks with pre-configured commands
- Save time with pre-configured commands
- Consistent results across projects
- Accessible via Copilot Chat with `/` prefix or command palette
- Common builtin prompts:
  - `/explain` - Understand code logic and functionality
  - `/fix` - Automatically fix bugs and errors
  - `/tests` - Generate comprehensive test suites
  - `/doc` - Create documentation and comments
  - `/simplify` - Refactor complex code
  - `/optimize` - Improve performance
- No need to craft detailed prompts for common tasks
- Customizable to add your own team-specific prompts

---

## Explain Code

- "Explain this code" prompt for instant understanding
- Get detailed explanations of complex algorithms
- Understand library usage and API patterns
- Learn from unfamiliar codebases quickly
- Copilot breaks down logic step-by-step
- Perfect for code reviews and onboarding
- Works with any programming language

---

## Generate Documentation

- Auto-generate docstrings and README content
- Create API documentation automatically
- Generate inline comments for complex logic
- Produce user guides and tutorials
- Supports multiple documentation formats (Markdown, reStructuredText, JSDoc)
- Maintains consistent documentation style across projects

---

## Generate Tests

- Builtin prompt for test generation in popular frameworks
- Automatically creates unit tests for functions and classes
- Generates integration and end-to-end tests
- Supports pytest, Jest, JUnit, Mocha, and more
- Includes edge cases and boundary conditions
- Creates test fixtures and mocks
- Ensures high code coverage

---

# Plan Mode

Copilot helps you plan and execute coding tasks.

- Break down complex features into manageable steps
- Get a structured roadmap before coding
- Review and approve each step before execution
- Perfect for large refactorings or new features
- Reduces errors by planning ahead
- Plan Mode structures your workflow
- Breaks tasks into actionable steps

---

## Steps: Plan, Verify, Execute

- **Plan:** Copilot outlines detailed implementation steps
  - Breaks down complex features into manageable tasks
  - Identifies dependencies and prerequisites
  - Suggests file structure and architecture
  - Example: "Plan a user authentication system with JWT"
- **Verify:** Review and modify Copilot's plan before execution
  - Check for missing requirements
  - Adjust priorities and sequencing
  - Add constraints or preferences
  - Approve or reject individual steps
- **Execute:** Implement with Copilot's guided assistance
  - Step-by-step code generation
  - Automatic file creation and updates
  - Progress tracking throughout implementation
  - Rollback capability if issues arise

---

## Planning Documentation Strategy

- Use Plan Mode to organize comprehensive documentation efforts
- Example: "Plan documentation for API endpoints"
- Copilot creates structured documentation roadmap:
  - API endpoint inventory and categorization
  - Required sections: overview, authentication, endpoints, examples
  - Code examples for each endpoint
  - Error response documentation
  - Rate limiting and usage guidelines
- Ensures consistent documentation style across project
- Identifies missing or incomplete documentation
- Generates documentation templates and scaffolding
- Perfect for API docs, user guides, and technical specifications

---

# Agent Mode

Advanced automation with Copilot Agents.

- Fully autonomous coding assistant
- Can work independently on complex tasks
- Iterates and refines solutions automatically
- Handles multi-file changes seamlessly
- Reviews and tests its own work
- Best for experienced developers

---

## TDD with Agent

- Agents guide Test-Driven Development workflow
- **Red-Green-Refactor cycle:**
  1. Agent writes failing tests first (Red)
  2. Implements minimal code to pass tests (Green)
  3. Refactors for quality while maintaining tests (Refactor)
- Suggests comprehensive test cases before implementation
- Example: "Create a calculator class using TDD"
- Agent generates:
  - Test specifications covering all requirements
  - Edge cases and boundary conditions
  - Minimal implementation to satisfy tests
  - Refactoring suggestions for cleaner code
- Ensures high code coverage from the start
- Catches design issues early in development

---

## Handling Edge Cases and Iteration

- Agents proactively identify edge cases and boundary conditions
- Examples of edge cases detected:
  - Null/undefined inputs
  - Empty arrays or collections
  - Maximum/minimum value boundaries
  - Concurrent access scenarios
  - Network timeouts and failures
- Iterative refinement process:
  - Agent suggests initial implementation
  - Runs tests to identify failures
  - Automatically refines code to handle edge cases
  - Adds defensive checks and validation
- Request: "Identify and handle all edge cases"
- Continues iterating until all tests pass
- Documents edge cases in code comments

---

## Prompt Creating

- Agents help craft effective prompts for complex tasks
- **Good prompt characteristics:**
  - Clear, specific objectives
  - Relevant context and constraints
  - Expected output format
  - Examples when helpful
- Agent can analyze your task and suggest optimal prompt
- Example: "Help me create a prompt to refactor this legacy code"
- Agent might suggest:
  ```
  "Refactor this Python 2.7 function to Python 3.11:
  - Use type hints
  - Replace deprecated methods
  - Add error handling
  - Include docstring with examples
  - Maintain backward compatibility where possible"
  ```
- Learns from successful prompts to improve future suggestions

---

## Review of Code

- Automated code review for style, logic, and errors
- Identifies potential bugs before they occur
- Suggests performance optimizations
- Checks for security vulnerabilities
- Ensures consistency with project standards
- Provides actionable feedback with explanations

---

## Context Awareness

- Agents maintain rich context across files, sessions, and conversations
- **Context sources:**
  - Currently open files and recent edits
  - Project structure and dependencies
  - Git history and commit messages
  - Previous chat conversations
  - Documentation and README files
  - Package.json, requirements.txt, etc.
- Understands relationships between files
- Tracks changes across refactoring sessions
- References previous discussions: "As we discussed earlier..."
- Adapts suggestions based on project conventions
- Example: Knows your preferred libraries and patterns
- Context window spans thousands of lines of code

---

## Code Generation

- Generate boilerplate, modules, or entire features from descriptions
- Follows your project's existing patterns and style
- **What agents can generate:**
  1. Complete CRUD APIs with database models
  2. React components with hooks and styling
  3. Authentication and authorization systems
  4. Data processing pipelines
  5. CLI tools with argument parsing
  6. Microservices with Docker configuration

---

## Code Generation Example

**Request:** "Generate a REST API for blog posts with CRUD operations"

**Agent creates:**
1. Database models and migrations
2. API routes and controllers
3. Input validation and error handling
4. Unit and integration tests
5. API documentation

---

## Logic Mapping

- Visualize and map code logic with agent assistance
- Useful for onboarding, debugging, and refactoring
- Keeps documentation synchronized with code changes
- **Agent helps create:**
  1. Flow diagrams of function execution
  2. Call graphs showing function dependencies
  3. Data flow through your application
  4. State transition diagrams
  5. Architecture documentation

---

## Logic Mapping Example

**Request:** "Map the data flow from API request to database"

**Agent analyzes code and produces:**
1. Step-by-step execution explanation
2. Mermaid diagrams embedded in documentation
3. Sequence diagrams for API interactions
4. Component relationship maps

---

## Error Handling

- Agents suggest robust error handling patterns
- Implements defensive programming techniques
- Adds logging and monitoring hooks
- Creates graceful degradation strategies
- Designs retry mechanisms for transient failures
- Suggests circuit breakers for external services

---

# Custom Instructions

Tailor Copilot's behavior to your needs.

- Define Copilot's persona, style and expertise level
- Enforce team coding standards automatically
- Set language-specific preferences
- Specify frameworks and libraries to use
- Create project-specific guidelines
- Share instructions across your team

---

## User Custom Instructions (GUI)

- Configure personal Copilot behavior via GUI settings
- Instructions apply across all your projects
- JetBrains and Visual Studio have similar settings
- **Access in VS Code:**
  1. Settings → GitHub Copilot → Edit Instructions
  2. Or use command palette: "Copilot: Edit Instructions"
- **What you can configure:**
  1. Code style preferences (camelCase, snake_case, etc.)
  2. Preferred frameworks and libraries
  3. Documentation format standards
  4. Testing approach and frameworks
  5. Language-specific guidelines

---

## User Custom Instructions Example

**Example instruction:**
```
"Always use async/await instead of promises.
Prefer functional components in React.
Use TypeScript strict mode."
```

**This tells Copilot:**
- Avoid `.then()` chains, use `async/await`
- Generate functional components with hooks
- Apply strict type checking in TypeScript

---

## Repository Instructions

- Define project-specific instructions for team consistency
- Create `.github/copilot-instructions.md` in repository root
- Instructions committed to version control
- Automatically loaded for all team members
- Overrides personal instructions when in this repository
- **Ensures team alignment:**
  1. Consistent coding standards
  2. Shared architectural patterns
  3. Common library usage
  4. Project-specific conventions

---

## Repository Instructions Example

**Example `.github/copilot-instructions.md`:**
```markdown
# Project Copilot Instructions

- Use Prisma for database queries, not raw SQL
- Follow Airbnb JavaScript style guide
- All API endpoints must have OpenAPI documentation
- Use Zod for runtime validation
- Prefer composition over inheritance
```

**Result:** All team members get these standards automatically when working in this repository.

---

## Ways to Create Custom Instructions

- **From Prompt:** Convert successful prompts to reusable instructions
  - After getting good results, click "Save as instruction"
  - Copilot extracts reusable patterns from your prompt
  - Example: Frequent "use error boundaries" prompt becomes permanent instruction
- **From Scratch:** Write instructions manually in settings
  - More control over exact wording
  - Reference documentation and style guides
  - Organize by concern (testing, documentation, style)

---

## Ways to Create Custom Instructions (continued)

- **From Templates:** Start with community instruction templates
  - GitHub maintains instruction library
  - Adapt templates to your needs
- **Iterative Refinement:** Test and improve over time
  - Monitor Copilot's responses
  - Adjust instructions for better results
  - A/B test different instruction phrasings

---

## Checklist

- **Role Definition:** Persona clarity
- **Code Style:** Naming, formatting
- **Type Safety:** Explicit hints
- **Testing Strategy:** Framework, style
- **Documentation:** Docstring formats
- **Error Handling:** Exception instructions
- **Library Preferences:** Usage guidance

---

# Advanced Instructions

Enhance Copilot's precision with advanced scoping.

- File-level instruction overrides
- Folder-specific configuration
- Pattern-based rule application
- Conditional instructions based on file type
- Priority and inheritance rules
- Powerful for monorepo projects

---

## Advanced File-Specific Scoping

- Apply different instructions to specific files, folders, or patterns
- **Scoping options:**
  - File pattern: `**/*.test.ts` - All test files
  - Folder: `src/components/**` - All components
  - Extension: `*.py` - All Python files
  - Specific file: `src/config.ts`
- **Use cases:**
  - Test files: "Always use describe/it syntax"
  - API routes: "Include OpenAPI comments"
  - Components: "Use React hooks, no class components"
  - Database: "Use Prisma, include transactions"

---

## Advanced File-Specific Scoping Example

- Example configuration:
  ```json
  {
    "**/*.test.js": "Use Jest, 100% coverage, mock external calls",
    "src/api/**": "Include error handling and logging"
  }
  ```
- Powerful for monorepos with different conventions per package

---

## How to Setup

- **Via Configuration File:** Create `.copilot/instructions.json`
  ```json
  {
    "global": {
      "instructions": "Use TypeScript strict mode"
    },
    "scoped": {
      "**/*.test.ts": "Use Jest with describe/it blocks",
      "src/api/**": "Include OpenAPI documentation"
    }
  }
  ```
- **Via GUI Settings:**
  - VS Code: Settings → Copilot → Advanced Instructions
  - Add rules with file patterns and instructions
- **Priority order:** File-specific > Folder > Repository > User > Global
- Test with `@workspace` questions: "What instructions apply to this file?"
- Validate rules work as expected before committing
- Document your instruction strategy in project README

---

# Reusable Prompts

Create and manage prompt files for repeated use.

- Reusable prompts streamline workflows.
- Save frequently used prompts as templates
- Share prompts with your team via Git
- Version control your prompt library
- Build a knowledge base over time
- Reduce repetitive typing and instructions
- Improve consistency across projects

---

## How to Setup

- **Create prompt files directory:** `.github/copilot/prompts/`
- **Organize by category:**
  - `code-review.md` - Code review checklist
  - `api-endpoint.md` - Create new API endpoint
  - `react-component.md` - Generate React component
  - `database-migration.md` - Create database migration
- **Reference in Copilot Chat:**
  - `@prompt code-review` - Loads code-review.md
  - `#file:prompts/api-endpoint.md` - Direct file reference

---

## How to Setup (continued)

- **Share with team via Git:**
  - Commit prompt files to repository
  - Team gets consistent prompt library
  - Version control for prompt improvements
- **Best practices:**
  - Use descriptive filenames
  - Include usage examples in prompts
  - Document variables and placeholders

---

## Anatomy of a Prompt File

- **Structure:**  
  ```markdown
  # Prompt Title
  Brief description of what this prompt does
  
  ## Context
  When to use this prompt
  
  ## Instructions
  1. Step-by-step instructions
  2. Include specific requirements
  3. Define expected output format
  
  ## Variables
  - {COMPONENT_NAME}: Name of component to create
  - {PATH}: Destination path
  
  ## Example Usage
  Create a {COMPONENT_NAME} at {PATH} with props: {PROPS}
  
  ## Expected Output
  - Component file with TypeScript
  - Unit test file
  - Storybook story
  ```

---

## Anatomy of a Prompt File (continued)

- Include metadata: author, version, last updated
- Use markdown for formatting and code blocks
- Reference other prompts: `See also: api-endpoint.md`

---

## Using Prompt Files

- **Invoke via Copilot Chat:**
  - `@prompt [prompt-name]` - Load by name
  - Copilot searches `.github/copilot/prompts/`
- **Direct file reference:**
  - `#file:path/to/prompt.md` - Load specific file
  - Works with relative or absolute paths
- **Combine with context:**
  - `@prompt code-review #selection` - Review selected code
  - `@prompt refactor #file:utils.ts` - Refactor specific file

---

## Using Prompt Files (continued)

- **Parameterize prompts:**
  - `@prompt component name=Button path=src/components`
  - Replace variables in prompt template
- **Chain multiple prompts:**
  - Use one prompt's output as input to another
  - Example: Generate code → Generate tests → Generate docs
- **Best for:** Repeatable workflows that would otherwise require manual setup

---

# Custom Agents & Chat Extensions

Extend Copilot with custom agents and chat features.

- Custom agents automate complex tasks
- Agents consist of modules, models, and prompt logic

---

## “Beast Mode” Agent

- High-performance agent for intensive, complex coding tasks
- **Capabilities:**
  - Multi-file refactoring across entire codebase
  - Architecture redesign and modernization
  - Performance optimization at scale
  - Security audit and vulnerability fixes
  - Complete feature implementation from scratch
- **When to use:**
  - Legacy code migration (Python 2 → 3, JavaScript → TypeScript)
  - Framework upgrades (React 16 → 18, Angular migrations)
  - Large-scale refactoring (100+ files)
  - Complex algorithm implementation

---

## "Beast Mode" Agent - How It Works

- **What it does differently:**
  - Analyzes entire project before starting
  - Creates comprehensive execution plan
  - Runs automated tests after each change
  - Self-corrects when tests fail

---

## "Beast Mode" Agent Examples

- **Example 1:** "Migrate this Express.js app to NestJS"
  - Converts all routes to NestJS controllers
  - Updates middleware to NestJS guards and interceptors
  - Migrates dependencies and configuration
  - Generates comprehensive tests

- **Example 2:** "Refactor this monolith into microservices"
  - Analyzes code to identify service boundaries
  - Extracts modules into separate services
  - Implements inter-service communication
  - Sets up Docker and orchestration

---

## "Beast Mode" Agent Examples (continued)

- **Example 3:** "Upgrade React codebase from v16 to v18"
  - Updates all component lifecycle methods
  - Replaces deprecated APIs with new equivalents
  - Implements concurrent features where beneficial
  - Updates tests and documentation

- **Example 4:** "Convert JavaScript codebase to TypeScript"
  - Adds type annotations across entire project
  - Creates interface definitions for all data structures
  - Configures strict TypeScript compiler settings
  - Resolves all type errors systematically

---

## Module & Model Selection

- **Modules:** Specialized components for different tasks
  - `code-review`: Analyzes code quality and suggests improvements
  - `test-generation`: Creates comprehensive test suites
  - `documentation`: Generates docs and comments
  - `security-scan`: Identifies vulnerabilities
  - `performance`: Optimizes code efficiency
  - `refactoring`: Improves code structure
- **AI Models:** Choose based on task complexity
  - `gpt-4`: Most capable, best for complex reasoning
  - `gpt-3.5-turbo`: Faster, good for simple tasks
  - `claude-2`: Excellent for long context
  - `codex`: Specialized for code generation

---

## Module & Model Selection (continued)

- **Selection strategy:**
  - Simple completions → Fast models
  - Complex architecture → Advanced models
  - Cost vs. quality trade-offs
- Configure in agent settings or per-request

---

## Context & History

- **Agents track comprehensive context:**
  - Conversation history across sessions
  - Code changes and evolution
  - Previous decisions and rationale
  - Failed approaches and lessons learned
  - User preferences and feedback
- **Context window:** Up to 100K tokens (≈75K words)
  - Entire small projects fit in context
  - Large files summarized intelligently

---

## Context & History (continued)

- **Historical awareness:**
  - "Continue refactoring from yesterday"
  - "Why did we choose this approach?"
  - References specific past conversations
  - Learns from correction patterns
- **Context management:**
  - Automatic pruning of old/irrelevant context
  - Manual context reset: "Start fresh"
  - Context export for sharing with team
- Enables true long-term collaborative development

---

## Tool Calling (Function Calling)

- Agents invoke external tools and functions for enhanced capabilities
- **Available tools:**
  - `file_search`: Find files matching patterns
  - `grep`: Search code content
  - `run_command`: Execute terminal commands
  - `api_call`: Fetch external data
  - `database_query`: Query databases
  - `git_operations`: Commit, branch, merge
- **Example workflow:**
  1. User: "Find all TODO comments and create GitHub issues"
  2. Agent calls `grep` to find TODOs
  3. Agent calls `github_api` to create issues
  4. Agent calls `git_operations` to commit changes

---

## Tool Calling (Function Calling) - continued

- **Custom tools:** Create project-specific functions
  ```python
  @tool
  def deploy_to_staging():
      """Deploy current branch to staging environment"""
  ```
- Agents decide when and how to use tools automatically
- Chaining tools creates powerful automation workflows

---

## Designing Your Agent

- **Define agent goals and personality:**
  - Purpose: Code reviewer, test generator, documentation writer
  - Tone: Friendly mentor, strict enforcer, collaborative partner
  - Expertise: Junior-friendly explanations vs. expert-level
- **Agent configuration file:**
  ```yaml
  name: "Code Reviewer Pro"
  description: "Reviews code for quality and security"
  personality: "Thorough but encouraging"
  modules: [code-review, security-scan]
  model: gpt-4
  tools: [file_search, grep, git_operations]
  instructions: |
    - Check for common security vulnerabilities
    - Suggest performance improvements
    - Ensure code follows team style guide
    - Provide specific examples in feedback
  ```
- **Interaction style:** Command-based vs. conversational
- **Guardrails:** Define what agent can/cannot do
- **Testing:** Validate agent behavior with test scenarios

---

# Custom Prompts

Master prompt creation for tailored results.

- Custom prompts guide Copilot's responses
- Clear, concise instructions yield better results
- **Bad:** "Write code."
- **Good:** "Write a Python function to parse CSV files and handle errors."

---

# Prompt Engineering (Advanced Strategies)

- Master advanced techniques for effective prompting
- **Core principles:**
  - Clarity: Be specific about what you want
  - Context: Provide relevant background
  - Constraints: Define limitations and requirements
  - Examples: Show desired output format
- **Why it matters:**
  - Better prompts = Better code
  - Reduces back-and-forth iterations
  - Saves time and improves accuracy
  - Unlocks Copilot's full potential

---

# Prompt Engineering (Advanced Strategies) - continued

- **Prompt engineering is a skill:**
  - Improves with practice and experimentation
  - Learn from successful patterns
  - Adapt to different contexts and models
- Following slides cover specific advanced techniques

---

## Role Prompting (Persona)

- Define Copilot's role/persona for better context-specific responses
- **Examples:**
  - "You are a senior Python developer expert in Django"
  - "Act as a security engineer reviewing this authentication code"
  - "You are a technical writer creating API documentation"
  - "Be a code reviewer focused on performance optimization"
- **Why roles work:**
  - Activates relevant training data
  - Sets appropriate expertise level
  - Defines perspective and priorities
  - Adjusts language and detail level

---

## Role Prompting (Persona) - continued

- **Combine role with task:**
  ```
  "As a React expert, refactor this class component 
  to a functional component with hooks."
  ```
- **Pro tip:** Match role to your actual need (don't always use "senior expert")
- Roles particularly effective for reviews, explanations, and architecture decisions

---

## Zero-Shot Prompting

- Request tasks without providing examples
- **When to use:**
  - Common, well-known tasks
  - Standard programming patterns
  - Tasks Copilot has seen many times
- **Examples:**
  - "Create a function to validate email addresses"
  - "Write a binary search algorithm"
  - "Generate a REST API endpoint for user registration"
- **Advantages:**
  - Faster - no need to craft examples
  - Leverages Copilot's existing knowledge
  - Good for standard implementations

---

## Zero-Shot Prompting (continued)

- **Limitations:**
  - May not match your specific style
  - Less control over output format
  - Can produce generic solutions
- **Best practices:**
  - Be specific about requirements
  - Specify language and framework
  - Add constraints: "with error handling", "using async/await"

---

## One-Shot Prompting

- Provide a single example to guide Copilot's response
- **When to use:**
  - Custom formats or patterns
  - Project-specific conventions
  - Less common implementations

- **Advantages:**
  - Shows exact format you want
  - Copilot adapts example to new context
  - Good balance of guidance and flexibility
- **Pro tip:** Use examples from your existing codebase for consistency



---

## One-Shot Prompting (Examples)

- **Example 1:**
  ```
  "Create a validation function following this pattern:
  
  function validateEmail(email: string): ValidationResult {
    return {
      valid: /^[^@]+@[^@]+$/.test(email),
      errors: email.includes('@') ? [] : ['Missing @ symbol']
    };
  }
  
  Now create validatePassword with similar structure."
  ```
- **Example 2:**
  ```
  "Generate an API handler following this pattern:
  
  async function getUser(req: Request): Promise<Response> {
    const { id } = req.params;
    const user = await db.users.findById(id);
    return { status: 200, data: user };
  }
  
  Now create getProduct with the same structure."
  ```

---

## Few-Shot Prompting

- Supply multiple examples for nuanced, complex results
- **When to use:**
  - Complex patterns with variations
  - Multiple edge cases to handle
  - Subtle distinctions in behavior

- **Advantages:** Most accurate results, handles complexity

- **Trade-off:** Requires more setup time

---

## Few-Shot Prompting (Example)
  
- **Example:**
  ```
  "Create validation functions following these patterns:
  
  // Example 1: Simple field
  validateUsername(value) {
    return value.length >= 3 && /^[a-z0-9_]+$/i.test(value);
  }
  
  // Example 2: Optional field
  validatePhone(value) {
    return !value || /^\d{10}$/.test(value);
  }
  
  // Example 3: Complex validation
  validatePassword(value) {
    return value.length >= 8 && 
           /[A-Z]/.test(value) && 
           /[0-9]/.test(value);
  }
  
  Now create validateAddress with similar structure."
  ```


---

## Explicit Reasoning

<br>

- Ask Copilot to explain its logic step-by-step before or after generating code
- **Prompts that trigger reasoning:**
  - "Explain your approach before implementing"
  - "Think through this problem step-by-step"
  - "What are the trade-offs of different approaches?"
  - "Show your reasoning for choosing this solution"

- **Benefits:**
  - Better solutions through deliberate thinking
  - Helps you understand the code
  - Identifies potential issues early
  - Educational - learn problem-solving approaches

---

## Explicit Reasoning (Example)

<br>

- **Example:**
  ```
  "Before implementing a cache, explain:
  1. What caching strategy is best for this use case
  2. Where to store cached data
  3. When to invalidate cache
  4. Then implement the solution"
  ```

- **Chain of thought:** Leads to more accurate, well-considered code

- Particularly valuable for complex algorithms and architecture decisions

---

## Iterative Refinement

- Refine prompts based on output feedback in multiple rounds
- **Process:**
  1. **Initial prompt:** "Create a user authentication function"
  2. **Review output:** Too simple, missing features
  3. **Refined prompt:** "Add password hashing and JWT token generation"
  4. **Review again:** Good, but needs error handling
  5. **Final refinement:** "Add try-catch and specific error messages"
- **Why iterate:**
  - First attempt rarely perfect
  - Clarify requirements as you see output
  - Add forgotten details incrementally
  - Fine-tune style and structure

---

## Iterative Refinement (continued)

- **Iterative patterns:**
  - "Now add [feature]"
  - "Modify to include [requirement]"
  - "Make it more [adjective]"
  - "Fix the [specific issue]"
- **Pro tip:** Save successful prompts for future use
- Build on previous responses rather than starting over

---

## Mastering Context

- Leverage file, project, and conversation context for better results
- **Types of context:**
  - **File context:** Code in current file and related files
  - **Project context:** Package dependencies, config, README
  - **Conversation context:** Previous chat messages
  - **Selection context:** Highlighted code
  - **Workspace context:** All files in project
- **Context references in prompts:**
  - `#selection` - Currently selected code
  - `#file:path/to/file.ts` - Specific file
  - `@workspace` - Entire project
  - `#codebase` - All code files

---

## Mastering Context (continued)

- **Example with context:**
  ```
  "Refactor #selection to use the same pattern 
  as #file:src/utils/validator.ts"
  ```
- **Context best practices:**
  - Open related files before prompting
  - Reference specific files for consistency
  - Use workspace context for architecture questions
- **Context window limits:** ~128K tokens, Copilot auto-prioritizes most relevant

---

## The 4 S's

A simple framework for writing effective prompts

- **Single:** One task per prompt
  - Focus on one objective at a time
  - Example: ❌ "Add error handling, tests, and documentation"
  - Example: ✅ "Add error handling with try-catch blocks"

- **Specific:** Clear requirements
  - Include exact details about what you want
  - Example: ❌ "Make it better"
  - Example: ✅ "Add TypeScript strict types with JSDoc comments"

---

## The 4 S's (continued)

- **Short:** Concise wording
  - Keep prompts brief but complete
  - Example: ❌ "I need you to please create a function that validates..."
  - Example: ✅ "Create a function to validate email addresses"

- **Surround:** Provide context
  - Reference files, frameworks, and patterns
  - Example: ❌ "Refactor this"
  - Example: ✅ "Refactor #selection to use React hooks like in #file:components/User.tsx"

---

# The End

---

## Quick Recap

- **Explored comprehensive Copilot features:**
  - Inline suggestions for instant code completion
  - Inline chat for in-editor assistance
  - Full chat for complex conversations
  - Builtin prompts for common tasks
- **Discovered powerful modes:**
  - Plan Mode for structured task breakdown
  - Agent Mode for autonomous development

---

## Quick Recap (continued)

- **Learned customization:**
  - Custom instructions for personalized behavior
  - Reusable prompts for consistency
  - Custom agents for specialized workflows
- **Mastered prompt engineering:**
  - Role prompting, few-shot learning
  - Iterative refinement and context mastery
  - The 4 S's framework
- You now have the tools to maximize Copilot's potential!

---

## Summary

- **GitHub Copilot is a productivity multiplier:**
  - Writes boilerplate code in seconds
  - Generates tests, docs, and explanations
  - Refactors and optimizes existing code
  - Learns and adapts to your style
- **Key success factors:**
  - Clear, specific prompts
  - Appropriate context and examples
  - Custom instructions for consistency
  - Right mode/agent for the task

---

## Summary (continued)

- **Continuous improvement:**
  - Experiment with different prompt techniques
  - Build your prompt library over time
  - Share best practices with your team
  - Stay updated on new features
- **Remember:** Copilot is your pair programmer, not a replacement
- **You're still in control:** Review, refine, and learn from AI suggestions

---

## Conclusions

- **Effective Copilot usage requires:**
  - Understanding available features and when to use them
  - Crafting clear, well-structured prompts
  - Providing appropriate context and examples
  - Iterating and refining based on results
- **Best practices to adopt:**
  - Start simple with inline suggestions
  - Progress to chat for complex tasks
  - Use agents for large-scale work
  - Customize with instructions and prompts

---

## Conclusions (continued)

- **Common pitfalls to avoid:**
  - Vague, ambiguous prompts
  - Accepting suggestions without review
  - Forgetting to provide context
  - Not leveraging customization features
- **The future of AI-assisted development:**
  - More capable agents and models
  - Better understanding of intent
  - Seamless team collaboration
  - Integration with entire development lifecycle
- **Your journey starts now - experiment, learn, and master Copilot!**

---

## Invitation for Hands-On Training

Try the labs at:

https://nirgeier.github.io/Copilot-Prompts-Workshop

for practical Copilot prompting experience!

Will you accept the challenge???

---
layout: end
---

# Happy Coding!

Continue exploring the labs in the repository.

[Workshop Repository](https://github.com/nirgeier/Copilot-Prompts-Workshop)
```
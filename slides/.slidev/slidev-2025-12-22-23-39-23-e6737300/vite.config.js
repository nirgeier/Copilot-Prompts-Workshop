
      import { defineConfig } from 'vite';

      export default defineConfig({
        server: {
          fs: {
            allow: [
              // Allow the template project path which contains node_modules
              '/Users/nirg/.vscode-insiders/extensions/robothy.slidev-copilot-0.1.4/resources/slidev-template',
              // Allow the session project path
              '/Users/nirg/repositories/slidevjs/.slidev/slidev-2025-12-22-23-39-23-e6737300',
              // Add the root directory containing the node_modules
              '/Users/nirg/.vscode-insiders/extensions/robothy.slidev-copilot-0.1.4/resources'
            ]
          }
        }
      });
    
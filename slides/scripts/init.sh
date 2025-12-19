#!/bin/bash

npm i -g pnpm
pnpm create slidev my-presentation -- --force
cd my-presentation
pnpm install
pnpm run dev
echo "Setup complete. You can now start editing your presentation."

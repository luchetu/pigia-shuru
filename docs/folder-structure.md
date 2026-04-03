# Pigia Shuru Folder Structure

## Recommended Structure
```text
pigia-shuru/
├── app/
│   ├── api/
│   │   ├── routes/
│   │   ├── schemas/
│   │   └── dependencies/
│   ├── core/
│   ├── services/
│   ├── integrations/
│   │   ├── twilio/
│   │   ├── livekit/
│   │   ├── gemini/
│   │   └── kra/
│   ├── agents/
│   │   ├── flows/
│   │   ├── prompts/
│   │   ├── tools/
│   │   └── session/
│   ├── models/
│   ├── repositories/
│   ├── workers/
│   ├── utils/
│   └── main.py
├── tests/
│   ├── unit/
│   ├── integration/
│   └── fixtures/
├── scripts/
├── docs/
├── deployment/
│   ├── docker/
│   └── env/
├── .env.example
├── pyproject.toml
├── README.md
└── .gitignore
```

## Folder Purpose
### `app/api`
FastAPI HTTP entrypoints, request validation, and dependency wiring.

### `app/core`
App configuration, settings, logging, security helpers, and shared startup logic.

### `app/services`
Business logic that is not tied to a specific transport or vendor.

### `app/integrations`
External system adapters for Twilio, LiveKit, Gemini Realtime, and future KRA-facing integrations.

### `app/agents`
Voice-agent orchestration, prompts, tool definitions, and session-level behaviors.

### `app/models`
Internal domain models and persistence-facing entities.

### `app/repositories`
Database access and persistence abstraction if you later add Postgres or another store.

### `app/workers`
Async jobs for callbacks, retries, transcript post-processing, reminders, and outbound notifications.

### `tests`
Unit and integration coverage for API routes, integrations, and agent flows.

### `scripts`
Developer utilities such as local bootstrapping, tunnel setup, or fixture loading.

### `deployment`
Container and environment-specific deployment assets.

## Notes For Your Stack
- Keep telephony concerns inside `app/integrations/twilio`.
- Keep WebRTC room and participant handling inside `app/integrations/livekit`.
- Keep Gemini Realtime session bootstrapping and model-specific adapter code inside `app/integrations/gemini`.
- Keep call logic such as `nil_return`, `tot_guidance`, and `payment_help` inside `app/agents/flows`.
- Keep agent prompts versioned as files in `app/agents/prompts` so they are easy to iterate on.

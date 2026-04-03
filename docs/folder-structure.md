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
│   │   ├── telephony/
│   │   ├── transport/
│   │   ├── ai/
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
External system adapters grouped by capability rather than vendor. This keeps the architecture provider-agnostic while still allowing concrete implementations under each integration area.

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
- Keep call ingress and PSTN provider adapters inside `app/integrations/telephony`.
- Keep WebRTC room, media transport, and session transport adapters inside `app/integrations/transport`.
- Keep realtime model adapters and session bootstrapping inside `app/integrations/ai`.
- Keep call logic such as `nil_return`, `tot_guidance`, and `payment_help` inside `app/agents/flows`.
- Keep agent prompts versioned as files in `app/agents/prompts` so they are easy to iterate on.

## Provider Mapping
- `app/integrations/telephony`: current provider can be Twilio, but the folder should represent the telephony boundary, not the vendor.
- `app/integrations/transport`: current provider can be LiveKit, but the folder should represent the media or session transport boundary.
- `app/integrations/ai`: current provider can be Gemini Realtime, but the folder should represent the model or realtime intelligence boundary.

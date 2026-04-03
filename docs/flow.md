# Pigia Shuru Call Flow

## Primary User Flow
```mermaid
flowchart TD
    A["Caller dials Pigia Shuru"] --> B["Welcome prompt"]
    B --> C["Choose language<br/>English / Kiswahili"]
    C --> D["Choose intent<br/>NIL return / TOT / PIN check / Payment help"]

    D --> E["Authenticate caller<br/>Phone + KRA PIN + OTP if required"]
    E --> F{"Confidence and policy check"}

    F -->|Low risk| G["Answer directly or calculate result"]
    F -->|Needs confirmation| H["Repeat important values back to caller"]
    F -->|High risk or unsupported| I["Escalate to human support or handoff"]

    G --> J["Send SMS or WhatsApp summary"]
    H --> K{"Caller confirms?"}
    K -->|Yes| L["Proceed with assisted action"]
    K -->|No| M["Correct captured values"]
    M --> H

    L --> J
    I --> N["Create support ticket and transfer context"]
    N --> J
    J --> O["End call"]
```

## Detailed Flow
### 1. Entry
- The caller places a call to the Pigia Shuru number.
- The system answers with a short welcome prompt.
- The caller selects English or Kiswahili.

### 2. Intent Capture
- The assistant asks what the caller needs help with.
- The caller can speak or use keypad input.
- Initial MVP intents:
  - NIL return help
  - Turnover Tax guidance
  - PIN or compliance status check
  - Payment instructions

### 3. Authentication
- For basic FAQs, no authentication is required.
- For account-specific actions, the assistant requests:
  - phone number confirmation
  - KRA PIN
  - OTP or another approved verification step
- The MVP should not use biometric authentication.
- Voice biometrics can be considered later, but they are not part of the initial trust model because phone audio quality, spoofing risk, and failure handling are harder to manage safely.

## Authentication Model
### Trust Levels
- `Anonymous`: general guidance with no account-specific data.
- `Known caller`: the system recognizes the caller number but does not treat that as full identity.
- `Caller + KRA PIN`: enough for some medium-risk account-specific flows.
- `Caller + KRA PIN + OTP`: required for higher-risk actions or anything closer to submission.
- `Verified + explicit confirmation`: required before any sensitive action is completed.

### Recommended Approach
- Use caller phone number as the first signal, not the only signal.
- Ask for KRA PIN for account-specific flows.
- Send an OTP over SMS or WhatsApp when the requested action is sensitive.
- Read back important values and require a clear spoken or keypad confirmation before continuing.
- Log verification level, confirmation result, and timestamps for auditability.

### Why Not Biometrics In V1
- PSTN and mobile call quality can degrade voiceprint accuracy.
- Replay and spoofing risks are difficult to handle in a voice-only channel.
- False rejects would create a poor experience for legitimate callers.
- OTP plus explicit confirmation is simpler, clearer, and easier to audit.

### 4. Workflow Handling
- For low-risk requests:
  - give direct answers
  - provide deadlines
  - compute estimates such as TOT from user-supplied sales
- For medium-risk requests:
  - read values back
  - request explicit spoken confirmation
  - proceed only after confirmation
- For high-risk or unsupported requests:
  - do not automate submission
  - transfer to an agent or provide a secure handoff path

### 5. Notification and Closure
- Send a summary by SMS or WhatsApp after the call.
- Include due date, amount, next action, and reference number where relevant.
- End the call only after confirming the recap was sent.

## Example TOT Flow
```mermaid
sequenceDiagram
    participant U as User
    participant V as Voice Agent
    participant P as Policy Layer
    participant N as Notification Service

    U->>V: Calls and chooses Turnover Tax
    V->>U: Ask for gross sales for the month
    U->>V: Provides amount
    V->>P: Validate risk and completeness
    P-->>V: Safe to continue with confirmation
    V->>U: Read back amount and tax estimate
    U->>V: Confirms
    V->>N: Send SMS recap with due date and next steps
    N-->>U: SMS delivered
    V->>U: Close call
```

## Escalation Rules
- Escalate when speech confidence is low after retry.
- Escalate when a caller disputes calculated values.
- Escalate when the request involves unsupported filing actions.
- Escalate when the caller requests a live agent.
- Escalate when OTP verification fails repeatedly.
- Escalate when the caller cannot complete the required verification level for the requested action.

## MVP Success Criteria
- Caller completes a basic flow in under 3 minutes.
- SMS recap is delivered successfully after the call.
- Human handoff preserves call context.
- All critical values are confirmed before action.

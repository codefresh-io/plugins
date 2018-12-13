# Codefresh Slack Plugin

Use Codefresh Slack plugin to send a message to a channel.

## Usage

Simple mode - just send text or attachment to slack channel

```yaml
---
version: '1.0'

steps:

  ...

 SendToSlack:
    title: Sending message to slack
    image: codefresh/slacknotifier
    environment:
    - SLACK_WEBHOOK_URL=${{SLACK_HOOK_URL}}
    - SLACK_TEXT=${{SLACK_TEXT}}
    - SLACK_ATTACHMENTS=${{SLACK_ATTACHMENTS}}
  ...

```

Template mode - ability to have one template body and just override fields

```yaml
---
version: '1.0'

steps:

  ...

 SendToSlack:
     title: Sending message to slack
     image: codefresh/slacknotifier
     environment:
     - SLACK_HOOK_URL=${{SLACK_HOOK_URL}}
     - SLACK_TEXT=cool
     - SLACK_TEMPLATE_FIELDS=${{SLACK_TEMPLATE_FIELDS}}
     - SLACK_TEMPLATE_BODY=${{SLACK_TEMPLATE_BODY}}
     - MODE=template
  ...

```

Default template mode - send information about build

```yaml
---
version: '1.0'

steps:

  ...

 SendToSlack:
     title: Sending message to slack
     image: codefresh/slacknotifier
     environment:
     - SLACK_HOOK_URL=${{SLACK_HOOK_URL}}
     - MODE=default-template
  ...

```



## Environment Variables

- **required** `WEBHOOK_URL` - Url to the channel. Slack official [docs](https://api.slack.com/incoming-webhooks)
- **required** `SLACK_TEXT` - The message that will be sent
- `SLACK_ATTACHMENTS` - print verbose output
- `MODE` - template | simple mode
- `SLACK_TEMPLATE_FIELDS` - fields for override if use template mode
- `SLACK_TEMPLATE_BODY` - message body if use template mode

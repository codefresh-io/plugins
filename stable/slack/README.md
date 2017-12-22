# Codefresh Slack Plugin

Use Codefresh Slack plugin to send a message to a channel.

## Usage


```yaml
---
version: '1.0'

steps:

  ...

  SendToSlack:
    title: Sending message to slack
    image: codefresh/slack-message-sender
    commands:
      - slack-message-sender send
    environment:
    - WEBHOOK_URL=${{SLACK_WEBHOOK_URL}}
    - SLACK_MESSAGE=${{CF_COMMIT_MESSAGE}}
  ...

```

## Environment Variables

- **required** `WEBHOOK_URL` - Url to the channel. Slack official [docs](https://api.slack.com/incoming-webhooks)
- **required** `SLACK_MESSAGE` - The message that will be sent
- `DEBUG` - print verbose output

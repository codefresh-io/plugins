# Telegram notify plugin

Telegram plugin which gives the opportunity send any messages to users via bot.

## Usage

```yaml
version: '1.0'
...
steps:
  ...
  sendMessage:
    image: codefresh/telegramnotifier
    environment:
      - TELEGRAM_TOKEN=TOKEN
      - TELEGRAM_TO=99999999
      - TELEGRAM_MESSAGE=Hello {{{userLink}}}, how are you
      - TELEGRAM_IMAGES=https://codefresh.io/docs/assets/brand/codefresh-social.png
```

## Required variables

- `TELEGRAM_TOKEN` - token of your bot (cat get from [@BotFather](https://t.me/BotFather))
- `TELEGRAM_TO` - array of bot`s user id who will receive a message separated by comma (id you can retrieve from [@myidbot](https://t.me/myidbot))

## Optional variables

- `TELEGRAM_STATUS` - send info about current build, **if pass - all others variables will be ignored**
- `TELEGRAM_MESSAGE` - text of message which will be sent to user, with [Handlebars.js](https://github.com/wycats/handlebars.js/), 
  - available vars:
      - `{{buildTrigger}}` 
      - `{{buildInitiator}}`  
      - `{{buildId}}` 
      - `{{buildTimestamp}}`  
      - `{{buildUrl}}` 
      - `{{repoOwner}}`  
      - `{{repoName}}`  
      - `{{branch}}` 
      - `{{revision}}` 
      - `{{commitAuthor}}` 
      - `{{commitUrl}}` 
      - `{{commitMessage}}` 
      - `{{userID}}` - id of current telegram user
      - `{{{userLink}}}` - link to current telegram user 
  
  - for text markup use Markdown
- `TELEGRAM_IMAGES` - array of image links for attaching to message

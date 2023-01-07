# Slack Bot for Generating Mid Journey-style Images

This app is a Slack bot that generates images in the style of Mid Journey using the Replicate API. It is triggered by the `/create-image` slash command and responds with a generated image in the same thread.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

* A Slack app and bot set up and configured
* An API key for Replicate
* Python 3.6 or higher
* Pipenv (optional but recommended)

### Installing

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/slack-midjourney-bot.git
    ```

2. Change into the project directory:

    ```bash
    cd slack-midjourney-bot
    ```

3. Set the following environment variables:

    ```bash
    export SLACK_BOT_TOKEN=your_bot_token_here
    export SLACK_APP_TOKEN=your_app_token_here
    export REPLICATE_API_KEY=your_api_key_here
    ```

4. If you're using Pipenv, create a virtual environment and install the dependencies:

    ```bash
    pipenv install
    ```

5. If you're not using Pipenv, install the dependencies with pip:

    ```bash
    pip install -r requirements.txt
    ```

### Running the app

To start the app, run the following command:

```bash
python app.py
```

## Built With

* [Slack Bolt](https://slack.dev/bolt-js/) - The Slack API SDK used for creating and managing the Slack app
* [Replicate](https://replicate.ai/) - The image generation API used for creating the images
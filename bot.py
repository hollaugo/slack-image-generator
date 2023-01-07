import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import replicate

# Initializes your slack app with your bot token 
app = App(token=os.environ.get("SLACK_BOT_TOKEN"))

#Initialize the replicate
model = replicate.models.get("prompthero/openjourney")
version = model.versions.get("9936c2001faa2194a261c01381f90e65261879985476014a0a37a334593a05eb")

#Listen and handle slash command for stable diffusion image generation
@app.command("/create-image")
def create_image(ack, command, client):

    #Acknowledge command request from slack
    ack()

    #Get prompt from command text and add midjourney style to it
    prompt = f"mdjrny-v4 style {command['text']}"

    #Post message to channel indicating that image is being generated
    initial_message = client.chat_postMessage(channel=command["channel_id"], text="Generating image...")

    #Generate image using the prompt
    image = version.predict(prompt = prompt, num_inference_steps=50)

    #Update message to channel with the generated image 
    client.chat_update(
        channel=command["channel_id"],
        ts=initial_message["ts"],
        blocks= [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Image generated! :white_check_mark:"
            }
            },
            {
                "type": "image",
                "title": {
                    "type": "plain_text",
                    "text": f"Prompt: {prompt}",
                    "emoji": True
                },
                "image_url": image[0],
                "alt_text": "Generated image"

            }
        ]

    )


# Start your app
if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
from anthropic import Anthropic
from endor.common.auth import oidc_client

# Generate token
token = oidc_client.get_oidc_token()

# Generate Anthropic client
client = Anthropic(
            auth_token = token,
            base_url = "https://api.endor.apple.com/anthropic"
        )

# Send message
message = client.messages.create(
    model = "anthropic.claude-sonnet-4-6",
    max_tokens = 2048,
    messages = [
        { "role": "user",
          "content": "Hello, Claude!"
         }
    ]
)

print(message.content[0].text)

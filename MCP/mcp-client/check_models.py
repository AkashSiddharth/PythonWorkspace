from anthropic import Anthropic
from endor.common.auth import oidc_client
 
# Generate token
token = oidc_client.get_oidc_token()
 
# Create Anthropic client
client = Anthropic(
    auth_token=token,
    base_url="https://api.endor.apple.com/anthropic"
)
 
# List available models
models = client.models.list()
for model in models.data:
    print(f"Model ID: {model.id}")
    print(f"Display Name: {model.display_name}")
    print(f"Created: {model.created_at}")
    print("---")

from flask import Flask, render_template
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from azure.storage.blob import BlobServiceClient
 
app = Flask(__name__)
 
# Function to retrieve Blob Storage connection string from Azure Key Vault
def get_blob_storage_connection_string():
    # Authenticate with Azure Key Vault using DefaultAzureCredential
    credential = DefaultAzureCredential()
    key_vault_uri = "https://demokeyvault1472.vault.azure.net/secrets/demosecret/22f0bc273eff4066b312318e00963c7c"
    secret_name = "demosecret"
    secret_version = "22f0bc273eff4066b312318e00963c7c"
 
    # Create a SecretClient to retrieve the secret from Azure Key Vault
    secret_client = SecretClient(vault_url=key_vault_uri, credential=credential)
    secret_value = secret_client.get_secret(secret_name, secret_version)
 
    return secret_value.value
 
# Function to retrieve image URL from Azure Blob Storage
def get_image_url():
    blob_storage_connection_string = get_blob_storage_connection_string()
 
    # Connect to Blob Storage
    blob_service_client = BlobServiceClient.from_connection_string(blob_storage_connection_string)
    blob_client = blob_service_client.get_blob_client(container="demoimage", blob="1705549725820.jpg")
 
    # Get the image URL
    image_url = blob_client.url
    return image_url
 
# Route to display the image in the web browser
@app.route("/")
def display_image():
    image_url = get_image_url()
    return render_template("main.html", image_url=image_url)
 
if __name__ == "__main__":
    app.run(debug=True)

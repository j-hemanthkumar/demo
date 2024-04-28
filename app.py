from flask import Flask, render_template
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient
 
app = Flask(__name__)
 
# Function to retrieve image URL from Azure Blob Storage
def get_image_url():
    # Authenticate with Azure Key Vault
    credential = DefaultAzureCredential()
    key_vault_uri = "c219cf67-c90d-48ff-a0fc-36b560fe855b"
    # Retrieve the connection string secret from Azure Key Vault
    blob_storage_connection_string = ...
 
    # Connect to Blob Storage
    blob_service_client = BlobServiceClient.from_connection_string(blob_storage_connection_string)
    blob_client = blob_service_client.get_blob_client(container="demoimage", blob="1705549725820.jpg")
 
    # Get the image URL
    image_url = blob_client.url
    return render_template("main.html", image_url=image_url)
 
# Route to display the image in the web browser
@app.route("/")
def display_image():
    image_url = get_image_url()
    return render_template("index.html", image_url=image_url)
 
if __name__ == "__main__":
app.run(debug=True)

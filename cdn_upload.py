import cloudinary
# Import the cloudinary.api for managing assets
import cloudinary.api
# Import the cloudinary.uploader for uploading assets
import cloudinary.uploader


cloudinary.config(
    cloud_name="dcf6uk047",
    api_key="176572318442856",
    api_secret="C0hg2pOkd-7MoOdoeXLcF-RMHTk",
    secure=True,
)

upload=cloudinary.uploader.upload("./pic2.jpeg", 
  public_id = "nft_assets/pic")

url=upload['secure_url']

print(url)
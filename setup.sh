mkdir -p ~/.streamlit/
echo "[general]
email = \"shampa077@gmail.com\"
" > ~/.streamlit/credentials.toml
echo "[server]
headless = true
port = $PORT
enableCORS = false
" > ~/.streamlit/config.toml
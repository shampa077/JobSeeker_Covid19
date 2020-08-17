mkdir -p ~/.streamlit/
echo "\
[general]\n\
email = \"shampa077@gmail.com\"\n\
" > ~/.streamlit/credentials.toml
echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = 8501\n\ 
" >> ~/.streamlit/credentials.toml

echo "\
[browser]\n\
gatherUsageStats=false\n\
" >> ~/.streamlit/credentials.toml
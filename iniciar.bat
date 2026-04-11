@echo off
cd /d "c:\Users\ullokevi\OneDrive - amazon.com\Documents\ESCUELA"
start "" python -m streamlit run app.py --server.address 0.0.0.0 --server.headless true
timeout /t 5 /nobreak >nul
start http://localhost:8501
pause

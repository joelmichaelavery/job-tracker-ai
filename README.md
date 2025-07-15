# AI-Powered Job Application Tracker

A full-stack web application that helps job seekers track their job applications and optimize their resumes using AI.  
Includes an intelligent resume analyzer and job fit scoring based on job descriptions.

---

## 🚀 Features
- **Job Application Management**: Add, update, and track your job applications.
- **AI-Powered Resume Analyzer**: Suggests improvements by comparing resumes to job descriptions.
- **Job Fit Score**: Predicts how well your resume matches a given job post.
- **Full-Stack App**: FastAPI backend, PostgreSQL database, React frontend.
- **Deployment**: Dockerized and ready for cloud deployment.

---

## 🛠 Tech Stack
**Backend**: FastAPI, SQLAlchemy  
**Database**: PostgreSQL  
**Frontend**: React, TailwindCSS  
**AI/ML**: Hugging Face Transformers, Scikit-learn  
**Deployment**: Docker, Render/AWS  
**Testing**: Pytest, Jest  

---

## 📂 Project Structure
job-tracker-ai/
│
├── backend/ # FastAPI app
│ ├── app/
│ │ ├── main.py
│ │ ├── models/
│ │ ├── routes/
│ │ └── utils/
│ ├── tests/
│ ├── requirements.txt
│ └── Dockerfile
│
├── frontend/ # React app
│ ├── src/
│ ├── public/
│ ├── package.json
│ └── Dockerfile
│
├── ml/ # AI Models & Scripts
│ ├── models/
│ ├── preprocess.py
│ └── inference.py
│
└── docker-compose.yml

---

## ✅ Installation & Setup
### 1. Clone the repo
```bash
git clone https://github.com/<your-username>/job-tracker-ai.git
cd job-tracker-ai

2. Backend Setup
bash
Copy
Edit
cd backend
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
3. Frontend Setup
bash
Copy
Edit
cd frontend
npm install
npm start
✅ Running with Docker
bash
Copy
Edit
docker-compose up --build
✅ Features in Progress
 Backend CRUD for job applications

 AI integration for resume analysis

 JWT authentication

 Deployment to Render/AWS

🤝 Contributing
Contributions are welcome! Please open an issue or submit a pull request.

📜 License
This project is licensed under the MIT License.

yaml
Copy
Edit

---





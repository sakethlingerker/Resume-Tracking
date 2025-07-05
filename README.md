# 🧠 ATS Resume Tracking System

A powerful AI-powered resume analysis tool that helps job seekers optimize their resumes for Applicant Tracking Systems (ATS) and improve their chances of getting hired.

## 🌟 Features

- **📄 PDF Resume Analysis**: Upload and analyze PDF resumes using advanced AI
- **🎯 Job Description Matching**: Compare your resume against specific job descriptions
- **📊 ATS Compatibility Score**: Get percentage match scores for ATS optimization
- **🔍 Keyword Analysis**: Identify missing keywords and skills
- **💡 Professional Evaluation**: Receive detailed feedback from an AI HR perspective
- **🚀 Real-time Processing**: Instant analysis using Google's Gemini AI

## 🚀 Live Demo

**Try the application live:** [ATS Resume Tracking System on Streamlit](https://resumetracking.streamlit.app/)

## 🛠️ Technology Stack

- **Frontend**: Streamlit
- **AI/ML**: Google Gemini 1.5 Flash
- **PDF Processing**: PyMuPDF (fitz)
- **Environment Management**: python-dotenv
- **Deployment**: Streamlit Cloud

## 📋 Prerequisites

- Python 3.7+
- Google AI API Key
- Streamlit account (for deployment)

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone <https://github.com/manashwini27/Resume-Tracking-using-Gemini-pro-vision-api >
cd Resume-Tracking
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables
Create a `.env` file in the root directory:
```env
GOOGLE_API_KEY="your_google_api_key_here"
```

### 4. Get Google AI API Key
1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Add it to your `.env` file

### 5. Run the Application Locally
```bash
streamlit run app.py
```

The application will be available at `http://localhost:8501`

## 📖 How to Use

1. **Upload Your Resume**: Click "Browse files" and select your PDF resume
2. **Enter Job Description**: Paste the job description you're applying for
3. **Choose Analysis Type**:
   - **"Tell Me About the Resume"**: Get detailed professional evaluation
   - **"Percentage Match"**: Get ATS compatibility score and missing keywords
4. **Review Results**: Analyze the AI-generated feedback and recommendations

## 🔧 Configuration

### Streamlit Secrets (for deployment)
Create `.streamlit/secrets.toml`:
```toml
GOOGLE_API_KEY = "your_google_api_key_here"
```

## 🚀 Deployment on Streamlit

This application is deployed on Streamlit Cloud. To deploy your own version:

1. **Push to GitHub**: Ensure your code is in a public GitHub repository
2. **Connect to Streamlit**: 
   - Visit [share.streamlit.io](https://share.streamlit.io)
   - Connect your GitHub account
   - Select your repository
3. **Configure Secrets**: Add your `GOOGLE_API_KEY` in the Streamlit secrets management
4. **Deploy**: Click deploy and your app will be live!

## 📁 Project Structure

```
Resume-Tracking/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── .env                  # Environment variables (local)
├── .streamlit/
│   └── secrets.toml      # Streamlit secrets (deployment)
├── .gitignore           # Git ignore file
└── README.md            # This file
```

## 🔍 Key Functions

- **`input_pdf_setup()`**: Converts PDF to image format for AI processing
- **`get_gemini_response()`**: Handles AI model interactions
- **Streamlit UI**: Provides user-friendly interface for resume analysis

## 🎯 Use Cases

- **Job Seekers**: Optimize resumes for specific job applications
- **HR Professionals**: Quick resume screening and evaluation
- **Career Coaches**: Provide data-driven resume improvement advice
- **Students**: Learn about ATS optimization and keyword matching

## 🔒 Security Notes

- API keys are stored securely using environment variables
- No resume data is permanently stored
- All processing is done in real-time

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🆘 Support

If you encounter any issues or have questions:
- Check the [Streamlit documentation](https://docs.streamlit.io/)
- Review the [Google AI documentation](https://ai.google.dev/)
- Open an issue in this repository

## 🔄 Updates

Stay updated with the latest features and improvements by:
- Starring this repository
- Watching for updates
- Following the deployment link for the latest version

---

**Built with ❤️ using Streamlit and Google Gemini AI** 
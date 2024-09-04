# CareerCraft: ATS-Optimized Resume Analyzer

## Project Description

**CareerCraft** is an advanced resume analysis tool designed to optimize job applications for Applicant Tracking Systems (ATS). Using the Gemini AI model, this tool evaluates resumes against job descriptions to help job seekers enhance their compatibility and increase their chances of passing through ATS filters.

## Project Milestones

1. **Project Planning:**
   - Defined project scope and objectives.
   - Created a project plan with key milestones and deliverables.

2. **Development Phase:**
   - Integrated Gemini AI model for resume analysis.
   - Implemented features for keyword identification and profile summary generation.
   - Added support for PDF and DOCX resume formats.

3. **Testing Phase:**
   - Conducted unit tests and integration tests.
   - Validated the tool with sample resumes and job descriptions.

4. **Documentation and Finalization:**
   - Prepared project documentation and README file.
   - Created output screenshots and a project demonstration video.

## Activities

- **Setup and Configuration:**
  - Configured environment variables and API keys.
  - Set up the development environment with necessary packages.

- **Feature Development:**
  - Developed functionality for ATS compatibility analysis.
  - Implemented resume parsing and keyword extraction features.

- **Testing and Debugging:**
  - Tested the application with various resume and job description formats.
  - Fixed bugs and improved functionality based on test results.

- **Documentation:**
  - Created a detailed README file.
  - Compiled project report and prepared screenshots and video for demonstration.

## References

- **Google Generative AI Documentation:** [Google Generative AI](https://cloud.google.com/generative-ai)
- **Streamlit Documentation:** [Streamlit Documentation](https://docs.streamlit.io/)
- **PyPDF2 Documentation:** [PyPDF2](https://pypi.org/project/PyPDF2/)
- **Resume and Job Description Best Practices:** [Example Guide](https://example.com)

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/CareerCraft-ATS-Optimized-Resume-Analyzer.git
   ```

2. **Navigate to the Project Directory:**
   ```bash
   cd CareerCraft-ATS-Optimized-Resume-Analyzer
   ```

3. **Install Required Packages:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables:**
   - Create a `.env` file in the root directory.
   - Add your API key to the `.env` file:
     ```
     GOOGLE_API_KEY=your_api_key_here
     ```

## Usage

1. **Run the Application:**
   ```bash
   streamlit run app.py
   ```

2. **Interact with the Application:**
   - Open your web browser and go to `http://localhost:8501`.
   - Paste the job description in the provided text area.
   - Upload your resume file (PDF or DOCX).
   - Click “Submit” to get the analysis results.

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Create a new Pull Request.

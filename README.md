# AI-Powered Dating Search Application

## Overview
The AI-powered dating search application is designed to find profiles on **Hinge and Bumble** using **name-matching, facial recognition, and location-based search**. The backend is built using **Python (Flask)**, while the frontend is developed with **React.js** for an interactive user experience. The application leverages **Selenium and Requests** for web scraping and API interaction, along with **SQLAlchemy** for database management. **FuzzyWuzzy** (for text similarity) and **face_recognition** (for facial matching) enhance search accuracy.

## Features
- **Facial Recognition:** Identifies and matches faces from uploaded images.
- **Name Matching:** Uses fuzzy logic to find profiles with similar names.
- **Location-Based Search:** Attempts to filter results based on geographic proximity.
- **Web Scraping:** Extracts relevant data from Hinge and Bumble using Selenium.
- **Interactive UI:** A simple and intuitive React.js frontend for users.
- **Database Management:** Stores and retrieves profile data using SQLAlchemy.

## Technologies Used
### **Backend:**
- Python (Flask)
- SQLAlchemy (Database Management)
- face_recognition (AI-based facial matching)
- FuzzyWuzzy (Text similarity matching)
- Selenium (Web Scraping)
- Requests (API interaction)

### **Frontend:**
- React.js (UI Development)
- HTML, CSS, JavaScript

## Installation & Setup
### **Prerequisites**
- Python 3.x
- Node.js & npm
- Virtual Environment (recommended)

### **Backend Setup**
1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/ai-dating-search.git
   cd ai-dating-search/backend
   ```
2. Create a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Run the Flask server:
   ```sh
   flask run
   ```

### **Frontend Setup**
1. Navigate to the frontend folder:
   ```sh
   cd ../frontend
   ```
2. Install dependencies:
   ```sh
   npm install
   ```
3. Start the React development server:
   ```sh
   npm start
   ```

## Usage
1. Open the frontend in a browser.
2. Enter a name, upload an image, and submit the search request.
3. View matching profiles with names, images, and platform details.

## Challenges Faced
| **Challenge** | **Solution Attempted** |
|--------------|----------------------|
| Hinge and Bumble API restrictions | Used HTTP Toolkit to capture network requests |
| Authentication & session handling | Explored session-based authentication & token retrieval |
| Facial recognition accuracy | Optimized image encoding comparisons using `face_recognition` |
| Name variations | Implemented fuzzy logic for better text matching |
| Scraping limitations | Considered proxies and captcha solvers (with ethical constraints) |

## Future Scope
- **Alternative Data Sources:** Explore public APIs or manual profile entries.
- **Better Scraping Techniques:** Use advanced scraping methods with ethical considerations.
- **Improved UI/UX:** Enhance the frontend with modern UI frameworks.
- **Cloud Deployment:** Deploy on AWS/GCP for scalability.

## Conclusion
While API restrictions posed challenges, this project successfully demonstrates AI-powered search capabilities using **facial recognition, name-matching, and web scraping techniques**. It provided valuable experience in **authentication handling, data automation, and AI-based matching**. Future improvements will focus on overcoming scraping limitations and enhancing usability.

## Thank You!

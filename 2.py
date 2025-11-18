import fitz  # PyMuPDF
import os
import re

# === CONFIGURATION ===
input_pdf = "1conf.pdf"  # your PDF file
output_folder = "output_images"  # folder to save JPEGs

# Titles in the same order as pages
titles = [
"Human Emotion Detection Using AI",

"Privacy-Preserving Mechanisms for SaaS-Based Applications in Multi-Tenant Environments",

"Experimental Study on Self Compacting Concrete with Fly Ash and GGBS",

"Effects Of Coconut Fibre In Improving The Strength Property Of Clay Soil",

"Early Detection of Skin Cancer using Evolving AI Approach",

"LoRa-Based RSSI Alert System for Maritime Boundary Monitoring and Fishermen Safety",

"Tea Leaf Harvesting Using BLDC Motor",

"DeepEyeNet: Hybrid CNN with Genetic Bayesian Optimization for Glaucoma Detection",

"Groundwater Flow Model Development Within A Coastal Watershed",

"Assessment of Ecofriendly Geopolymer Concrete Paver Blocks Incorporating Textile Sludge and Polypropylene Fibers",

"Intrusion Detection Using AI in Cloud Infrastructure",

"AI-Powered Disease Prediction Using Patient Data",

"Smart Diagnosis System for Skin Cancer Using CNN",

"Early Detection of Parkinson’s Disease Using Voice Analysis",

"Medical Image Classification Using Deep Learning",

"Mental Health Monitoring Chatbot Using NLP",

"Product Recommendation Engine Using Collaborative Filtering",

"Customer Sentiment Analysis from Reviews Using NLP",

"AI-Based Dynamic Pricing System for E-commerce",

"Sales Forecasting Using Time Series and ML",

"Fake Product Review Detection Using BERT",

"News Headline Classification Using Transformer Models",

"Text Summarization for Legal Documents Using NLP",

"AI-Based Resume Screening Tool Using Named Entity Recognition",

"Emotion Detection from Chat Conversations",

"Automatic Question Generator for Education Using GPT",

"Deep Fake Detection Using Deep Learning",

"Anomaly Detection in Network Traffic Using Autoencoders",

"AI-Based Phishing Website Detection",

"Malware Classification Using Deep Neural Networks",

"Password Strength Checker Using Machine Learning",

"AI-Driven Email Spam Classifier",

"Loan Default Prediction Using Supervised Learning",

"AI Chatbot for Student Assistance Using Intent Detection",

"Real-Time Traffic Prediction Using ML",

"Enhancing Communication Security Through Machine Learning and Streamlit",

"Automatic Attendance System Using Face Recognition",

"Credit Card Fraud Detection System",

"Driver Drowsiness Detection Using OpenCV and ML",

"Self-Driving Car Simulation Using Reinforcement Learning",

"License Plate Detection System Using YOLO",

"Smart Vehicle Accident Detection and Alert System",

"Pedestrian Detection in Real-Time Using Deep Learning",

"Crop Disease Detection Using Leaf Image Analysis",

"Forest Fire Detection Using Satellite Data and AI",

"AI-Powered Waste Segregation System",

"Air Quality Prediction System Using ML",

"Energy Consumption Prediction Using Machine Learning",

"Voice Cloning and Speech Synthesis Using AI",

"AI-Based Video Summarization Tool",

"Real-Time Language Translator Using NLP",

"Music Genre Classification Using ML",

"Fake News Detection Using Deep Learning",

"AI Based Human Detecting Robot for Environment Disaster Management",

"IoT-Based Weather Prediction System",
]

# ======================

def sanitize_filename(name):
    """Remove unsafe filename characters."""
    name = re.sub(r'[<>:\"/\\|?*]', '', name)
    return name.strip()[:180]

def pdf_to_jpegs(input_pdf, output_folder, titles):
    os.makedirs(output_folder, exist_ok=True)

    doc = fitz.open(input_pdf)
    num_pages = len(doc)

    if len(titles) != num_pages:
        print(f"⚠️ PDF has {num_pages} pages but {len(titles)} titles provided.")
        print("   Only converting up to the smaller count.")

    page_count = min(len(titles), num_pages)

    print("\n🖼️ Converting PDF pages to JPEG images...\n")

    for i in range(page_count):
        page = doc.load_page(i)
        pix = page.get_pixmap(dpi=300)  # render page as image
        filename = f"{i+1:03d}_{sanitize_filename(titles[i])}.jpg"
        output_path = os.path.join(output_folder, filename)
        pix.save(output_path)
        print(f"✅ [{i+1}/{page_count}] Saved as: {filename}")

    doc.close()
    print("\n🎉 All pages converted to JPEG successfully!")

if __name__ == "__main__":
    pdf_to_jpegs(input_pdf, output_folder, titles)

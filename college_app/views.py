from django.shortcuts import render
from django.http import FileResponse, Http404
from django.contrib.staticfiles import finders
import os
from datetime import datetime

def website_home(request):
    current_year = datetime.now().year
    admission_session = f"{current_year}-{str(current_year + 1)[2:]}" 
    
    context = {
        'college_name': 'THAKUR SHREE DPS COLLEGE OF ENGINEERING & MANAGEMENT',
        'trust_name': "Thakur Educational Trust's (Regd.)",
        'tagline': "Empowering Tomorrow's Leaders in Technology & Management.",
        'approvals': "Approved by AICTE & Government of Maharashtra | Affiliated to University of Mumbai",
        'session_year': admission_session,
        
        'contact_info': {
            'address_line1': 'Madhuban, Gokhiware, Vasai (East)',
            'address_line2': 'Palghar - 401208, Maharashtra.',
            'website': 'www.tsdcem.ac.in',
            'email': 'admin@tsdcem.ac.in',
            'phone': '+91 9137518608'
        },
        
        'external_links': {
            'abc_portal': 'https://www.abc.gov.in/',
            'e_samarth': 'https://samarth.edu.in/',
            'mahadb_scholarship': 'https://mahadbt.maharashtra.gov.in/'
        },
        
        'documents_checklist': [
            "SSC Marksheet", "HSC Marksheet", "CET Score Card", 
            "CAP Seat Acceptance Letter", "CAP Registration Acknowledgement (Stamped)", 
            "College Leaving Certificate", "Migration Certificate (if applicable)"
        ],
        'identity_checklist': ["Student Aadhar Card", "ABC ID Proof", "Nationality Proof"],
        'caste_documents': ["Caste Certificate", "Non-Creamy Layer", "Caste Validity", "Current Year Income Certificate"],
        
        'departments': [
            {'id': 'ce', 'name': 'Computer Engineering (CE)', 'intake': 120, 'combined_file': 'ce_sem1_sem2_syllabus.pdf'},
            {'id': 'it', 'name': 'Information Technology (IT)', 'intake': 120, 'combined_file': 'it_sem1_sem2_syllabus.pdf'},
            {'id': 'aids', 'name': 'Artificial Intelligence & Data Science (AIDS)', 'intake': 120, 'combined_file': 'aids_sem1_sem2_syllabus.pdf'},
            {'id': 'ece', 'name': 'Electronics & Computer Engineering (ECE)', 'intake': 60, 'combined_file': 'ece_sem1_sem2_syllabus.pdf'},
            {'id': 'mca', 'name': 'Master of Computer Applications (MCA)', 'intake': 120, 'combined_file': 'mca_sem1_sem2_syllabus.pdf'},
        ],

        # References kept safe as per Screenshot 2026-07-03 191740.pdf
        'principal': {
            'name': 'Dr. Ravish R. Singh',
            'designation': 'Principal & Professor',
            'qualifications': 'Ph.D., M.E., B.E.',
            'experience': '25+ Years',
            'research': 'Signal Processing, Embedded Systems, Microwave Engineering'
        },
        'faculty_members': [
            {'name': 'Ms. Komal A. Champanerkar', 'designation': 'Assistant Professor', 'subject': 'Computer Engineering', 'qualifications': 'M.E. (Computer Engineering), B.E.', 'experience': '12+ Years', 'research': 'Machine Learning, Network Security'},
            {'name': 'Mr. Rajendra R. Bade', 'designation': 'Assistant Professor', 'subject': 'Computer Engineering', 'qualifications': 'M.Tech (CSE), B.Tech', 'experience': '10+ Years', 'research': 'Cloud Computing, Distributed Databases'},
            {'name': 'Ms. Aarti Naik', 'designation': 'Assistant Professor', 'subject': 'Information Technology', 'qualifications': 'M.E. (IT), B.E.', 'experience': '8+ Years', 'research': 'Data Mining, Soft Computing'},
            {'name': 'Mr. Chintamani Mohan Chavan', 'designation': 'Assistant Professor', 'subject': 'Information Technology', 'qualifications': 'M.Tech (IT)', 'experience': '9+ Years', 'research': 'Internet of Things (IoT), Wireless Networks'},
            {'name': 'Mr. Rahul Mahendra Dhuru', 'designation': 'Assistant Professor', 'subject': 'Artificial Intelligence & Data Science', 'qualifications': 'M.E. (Computer Engineering)', 'experience': '7+ Years', 'research': 'Deep Learning, Big Data Analytics'},
            {'name': 'Ms. Sanketi Paresh Raut', 'designation': 'Assistant Professor', 'subject': 'Artificial Intelligence & Data Science', 'qualifications': 'M.Tech (Data Science), B.E.', 'experience': '6+ Years', 'research': 'Natural Language Processing, Computer Vision'},
            {'name': 'Mr. Darshan A. Shah', 'designation': 'Assistant Professor', 'subject': 'Electronics & Computer Engineering', 'qualifications': 'M.E. (Electronics), B.E.', 'experience': '11+ Years', 'research': 'VLSI Design, Robotics & Automation'},
            {'name': 'Mr. Aniket Kalpana Kamalakar Patil', 'designation': 'Assistant Professor', 'subject': 'Electronics & Computer Engineering', 'qualifications': 'M.Tech (Embedded Systems)', 'experience': '5+ Years', 'research': 'Microcontrollers, Smart Instrumentation Grid'},
            {'name': 'Dr. Abhilasha Saini', 'designation': 'Associate Professor', 'subject': 'Master of Computer Applications (MCA)', 'qualifications': 'Ph.D. (Computer Applications), MCA', 'experience': '14+ Years', 'research': 'Software Engineering, Agile Methodologies Management'},
            {'name': 'Dr. Shivam Mahendra Shukla', 'designation': 'Assistant Professor', 'subject': 'Applied Mathematics & Engineering Graphics', 'qualifications': 'Ph.D. (Mathematics), M.Sc.', 'experience': '8+ Years', 'research': 'Numerical Analysis, Fluid Dynamics'},
            {'name': 'Mr. Shashi Prem Gupta', 'designation': 'Assistant Professor', 'subject': 'Master of Computer Applications (MCA)', 'qualifications': 'MCA, B.Sc. (IT)', 'experience': '6+ Years', 'research': 'Web Application Frameworks, Mobile Computing'},
            {'name': 'Dr. Sheetal Vijay Palande', 'designation': 'Assistant Professor', 'subject': 'Applied Chemistry', 'qualifications': 'Ph.D. (Chemistry), M.Sc.', 'experience': '13+ Years', 'research': 'Polymer Chemistry, Environmental Engineering Science'},
            {'name': 'Dr. Rajendra Nana Mahajan', 'designation': 'Assistant Professor', 'subject': 'Applied Physics', 'qualifications': 'Ph.D. (Physics), M.Sc.', 'experience': '15+ Years', 'research': 'Nanotechnology, Material Science Modeling'},
            {'name': 'Ms. Rashmi Vinod Bordiwala', 'designation': 'Assistant Professor', 'subject': 'Applied Chemistry', 'qualifications': 'M.Sc. (Organic Chemistry)', 'experience': '9+ Years', 'research': 'Analytical Chemical Testing Process'},
            {'name': 'Ms. Sadiqa Beg', 'designation': 'Assistant Professor', 'subject': 'Applied Mathematics', 'qualifications': 'M.Sc. (Mathematics), MH-SET, B.Ed.', 'experience': '16+ Years', 'research': 'Mathematical Software Optimization'},
            {'name': 'Ms. Bijal S Gala', 'designation': 'Assistant Professor', 'subject': 'Applied Mathematics', 'qualifications': 'M.Sc. Mathematics, MH-SET, B.Ed.', 'experience': '16+ Years'},
            {'name': 'Sharayu Naik', 'designation': 'Assistant Professor', 'subject': 'Applied Mathematics', 'qualifications': 'M.Sc. (Mathematics), MHT-SET, GATE', 'experience': '3+ Years', 'research': 'Applied Mathematics in Data Science'}
        ],
        
        'toppers': [
            {'name': 'Meet Shah', 'sgpa': '9.84', 'dept': 'Computer Engineering'},
            {'name': 'Priya Sharma', 'sgpa': '9.71', 'dept': 'Information Technology'},
        ],
        'reviews': [
            {
                'student': 'Rahul Sharma',
                'div': 'FY CE - Div A',
                'photo_url': '/static/images/student.png', # Path to student's photo
                'msg': 'The computational infrastructure is phenomenal.'
            },
            {
                'student': 'Sneha Kulkarni',
                'div': 'SY IT - Div B',
                'photo_url': '/static/images/student.png', # Path to student's photo
                'msg': 'The faculty members are incredibly supportive, and the focus on practical coding labs really helped me clear my technical interviews.'
            },
            {
                'student': 'Aditya Panchal',
                'div': 'TY AIDS - Div A',
                'photo_url':  '/static/images/student.png' , # Path to student's photo
                'msg': 'Excellent exposure to machine learning projects. The collaborative environment in the AI labs is top-notch.'
            }
        ],
    }
    
    return render(request, 'college_app/home.html', context)


def download_fees(request):
    """Serve the fees.png as an attachment so browsers will download it."""
    # Try to locate the static file
    file_path = finders.find('images/fees.png')
    if not file_path or not os.path.exists(file_path):
        raise Http404("Fees file not found")
    return FileResponse(open(file_path, 'rb'), as_attachment=True, filename='fees.png')
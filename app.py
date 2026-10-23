import streamlit as st
import datetime

# --- APP CONFIGURATION ---
st.set_page_config(page_title="LYDA HUB", page_icon="📱", layout="wide")

# Initialize session states for mock data
if "donations" not in st.session_state:
    st.session_state.donations = 185000.00
if "vendors" not in st.session_state:
    st.session_state.vendors = [
        {"name": "Diepsloot Crafts", "product": "Handmade Beaded Necklace", "price": 120.0, "youth": True, "stock": 5},
        {"name": "Kasi Tech Solutions", "product": "Custom Phone Stands", "price": 45.0, "youth": True, "stock": 12},
        {"name": "Alex Styles", "product": "Printed Tote Bags", "price": 85.0, "youth": False, "stock": 3}
    ]

# --- APP HEADER ---
st.title("📱 LYDA HUB")
st.caption("Live Your Dream Africa Foundation — Youth Development Ecosystem")

# --- NAVIGATION SIDEBAR ---
page = st.sidebar.radio("Navigate Workspace", [
    "🎓 Higher Education", 
    "📚 Free Tutoring", 
    "💰 Bursaries", 
    "💻 Online Courses", 
    "💼 Corporate Recruitment", 
    "❤️ Donors Portal", 
    "🛍️ LYDA Shop"
])

# --- 1. HIGHER EDUCATION ---
if page == "🎓 Higher Education":
    st.header("🎓 Higher Education Portal")
    st.subheader("University & TVET Registration Gateway")
    
    inst_type = st.radio("Select Institution Type", ["Public University", "TVET College"])
    
    with st.form("edu_form"):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Full Name (as in ID)")
            id_num = st.text_input("South African ID Number")
        with col2:
            email = st.text_input("Email Address")
            choice = st.text_input("Preferred Field of Study (e.g. BCom, Engineering)")
            
    st.info("Ensure certified copies of your ID and Matric results are ready for submission evaluation.")

# --- 2. FREE TUTORING ---
elif page == "📚 Free Tutoring":
    st.header("📚 Free Academic Tutoring")
    subject = st.selectbox("Choose a Subject", ["Mathematics", "Physical Sciences", "Accounting", "English First Additional Language"])
    date = st.date_input("Select Date", datetime.date.today())
    time_slot = st.selectbox("Preferred Time", ["14:00 - 15:30", "16:00 - 17:30"])
    
    if st.button("Schedule Free Session"):
        st.success(f"Successfully requested tutoring for {subject} on {date} at {time_slot}. A volunteer mentor will confirm via SMS.")

# --- 3. BURSARIES ---
elif page == "💰 Bursaries":
    st.header("💰 Financial Aid & Bursaries Board")
    st.write("Browse open applications targeting community students.")
    st.markdown("- **LYDA Community Trust Bursary** (Closes: 30 Nov | Covers: Full Tuition & Books)")
    st.markdown("- **Gauteng Digital Skills Fund** (Closes: 15 Dec | Covers: IT/Tech Diploma programs)")

# --- 4. ONLINE COURSES ---
elif page == "💻 Online Courses":
    st.header("💻 Free Digital Skills Academy")
    course = st.selectbox("Choose a Learning Path", ["Digital Literacy 101", "Introduction to Web Development", "Entrepreneurship Fundamentals"])
    st.progress(45)
    st.caption("Your current module course progress: 45% Completed")

# --- 5. CORPORATE RECRUITMENT ---
elif page == "💼 Corporate Recruitment":
    st.header("💼 Corporate Recruitment Desk")
    st.subheader("Partner Vetting & Registration")
    
    with st.expander("🛡️ Multi-Tiered Corporate Verification Panel", expanded=True):
        cipc = st.text_input("CIPC Registration Number (Format: 20XX/XXXXXX/07)")
        corp_email = st.text_input("Official Corporate Email Address")
        bbbee = st.file_uploader("Upload B-BBEE Affidavit / Certificate")
        
        if corp_email and ("@gmail.com" in corp_email or "@yahoo.com" in corp_email):
            st.error("Access Denied: Public email domains (Gmail/Yahoo) are strictly barred. Please use your official corporate domain email.")

# --- 6. DONORS PORTAL ---
elif page == "❤️ Donors Portal":
    st.header("❤️ Foundation Donors Portal")
    
    target = 250000.0
    current = st.session_state.donations
    progress_pct = min(current / target, 1.0)
    
    st.metric(label="Raised Towards Dream Center Goal", value=f"R{current:,.2f}", delta=f"Target: R{target:,.2f}")
    st.progress(progress_pct)
    
    freq = st.radio("Donation Type", ["Single Gift", "Monthly Debit Order Recurrence"])
    amount = st.number_input("Contribution Amount (ZAR)", min_value=0.0, step=10.0, value=50.0)
    
    if freq == "Monthly Debit Order Recurrence":
        deduct_date = st.selectbox("Preferred Monthly Deduction Date", ["1st of the month", "25th of the month", "30th of the month"])
        mandate = st.checkbox("I authorize LYDA Foundation to debit this account monthly under regulatory requirements.")
        
    if st.button("Process Secure Donation"):
        if amount < 10.0:
            st.error("Processing Limit Exception: Minimum contribution limit is R10.")
        else:
            st.session_state.donations += amount
            st.success(f"Thank you! Your donation of R{amount:.2f} has been processed successfully.")

# --- 7. LYDA SHOP ---
elif page == "🛍️ LYDA Shop":
    st.header("🛍️ LYDA Community Marketplace")
    
    tab1, tab2 = st.tabs(["Browse Market", "Micro-Vendor Dashboard"])
    
    with tab1:
        st.subheader("Support Local Local Entrepreneurs")
        for item in st.session_state.vendors:
            col1, col2 = st.columns([3, 1])
            with col1:
                title_str = f"**{item['product']}** — *by {item['name']}*"
                if item['youth']:
                    title_str += " 🛡️ [Verified Youth-Owned]"
                st.write(title_str)
                st.caption(f"Stock remaining: {item['stock']} units")
            with col2:
                if st.button(f"Buy for R{item['price']:.2f}", key=item['product']):
                    st.toast("Escrow Payment Initialized!")
                    st.info("🔒 Secure Escrow Activated: Funds held safely in trust until delivery is confirmed.")
                    
    with tab2:
        st.subheader("List Your Product in 60 Seconds")
        v_prod = st.text_input("What are you selling?")
        v_price = st.number_input("Selling Price (R)", min_value=0.0, step=5.0)
        v_youth = st.checkbox("Apply for Youth-Owned Verification Badge (Requires SA ID)")
        if v_youth:
            v_id = st.text_input("Enter Your 13-Digit South African ID Number")
            
        if st.button("Publish Listing Live"):
            if v_prod and v_price > 0:
                st.session_state.vendors.append({
                    "name": "Local Community Vendor",
                    "product": v_prod,
                    "price": v_price,
                    "youth": v_youth,
                    "stock": 10
                })
                st.success("Your listing is live on the marketplace!")

# Automated Slot Reservation & Query Ticketing System

A robust, data-driven full-stack web application designed to manage real-time scheduling allocations and resolve user inquiries. This system replaces manual scheduling processes with a dynamic slot-reservation engine and pairs it with a structured ticketing pipeline for tracking internal queries from submission to resolution.

## 🚀 Key Features
* **Real-Time Slot Reservation:** Features an automated availability checker preventing double-booking and managing slot allocations dynamically.
* **Query Ingestion Pipeline:** Secure input handling that captures structured ticket data, priorities, and user contexts.
* **Full-Stack CRUD Architecture:** Secure relational database management to read availability, write reservations, and update the lifecycle of active query tickets.
* **Administrative Operations Console:** A centralized dashboard built for administrators to monitor active reservations, allocate system resources, and update ticket states (e.g., Open, Pending, Resolved).

## 🛠️ Technical Stack
* **Languages:** Python, SQL, JavaScript, HTML5, CSS3
* **Backend Architecture:** Flask
* **Database Layer:** MySQL
* **Design Pattern:** MVC (Model-View-Controller) structure

## 🏗️ System Workflow & Logic
1. **Capacity & Slot Allocation:** Users view real-time available time windows. The backend validation engine ensures entries do not conflict with existing database records.
2. **Ticketing Lifecycle:** When an inquiry is submitted, it is assigned a unique identifier and grouped by categorization rules for rapid administrative sorting.
3. **State Management:** Administrators track and execute status changes directly through the secure dashboard, ensuring live updates are reflected across user profiles instantly.

## 💻 Installation & Setup
```bash
# Clone the repository
git clone [https://github.com/ppoobesh/slot-reservation-ticketing-system.git](https://github.com/ppoobesh/slot-reservation-ticketing-system.git)

# Navigate to the project directory
cd slot-reservation-ticketing-system

# Install dependencies
pip install -r requirements.txt

# Execute application script
python app.py

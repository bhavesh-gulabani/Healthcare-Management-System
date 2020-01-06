# Healthcare Management System

<h1> Project Description </h1>
<h2>Abstract</h2>
  <b>Title</b><p>Healthcare Management System</p>
  <b>Aim</b><p>This project aims at developing a comprehensive system which is designed to manage the medical, financial and administrative aspects related to a Healthcare centre.</p>
  <b>Objective</b><p>The main objective of this project is to automate the maintenance of patient and staff details in the hospital. The       information of patients, their appointments, and doctors will be stored in a structured manner for easy and efficient retrieval. It will   also provide an interactive GUI which will be easy to navigate.</p>
  <p>The system implemented will be a Web Application which will be accessible primarily through a Web Browser. The database management system   used will be MySQL, and Python will be used as a server-side scripting language and for connectivity between the database and the front-   end.</p>
  <b>Project Category</b><p>Database Management Information System.</p>
  <b>Outcome</b><p>The developed system will improve the quality and management of all of the traditional hospital processes and thus increase the efficiency and quality of work.</p>

<h2> Introduction </h2>
<b>Problem Statement</b>
<p>Develop a Healthcare Management System which will manage the medical, financial and administrative aspects related to a Healthcare centre. The system is expected to automate the existing manual processes of patients, doctors and appointment management.</p>
<b>Project Idea</b>
<p>The idea came by when we wanted to develop a lightweight system which can be used by every kind of hospital as well as small clinics.</p>
<b>Motivation</b>
<p>We came up with this idea when we visited a local government clinic where the documentation was done manually which was a tedious process for the person handling the things.</p>
<b>Scope</b>
<p>This project can be used by any hospital and doesn’t require any state of the art facilities to run the software. This system will be able to manage the patient records and the processes like admission, medical record creation, booking appointment as well as billing procedure.</p>
<b>Requirement Analysis</b>
<p>The system will be scalable and the hospitals can add their own data
The database will have a backup and if the main database is lost the backup database will be safe and the data will be recoverable from that database. Data integrity will be provided for the hospitals, every user will have a unique ID</p>


<h2>Project Design </h2>
<h3>Software Model</h3>
<ul>
  <li>Agile model</li>
  <li>Scrum Method</li>
  <ul>
    <li>Use Case Diagram</li>
    <li>Stake Holders identification</li>
    <li>Class design</li>
    <li>Class diagram and elaboration</li>
    <li>Architecture diagram</li>
    <li>Component design and diagram</li>
    <li>Component Elaboration</li>
    <li>Estimation</li>
    <li>Scheduling</li>
    <li>Risk Analysis</li>
  </ul>
  </ul>
<h3>Hardware, Software and Resources</h3>
<p>The hardware required will be a fully operational desktop with proper network connection to the Web server.The software required will be a Web browser which will access the Web Application.</p>
<h4>The software used to develop this project are</h4>
  <ul>
    <li>XAMPP (Cross Platform – Apache – MySQL – PHP). It is a complete software package which consists of Apache Web Server, MySQL database and supports multiple programming languages for server-side scripting with PHP being the most popular one.</li>
    <li>The database management system used is MySQL.</li>
    <li>Python programming language is used for server-side scripting and for connectivity between the database and the front-end.</li>
<li>HTML and CSS are used for the front-end design and structuring to design and develop the web-pages.</li>
  </ul></p>
  
<h3>E-R Model</h3>
<p>For the creation of conceptual design, the Entity-Relationship(ER) model is used. We have specified the entities that are represented in the database, the attributes of the entities, the relationships among the entities, and constraints on the entities and relationships. This phase resulted in the creation of an entity-relationship diagram that provides a graphical representation of the system.</p>
<p><img src = "https://github.com/bhavesh-gulabani/Healthcare-Management-System/blob/master/Images/ER-Diagram.png" alt = "ER Diagram"></p>

<h3>Normalization</h3>
<p><ul>
  <li>The tables were designed to follow the first normal form. The primary keys were assigned such that no non-prime attribute is functionally dependent on any proper subset of any candidate key of the relation.</li>
<li>We designed the tables such that any non-prime attribute is not transitively dependent on another prime attribute.</li>
  <li>Thus the tables satisfy first three normal forms.</li>
  </ul>
<h2>Module Description </h2>
<h3>Patient Registration Module</h3>
<p>This module registers patient details based on general and demographic information. Patients are allocated a Unique Identification Number (UID) and at the time of registration.</p>
<h4>Salient Features Include</h4>
<ul>
  <li>Detailed information of patients</li>
  <li>Mandatory fields for crucial patient information</li>
  <li>Alerts in place to prevent erroneous data entry</li>
  <li>Generates Unique Identification Number (UID)</li>
 </ul> 
  <h3>Patient Medical Record Module</h3>
<p>This module deals with the generation of a medical record for a patient where in along with the personal details, additional information about the diagnosis and consulting doctor, as well as date of admission and discharge are recorded.</p>
<h4>Salient Features Include</h4>
<ul>
  <li>Additional information about the patient treatment</li>
  <li>Alerts in place to prevent erroneous data entry</li>
  <li>Generates Unique Record Number (URD)</li>
  </ul>
<h3>Consulting Appointment Module</h3>
<p>Consulting Appointment Management Patients reach hospitals either through direct walking or through a reference from referral hospitals. Using this module, appointments can be issued in advance for new patients as well as for follow-up patients. Appointments can be rescheduled or cancelled as per the requirement. Some patients may come for lab tests and radiology services and registrations for these, too, will be carried out and bills will be generated for the required services.</p>
<h4>Salient Features Include</h4>
<ul>
  <li>Appointment booking</li>
  <li>Appointment display</li>
  <li>Appointment cancellation due to a valid reason</li>
  <li>Display list of doctors available</li>
  </ul>
<h3>Cashier Module</h3>
<p>This module facilitates cashier and billing operations for different Outpatient and Inpatient categories. It provides automatic posting of charges related to different services like bed charges, lab tests conducted, medicines issued, consultant’s fee, food, beverage and telephone charges etc.</p>
  <h4>Salient Features Include</h4>
  <ul>
    <li>Payment modes/details</li>
    <li>Patient billing details</li>
    <li>Time and date of receipt generation</li>
  </ul>

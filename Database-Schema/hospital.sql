-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 04, 2019 at 05:20 PM
-- Server version: 5.7.27
-- PHP Version: 7.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hospital`
--

-- --------------------------------------------------------

--
-- Table structure for table `accesses`
--

CREATE TABLE `accesses` (
  `E_ID` int(10) NOT NULL,
  `Record_no` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `admin_staff`
--

CREATE TABLE `admin_staff` (
  `E_ID` int(10) NOT NULL,
  `Position` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `appointment`
--

CREATE TABLE `appointment` (
  `Appointment_ID` int(10) NOT NULL,
  `P_ID` int(10) NOT NULL,
  `Doctor_ID` int(10) NOT NULL,
  `Receptionist_ID` int(10) NOT NULL,
  `Time` time NOT NULL,
  `Date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `appointment`
--

INSERT INTO `appointment` (`Appointment_ID`, `P_ID`, `Doctor_ID`, `Receptionist_ID`, `Time`, `Date`) VALUES
(3301, 1101, 101, 103, '15:03:00', '2019-10-10'),
(3302, 1102, 102, 103, '05:03:00', '2019-10-18'),
(3303, 1103, 104, 105, '12:01:00', '2019-10-19');

-- --------------------------------------------------------

--
-- Table structure for table `attends`
--

CREATE TABLE `attends` (
  `E_ID` int(10) NOT NULL,
  `P_ID` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `billing`
--

CREATE TABLE `billing` (
  `Receipt_ID` int(10) NOT NULL,
  `P_ID` int(10) NOT NULL,
  `Mode_of_payment` varchar(20) NOT NULL,
  `Amount` decimal(20,0) NOT NULL,
  `Status` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `billing`
--

INSERT INTO `billing` (`Receipt_ID`, `P_ID`, `Mode_of_payment`, `Amount`, `Status`) VALUES
(4401, 1101, 'Cash', '5000', 'Not Paid'),
(4402, 1102, 'Online', '10000', 'Paid'),
(4403, 1103, 'Cash', '4000', 'Paid'),
(4404, 1104, 'Online', '6000', 'Not Paid');

-- --------------------------------------------------------

--
-- Table structure for table `confirms`
--

CREATE TABLE `confirms` (
  `E_ID` int(10) NOT NULL,
  `Appointment_no` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `doctor`
--

CREATE TABLE `doctor` (
  `Doctor_ID` int(10) NOT NULL,
  `Speciality` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `doctor`
--

INSERT INTO `doctor` (`Doctor_ID`, `Speciality`) VALUES
(101, 'ENT'),
(102, 'Cardiologist'),
(104, 'Allergist');

-- --------------------------------------------------------

--
-- Table structure for table `employee`
--

CREATE TABLE `employee` (
  `E_ID` int(10) NOT NULL,
  `Name` varchar(20) DEFAULT NULL,
  `Sex` varchar(10) DEFAULT NULL,
  `Salary` float DEFAULT NULL,
  `Qualification` varchar(20) DEFAULT NULL,
  `Address` varchar(25) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `employee`
--

INSERT INTO `employee` (`E_ID`, `Name`, `Sex`, `Salary`, `Qualification`, `Address`) VALUES
(101, 'Alex', 'Male', 100000, 'MD', 'Brooklyn, NY'),
(102, 'Meredith', 'Female', 150000, 'MD', 'Queens, NY'),
(103, 'Derek', 'Male', 120000, 'MD', 'Staten Island, NY'),
(104, 'Andrew', 'Male', 145000, 'MD', 'Bronx, NY'),
(105, 'Christina', 'Female', 150000, 'MD', 'Brooklyn, NY');

-- --------------------------------------------------------

--
-- Table structure for table `employee_contact`
--

CREATE TABLE `employee_contact` (
  `E_ID` int(10) NOT NULL,
  `Phone_number` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `employee_contact`
--

INSERT INTO `employee_contact` (`E_ID`, `Phone_number`) VALUES
(101, 264582),
(101, 274582),
(102, 274583),
(103, 264584),
(103, 274584),
(104, 274585),
(105, 274586);

-- --------------------------------------------------------

--
-- Table structure for table `maintains`
--

CREATE TABLE `maintains` (
  `E_ID` int(10) NOT NULL,
  `Record_no` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `medical_record`
--

CREATE TABLE `medical_record` (
  `Record_no` int(10) NOT NULL,
  `P_ID` int(10) NOT NULL,
  `Doctor_ID` int(10) NOT NULL,
  `Date_admitted` date NOT NULL,
  `Date_discharged` date NOT NULL,
  `Diagnosis` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `medical_record`
--

INSERT INTO `medical_record` (`Record_no`, `P_ID`, `Doctor_ID`, `Date_admitted`, `Date_discharged`, `Diagnosis`) VALUES
(2201, 1101, 102, '2019-10-09', '2019-10-19', 'High Fever'),
(2202, 1102, 102, '2019-10-05', '2019-10-15', 'Sore throat'),
(2203, 1103, 101, '2019-10-16', '2019-10-26', 'High Blood pressure');

-- --------------------------------------------------------

--
-- Table structure for table `patient`
--

CREATE TABLE `patient` (
  `P_ID` int(10) NOT NULL,
  `Name` varchar(20) DEFAULT NULL,
  `Sex` varchar(8) DEFAULT NULL,
  `DOB` date DEFAULT NULL,
  `Age` int(5) DEFAULT NULL,
  `Email` varchar(25) NOT NULL,
  `Address` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `patient`
--

INSERT INTO `patient` (`P_ID`, `Name`, `Sex`, `DOB`, `Age`, `Email`, `Address`) VALUES
(1101, 'William', 'Male', '1989-09-11', 30, 'william_mathew@gmail.com', 'Brooklyn, NY'),
(1102, 'Ema', 'Female', '1989-06-20', 30, 'ema_halpert@gmail.com', 'Queens, NY'),
(1103, 'Joey', 'Male', '1992-10-01', 27, 'joey_123@gmail.com', 'Queens, NY'),
(1104, 'Robin', 'Female', '1985-05-23', 34, 'robin_456@gmail.com', 'Brooklyn, NY');

-- --------------------------------------------------------

--
-- Table structure for table `receptionist`
--

CREATE TABLE `receptionist` (
  `Receptionist_ID` int(10) NOT NULL,
  `Working hours` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `receptionist`
--

INSERT INTO `receptionist` (`Receptionist_ID`, `Working hours`) VALUES
(103, 8),
(105, 10);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `accesses`
--
ALTER TABLE `accesses`
  ADD PRIMARY KEY (`E_ID`,`Record_no`);

--
-- Indexes for table `admin_staff`
--
ALTER TABLE `admin_staff`
  ADD PRIMARY KEY (`E_ID`,`Position`);

--
-- Indexes for table `appointment`
--
ALTER TABLE `appointment`
  ADD PRIMARY KEY (`Appointment_ID`),
  ADD KEY `P_ID` (`P_ID`);

--
-- Indexes for table `attends`
--
ALTER TABLE `attends`
  ADD PRIMARY KEY (`E_ID`,`P_ID`);

--
-- Indexes for table `billing`
--
ALTER TABLE `billing`
  ADD PRIMARY KEY (`Receipt_ID`),
  ADD KEY `P_ID` (`P_ID`);

--
-- Indexes for table `confirms`
--
ALTER TABLE `confirms`
  ADD PRIMARY KEY (`E_ID`,`Appointment_no`);

--
-- Indexes for table `doctor`
--
ALTER TABLE `doctor`
  ADD PRIMARY KEY (`Doctor_ID`,`Speciality`);

--
-- Indexes for table `employee`
--
ALTER TABLE `employee`
  ADD PRIMARY KEY (`E_ID`);

--
-- Indexes for table `employee_contact`
--
ALTER TABLE `employee_contact`
  ADD PRIMARY KEY (`E_ID`,`Phone_number`);

--
-- Indexes for table `maintains`
--
ALTER TABLE `maintains`
  ADD PRIMARY KEY (`E_ID`,`Record_no`);

--
-- Indexes for table `medical_record`
--
ALTER TABLE `medical_record`
  ADD PRIMARY KEY (`Record_no`),
  ADD KEY `P_ID` (`P_ID`);

--
-- Indexes for table `patient`
--
ALTER TABLE `patient`
  ADD PRIMARY KEY (`P_ID`);

--
-- Indexes for table `receptionist`
--
ALTER TABLE `receptionist`
  ADD PRIMARY KEY (`Receptionist_ID`,`Working hours`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `admin_staff`
--
ALTER TABLE `admin_staff`
  ADD CONSTRAINT `admin_staff_ibfk_1` FOREIGN KEY (`E_ID`) REFERENCES `employee` (`E_ID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `appointment`
--
ALTER TABLE `appointment`
  ADD CONSTRAINT `appointment_ibfk_1` FOREIGN KEY (`P_ID`) REFERENCES `patient` (`P_ID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `billing`
--
ALTER TABLE `billing`
  ADD CONSTRAINT `billing_ibfk_1` FOREIGN KEY (`P_ID`) REFERENCES `patient` (`P_ID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `doctor`
--
ALTER TABLE `doctor`
  ADD CONSTRAINT `doctor_ibfk_1` FOREIGN KEY (`Doctor_ID`) REFERENCES `employee` (`E_ID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `employee_contact`
--
ALTER TABLE `employee_contact`
  ADD CONSTRAINT `employee_contact_ibfk_1` FOREIGN KEY (`E_ID`) REFERENCES `employee` (`E_ID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `medical_record`
--
ALTER TABLE `medical_record`
  ADD CONSTRAINT `medical_record_ibfk_1` FOREIGN KEY (`P_ID`) REFERENCES `patient` (`P_ID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `receptionist`
--
ALTER TABLE `receptionist`
  ADD CONSTRAINT `receptionist_ibfk_1` FOREIGN KEY (`Receptionist_ID`) REFERENCES `employee` (`E_ID`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

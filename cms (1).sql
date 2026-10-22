-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 23, 2025 at 11:38 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `cms`
--

-- --------------------------------------------------------

--
-- Table structure for table `custmast`
--

CREATE TABLE `custmast` (
  `cno` int(10) NOT NULL,
  `cname` varchar(30) NOT NULL,
  `cadd` varchar(30) NOT NULL,
  `city` varchar(30) NOT NULL,
  `contact` varchar(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `custmast`
--

INSERT INTO `custmast` (`cno`, `cname`, `cadd`, `city`, `contact`) VALUES
(1, 'vishal mahajan', 'deopur', 'dhule', '578485446'),
(2, 'harshu', 'sakri', 'dhule', '46789099'),
(3, 'Disha nemane', 'fashi pool', 'dhule', '367880346'),
(4, 'nitya', 'bajrang chaouk', 'dhule', '68096444'),
(5, 'tanishq', 'vaghadi', 'songir', '499587768'),
(6, 'kranti patil', 'nandre', 'dhule', '377898990'),
(7, 'anamika sharma', 'deopur', 'dhule', '9011223344');

-- --------------------------------------------------------

--
-- Table structure for table `itemmast`
--

CREATE TABLE `itemmast` (
  `Icode` int(10) NOT NULL,
  `Iname` varchar(20) NOT NULL,
  `Idesc` varchar(20) NOT NULL,
  `Irate` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `itemmast`
--

INSERT INTO `itemmast` (`Icode`, `Iname`, `Idesc`, `Irate`) VALUES
(1, 'cold coffee', 'full', '150'),
(2, 'burger', 'large', '150'),
(3, 'pasta', 'full', '250'),
(4, 'garlic bread', 'half', '80'),
(5, 'french fries', 'full', '130'),
(6, 'burger', 'full', '180'),
(7, 'small pizza', 'made with buttor', '500');

-- --------------------------------------------------------

--
-- Table structure for table `orderdetail`
--

CREATE TABLE `orderdetail` (
  `Ordno` int(10) NOT NULL,
  `Icode` int(10) NOT NULL,
  `Qty` int(10) NOT NULL,
  `Rate` int(10) NOT NULL,
  `Amt` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `orderdetail`
--

INSERT INTO `orderdetail` (`Ordno`, `Icode`, `Qty`, `Rate`, `Amt`) VALUES
(1, 1, 6, 80, 480),
(2, 3, 5, 120, 600),
(3, 3, 3, 100, 300),
(4, 2, 6, 90, 270),
(5, 2, 3, 90, 270),
(6, 4, 2, 50, 100),
(7, 7, 2, 500, 1000);

-- --------------------------------------------------------

--
-- Table structure for table `tablemast`
--

CREATE TABLE `tablemast` (
  `Tbno` int(10) NOT NULL,
  `Tbcapacity` int(10) NOT NULL,
  `Tbtype` varchar(30) NOT NULL,
  `Tbrate` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tablemast`
--

INSERT INTO `tablemast` (`Tbno`, `Tbcapacity`, `Tbtype`, `Tbrate`) VALUES
(1, 5, 'family', 2000),
(2, 6, 'formal', 700),
(3, 8, 'casual', 2000),
(4, 6, 'casual', 1500),
(5, 4, 'formal', 1000),
(6, 2, 'formal', 500);

-- --------------------------------------------------------

--
-- Table structure for table `transmast`
--

CREATE TABLE `transmast` (
  `Trno` int(10) NOT NULL,
  `Trdate` date NOT NULL,
  `cno` int(10) NOT NULL,
  `Tbno` int(10) NOT NULL,
  `Amount` int(10) NOT NULL,
  `Discount` int(10) NOT NULL,
  `Netamt` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `transmast`
--

INSERT INTO `transmast` (`Trno`, `Trdate`, `cno`, `Tbno`, `Amount`, `Discount`, `Netamt`) VALUES
(1, '2025-02-08', 1, 1, 480, 8, 472),
(2, '2025-02-11', 2, 2, 600, 20, 580),
(3, '2025-03-13', 5, 3, 300, 30, 270),
(4, '2025-03-12', 6, 3, 270, 20, 250),
(5, '2025-03-06', 3, 5, 600, 50, 550),
(6, '2025-04-23', 7, 6, 200, 2, 198),
(7, '2025-04-23', 1, 6, 1000, 12, 988);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `custmast`
--
ALTER TABLE `custmast`
  ADD PRIMARY KEY (`cno`);

--
-- Indexes for table `itemmast`
--
ALTER TABLE `itemmast`
  ADD PRIMARY KEY (`Icode`);

--
-- Indexes for table `tablemast`
--
ALTER TABLE `tablemast`
  ADD PRIMARY KEY (`Tbno`);

--
-- Indexes for table `transmast`
--
ALTER TABLE `transmast`
  ADD PRIMARY KEY (`Trno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `custmast`
--
ALTER TABLE `custmast`
  MODIFY `cno` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `itemmast`
--
ALTER TABLE `itemmast`
  MODIFY `Icode` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `tablemast`
--
ALTER TABLE `tablemast`
  MODIFY `Tbno` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `transmast`
--
ALTER TABLE `transmast`
  MODIFY `Trno` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
